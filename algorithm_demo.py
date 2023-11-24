from collections import deque
import numpy as np

class ColoredWater:
    def __init__(self, pos):
        self.pos = pos

    @staticmethod
    def get_first_non_zero(arr):
        try:
            return arr[arr != 0][0]
        except IndexError:
            return 0

    @staticmethod
    def get_first_non_zero_index(arr):
        try:
            return np.where(arr != 0)[0][0]
        except IndexError:
            return 3

    @staticmethod
    def get_last_zero_index(arr):
        try:
            return np.where(arr == 0)[0][-1]
        except IndexError:
            return 3

    def get_legal_moves_to(self, moveable_to):
        first_non_zero = self.first_non_zero
        n = first_non_zero.shape[0]
        if first_non_zero[moveable_to] == 0:
            return np.where((first_non_zero != 0) & (np.arange(n) != moveable_to))[0], moveable_to
        else:
            return np.where((first_non_zero == first_non_zero[moveable_to]) & (np.arange(n) != moveable_to))[0], moveable_to

    def swap(self, i, j):
        out = self.pos.copy()
        idx_from = (self.get_first_non_zero_index(self.pos[:, i]), i)
        idx_to = (self.get_last_zero_index(self.pos[:, j]), j)
        out[idx_from], out[idx_to] = out[idx_to], out[idx_from]
        return ColoredWater(out)

    def is_goal(self):
        return np.array_equiv(self.pos, self.pos[0])

    def __iter__(self):
        self.first_non_zero = np.apply_along_axis(self.get_first_non_zero, 0, self.pos)
        moveable_to = np.where(self.pos[0] == 0)[0]
        legal_moves = tuple(map(self.get_legal_moves_to, moveable_to))

        out = [self.swap(origin, target)
               for origins, target in legal_moves
               for origin in origins]

        def number_of_full_stacks(pos):
            return np.sum(np.all((pos == [pos[0]]), axis=0))

        def fillings_of_stacks(game):
            pos = game.pos
            return number_of_full_stacks(pos), number_of_full_stacks(pos[1:]), number_of_full_stacks(pos[2:])

        return iter(sorted(out, key=fillings_of_stacks, reverse=True))

    def set_rep(self):
        return frozenset(map(tuple, self.pos.T))

    def __repr__(self):
        rows, cols = self.pos.shape
        output = ""
        for i in range(rows):
            output += "| "
            for j in range(cols):
                output += f"{self.pos[i, j]:2} "
            output += "|\n"
        return output

    @classmethod
    def solve(cls, pos, depth_first=False):
        queue = deque([pos])
        trail = {pos.set_rep(): None}
        solution = deque()
        load = queue.append if depth_first else queue.appendleft

        while not pos.is_goal():
            for m in pos:
                if m.set_rep() in trail:
                    continue
                trail[m.set_rep()] = pos
                load(m)
            pos = queue.pop()

        while pos:
            solution.appendleft(pos)
            pos = trail[pos.set_rep()]

        return list(solution)

# Usage example
initial_state = np.array([[0, 1, 0, 5, 8, 9, 7, 4, 2, 8, 2, 5, 5, 10, 12],
                          [0, 2, 0, 6, 3, 10, 9, 7, 11, 3, 11, 12, 3, 6, 13],
                          [0, 3, 0, 7, 4, 2, 11, 11, 6, 12, 12, 13, 1, 13, 1],
                          [0, 4, 0, 5, 9, 9, 7, 6, 8, 8, 13, 1, 4, 10, 10]])

initial_game = ColoredWater(initial_state)
solution = ColoredWater.solve(initial_game, depth_first=True)

for step, state in enumerate(solution):
    print(f"Step {step + 1}:\n{state}\n")
