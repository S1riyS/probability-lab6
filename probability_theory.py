import math


class ProbabilityTheory:
    def __init__(self, values):
        self.values = values
        self.xi = []
        self.ni = []
        self.pi = []

    def get_var_values(self):
        self.values.sort()
        print("! Вариационный ряд: ", end="")
        print(" ".join(map(str, self.values)))

    def get_extreme_values(self):
        print("! MIN = " + str(self.values[0]) + "\n! MAX = " + str(self.values[-1]))

    def get_selection_size(self):
        print("! Размах выборки " + str(self.values[-1] - self.values[0]))

    def discrepancy_calculation(self):
        for x in set(self.values):
            count = self.values.count(x)
            self.xi.append(x)
            self.ni.append(count)
            self.pi.append(count / len(self.values))

        expected_value = sum([x * p for x, p in zip(self.xi, self.pi)])
        print("! Оценка математического ожидания " + str(expected_value))

        disperancy = sum([p * (x - expected_value) ** 2 for x, p in zip(self.xi, self.pi)])
        print("! Дисперсия " + str(disperancy))
        fixed_disperancy = disperancy * len(self.xi) / (len(self.xi) - 1)
        print("! Исправленная дисперсия " + str(fixed_disperancy))
        print("! Cреднеквадратическоe отклонение " + str(math.sqrt(disperancy)))
        print("! Исправленное СКО " + str(math.sqrt(fixed_disperancy)))

    def get_h(self):
        return (self.values[-1] - self.values[0]) / (1 + math.log2(len(self.values)))

    def get_m(self):
        return math.ceil(1 + math.log2(len(self.values)))

    def calculate_empiric_function(self):
        print("! Функция ")
        print("\t\tx\t<=\t" + str(self.xi[0]) + "\t->\t" + str(0.0))

        h = self.pi[0]
        for i in range(len(self.xi) - 1):
            print(str(self.xi[i]) + "\t<\tx\t<=\t" + str(self.xi[i + 1]) + "\t->\t" + str(h))
            h += self.pi[i + 1]

        print(str(self.xi[-1]) + "\t<\tx\t\t\t->\t" + str(h))

    def draw_frequency_polygon(self):
        x_start = self.values[0] - self.get_h() / 2
        for i in range(self.get_m()):
            count = 0
            for value in self.values:
                if value >= x_start and value < (x_start + self.get_h()):
                    count += 1

            print("[ " + str(x_start) + " : " + str(x_start + self.get_h()) + " ) -> " + str(count / len(self.values)))

            x_start += self.get_h()

    def draw_histogram(self, size):
        x_start = self.values[0] - self.get_h() / 2

        for i in range(self.get_m()):
            s = 0
            for value in self.values:
                if value >= x_start and value < (x_start + self.get_h()):
                    s += 1

            print("[ " + str(x_start) + " : " + str(x_start + self.get_h()) + " ) -> " + str(s / size / self.get_h()))

            x_start += self.get_h()

    def print_data(self):
        print("\n\n! DEBUG:\n")
        for i in range(len(self.xi)):
            print(str(self.xi[i]) + " " + str(self.ni[i]) + " " + str(self.pi[i]))
