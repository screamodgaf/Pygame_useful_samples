1. A matrix is created by initializing all its elements to 0 (self.matrix = [0] * self.MATRIX_HEIGHT * self.MATRIX_WIDTH)
2. Within the matrix, i create random impassable obstacles marked by 1
3. Each element in the matrix is then scaled by a given height and width, resulting in a square that is then rendered
4. Next, i create a player rectangle controlled by arrow keys 
5. Then, i project the player’s coordinates onto the matrix dimensions. After adding a movement vector to the player’s position, i check whether the player would end up in an adjacent matrix position. If so, I verify whether the neighboring position contains a 1. If it does, that indicates an invalid move. It allows for improved program efficiency by avoiding explicit rectangular collision calculations