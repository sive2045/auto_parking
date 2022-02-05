from crypt import methods
from flask import Flask, redirect, render_template
from Ultrasonic import *
import Car_Motor
import time

car = Car_Motor.Car_Motor()
sonic = UltraSonic()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/go', methods=['GET'])
def go():
    car.Car_Run(150, 150)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/go_left', methods=['GET'])
def go_left():
    car.Car_Run(50, 150)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/go_right', methods=['GET'])
def go_right():
    car.Car_Run(150, 50)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/left', methods=['GET'])
def turn_left():
    car.Car_Left(50, 150)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/right', methods=['GET'])
def turnright():
    car.Car_Right(150, 0)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/back', methods=['GET'])
def back():
    car.Car_Back(150, 150)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/back_left', methods=['GET'])
def back_left():
    car.Car_Back(50, 150)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state, distance=distance)

@app.route('/back_right', methods=['GET'])
def back_right():
    car.Car_Back(150, 50)
    time.sleep(0.3)
    car.Car_Stop()
    state = '주행 중'
    return render_template('main.html',state=state)

@app.route('/auto_parking', methods=['GET'])
def auto_parking():
    state='주차 중'
    car.Car_Run(50,50)
    time.sleep(1)
    car.Car_Stop()
    time.sleep(0.3)
    # parking while dist >= 5
    try:
        while True:
            distance = sonic.Distance_test()
            if distance < 5:
                car.Car_Stop()
                break
            else:
                car.Car_Run(25,100)
            time.sleep(0.03)
    except KeyboardInterrupt:
        pass
    car.Car_Stop()
    print("Parking Ending")
    state='주차 완료'
    GPIO.cleanup()
    return render_template('main.html',state=state)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")