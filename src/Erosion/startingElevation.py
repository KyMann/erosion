import csv
import random
import os
try:
    from ..config import StartingDataDirectory
except:
    from config import StartingDataDirectory

def randomZ(z_max):
    #TODO: introduce some sort of smoothing over this, maybe a perlin noise?
    return random.randint(0, z_max)

def generateStartingElevation(name, x_width=25, y_width=20, z_max=400):
    #TODO: save the file into the StartingData directory
    fileName = os.path.join(StartingDataDirectory, name)
    with open(fileName, 'w', newline='') as csvfile:
        elevationwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        columnHeaders = ',' + ','.join(map(str, range(x_width)))
        elevationwriter.writerow(columnHeaders)
        #then every row starts with y index, followed by x random numbers
        for y in range(y_width):
            row = str(y) + ','
            for x in range(x_width):
                row = row + str(randomZ(z_max)) + ','
            elevationwriter.writerow(row)

if __name__ == '__main__':
    generateStartingElevation(name='test.csv')


