import random

class Minesweeper():
    def __init__(self, width_cell, heigh_cell, number_of_mine):
        self.wcell = width_cell
        self.hcell = heigh_cell
        self.nmine = number_of_mine
        self.map = ["B" for i in range(self.nmine)] + \
                   ["" for i in range(self.wcell * self.hcell - self.nmine)]

    def check_mine(self, index):
        if self.map[index] == "B":
            return True
        return False

    def get_neighbor(self, index):
        neighbor_list = []
        max_cell = self.hcell * self.wcell
        remainder = index % self.wcell
        if remainder == 0:
            for i in range(2):
                for j in range(index - self.wcell + i, 
                               index + self.wcell + i + 1, self.wcell):
                    if j >= max_cell or j < 0:
                        continue
                    neighbor_list.append(j)
        elif remainder < self.wcell - 1:
            for i in range(3):
                for j in range(index - self.wcell + i - 1, 
                               index + self.wcell + i, self.wcell):
                    if j >= max_cell or j < 0:
                        continue
                    neighbor_list.append(j)
        else:
            for i in range(2):
                for j in range(index - self.wcell + i - 1, 
                               index + self.wcell + i, self.wcell):
                    if j >= max_cell or j < 0:
                        continue
                    neighbor_list.append(j)
        return neighbor_list


    def check_first_move(self, index):
        if self.map[index] == "B":
            return False
        
        neighbor_list = self.get_neighbor(index)
        for i in neighbor_list:
            if self.check_mine(i):
                return False
        return True

    def count_adjacent_mines(self, index):
        if self.map[index] == "B":
            return "B"
        
        neighbor_list = self.get_neighbor(index)
        count = sum(1 for i in neighbor_list if self.check_mine(i))
        return count

    def create_map(self, index):
        while True:
            random.shuffle(self.map)

            if self.check_first_move(index):
                for i in range(self.wcell * self.hcell):
                    self.map[i] = self.count_adjacent_mines(i)
                    print(self.map[i])
                break

    def get_number_of_mines(self, index):
        return self.map[index]