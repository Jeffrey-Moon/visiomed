#include <WiFi.h>
#include <HTTPClient.h>

#include "FS.h"
#include "SPIFFS.h"
//SPIFFS : ESP32는 SPIFFS(Serial Interface Flash File System)을 가지고 있다.
//         SPI 버스에 연결된 플래쉬 칩을 가지고 있는 ESP32같은 마이크로 컨트롤러를 위해
//         만들어 진 경량 파일 시스템이다. 이것을 사용하면 플래쉬 메모리를 컴퓨터에서 일반 파일을
//         access 하는 것처럼 사용할 수 있게 해준다. 간단한 만큼 기능은 제한적으로 파일을 읽고,
//         쓰고, 삭제하는 것을 가능하게 해준다.
//         위의 개념은 보통적으로 명시하지만, 내가 정리를 한다면 쉽게말하면 파일 I/O를 가능하게
//         해주는 라이브러리다. 주의할 점으로는 아두이노 우노에서는 SPI. 즉, 데이터 연결통로가
//         1개뿐이기 때문에. 같은 통로를 가지는 핀을 공유할 수 없다. 그렇기 때문에 LED화면이나
//         SD카드 모듈과 함께 쓸 수 없다고 한다.(**아두이노 우노)

#include "AudioFileSourceSPIFFS.h"
#include "AudioFileSourceID3.h"
#include "AudioGeneratorMP3.h"
#include "AudioOutputI2SNoDAC.h"
#include "AudioOutputI2S.h"



#define MP3_FILENAME "/tts.mp3"
#define BUFFER_SIZE 3000

//버튼 핀번호
#define pushButton1 23
#define pushButton2 18
//버튼 상태
int buttonState1;
int buttonState2;
String requestData; //Servelet host에 요청할 데이터 약보관함 인덱스 번호
String requestResult = ""; // Servelet host에서 응답한 데이터 결괏값 저장
String kakaoiVoice = ""; // tts로 만들 데이터 보관

AudioGeneratorMP3 *mp3;
AudioFileSourceSPIFFS *file;
AudioOutputI2S *out;
AudioFileSourceID3 *id3;

void setup() {
  pinMode(pushButton1, INPUT_PULLUP);
  pinMode(pushButton2, INPUT_PULLUP);
  
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

  delay(1000);

}

void loop() {
  requestData = "";
  buttonState1 = digitalRead(pushButton1);
  buttonState2 = digitalRead(pushButton2);
  
  Serial.print("button state1 : ");
  Serial.println(buttonState1);
  Serial.print("button state2 : ");
  Serial.println(buttonState2);
  delay(1);
  
  if (buttonState1 == HIGH) {
    requestData = "0";     //핀 이름은 1번이지만 데이터베이스의 index는 0번부터이므로 1번핀일때 0번 값을 전달
    getData(requestData);  // 서블릿에서 데이터를 가지고 오는 함수
  }
  else if (buttonState2 == HIGH) {
    requestData = "1";
    getData(requestData);
  }
}

// 서블릿에서 데이터를 가지고 오는 함수
void getData(String requestData){
  if ((WiFi.status() == WL_CONNECTED)) { //Check the current connection status
      HTTPClient http;

      http.begin(host+requestData); // http연결함수 Specify the URL : "http://211.227.224.240:8087/Test213/Test1111?data=0" 
      int httpCode = http.GET();    //request GET

      if (httpCode > 0) { //http 응답코드
        Serial.println(httpCode);
        
        requestResult = http.getString();
        Serial.println(requestResult);
        
        kakaoiVoice = requestResult;
        runAPIVoice(kakaoiVoice);
      } else {
        Serial.println("Error on HTTP request");
      }
      http.end(); //Free the resources
    }
    delay(1000);
}

//response 받은 데이터를 카카오i로 전송하여 데이터를 받아 파일로 쓰고 읽는 함수
//#include <ArduinoJson.h>
//Json활용하려다 2차원배열형태의 JSON을 넘겨주는 형태에 대한 학습이 부족하여 일단 고려했었던 
//1.JSON형태 데이터값 2.아두이노 자체 데이터베이스 조회 3.문자열 형태 값 넘김 3가지 방법 중 3번째 방법을 선택했다.
//*챌린지포인트
//추후 JSON에 대한 추가 학습 후 재구현해볼 예정
 
const char *ssid = "SHIN";                 //wifi name
const char *password = "dlqdn015";         //wifi password
const char *host = "http://211.227.224.240:8087/Test213/Test1111?data=";  //Servelet GET host
const char *voiceAPI = "https://tts-translate.kakao.com/newtone?message="; //KAKAO i API host

void runAPIVoice(String kakaoiVoice) {
  kakaoiVoice = urlencode(kakaoiVoice);
  kakaoiVoice = voiceAPI + kakaoiVoice;

  Serial.println(kakaoiVoice);

  HTTPClient http;
  http.begin(kakaoiVoice);

  int httpCode = http.GET();

  if (httpCode > 0)
  {
    Serial.printf("[HTTP] GET... Kakao i code: %d\n", httpCode);
    if (httpCode == HTTP_CODE_OK)
    {
      int32_t len = http.getSize();
      Serial.println(len);
      uint8_t buff[BUFFER_SIZE] = { 0 };
      WiFiClient *stream = http.getStreamPtr();

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
                      // (*stream).available()
                      // stream->available()

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

//16진수 UTF-8로 한글을 char-set type 변경
String urlencode(String str) {
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
