import RPi.GPIO as GPIO
import time, math

SERVO_NEUTRAL, SERVO_EXTENT = 14, 6
MAX_ANGULAR_SPEED = 1.2 * math.pi # fastest possible angular speed of a wheel (radians/second)
MAX_TURNING_SPEED = 0.7 * math.pi # fastest possible angular speed of the entire robot (radians/second)
WHEEL_CIRCUMFERENCE = 0.045 # circumference of each wheel (meters)

# set up PWM pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
left_pwm = GPIO.PWM(12, 100)
left_pwm.start(15)
GPIO.setup(33, GPIO.OUT)
right_pwm = GPIO.PWM(33, 100)
right_pwm.start(15)

def move(distance, speed = 1):
    """
    Moves linearly by distance `distance` (meters) at speed `speed` (0 to 1).
    """
    assert 0 <= speed <= 1

    left_pwm.ChangeDutyCycle(SERVO_NEUTRAL + SERVO_EXTENT * speed * (1 if distance >= 0 else -1))
    right_pwm.ChangeDutyCycle(SERVO_NEUTRAL - SERVO_EXTENT * speed * (1 if distance >= 0 else -1))

    speed_meters_per_second = speed * MAX_ANGULAR_SPEED * WHEEL_CIRCUMFERENCE
    time.sleep(abs(distance) / speed_meters_per_second)

    left_pwm.ChangeDutyCycle(SERVO_NEUTRAL)
    right_pwm.ChangeDutyCycle(SERVO_NEUTRAL)

def turn(angle, speed = 1):
    """
    Turns in-place by angle `angle` (radians) at angular speed `speed` (0 to 1).
    """
    assert 0 <= speed <= 1

    duty = SERVO_NEUTRAL - SERVO_EXTENT * speed * (1 if angle >= 0 else -1)
    left_pwm.ChangeDutyCycle(duty)
    right_pwm.ChangeDutyCycle(duty)

    speed_radians_per_second = speed * MAX_TURNING_SPEED
    time.sleep(abs(angle) / speed_radians_per_second)
    
    left_pwm.ChangeDutyCycle(SERVO_NEUTRAL)
    right_pwm.ChangeDutyCycle(SERVO_NEUTRAL)

if __name__ == "__main__":
    move(10)
    turn(math.pi / 2)
