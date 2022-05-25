class DriveBot:

    def __init__ (self, motor_speed=0, sensor_range=0, direction=0):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot(5, 10, 90)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

new_speed = robot_1.control_bot(10, 180)
new_sensor_range = robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)