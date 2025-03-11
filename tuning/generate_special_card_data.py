import random
import json

# Function to generate a random test case array of size n
def generate_array(n):
    # We define a series of numbers from which the array can be made
    series = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    # Randomly choose n elements from the series (with possible repetition)
    return [random.choice(series) for _ in range(n)]

# Function to select either 2, 10, or 0 based on the array's content
def select_value(arr):
    # Check for the presence of 2 or 10, prioritizing 2
    if 2 in arr:
        return 2
    elif 10 in arr:
        return 10
    else:
        return 0

# Function to generate a test case in the required format
def generate_test_case(n):
    arr = generate_array(n)  # Generate an array with n elements
    selected_value = select_value(arr)  # Get the value based on the rule
    test_case = {
        "instruction": "Given an array of numbers, your task is to select the first occurrence of either a 2 or a 10. If both exist, select the 2 (giving priority to 2 over 10). If neither 2 nor 10 is found in the array, return 0.",
        "input": f"{arr}",
        "output": f"{selected_value}"
    }
    return test_case

# Function to generate n test cases and output them as JSON
def generate_multiple_test_cases(n_cases, n_elements):
    test_cases = []
    for _ in range(n_cases):
        test_cases.append(generate_test_case(n_elements))
    return test_cases

# Example: Generate 5 test cases with arrays of 10 elements each
n_cases = 2000  # Number of test cases to generate
n_elements = 10  # Number of elements in each array
test_cases = generate_multiple_test_cases(n_cases, n_elements)

# Output the results to a JSON file
output_filename = 'output-special-cards.json'

# Write the result to a file
with open(output_filename, 'w') as f:
    json.dump(test_cases, f, indent=2)

print(f"Test cases have been saved to {output_filename}")
