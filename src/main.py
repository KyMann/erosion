from Erosion import startingElevation
from Drawing import draw

name = 'test2' + '.csv'
startingElevation.generateStartingElevation(name)

draw.draw(name)


