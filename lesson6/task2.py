# Задание-2:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно)
# комплексными числами \ матрицами \ светофор \ микроволновка

import time

class TrafficLights:
    def __init__(self, redTime, greenTime, yellowTime):
        self.redTime = redTime
        self.greenTime = greenTime
        self.yellowTime = yellowTime
        self.period = redTime + yellowTime + greenTime
        self.startTime = TrafficLights._current_time()

    def get_light(self):
        phase = (TrafficLights._current_time() - self.startTime) % self.period
        if phase < self.redTime:
            return 'Red'
        elif phase < self.redTime + self.greenTime:
            return 'Green'
        else:
            return 'Yellow'

    def _current_time():
        return int(time.time())
        