from time import sleep
from gpiozero import AngularServo

servo = AngularServo(18 , min_pulse_width=0.0006 , max_pulse_width=0.0023)

while True:

    for angle in [90 , 0 , -90]: 
        print(f"Moving to angle: {angle}")
        servo.angle = angle
        sleep(2)