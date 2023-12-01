from collections import deque
import numpy as np


class ColoredWater:
    def __init__(self, pos):
        self.pos = pos

        """
        __init__(self, pos)
        Bu metot, ColoredWater sınıfının yapıcı metodu olarak adlandırılır 
        ve sınıfın örneğini oluştururken çağrılır. pos parametresi, renkli
        suyun bulunduğu pozisyonları içeren bir NumPy array'ini temsil eder.
        
        """

    @staticmethod
    def get_first_non_zero(arr):
        try:
            return arr[arr != 0][0]
        except IndexError:
            return 0

        """
        get_first_non_zero(arr)
        Bu statik metot, verilen bir NumPy array'indeki ilk sıfır olmayan
        elemanı döndürür.
        
        [arr != 0] - sıfır olmayan elemanları seçer
        [0] - ilk elemanı yani sıfırıncı indeksi getirir.
        """

    @staticmethod
    def get_first_non_zero_index(arr):
        try:
            return np.where(arr != 0)[0][0]
        except IndexError:
            return 3

        """
        get_first_non_zero_index(arr)
        Bu statik metot, verilen bir 
        NumPy array'indeki ilk sıfır olmayan elemanın indeksini döndürür.
        """

    @staticmethod
    def get_last_zero_index(arr):
        try:
            return np.where(arr == 0)[0][-1]
        except IndexError:
            return 3

        """
        get_last_zero_index(arr)
        Bu statik metot, verilen bir 
        NumPy array'indeki son sıfırın indeksini döndürür.
        """

    def get_legal_moves_to(self, moveable_to):
        first_non_zero = self.first_non_zero
        n = first_non_zero.shape[0]
        if first_non_zero[moveable_to] == 0:
            return np.where((first_non_zero != 0) & (np.arange(n) != moveable_to))[0], moveable_to
        else:
            return np.where((first_non_zero == first_non_zero[moveable_to]) & (np.arange(n) != moveable_to))[
                0], moveable_to

        """
        get_legal_moves_to(self, moveable_to)
        Bu metot, belirli bir hücreye suyun taşınabileceği 
        yasal hamleleri belirler.
        Hücreye su taşınabilirse, taşınabilen hücrelerin indekslerini 
        ve taşınacak hücrenin indeksini döndürür.
        """

    def swap(self, i, j):
        out = self.pos.copy()
        idx_from = (self.get_first_non_zero_index(self.pos[:, i]), i)
        idx_to = (self.get_last_zero_index(self.pos[:, j]), j)
        out[idx_from], out[idx_to] = out[idx_to], out[idx_from]

        move_description = f"{i + 1}. bottle's '{self.pos[idx_from]}', moved to {j + 1}. bottle"

        return ColoredWater(out)

    """
        swap(self, i, j)
        Bu metot, suyun iki hücre arasında değiştirilmesini simüle eder. 
        İlk olarak, get_first_non_zero_index ve get_last_zero_index 
        metotlarıyla ilgili hücrelerin indeksleri bulunur ve 
        ardından bu indekslere göre suyun taşınması simüle edilir.
    """

    def is_goal(self):
        return np.array_equiv(self.pos, self.pos[0])


    """
    is_goal(self)
    Bu metot, mevcut durumun bir hedef durumu olup olmadığını 
    kontrol eder.
    """

    # Modify the __iter__ method in ColoredWater class
    def __iter__(self):
        self.first_non_zero = np.apply_along_axis(self.get_first_non_zero, 0, self.pos)
        moveable_to = np.where(self.pos[0] == 0)[0]
        legal_moves = tuple(map(self.get_legal_moves_to, moveable_to))

        out = [(self.swap(origin, target),
                f"{origin + 1}. bottle's '{self.pos[:, origin][self.get_first_non_zero_index(self.pos[:, origin])]}', moved to {target + 1}. bottle")
               for origins, target in legal_moves
               for origin in origins]

        def number_of_full_stacks(pos):
            return np.sum(np.all((pos == [pos[0]]), axis=0))

        def fillings_of_stacks(game):
            pos = game.pos
            return number_of_full_stacks(pos), number_of_full_stacks(pos[1:]), number_of_full_stacks(pos[2:])

        return iter(sorted(out, key=lambda x: fillings_of_stacks(x[0]), reverse=True))

    """
        __iter__(self)
        Bu metot, ColoredWater örneğinin yasal hamlelerini üretir. 
        get_legal_moves_to metodu kullanılarak suyun taşınabileceği 
        hücreler belirlenir ve bu hücrelerdeki su değişimleri simüle edilir.
    """

    def set_rep(self):
        return frozenset(map(tuple, self.pos.T))

    """
        set_rep(self)
    Bu metot, pozisyonun bir temsilini oluşturur. 
    Bu temsil, pozisyonun sütunlarındaki elemanların 
    tuple'larından oluşan bir frozenset'tir.
    
    - map(tuple, self.pos.T): Bu, her sütunu bir demet (tuple) olarak dönüştürür. Yani, 
    her sütunun elemanlarını bir demet içinde gruplar.
    """

    def __repr__(self):
        rows, cols = self.pos.shape
        output = ""
        for i in range(rows):
            output += "| "
            for j in range(cols):
                output += f"{self.pos[i, j]:2} "
            output += "|\n"
        return output

    """
    __repr__(self)
    Bu metot, sınıfın temsilini oluşturan bir string döndürür. 
    Matris formundaki su pozisyonunu güzel bir şekilde formatlar.
    """

    @classmethod
    def solve(cls, pos, depth_first=False):
        queue = deque([(pos, "Initial State")])
        trail = {pos.set_rep(): (None, "Initial State")}
        solution = deque()
        load = queue.append if depth_first else queue.appendleft

        while not pos.is_goal():
            for m, move_description in pos:
                if m.set_rep() in trail:
                    continue
                trail[m.set_rep()] = (pos, move_description)
                load((m, move_description))
            pos, move_description = queue.pop()

        while pos:
            solution.appendleft((pos, move_description))
            pos, move_description = trail[pos.set_rep()]

        return list(solution)

    """
    solve(cls, pos, depth_first=False)
    Bu metot, genişlik öncelikli arama veya derinlik öncelikli 
    arama kullanarak suyun hedef durumuna nasıl ulaşılacağını çözer.
    Kullanılacak arama yöntemi, depth_first parametresi ile belirlenir.
    """

# Usage example
initial_state = np.array([[ 4, 8, 6, 11, 3, 7, 7, 9, 3, 9, 7, 10, 0, 0],
                       [ 3, 7, 1, 10, 1, 1, 11, 12, 11, 3, 10, 10, 0, 0],
                       [ 2, 6, 9, 8, 11, 5, 4, 5, 5, 12, 2, 12, 0, 0],
                       [ 1, 5, 2, 2, 9, 12, 6, 8, 8, 4, 4, 6, 0, 0]])

initial_game = ColoredWater(initial_state)
solution = ColoredWater.solve(initial_game, depth_first=False)

for step, (state, move_description) in enumerate(solution):
    print(f"Step {step + 1}:\n{state}\nMove: {move_description}\n")

