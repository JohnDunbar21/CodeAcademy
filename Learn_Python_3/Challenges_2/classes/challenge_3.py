class DriveBot:

    def __init__ (self, motor_speed=0, sensor_range=10, direction=180):
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_2 = DriveBot(35, 25, 75)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)