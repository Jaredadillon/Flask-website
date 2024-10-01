import email
import smtplib
import sqlite3 as sql
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def start():
    return redirect(url_for('index'), code=302)


@app.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('index.html')
    return url_for('static', filename='styles.css')


@app.route('/donate')
def donate():
    return render_template('donate.html')
    return url_for('static', filename='styles.css')


@app.route('/hungerfacts')
def hungerfacts():
    return render_template('hungerfacts.html')
    return url_for('static', filename='styles.css')


@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')
    return url_for('static', filename='styles.css')


@app.route('/about')
def about():
    return render_template('about.html')
    return url_for('static', filename='styles.css')


@app.route('/homeform', methods=['POST', 'GET'])
def homeform():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('mail')

        # change from test db
        with sql.connect('newsletter.db') as con:
            con.execute('INSERT INTO USER (name, age) values(?, ?)', (name, email))

            data = con.execute("SELECT * FROM USER")
            for row in data:
                print(row)

        return redirect(url_for('index'), code=302)


@app.route('/aboutform', methods=['POST', 'GET'])
def aboutform():
    if request.method == 'POST':
        name = request.form.get('Name')
        address = request.form.get('Address')
        message = request.form.get('Message')

        aboutEmail = f'Subject: {name} sent us a message.\n\nName: {name}\n' \
                     f'Address: {address}\n\n-- Message --\n{message}'

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('jaredadillon76@gmail.com', '8cY8xWuVStHLqsF')

        # I changed it to your email so you can see it
        smtpObj.sendmail('jaredadillon76@gmail.com', ['mbarnes@asumh.edu'], aboutEmail)
        smtpObj.quit()

        return redirect(url_for('about'), code=302)


@app.route('/volunteerform', methods=['POST', 'GET'])
def volunteerform():
    if request.method == 'POST':
        name = request.form.get('Name')
        address = request.form.get('Address')
        phone = request.form.get('Phone')
        email = request.form.get('Email')
        state = request.form.get('State')
        emergencyName = request.form.get('EmergencyName')
        emergencyPhone = request.form.get('EmergencyPhone')
        relationship = request.form.get('Relationship')
        age = request.form.get('ageCheck')
        male = request.form.get('Male')
        female = request.form.get('Female')
        education = request.form.get('Education')
        serviceYes = request.form.get('Yes')
        serviceNo = request.form.get('No')
        serviceType = request.form.get('Service')
        acceptance = request.form.get('acceptance')

        age = 'No' if not age else 'Yes'
        gender = 'Male' if male else 'Female'
        mandatedService = 'Yes' if serviceYes else 'No'
        serviceType = '' if serviceType == 'Choose...' else 'Service type: ' + serviceType + '\n'
        terms = 'No' if not acceptance else 'Yes'

        volunteerEmail = f'Subject: {name} wants to volunteer for our foodbank!\n-- Contact info --\nEmail: {email}\n' \
                         f'Address: {address} {state}\nPhone: {phone}\n\n-- Emergency contact info --\n' \
                         f'Name: {emergencyName}\nPhone: {emergencyPhone}\nRelationship: {relationship}\n\n' \
                         f'-- Other --\nAre they over 18?: {age}\nGender: {gender}\nHighest education: {education}\n' \
                         f'Is this mandated community service?: {mandatedService}\n{serviceType}' \
                         f'\nDid they accept the terms?: {terms}'

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login('jaredadillon76@gmail.com', '8cY8xWuVStHLqsF')

        # I changed it to your email so you can see it
        smtpObj.sendmail('jaredadillon76@gmail.com', ['mbarnes@asumh.edu'], volunteerEmail)
        smtpObj.quit()

        return redirect(url_for('volunteer'), code=302)


# code to create database

# con = sql.connect('newsletter.db')
#
# with con:
#     con.execute("""
#         CREATE TABLE USER (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             age INTEGER
#         );
#     """)


app.run()
