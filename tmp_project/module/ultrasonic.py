import RPi.GPIO as GPIO
import time

class UltraSonic(object):
    """
    Ultrasonic set class
    """
    def __init__(self):
        GPIO.setwarnings(False)
        self.EchoPin = 18
        self.TrigPin = 16
        #Set GPIO port to BCM coding mode
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.EchoPin,GPIO.IN)
        GPIO.setup(self.TrigPin,GPIO.OUT)

    #Ultrasonic function 
    def Distance(self):
        GPIO.output(self.TrigPin,GPIO.LOW)
        time.sleep(0.000002)
        GPIO.output(self.TrigPin,GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.TrigPin,GPIO.LOW)

        t3 = time.time()

        while not GPIO.input(self.EchoPin):
            t4 = time.time()
            if (t4 - t3) > 0.03 :
                return -1
        t1 = time.time()
        while GPIO.input(self.EchoPin):
            t5 = time.time()
            if(t5 - t1) > 0.03 :
                return -1

        t2 = time.time()
        time.sleep(0.01)
        #print ("distance_1 is %d " % (((t2 - t1)* 340 / 2) * 100))
        return ((t2 - t1)* 340 / 2) * 100
    
    def Distance_test(self):
        num = 0
        ultrasonic = []
        while num < 5:
                distance = self.Distance()
                #print("distance is %f"%(distance) )
                while int(distance) == -1 :
                    distance = self.Distance()
                    #print("Tdistance is %f"%(distance) )
                while (int(distance) >= 500 or int(distance) == 0) :
                    distance = self.Distance()
                    #print("Edistance is %f"%(distance) )
                ultrasonic.append(distance)
                num = num + 1
                time.sleep(0.01)
        distance = (ultrasonic[1] + ultrasonic[2] + ultrasonic[3])/3
        print("distance is %f"%(distance) ) 
        return distance