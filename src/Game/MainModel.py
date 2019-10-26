class MainModel:
    def __init__(self):
        self.curr_x_pos = 4
        self.curr_y_pos = 1
        self.level = 1
        self.score = 0

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score