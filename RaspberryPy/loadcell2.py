#! /user/bin/env python3

# 모듈

import serial
import RPi.GPIO as GPIO
import time
from datetime import datetime

# firebase module

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# firebase document name 불러오기
while True:
    try :
        f = open("/home/pi/Desktop/id", 'r')
        id_data = f.readline()
        break

    except FileNotFoundError:  # 파일이 생성되어 있지 않은 경우
        print("블루투스 연결이 필요합니다.")
        time.sleep(3600)

# firestore 접근하기

cred = credentials.Certificate("/home/pi/Desktop/learndry-bin-firebase-adminsdk-dqbsn-4dc8a30be2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 받아온 id값에 해당하는 문서 열기

doc_ref = db.collection(u'datas').document(id_data)

doc_ref_FA_p2 = doc_ref.collection(u'featureAnalysis').document(u'period2')



# 라즈베리파이 초음파센서 작동시키기

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

trig = 19
echo = 26

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
    while True :
        GPIO.output(trig, False)
        time.sleep(0.1)    # need test!
        GPIO.output(trig, True)
        time.sleep(0.0001)
        
        GPIO.output(trig, False)
        
        while GPIO.input(echo) == 0 :
            pulse_start = time.time()
            
        while GPIO.input(echo) == 1 :
            pulse_end = time.time()

        # 거리 계산 기준치(40cm) 미만이면 loadcell 센서 작동

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        if distance < 40:

            # loadcell 센서 동작 serial 통신
            '''
            while True:

                # 다른 python 파일에서 data값을 올리고 있는 경우 동작x

                if doc_ref.get()['on_off2'] == 1:
                    time.sleep(5000)
                    continue
                else:
                    break
            ''' 
            # 실제 serial 통신 동작 부분

            if __name__ == '__main__':
                ser = serial.Serial('/dev/ttyUSB0', 57600, timeout = 1)
                ser.flush()

                while True:
                    if ser.in_waiting > 0:
                        line = ser.readline().decode('utf-8').rstrip()
                        # print(line)
                        
                        if float(line) == -1000:
                            continue

                        data = float(line)

                        break

                # data < 0 인 순간 => 빨래하는 날이므로 빨래를 언제, 얼마나 하는지 데이터 저장

                if data <= - 0.1 :
                    
                    print(data)

                    # 오늘 날짜 불러오기

                    date = datetime.today()

                    # 업데이트 되기전 빨래통의 무게를 빨래양으로 db에 업데이트

                    pre_weight = doc_ref.get().to_dict()['weight2']
                    doc_ref_FA_p2.update({
                        date.strftime("%Y%m%d") : pre_weight
                    })

                    # 빨래양과 주기 가져오기

                    dic_ideal = doc_ref_FA_p2.get().to_dict()
                    
                    print(dic_ideal)
                    
                    list_d = list(dic_ideal.keys())
                    list_d.sort()
                    
                    list_w = list(dic_ideal.values())
                    
                    
                    count = 0  # 빨래 한 날의 수
                    sum_d = 0  # 날짜의 차이를 더함
                    sum_w = sum(list_w)  # weight를 더함

                    # for 문 item key : 날짜, value : 무게
                    for day in list_d:
                        
                        if count > 0:
                            
                            day1 = datetime.strptime(pre_day, '%Y%m%d')
                            day2 = datetime.strptime(day, '%Y%m%d')
                            
                            delta_time = (day2 - day1).days

                            sum_d += delta_time
                        
                        pre_day = day
                        count += 1 
                    
                    mean_w = sum_w / count  # 사용자의 평균 빨래양

                    if count > 1:
                        mean_d = sum_d / (count - 1)
                    else:
                        mean_d = 7 # 주기 초기값?  주기 초깃값을 7로 설정

                    # 평균빨래양, 평균 주기 업데이트 

                    doc_ref.collection(u'userinfo').document(u'userFeature').update({
                        u'ideal_w2' : mean_w,
                        u'period_w2' : mean_d
                        })

                # weight2값 업데이트, on_off 업데이트

                doc_ref.update({
                    u'weight2' : data
                    })


except:
    GPIO.cleanup()