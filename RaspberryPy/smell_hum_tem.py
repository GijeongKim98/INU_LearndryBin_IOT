import serial
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# document name 

f = open("/home/pi/Desktop/id", 'r')
id_data = f.readline()

# firestore update 
cred = credentials.Certificate("/home/pi/Desktop/learndry-bin-firebase-adminsdk-dqbsn-4dc8a30be2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
                
doc_ref = db.collection(u'datas').document(id_data)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    count = 0
    while True:
        if ser.in_waiting > 0:
            nh4 = ser.readline().decode('utf-8').rstrip()
            hum = ser.readline().decode('utf-8').rstrip()
            if float(hum) < 0 :
                continue
            tem = ser.readline().decode('utf-8').rstrip()
                        
            nh4_data = float(nh4)
            hum_data = float(hum)
            tem_data = float(tem)
            
            doc_ref.update({
                    u'smell': nh4_data,
                    u'hum': hum_data,
                    u'temp': tem_data
                    })
            
            time.sleep(3600)
                        
                        