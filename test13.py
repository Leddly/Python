from collections import namedtuple


Colour = namedtuple('Colour', ['Red', 'Blue', 'Green'])

colour = Colour(55, 155, 255)

print(colour)
