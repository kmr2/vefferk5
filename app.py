from flask import Flask
from pyrebase import pyrebase

app = Flask(__name__)

# tengin við firebase realtime database á firebase.google.com ( db hjá danielsimongalvez@gmail.com )
config = {
    "apiKey":"AIzaSyB6L9PLOIa-y8spupA2UFiegQGN7gmp12E",
    "authDomain": "vefferk5.firebaseapp.com",
    "databaseURL": "https://vefferk5.firebaseio.com",
    "projectId": "vefferk5",
    "storageBucket": "vefferk5.appspot.com",
    "messagingSenderId": "683227377425",
    "appId": "1:683227377425:web:1317e8ebac70100ee126b0",
    "measurementId": "G-0BBSXPYZF8"


}

fb = pyrebase.initialize_app(config)
db = fb.database()

# Test route til að setja gögn í db
@app.route('/')
def index():
    return "Skrifað í grunn"

# Test route til að sækja öll gögn úr db
@app.route('/lesa')
def lesa():
    return "Lesum úr grunni"

if __name__ == "__main__":
	app.run(debug=True)

# skrifum nýjan í grunn hnútur sem heitir notandi 
# db.child("notandi").push({"notendanafn":"dsg", "lykilorð":1234}) 

# # förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items())
