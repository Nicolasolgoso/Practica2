# import necessary libraries
import numpy as np
from scipy import stats  # ¡Agrega esta línea!

# function to calculate mean
def calculate_mean(data):
    return np.mean(data)

# function to calculate standard deviation
def calculate_standard_deviation(data):
    return np.std(data)

# function to perform one-sample t-test
def one_sample_t_test(data, null_hypothesis_mean):
    t_stat, p_value = stats.ttest_1samp(data, null_hypothesis_mean)
    return t_stat, p_value

# function to perform two-sample t-test
def two_sample_t_test(data1, data2):
    t_stat, p_value = stats.ttest_ind(data1, data2)
    return t_stat, p_value

# function to perform chi-squared test
def chi_squared_test(observed, expected):
    chi_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
    return chi_stat, p_value

# main function to run the program
def main():
    print("Welcome to the Statistical Analysis Program!")
    
    # input experimental data
    data = list(map(float, input("Enter your experimental data separated by spaces: ").split()))
    
    # calculate and display mean
    mean = calculate_mean(data)
    print(f"Mean: {mean}")
    
    # calculate and display standard deviation
    standard_deviation = calculate_standard_deviation(data)
    print(f"Standard Deviation: {standard_deviation}")
    
    # hypothesis testing options
    print("\nHypothesis Testing:")
    print("1. One-sample t-test")
    print("2. Two-sample t-test")
    print("3. Chi-squared test")
    
    test_choice = int(input("Choose a hypothesis test (1/2/3): "))
    
    if test_choice == 1:
        null_mean = float(input("Enter the null hypothesis mean: "))
        t_stat, p_value = one_sample_t_test(data, null_mean)
        print(f"One-sample t-test: t_stat = {t_stat}, p_value = {p_value}")
    elif test_choice == 2:
        data2 = list(map(float, input("Enter the second set of data for two-sample t-test: ").split()))
        t_stat, p_value = two_sample_t_test(data, data2)
        print(f"Two-sample t-test: t_stat = {t_stat}, p_value = {p_value}")
    elif test_choice == 3:
        observed = list(map(float, input("Enter the observed frequencies separated by spaces: ").split()))
        expected = list(map(float, input("Enter the expected frequencies separated by spaces: ").split()))
        chi_stat, p_value = chi_squared_test(observed, expected)
        print(f"Chi-squared test: chi_stat = {chi_stat}, p_value = {p_value}")
    else:
        print("Invalid choice. Exiting program.")

# run the program
if __name__ == "__main__":
    main()
