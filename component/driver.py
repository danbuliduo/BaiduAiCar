#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import sys
sys.path.append("../")
sys.path.append("../component")
from component.chassis import Chassis

class Driver:
    '''
    巡航驱动类
    '''
    angle_threshold = 0.2

    def __init__(self):
        self.full_speed = 40
        self.chassis = Chassis(115200)
        self.speed = self.full_speed
        self.proportion = 1.5

    def steer(self, angle):
        self.chassis.steer(angle)

    def run(self, l_speed, r_speed):
        self.chassis.move([l_speed, r_speed, l_speed, r_speed])

    def move(self, speed):
        self.chassis.move(speed)

    def stop(self):
        self.chassis.stop()

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.chassis.speed = speed

    def set_proportion(self, proportion):
        self.proportion = proportion

    def set_kx(self, kx):
        self.chassis.kx = kx

    def get_min_speed(self):
        return self.chassis.min_speed

    def change_posture(self, base_speed):

        l_speed = base_speed
        r_speed = base_speed * 0.4
        self.run(l_speed, r_speed)
        time.sleep(1)
        l_speed = base_speed * 0.4
        r_speed = base_speed
        self.run(l_speed, r_speed)
        time.sleep(1)
        self.stop()

    def change_posture_cm(self, distance):
        base_speed = 15
        speed_ratio = 0.4
        drive_time = distance * 0.9
        if distance < 2:
            speed_ratio = 0.2
            drive_time = distance * 0.95
        elif distance < 4:
            speed_ratio = 0.15
            drive_time = distance * 0.75
        else:
            speed_ratio = -0.05
            drive_time = distance * 0.5
        l_speed = base_speed
        r_speed = base_speed * speed_ratio
        self.run(l_speed, r_speed)
        time.sleep(drive_time)
        l_speed = base_speed * speed_ratio
        r_speed = base_speed
        self.run(l_speed, r_speed)
        time.sleep(drive_time - 0.5)
        self.stop()


if __name__ == '__main__':
    d = Driver()
    while True:
        d.steer(1)
        #time.sleep(2)
        #d.set_speed(20)
        #d.run(25, 25)
        #time.sleep(2)
        #d.stop()
        #time.sleep(1)


