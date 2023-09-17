import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# import speechrecognition as sp

# file_name=sp.speech()

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://contactlessvending-default-rtdb.firebaseio.com/"
})
ref= db.reference('Students')
data={
    "Devansh":
        {
            "name":"Devansh Matha",
            "Credits":69
        },
    "Deepak":
    {
        "name":"Deepak",
        "Credits":70
    }
}
for key,value in data.items():
    ref.child(key).update(value)

