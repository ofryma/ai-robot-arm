from time import sleep
from gpiozero import AngularServo

ud_servo = AngularServo(18 , min_pulse_width=0.0005 , max_pulse_width=0.0023)
lr_servo = AngularServo(17 , min_pulse_width=0.0005 , max_pulse_width=0.0023)

while True:
    for index , servo in enumerate([ud_servo , lr_servo]):
        print(f"Moving servo {index + 1}")
        for angle in range(-90 , 90):
            servo.angle = angle
            sleep(0.1)
        print(f"Finished servo {index+1}")