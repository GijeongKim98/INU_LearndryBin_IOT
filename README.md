# INU_LearndryBin_IOT
인천대 컴퓨터공학부 2022 졸업작품 (수야호) - IOT

## LearndryBin

### Members
![image](https://user-images.githubusercontent.com/83777482/211185871-fc80f5dd-7ea3-4042-8188-ed06b2be6c17.png)


### 프로젝트 설명
위 프로젝트는 홀로 생활하는 사람들이 많아지면서 사람들은 빨래에 대해 대부분 방치하거나 제대로된 세탁을 하기 어렵다. 그래서 사람들의 빨래통을 관리할 수 있도록 직접 빨래통을 제작하고 어플을 만들어 사람들의 세탁방법을 개선시키고 빨래날짜를 추천해 비가 오는 날에는 빨래를 하지않도록 한다.

### 프로젝트 목적
어플을 통한 집에 있는 빨래통을 어디서든 관리가 가능하다. 또한 빨래 날짜 추천기능으로 사용자의 빨래습관을 개선할 수 있다.

### 아키텍쳐
![image](https://user-images.githubusercontent.com/83777482/211186020-2b251098-5b1f-448a-be32-013ae3a2c83e.png)
저희가 사용한 오픈소스하드웨어는 라즈베리파이이다. 아두이노와 같이 빨래의 무게, 냄새, 방안의 온습도를 파악한다.

### IOT 세부 아키텍쳐
![image](https://user-images.githubusercontent.com/83777482/211187139-8e7d9589-b7a4-476f-8486-5a918c7e3219.png)
라즈베리파이에 아두이노우노, 2개의 아두이노 미니, 2개의 초음파센서 즉 HC-SR04가 연결 되어있다. 그리고 아두이노우노에는 온습도를 측정하는 DHT-22센서와 냄새(암모니아가스)를 측정하는 MQ-135가 연결되어 있다. 각각의 아두이노 미니는 증폭기인 HX-711, 무게를 측정하는 load-cell sensor가 연결되어 있다. 초음파센서를 사용해서 부피를 측정하는 목적이 아닌 빨래가 들어오는 것을 감지한다. 빨래통을 두개를 사용해서 옷들을 분류할 수 있다.

### IOT 설계
![image](https://user-images.githubusercontent.com/83777482/211187330-0d0ba581-b2ca-48e6-888a-1b2a770da486.png)
### IOT 실제 사진
![image](https://user-images.githubusercontent.com/83777482/211187354-2c227a41-5c2e-4329-ab7f-96fd2b6cd68d.png)




