import random
import json

# Function to generate a random play_list with a size between 1 and 10
def generate_play_list():
    play_list_size = random.randint(1, 10)  # Choose random size between 1 and 10
    available_numbers = [3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
    return random.sample(available_numbers, play_list_size)

# Function to generate a random current_play from the constrained set
def generate_current_play():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14])

# Function to generate the output based on the play_list and current_play
def generate_output(play_list, current_play):
    # Find the smallest integer in the play_list >= current_play
    valid_numbers = [x for x in play_list if x >= current_play]
    if valid_numbers:
        return str(min(valid_numbers))  # Return the smallest valid number
    else:
        return "0"  # If no valid number is found, return 0

# Function to generate a single entry in the dataset
def generate_entry():
    play_list = generate_play_list()
    current_play = generate_current_play()
    output = generate_output(play_list, current_play)
    
    return {
        "instruction": "Find the smallest integer in the playlist that is greater than or equal to the current play. If no such number exists, return 0.",
        "input": json.dumps({"play_list": play_list, "current_play": current_play}),
        "output": output
    }

# Function to generate the dataset
def generate_dataset(num_entries):
    dataset = [generate_entry() for _ in range(num_entries)]
    return dataset

# Main function to run the script
def main(num_entries, output_file):
    dataset = generate_dataset(num_entries)
    
    # Save the dataset to a file
    with open(output_file, 'w') as f:
        json.dump(dataset, f, indent=4)

    print(f"Dataset with {num_entries} entries has been saved to {output_file}")

if __name__ == "__main__":
    num_entries = 300
    output_file ='./output.json'
    main(num_entries, output_file)
