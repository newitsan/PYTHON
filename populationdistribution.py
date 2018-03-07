from .population import *

class populationdistribution(population):
    def __init__(self,male,female,ratio):
        super(). __init__(male,female)
        self.ratio=ratio
    def populationmethod1(self):
        print("male and female ratio in %s"  %self.ratio)
