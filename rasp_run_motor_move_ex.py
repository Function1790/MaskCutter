import Detect_Mask as dt
import pigpio
from time import sleep

servo_pin_a = 11          #마스크누르기모터
servo_pin_b = 13          #마스크자르기모터
servo_pin_c = 15          #마스크밀기모터
in_degree_a = 0
in_degree_b = 0
in_degree_c = 0
degree_a = 600+(in_degree_a * 10)
degree_b = 600+(in_degree_b * 10)
degree_c = 600+(in_degree_c * 10)

pi.set_servo_pulsewidth(servo_pin_a, 0)
pi.set_servo_pulsewidth(servo_pin_b, 0)
pi.set_servo_pulsewidth(servo_pin_c, 0)
sleep(1)

while True:
    #마스크가 있고, 잘렸다면
    if dt.isExistMask(True) & dt.isMaskSliced(True) :
        in_degree_a = 120
        degree_a = 600+(in_degree_a * 10)
        pi.set_servo_pulsewidth(servo_pin_c, degree_a)
        sleep(1)
        in_degree = 30
        degree_a = 600+(in_degree * 10)
        pi.set_servo_pulsewidth(servo_pin_c, degree_a)
        sleep(1)
        
    #마스크가 있고, 안잘렸다면
    elif dt.isExistMask(True) & dt.isMaskSliced(False):
        #마스크 자르기 (모터 움직임)
        in_degree_b = 90
        in_degree_c = 175
        degree_b = 600+(in_degree_b * 10)
        degree_c = 600+(in_degree_c * 10)
        pi.set_servo_pulsewidth(servo_pin_b, degree_b)
        sleep(1)
        pi.set_serco_pulsewidth(servo_pin_c, degree_c)
        sleep(1)
        in_degree_b = 5
        in_degree_c = 5
        degree_b = 600+(in_degree_b * 10)
        degree_c = 600+(in_degree_c * 10)
        pi.set_servo_pulsewidth(servo_pin_b, degree_b)
        sleep(1)
        pi.set_servo_pulsewidth(servo_pin_c, degree_c)
        sleep(1)

    sleep(1)


    