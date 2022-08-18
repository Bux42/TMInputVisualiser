class TMInput:
    def __init__(self, time, steer, accel, brake):
        self.time = int(time)
        self.steer = float(steer)
        self.accel = int(accel)
        self.brake = int(brake)
