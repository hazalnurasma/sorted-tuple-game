from collections import deque
import numpy as np

colors = ["pm", "ay", "sr", "kr", "kv", "gr", "mo", "yy", "ky", "lc", "mv", "tt"]

pm=1
ay=2
sr=3
kr=4
kv=5
gr=6
mo=7
yy=8
ky=9
lc=10
mv=11
tt=12

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

    def isgoal(self):
        return np.array_equiv(self.pos, self.pos[0])

    def __iter__(self):
        moveable_to = np.where(self.pos[0] == 0)[0]
        legal_moves = tuple(map(self.get_legal_moves_to, moveable_to))

        for origins, target in legal_moves:
            for origin in origins:
                new_game = self.swap(origin, target)
                new_game.first_non_zero = np.apply_along_axis(self.get_first_non_zero, 0, new_game.pos)
                yield new_game

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
        return repr(self.pos)

    @classmethod
    def solve(cls, pos, depthFirst=False):
        queue = deque([pos])
        trail = {pos.set_rep(): None}
        solution = deque()
        load = queue.append if depthFirst else queue.appendleft

        while not pos.isgoal():
            for m in pos:
                if m.set_rep() in trail:
                    continue
                trail[m.set_rep()] = pos
                load(m)

            if not queue:
                break  # Stop the loop if the queue is empty
            pos = queue.popleft()  # Use popleft() instead of pop()


        while pos:
            solution.appendleft(pos)
            pos = trail[pos.set_rep()]

        for step, state in enumerate(solution):
            print(f"Step {step + 1}:\n{state}\n")

        return list(solution)

# Kullanım örneği

initial_state = np.array([[4,3,2,1],
                          [8,7,6,5],
                          [3,9,4,7],
                          [3,5,11,10],
                          [9,10,4,2],
                          [12,8,4,6],
                          [7,1,10,6],
                          [5,8,12,9],
                          [5,8,10,2],
                          [1,12,2,9],
                          [1,3,11,6],
                          [7,12,11,11],
                          [],
                          []
                          ], dtype=object)

initial_game = ColoredWater(initial_state)
solution = ColoredWater.solve(initial_game, depthFirst=True)


