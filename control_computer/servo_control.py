from time import sleep
from gpiozero import AngularServo

ud_servo = AngularServo(18 , min_pulse_width=0.0006 , max_pulse_width=0.0023)
lr_servo = AngularServo(17 , min_pulse_width=0.0006 , max_pulse_width=0.0023)

while True:

    for index , servo in enumerate([ud_servo , lr_servo]):
        for angle in [90 , 0 , -90]: 
            print(f"Moving servo {index + 1} to angle: {angle}")
            servo.angle = angle
            sleep(2)