#Reciving a message mock!!
from flask import Flask, render_template, request
from test import detect_intent_texts
import os
from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def recieve_message():
    if(request.method =='POST'):
        text = request.form.get("sms")
        number = request.form.get("sms-number")
        detect_intent_texts(str(number),str(number)+" "+text)
    return render_template('index.html')
if __name__ == '__main__':
   app.run(debug = True)