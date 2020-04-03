from flask import Flask, render_template, request, session, redirect, url_for
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'covid_19'

config = {

    "apiKey": "AIzaSyB6L9PLOIa-y8spupA2UFiegQGN7gmp12E",
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
    return render_template("index.html")

# Test route til að sækja öll gögn úr db
@app.route('/login', methods=['GET', 'POST'])
def login():

    login = False
    if request.method == 'POST':

        notendanafn = request.form['uname']
        lykilorð = request.form['psw']

        u = db.child("notandi").get().val()
        lst = list(u.items())
        for i in lst:
            if notendanafn == i[1]['notendanafn'] and lykilorð == i[1]['lykilorð']:
                login = True
                break

        if login:
            session['logged_in'] = notendanafn
            return redirect("/topsecret")
        else:
            return render_template("nologin.html")

    else:
        return render_template("no_method.html")

@app.route('/register')
def register():
    return render_template('register.html')

# Test route til að sækja öll gögn úr db
@app.route('/doregister', methods=['GET', 'POST'])
def doregister():
    usernames = []
    if request.method == 'POST':

        notendanafn = request.form['uname']
        lykilorð = request.form['psw']

        u = db.child("notandi").get().val()
        lst = list(u.items())
        for i in lst:
            usernames.append(i[1]['notendanafn'])

        if notendanafn not in usernames:
            db.child("notandi").push({"notendanafn": notendanafn, "lykilorð": lykilorð})
            return render_template("registered.html")
        else:
            return render_template("userexists.html")


@app.route('/logout')
def logout():
    session.pop("logged_in", None)
    return render_template("index.html")


@app.route('/topsecret')
def topsecret():
    if 'logged_in' in session:
        return render_template("topsecret.html")
    else:
        return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)

# skrifum nýjan í grunn hnútur sem heitir notandi 
# db.child("notandi").push({"notendanafn":"dsg", "lykilorð":1234}) 

# # förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items())
