from flask import Flask, render_template, url_for, request, redirect        #$env:FLASK_APP = "server.py"   --->postavljamo za pokrenuti server
import csv
app=Flask(__name__)                                                         #flask run                      --->pokreće flask server
print(__name__)                                                             #$env:FLASK_ENV = "development" --->debug mode

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\nE-mail: {email} , Subject: {subject} , Message: {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except :
            return 'Did not save to database'
    else:
        print('something went wrong. Try again!')