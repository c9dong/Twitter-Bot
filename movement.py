import RPi.GPIO as GPIO
import time, math

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
left_pwm = GPIO.PWM(12, 100)
left_pwm.start(15)

#GPIO.setup(33, GPIO.OUT)
right_pwm = GPIO.PWM(33, 100)
right_pwm.start(15)

MAX_ANGULAR_SPEED = 3 * math.pi # fastest possible angular speed of a wheel (radians/second)
MAX_TURNING_SPEED = 0.7 * math.pi # fastest possible angular speed of the entire robot (radians/second)
WHEEL_CIRCUMFERENCE = 0.2775 # circumference of each wheel (meters)

def move(distance, speed = 1):
    """
    Moves linearly by distance `distance` (meters) at speed `speed` (0 to 1).
    """
    assert 0 <= speed <= 1

    left_pwm.ChangeDutyCycle(15 + 5 * speed * (1 if distance >= 0 else -1))
    right_pwm.ChangeDutyCycle(15 - 5 * speed * (1 if distance >= 0 else -1))

    speed_meters_per_second = speed * MAX_ANGULAR_SPEED * WHEEL_CIRCUMFERENCE
    time.sleep(abs(distance) / speed_meters_per_second)

    left_pwm.ChangeDutyCycle(15)
    right_pwm.ChangeDutyCycle(15)

def turn(angle, speed = 1):
    """
    Turns in-place by angle `angle` (radians) at angular speed `speed` (0 to 1).
    """
    assert 0 <= speed <= 1

    duty = 15 - 5 * speed * (1 if angle >= 0 else -1)
    left_pwm.ChangeDutyCycle(duty)
    right_pwm.ChangeDutyCycle(duty)

    speed_radians_per_second = speed * MAX_TURNING_SPEED
    time.sleep(abs(angle) / speed_radians_per_second)
    
    left_pwm.ChangeDutyCycle(15)
    right_pwm.ChangeDutyCycle(15)

if __name__ == "__main__":
    move(10)
    turn(math.pi / 2)
