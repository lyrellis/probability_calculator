# Import necessary modules
import copy
import random
from collections import Counter

class Hat:
    # Initializes hat
    def __init__(self, **kwargs):
        self.dict = kwargs # Input as dictionary
        # Converts dictionary to list
        self.contents = []
        for ball_color in kwargs:
            for _ in range(kwargs[ball_color]):
                self.contents.append(ball_color)

    # Draws number_balls_drawn from hat
    def draw(self, number_balls_drawn):
        # If number_balls_drawn is greater than the amount available, remove all from hat and store in their own list
        if number_balls_drawn > len(self.contents):
            self.drawn = self.contents.copy() # Creates copy and sets to drawn
            self.contents = [] # Sets original to empty
            return self.drawn
        # Draws balls from hat, removes drawn balls, and storing them in their own list, returns that list
        else:
            self.drawn = random.sample(self.contents, number_balls_drawn)
            for ball in self.drawn:
                self.contents.remove(ball)
            return self.drawn

# Defines experiment function
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    expected_balls_list = []

    # Performs the designated number of experiments
    for _ in range(num_experiments):
        # Creates a copy of hat so that the original remains immutable 
        hat_copy = copy.deepcopy(hat)
        # Draws from copy
        drawn_balls_list = hat_copy.draw(num_balls_drawn)
        # Uses counter from collections module
        drawn_counts = Counter(drawn_balls_list)
        
        # Uncomment the next line to debug
        # print(drawn_counts)

        # Defaults to a true condition, the upcoming for loop will check for failure, and est to false
        success = True

        # Returns false if the expected_balls were not drawn
        for color, count in expected_balls.items():
            
            # Uncomment the next line to debug
            # print(expected_balls.items())

            if drawn_counts[color] < count:
                success = False
                break

        # If experiment was successful, increases counter
        if success:
            successful_experiments += 1
        
        # Uncomment the next line to debug
        # print(successful_experiments)
    
    # Calculate probability
    return successful_experiments / num_experiments
    

# ---------- Example Input ----------

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
    expected_balls={'red':2,'green':1},
    num_balls_drawn=5,
    num_experiments=2000
)

print(probability)