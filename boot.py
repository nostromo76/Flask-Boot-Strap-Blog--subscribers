from flask import Flask, render_template, url_for, flash, redirect,request


app = Flask(__name__)

contacts=[]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/contact")
def contact():
    return render_template('contact.html',title='Contact')

@app.route('/form',methods=["POST"])
def form():

    first_name=request.form.get("first_name")
    last_name=request.form.get('last_name')
    email=request.form.get('email')
    contacts.append(f"{first_name} {last_name} |{email}")
    return render_template('form.html',title='form',contacts=contacts)





if __name__ == '__main__':
    app.run(debug=True)