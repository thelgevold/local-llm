import random
import json

def generate_example():
    # Generate a random array with at most 4 2s and at most 4 10s
    num_2s = random.randint(0, 4)  # At most 4 2s
    num_10s = random.randint(0, 4)  # At most 4 10s
    
    # Create the array by randomly placing 2s and 10s
    array = [2] * num_2s + [10] * num_10s
    random.shuffle(array)
    
    # Determine the instruction based on the array contents
    if 2 in array and 10 in array:
        label = 2
    elif 2 in array:
        label = 2
    elif 10 in array:
        label = 10
    else:
        label = 0
    
    # The instruction to be included with each example
    instruction = "Given an array containing only the numbers 2 and 10, please pick one number based on the following rules. If both 2 and 10 are present in the array, pick 2. If only 2 is present, pick 2. If only 10 is present, pick 10. If the array is empty, pick 0."
    
    # Convert the input array to a string representation
    input_str = str(array)  # Convert list to string
    
    # Return the object in the requested format
    return {"instruction": instruction, "input": input_str, "output": str(label)}

# Generate a list of examples (you can adjust the size of the dataset as needed)
num_examples = 1000  # You can generate as many examples as you want
data = [generate_example() for _ in range(num_examples)]

# Write the dataset to a JSON file
output_file = 'output-special-cards.json'

# Write the data as an array of objects to JSON
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Dataset written to {output_file}")
