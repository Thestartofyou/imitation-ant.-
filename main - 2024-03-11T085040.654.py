import random

class ImitationAnt:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.position = [random.randint(0, grid_size-1), random.randint(0, grid_size-1)]
    
    def move(self):
        # Randomly select a direction (up, down, left, right)
        direction = random.choice(['up', 'down', 'left', 'right'])
        
        # Update position based on the selected direction
        if direction == 'up':
            self.position[1] = max(0, self.position[1] - 1)
        elif direction == 'down':
            self.position[1] = min(self.grid_size - 1, self.position[1] + 1)
        elif direction == 'left':
            self.position[0] = max(0, self.position[0] - 1)
        elif direction == 'right':
            self.position[0] = min(self.grid_size - 1, self.position[0] + 1)
    
    def get_position(self):
        return tuple(self.position)

# Main simulation
grid_size = 10
ant = ImitationAnt(grid_size)

print("Initial position:", ant.get_position())

# Simulate 10 random moves
for i in range(10):
    ant.move()
    print("Move", i+1, "- Position:", ant.get_position())
