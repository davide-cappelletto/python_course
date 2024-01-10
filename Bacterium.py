class Bacterium:

    def __init__(self, x, y, shape, size, health):
        # Complete the class
        self.x = x
        self.y = y
        self.shape = shape
        self.size = size
        self.life_counter = health
    

# Create 3 instances
staphylococcus = Bacterium(1, 5, "round", 1, 250)
helicobacter = Bacterium(2, 0, "spiral", 4, 400)
bacillus = Bacterium(3, 4, "cylindrical", 2, 150)