import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://contactlessvending-default-rtdb.firebaseio.com/"
})
ref= db.reference('Students')
data={
    "Devansh":
        {
            "name":"heyyydevansh",
            "Credits":69
        }
}
for key,value in data.items():
    ref.child(key).set(value)
