import math

from probability_theory import ProbabilityTheory


def main():
    elements = []
    with open("input.txt", "r") as file:
        for line in file:
            elements.extend([float(x) for x in line.split()])

    runner = ProbabilityTheory(elements)

    # Variational series
    runner.get_var_values()

    runner.get_stat_values()

    runner.get_interval_stat_row()

    runner.get_avg()
    runner.get_median()
    runner.get_mode()

    # Extreme values
    runner.get_extreme_values()

    # Range
    runner.get_selection_size()

    # Estimates of the mathematical expectation and standard deviation
    runner.discrepancy_calculation()

    # Empirical distribution function and its graph
    runner.calculate_empiric_function()

    # Histogram and polygon of frequencies of the grouped sample
    runner.draw_frequency_polygon()
    runner.draw_histogram(len(elements))
    runner.print_data()


if __name__ == "__main__":
    main()
