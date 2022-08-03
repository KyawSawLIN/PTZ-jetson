import Jetson.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)

my_pwm_p = GPIO.PWM(33,50)
my_pwm_t = GPIO.PWM(32,50)

list_t = [90]
counter = 1

def tilt_angle(anglet):

    if anglet <= 180:
     var = (anglet * 2 / 270 ) + 0.4
     period_t = (var * 100) / 20
     return period_t
    else:
      print("should be under 180 degree")

def pan_angle(anglep):
    var = (anglep * 2 / 360 ) + 0.5
    period_p = (var * 100) / 20
    return period_p

def tilt_servo_control(current_tilt_angle,counter):


   list_t.append(current_tilt_angle)
   print("previous tilt angles : ", list_t)
   print(counter)
   previous_tilt_angle = list_t[counter-1]

   while previous_tilt_angle != current_tilt_angle:

        if previous_tilt_angle < current_tilt_angle:
            for i in range(previous_tilt_angle, current_tilt_angle+5, 5):
                my_servo_2_angle = tilt_angle(i)
                my_servo_2_angle = round(my_servo_2_angle,1)
                my_pwm_t.ChangeDutyCycle(my_servo_2_angle)
                time.sleep(0.05)
                print("angle ## ", i)
                previous_tilt_angle = i

        if previous_tilt_angle > current_tilt_angle:
            for j in range(previous_tilt_angle, current_tilt_angle-5, -5):
                my_servo_2_angle = tilt_angle(j)
                my_servo_2_angle = round(my_servo_2_angle,1)
                my_pwm_t.ChangeDutyCycle(my_servo_2_angle)
                time.sleep(0.05)
                print("angle ## ", j)
                previous_tilt_angle = j

while 1:
 d = input('pan or tilt')
 if d == 'p':
  pan = float(input(" 0 < angle  < 360 : "))
  pangle = pan_angle(pan)
  try:
   my_pwm_p.start(pangle)
   my_pwm_p.ChangeDutyCycle(pangle)
   time.sleep(0.1)
  except KeyboardInterrupt:
    continue
 elif d == 't':
  tilt = int(input(" 0 < angle < 180") )
  my_pwm_t.start(5.3)
  tilt_servo_control(tilt, counter)
  counter += 1
 elif d == 'i':
     my_pwm_p.ChangeDutyCycle(2.5)
     tilt_servo_control(90,counter)
     break