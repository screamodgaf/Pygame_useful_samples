Converting a Bitmap World Map into Pygame graphical objects

1. Creating a bitmap (BMP) file containing a map of the world. In the game map, white tiles are passable, allowing player movement, while black tiles are impassable, blocking player movement
2. Loading the bitmap
3. Converting the 2D map representation into a 1D array - this step is not required, but it is preferred by me because it allows access to a specific position on the map through:
tile = map[x + y * MAP_WIDTH]
4. Creating a custom Rectangle class to graphically represent elements in the map array
5. Associating each element in the map list with drawable objects, assigning arbitrary heights and widths to them
6. Rendering the rectangular objects representing the elements in the map array 
