import spidev #spi통신을 위한 라이브러리

spi = spidev.SpiDev() #spi 객체 생성
spi.open(0,0)
spi.max_speed_hz = 1000000 #통신속도 지정

def analog_read(portChanner):
    adc = spi.xfer2([1, (8+portChanner)<<4, 0])
    data = ((adc[1]&3)<<8)+adc[2]
    return data