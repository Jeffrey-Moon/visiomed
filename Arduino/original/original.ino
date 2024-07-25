#include <WiFi.h>
#include <HTTPClient.h>


#include "FS.h"
#include "SPIFFS.h"

#include "AudioFileSourceSPIFFS.h"
#include "AudioFileSourceID3.h"
#include "AudioGeneratorMP3.h"
#include "AudioOutputI2SNoDAC.h"
#include "AudioOutputI2S.h"

#define MP3_FILENAME "/tts.mp3"
#define BUFFER_SIZE 3000
#define btnpin1 18 // GIOP21 pin connected to button
#define btnpin2 19 // GIOP21 pin connected to button

const char* ssid     = "SHIN";
const char* password = "12345678";

int btnState1 = 0;
int btnState2 = 0;
String value="";
boolean btnStart = false;

AudioGeneratorMP3 *mp3;
AudioFileSourceSPIFFS *file;
AudioOutputI2S *out;
AudioFileSourceID3 *id3;

void setup()
{
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to the WiFi network");
  Serial.println("");
  
  Serial.begin(115200);
  
  if (!SPIFFS.begin())
  {
    Serial.println("SPIFFS Mount Failed");
    return;
  }
  pinMode(btnpin1, INPUT_PULLUP);
  pinMode(btnpin2, INPUT_PULLUP);
}

void loop()
{
  btnStart = false;
  btnState1 = digitalRead(btnpin1);
  btnState2 = digitalRead(btnpin2);
  
  if(btnState1 == HIGH){
    value = "한사랑병원 아침약입니다 식후 30분에 드세요오";
    btnStart = true;
  }
  else if(btnState2 == HIGH){
    value = "신동아병원 점심약입니다 식후 30분에 드세요오";
    btnStart = true;
  }
  if(btnStart == true){
    HttpConPlayVoice(value);
  }
}

//Http통신으로 음성사이트에 연결해서 재생까지 해주는 부분을 함수로 묶어서 만듬.
void HttpConPlayVoice(String value)
{
   value = urlencode(value);
   value = "https://fanyi.baidu.com/gettts?lan=kor&spd=3&source=web&text=" + value;

   Serial.println(value);

   HTTPClient http;
   http.begin(value);
   
   int httpCode = http.GET();

   if (httpCode > 0)
   {
     Serial.printf("[HTTP] GET... baidu code: %d\n", httpCode);
     if (httpCode == HTTP_CODE_OK)
     {
       int32_t len = http.getSize();
       Serial.println(len);
       uint8_t buff[BUFFER_SIZE] = { 0 };
       WiFiClient * stream = http.getStreamPtr();

       Serial.printf("Writing file: %s\r\n", MP3_FILENAME);

       File file2 = SPIFFS.open(MP3_FILENAME, FILE_WRITE);
       if (!file2)
       {
         Serial.println("- failed to open file for writing");
         return;
       }

       while (http.connected() && (len > 0 || len == -1))
       {
         // get available data size
         size_t size = stream->available();

         if (size)
         {
           int read_size = BUFFER_SIZE;
           if ( read_size > size ) read_size = size;
           int c = stream->readBytes(buff, read_size);
           file2.write(buff, c);
           if (len > 0)
           {
             len -= c;
           }
         }
         delay(1);
       }
       file2.flush();
       file2.close();
     }
     else
     {
       Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
     }
     http.end();
   }

   audioLogger = &Serial;
   file = new AudioFileSourceSPIFFS(MP3_FILENAME);
   id3 = new AudioFileSourceID3(file);
   out = new AudioOutputI2S(0, AudioOutputI2S::INTERNAL_DAC);
   mp3 = new AudioGeneratorMP3();
   mp3->begin(id3, out);

   while (mp3->isRunning())
   {
     if (!mp3->loop())
     {
       //delay(1000); 주석해줘야 지지직안거림
       mp3->stop();
     }
   }

   {
     Serial.printf("MP3 done\n");   
     delay(1000);
   }
}

//아두이노는 한글을 전송할수 없다. 그래서 인코딩해서 전송해주기위해 인코딩 함수를 씀.
String urlencode(String str)
{
  String encodedString = "";
  char c;
  char code0;
  char code1;
  char code2;
  for (int i = 0; i < str.length(); i++)
  {
    c = str.charAt(i);
    if (c == ' ')
    {
      encodedString += '+';
    }
    else if (isalnum(c))
    {
      encodedString += c;
    }
    else
    {
      code1 = (c & 0xf) + '0';
      if ((c & 0xf) > 9)
      {
        code1 = (c & 0xf) - 10 + 'A';
      }
      c = (c >> 4) & 0xf;
      code0 = c + '0';
      if (c > 9)
      {
        code0 = c - 10 + 'A';
      }
      code2 = '\0';
      encodedString += '%';
      encodedString += code0;
      encodedString += code1;
      //encodedString+=code2;
    }
    yield();
  }
  return encodedString;
}
