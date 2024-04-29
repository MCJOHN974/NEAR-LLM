import json
import random

def load_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

def process_data(data):
    # Combine title and content into a single string for each section
    processed_text = []
    for section in data:
        if 'title' in section and 'content' in section:
            content = ' '.join(section['content'])
            section_text = f"{section['title']} {content}"
            processed_text.append(section_text)
    return processed_text

def split_data(processed_text, train_size=0.8):
    # Randomly shuffle the data to ensure a good mix
    random.shuffle(processed_text)
    # Split the data into training and testing sets
    split_index = int(len(processed_text) * train_size)
    train_data = processed_text[:split_index]
    test_data = processed_text[split_index:]
    return train_data, test_data

def save_data(data, filename):
    # Save data to a file, one section per line
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(line + '\n')

def train_test_split():
    # Load and process the data
    data = load_data('data/nearcore_github_io.json')
    processed_text = process_data(data)

    # Split into training and testing datasets
    train_data, test_data = split_data(processed_text)

    # Save the datasets to files
    save_data(train_data, 'data/train.txt')
    save_data(test_data, 'data/test.txt')

    print("Training and testing data have been successfully created and saved.")
