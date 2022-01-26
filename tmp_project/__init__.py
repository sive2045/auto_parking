from crypt import methods
from flask import Flask, redirect, render_template
import Car_Motor
import time

car = Car_Motor.Car_Motor()
del car
car = Car_Motor.Car_Motor()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    car.Car_Stop()
    return render_template('main.html')

@app.route('/go', methods=['GET'])
def go():
    car.Car_Run(150, 150)
    time.sleep(0.3)
    return redirect('/')

@app.route('/go_left', methods=['GET'])
def go_left():
    car.Car_Run(50, 150)
    time.sleep(0.3)
    return redirect('/')

@app.route('/go_right', methods=['GET'])
def go_right():
    car.Car_Run(150, 50)
    time.sleep(0.3)
    return redirect('/')

@app.route('/left', methods=['GET'])
def turn_left():
    car.Car_Left(50, 150)
    time.sleep(0.3)
    return redirect('/')

@app.route('/right', methods=['GET'])
def turnright():
    car.Car_Right(150, 0)
    time.sleep(0.3)
    return redirect('/')

@app.route('/back', methods=['GET'])
def back():
    car.Car_Back(150, 150)
    time.sleep(0.3)
    return redirect('/')

@app.route('/back_left', methods=['GET'])
def back_left():
    car.Car_Back(50, 150)
    time.sleep(0.3)
    return redirect('/')

@app.route('/back_right', methods=['GET'])
def back_right():
    car.Car_Back(150, 50)
    time.sleep(0.3)
    return redirect('/')

@app.route('/auto_parking', methods=['GET'])
def auto_parking():
    car.Car_Run(150, 60)
    time.sleep(1.7)
    car.Car_Stop()

    car.Car_Back(80, 145)
    time.sleep(1)
    car.Car_Stop()

    car.Car_Back(150, 150)
    time.sleep(0.8)
    car.Car_Stop()
    return redirect('/')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")