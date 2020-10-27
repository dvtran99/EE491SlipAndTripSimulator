#!/bin/env python

# from Adafruit_BBIO import GPIO # not using this right now
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP0



import time
import numpy as np
from math import pi

class eqep_ops:

    def __init__(self, eqep):
        self.encoder = RotaryEncoder(eqep)
        self.encoder.setAbsolute()
        self.encoder.enable()


    def read(self):
        return self.encoder.position

    def reset(self):
        self.encoder.zero()

    def __del__(self):
        self.encoder.disable()


class motor_pwm_sweep:
    # Wheel Info
    # We are using 100mm diameter wheels
    wheel_radius = 0.05  # meters
    # Wheel Encoder Info (PPR)
    # Resolution for encoders used is 1024
    ticks_per_rev = 1024

    data = None
    pwm = None
    eqep = None
    eqep2 = None


    def calculate_wheel_rpm(self, encoder_ticks, time_secs):
        revs = float(encoder_ticks / self.ticks_per_rev)
        rpm = (revs * 60) / time_secs
        return rpm

    def calculate_wheel_velocity(self, encoder_ticks, time_secs):
        revs = float(encoder_ticks / self.ticks_per_rev)
        dist_per_rev = float(2 * pi * self.wheel_radius)
        distance = float(revs * dist_per_rev)
        speed = float(distance / time_secs)
        return speed

    def __del__(self):
        self.pwm.cleanup()
