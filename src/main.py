import os

from Erosion import startingElevation
from Drawing import draw

def main():
    name = 'test2' + '.csv'
    startingElevation.generateStartingElevation(name)

    draw.draw(name)

if __name__ == '__main__':
    main()
