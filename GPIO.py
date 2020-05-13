# 라즈베리파이일 경우 GPIO pin을 통해 신호를 내보내고 받는 코드

import RPi.GPIO as GPIO

GPIO.setmode( GPIO.BCM )

GPIO.setup( 21, GPIO.OUT )

GPIO.output( 21, True )

GPIO.setup( 21, GPIO.IN )

value_input = GPIO.input(21)
