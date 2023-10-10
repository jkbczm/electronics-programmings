import serial
from flask import Flask,render_template,request
import time
app=Flask(__name__)
arduino = serial.Serial('COM29',9600)
arduino.close()

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/send_data',methods = ['POST'])
def send_data():
    data = request.form['data']
    arduino.open()
    arduino.write(data.encode())
    time.sleep(1)
    arduino.close()
    return "dane zostaly wyslane"    
 

if __name__=='__main__':
    app.run(debug =True)