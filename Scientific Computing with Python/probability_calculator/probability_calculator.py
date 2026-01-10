import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    def draw(self, num):
        if num >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        drawn = random.sample(self.contents, num)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        temp_hat = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn = temp_hat.draw(num_balls_drawn)
        success_flag = all(drawn.count(color) >= count for color, count in expected_balls.items())
        if success_flag:
            success += 1
    return success / num_experiments
