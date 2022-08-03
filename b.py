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
  tilt = float(input(" 0 < angle < 180"))
  tangle = tilt_angle(tilt)
  try: 
   my_pwm_t.start(tangle)
   my_pwm_t.ChangeDutyCycle(tangle)
   time.sleep(0.1)
  except KeyboardInterrupt:
    continue
