from datetime import datetime

# firebase module

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("C:/Users/kkj98/test1-9da5a-firebase-adminsdk-1yzz5-14ce67d173.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'test2').document(u'aaa')

doc_ref.set({})

'''
dict1 = doc_ref.get().to_dict()

if '20220402'in dict1.keys():
    print(dict1['20220402'])
else:
    print('djkdjk')
print(list(dict1.keys())[0])

print(len(dict1))

print(doc_ref.get().to_dict()) 
for i,j in dict1.items():
    print(i, j)

doc_ref.update({
    '20220401' : firestore.DELETE_FIELD
})


day1 = '20170203'

day2 = '20170208'

day1_1 = datetime.strptime(day1, "%Y%m%d")
day2_1 = datetime.strptime(day2, "%Y%m%d")

print(day1_1)
print(day2_1)

print(type((day2_1 - day1_1).days))

'''