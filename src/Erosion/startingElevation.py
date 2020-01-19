import csv
import random

def randomZ(z_max):
    #TODO: introduce some sort of smoothing over this, maybe a perlin noise?
    return random.randint(0, z_max)

#TODO: generate a starting .csv of the form found in testData
def generateStartingElevation(fileName, x_width=25, y_width=20, z_max=400):
    #TODO: save the file into the StartingData directory
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

generateStartingElevation(fileName='test.csv')


