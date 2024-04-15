import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('path_to_your_csv_file.csv')

# Load the text files into a list
texts = []
for filename in df['filename_column']:
    with open(filename, 'r') as file:
        texts.append(file.read())

# Add the texts to the DataFrame
df['text'] = texts

# Truncate or split the texts if necessary
max_length = 32000  # This is the context window for ChatGPT-4
df['text'] = df['text'].apply(lambda x: x[:max_length])

#data is ready  
