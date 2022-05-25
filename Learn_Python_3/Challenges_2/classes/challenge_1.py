class DriveBot:

    def __init__ (self, motor_speed=0, sensor_range=0, direction=0):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction

robot_1 = DriveBot(5, 10, 90)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)