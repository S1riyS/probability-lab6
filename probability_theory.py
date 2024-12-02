import math

from chart import Chart


class ProbabilityTheory:
    def __init__(self, values):
        self.values = values
        self.values.sort()

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
        for x in sorted(set(self.values)):
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
        chart = Chart("x", "f(X)", "Эмпирическая функция")
        chart.add_chart("x <= " + str(self.xi[0]), self.xi[0] - 0.5, self.xi[0], 0)

        print("! Функция ")
        print("\t\tx\t<=\t" + str(self.xi[0]) + "\t->\t" + str(0.0))

        h = self.pi[0]
        for i in range(len(self.xi) - 1):
            print(str(self.xi[i]) + "\t<\tx\t<=\t" + str(self.xi[i + 1]) + "\t->\t" + str(h))
            chart.add_chart(str(self.xi[i]) + " < x <= " + str(self.xi[i + 1]), self.xi[i], self.xi[i + 1], h)
            h += self.pi[i + 1]

        print(str(self.xi[-1]) + "\t<\tx\t\t\t->\t" + str(h))
        chart.add_chart(str(self.xi[-1]) + " < x", self.xi[-1], self.xi[-1] + 1, h)
        chart.plot("EmpiricFunction")

    def draw_frequency_polygon(self):
        frequency_polygon = Chart("x", "p_i", "Полигон частот")

        x_start = self.values[0] - self.get_h() / 2
        for i in range(self.get_m()):
            count = 0
            for value in self.values:
                if value >= x_start and value < (x_start + self.get_h()):
                    count += 1

            frequency_polygon.polygonal_chart(x_start + self.get_h() / 2, count / len(self.values))
            print("[ " + str(x_start) + " : " + str(x_start + self.get_h()) + " ) -> " + str(count / len(self.values)))

            x_start += self.get_h()

        frequency_polygon.plot("frequency_polygon")

    def draw_histogram(self, size):
        histogram_chart = Chart("x", "p_i / h", "Гистограмма частот")

        x_start = self.values[0] - self.get_h() / 2

        for i in range(self.get_m()):
            s = 0
            for value in self.values:
                if value >= x_start and value < (x_start + self.get_h()):
                    s += 1

            histogram_chart.add_histogram(
                str(round(x_start, 3)) + " : " + str(round(x_start + self.get_h(), 3)),
                x_start,
                x_start + self.get_h(),
                (s / size) / self.get_h(),
            )

            print("[ " + str(x_start) + " : " + str(x_start + self.get_h()) + " ) -> " + str(s / size / self.get_h()))

            x_start += self.get_h()

        histogram_chart.plot("histogram")

    def print_data(self):
        print("\n\n! DEBUG:\n")
        for i in range(len(self.xi)):
            print(str(self.xi[i]) + " " + str(self.ni[i]) + " " + str(self.pi[i]))
