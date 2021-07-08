

seedsType = ['wheat', 'corn', 'sunflower', 'barley', 'rape', 'peas', 'soy']

class ConfigSeeds :
    def __init__(self, numberSeedsPoint = 0 , seedType = ''):
        self.numberSeedsPoint = numberSeedsPoint
        self.seedType = seedType

    def _repr_(self):
        return 'ConfigSeeds(%i, %s) ' % (self.numberSeedsPoint, self.seedType)

