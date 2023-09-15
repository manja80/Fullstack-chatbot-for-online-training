from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.secret_key = 'FLASK_KEY'

# Configure PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'training_details'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    mobile = db.Column(db.String(20), nullable=False)


@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        response = request.form.get("response")
        if response.lower() == "yes":
            return redirect(url_for("registration"))
        elif response.lower() == "no":
            return "Thank you for your response. Have a Great Day!"

    return render_template("chatbot.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        mobile = request.form.get("mobile")

        user = User(name=name, email=email, mobile=mobile)

        try:
            db.session.add(user)
            db.session.commit()
            flash('Your details have been securely saved. Thank you!')
            return redirect(url_for('chatbot'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred while saving data: {str(e)}')

    return render_template("registration.html")


if __name__ == "__main__":
    app.run(debug=False)
