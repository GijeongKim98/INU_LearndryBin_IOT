# firebase module

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


from datetime import datetime, timedelta

cred = credentials.Certificate("/home/pi/Desktop/learndry-bin-firebase-adminsdk-dqbsn-4dc8a30be2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

f = open("/home/pi/Desktop/id", 'r')
id_data = f.readline()

doc_ref = db.collection(u'datas').document(id_data)

doc_ref_W_I1 = doc_ref.collection(u'featureAnalysis').document(u'weight_increment1')  # 빨래를 할때 얼마나 빨래하고 언제 하는지

doc_ref_W_I2 = doc_ref.collection(u'featureAnalysis').document(u'weight_increment2')  # 빨래를 할때 얼마나 빨래하고 언제 하는지

doc_ref_W_I2.set({})
doc_ref_W_I1.set({})


date = datetime.today()

for i in range(15):
    
    date_slicing = date - timedelta(i)
    
    date_slicing = date_slicing.strftime('%Y%m%d')
    
    doc_ref_W_I1.update({  # 빨래한 날
                date_slicing: 1
            })
    
    
    doc_ref_W_I2.update({  # 빨래한 날
                date_slicing: 1
            })
    
