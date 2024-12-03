import math

from chart import Chart

PREFIX = "*"


class ProbabilityTheory:
    def __init__(self, values):
        self.values = values
        self.values.sort()

        self.xi = []
        self.ni = []
        self.pi = []

    def get_var_values(self):
        self.values.sort()
        print(f"{PREFIX} Вариационный ряд: {' '.join(map(str, self.values))}")

    def get_extreme_values(self):
        print(f"{PREFIX} MIN = {self.values[0]}")
        print(f"{PREFIX} MAX = {self.values[-1]}")

    def get_selection_size(self):
        print(f"{PREFIX} Размах выборки {self.values[-1] - self.values[0]}")

    def discrepancy_calculation(self):
        for x in sorted(set(self.values)):
            count = self.values.count(x)
            self.xi.append(x)
            self.ni.append(count)
            self.pi.append(count / len(self.values))

        expected_value = sum([x * p for x, p in zip(self.xi, self.pi)])
        print(f"{PREFIX} Оценка математического ожидания {expected_value}")

        disperancy = sum([p * (x - expected_value) ** 2 for x, p in zip(self.xi, self.pi)])
        print(f"{PREFIX} Дисперсия {disperancy}")
        fixed_disperancy = disperancy * len(self.xi) / (len(self.xi) - 1)
        print(f"{PREFIX} Исправленная дисперсия {fixed_disperancy}")
        print(f"{PREFIX} Cреднеквадратическоe отклонение {math.sqrt(disperancy)}")
        print(f"{PREFIX} Исправленное СКО {math.sqrt(fixed_disperancy)}")

    def get_h(self):
        return (self.values[-1] - self.values[0]) / (1 + math.log2(len(self.values)))

    def get_m(self):
        return math.ceil(1 + math.log2(len(self.values)))

    def calculate_empiric_function(self):
        chart = Chart("x", "f(x)", "Эмпирическая функция")
        chart.add_chart(f"x <= {self.xi[0]}", self.xi[0] - 0.5, self.xi[0], 0)

        print()
        print(f"{PREFIX} Империческая функция ")
        print(f"\t\tx\t<=\t{self.xi[0]}\t->\t{0.0}")

        h = self.pi[0]
        for i in range(len(self.xi) - 1):
            print(f"{self.xi[i]}\t<\tx\t<=\t{self.xi[i + 1]}\t->\t{h:.2f}")
            chart.add_chart(f"{self.xi[i]} < x <= {self.xi[i + 1]}", self.xi[i], self.xi[i + 1], h)
            h += self.pi[i + 1]

        print(f"{self.xi[-1]}\t<\tx\t\t\t->\t{h:.2f}")
        chart.add_chart(f"{self.xi[-1]} < x", self.xi[-1], self.xi[-1] + 1, h)
        chart.plot("empiric_function")

    def draw_frequency_polygon(self):
        frequency_polygon = Chart("x", "p_i", "Полигон частот")

        print()
        print(f"{PREFIX} Полигон частот")

        x_start = self.values[0] - self.get_h() / 2
        for _ in range(self.get_m()):
            count = 0
            for value in self.values:
                if value >= x_start and value < (x_start + self.get_h()):
                    count += 1

            frequency_polygon.polygonal_chart(x_start + self.get_h() / 2, count / len(self.values))
            print(f"[ {x_start} : {x_start + self.get_h()} ) -> {count / len(self.values)}")

            x_start += self.get_h()

        frequency_polygon.plot("frequency_polygon")

    def draw_histogram(self, size):
        histogram_chart = Chart("x", "p_i / h", "Гистограмма частот")

        print()
        print(f"{PREFIX} Гистограмма частот")

        x_start = self.values[0] - self.get_h() / 2
        for _ in range(self.get_m()):
            s = 0
            for value in self.values:
                if value >= x_start and value < (x_start + self.get_h()):
                    s += 1

            histogram_chart.add_histogram(
                f"{x_start:.3f} : {x_start + self.get_h():.3f}",
                x_start,
                x_start + self.get_h(),
                (s / size) / self.get_h(),
            )

            print(f"[ {x_start:.3f} : {x_start + self.get_h():.3f} ) -> {(s / size / self.get_h()):.3f}")

            x_start += self.get_h()

        histogram_chart.plot("histogram")

    def print_data(self):
        print()
        print(f"{PREFIX} DEBUG:")
        for i in range(len(self.xi)):
            print(f"{self.xi[i]} {self.ni[i]} {self.pi[i]}")
