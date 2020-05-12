import random
import math


class Electric:

    def __init__(self, name):
        self.name = name


class Load(Electric):

    def __init__(self, name, resistance, reactance):
        super().__init__(name)
        self.resistance = resistance
        self.reactance = reactance
        self.__n = (random.randint(1, 100) / 100)

    def current_load(self, voltage):
        self.__current = voltage / math.sqrt((self.resistance ** 2) + (self.reactance ** 2))
        print(f'The current at {voltage}Volt is {round(self.__current, 3)}Amper')
        return self.__current


class Generator(Electric):

    def __init__(self, name, power, voltage):
        super().__init__(name)
        self.power = power
        self.voltage = voltage

    def load_capacity(self, load_c):
        if (self.voltage * load_c) > self.power:
            print('Generator overloaded, expect trouble')
        else:
            print('System working properly')


load1 = Load('address#1', 10, 2)
gen1 = Generator('kuciurgan', 10000, 220)

print(f'The load at {load1.name} has R = {load1.resistance} and X = {load1.reactance}')
print(f'The generator at {gen1.name} gives {gen1.power}VA and stable {gen1.voltage}V')

gen1.load_capacity(load1.current_load(gen1.voltage))

