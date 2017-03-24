EmptyRoomCheck
--------------

- 회의실이 비어있는지 확인하기 위한 모듈용 코드

고려할 사항
--------
#### 일반 case
- lignt on (형광등 켜짐)
- TV, 빔프로젝트 켜짐
- 누군가 말을 하고 있음


#### 예외 case
##### light off (형광등 꺼짐)
- TV나 빔프로젝트만 켜둠 (빛이 있긴 있음)
- 누군가 말을 하고 있음
- 창문이 열려있고 세차장같은 곳에서 소리가 발생

##### lignt on (형광등 켜짐)
- 말 없이 모니터만 보고 키보드 치는 소리만 남 (e.g.장애 분석중)

사용할 센서 
---------
센서 타입 선택 필요: analog or digital 

- 조도 (CDS, Photoresistor sensor)
  - [광센서 사용 예](https://pimylifeup.com/raspberry-pi-light-sensor/)
  - [light sensor 사용 예제](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading)
  
- 소리 (사람의 소리 감지)

  - [FC-04 데모](http://www.instructables.com/id/Simple-FC-04-Sound-Sensor-Demo/)


SYSTEM
------
![alt tag](https://raw.githubusercontent.com/chocopy-telco/EmptyRoomCheck/master/empty_room.mmd.png)
