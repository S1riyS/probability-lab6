import math

from probability_theory import ProbabilityTheory


def main():
    with open("input.txt", "r") as file:
        elements = [float(line.strip()) for line in file]

    runner = ProbabilityTheory(elements)

    # Variational series
    runner.get_var_values()

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
