from time import sleep
from gpiozero import AngularServo

ud_servo = AngularServo(18 , min_pulse_width=0.0006 , max_pulse_width=0.0022)
lr_servo = AngularServo(17 , min_pulse_width=0.0006 , max_pulse_width=0.0022)

while True:

    for index , servo in enumerate([ud_servo , lr_servo]):
        
        print(f"Moving servo {index + 1} to min")
        servo.min()
        sleep(2)
        print(f"Moving servo {index + 1} to mid")
        servo.mid()
        sleep(2)
        print(f"Moving servo {index + 1} to max")
        servo.max()
        sleep(2)
        for i in range(-100 , 101):    
            servo.value = i / 100

