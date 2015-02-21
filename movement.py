import time

left_servo_velocity = 0
right_servo_velocity = 0
WHEEL_CIRCUMFERENCE = 0

#speed in meters/second, distance in meters
def move_forward(speed, distance):

	WHEEL_CONSTANT = 1
	start_time = time.time()

	left_servo_velocity = speed
	right_servo_velocity = speed

	speed_in_meters_per_second = WHEEL_CONSTANT * speed * WHEEL_CIRCUMFERENCE

	while True:
		current_time = time.time()
		if (current_time - start_time >= distance / speed_in_meters_per_second):
			break

	left_servo_velocity = 0
	right_servo_velocity = 0

#speed in radians/second, angle in radians
def turn_right(speed, angle):

	TURNING_CONSTANT = 1
	start_time = time.time()

	left_servo_velocity = speed
	right_servo_velocity = -speed

	speed_in_radians_per_second = TURNING_CONSTANT * speed

	while True:
		current_time = time.time()
		if (current_time - start_time >= angle / speed_in_radians_per_second):
			break

	left_servo_velocity = 0
	right_servo_velocity = 0