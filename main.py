import geometry
FORMAT = '>8,.2f'

def getUserInput():
    size = int(input('\nEnter Radius/Side: '))
    unit =     input('Enter Units of Measurement: ')
    return size, unit 

def dotLine():
    print('--------------')

def displayCircleResults(size,unit):
    circleCircum = geometry.circleA(size)
    circleArea   = geometry.circleB(size)
    print('\n\nCircle Results')
    dotLine()
    print('Circumference:',format(circleCircum,FORMAT),  'linear',unit)
    print('Area:         ',format(circleArea,FORMAT),    'square',unit)

def displaySphereResults(size,unit):
    sphereVolume   = geometry.sphereA(size)
    sphereSurfArea = geometry.sphereB(size)
    print('\n\nSphere Results')
    dotLine()
    print('Volume:       ',format(sphereVolume,FORMAT),   'cubic',unit)
    print('Surface Area: ',format(sphereSurfArea,FORMAT),'square',unit)

def displaySquareResults(size,unit):
    squarePerim = geometry.squareA(size)
    squareArea  = geometry.squareB(size)
    print('\n\nSquare Results')
    dotLine()
    print('Perimeter:    ',format(squarePerim,FORMAT),   'linear',unit)
    print('Area:         ',format(squareArea, FORMAT),   'square',unit)

def displayCubeResults(size,unit):
    cubeVolume   = geometry.cubeA(size)
    cubeSurfArea = geometry.cubeB(size)
    print('\n\nCube Results')
    dotLine()
    print('Volume:       ',format(cubeVolume,FORMAT),     'cubic',unit)
    print('Surface Area: ',format(cubeSurfArea,FORMAT),  'square',unit)

    
def main():
    size, unit = getUserInput()
    displayCircleResults(size,unit)
    displaySphereResults(size,unit)
    displaySquareResults(size,unit)
    displayCubeResults  (size,unit)
    
main()
