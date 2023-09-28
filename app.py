from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/events")
def events():
    return render_template('events.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route('/contact')
def open_contact():
    return render_template("contact.html")

@app.route('/submit', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert data into the contacts table
        conection = sqlite3.connect("contact.db")
        cursor = conection.cursor()
        query = "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)"
        cursor.execute(query,(name,email,message))
        conection.commit()
        conection.close()
        return render_template('contact.html')