import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Configure pandas display options to show all columns and rows
pd.set_option('display.max_columns', 400)
pd.set_option('display.max_rows', 400)

# Download required NLTK resources
nltk.download('punkt')

def preprocess_data(file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        
        # Print columns to check
        print("Columns in the dataset:", df.columns)
        
        # Remove any unnamed columns (typically empty or unnecessary columns)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        
        print("Columns after removing unnamed columns:", df.columns)
        
        # Check if 'English' column exists before applying tokenization
        if 'English' in df.columns:
            # Ensure the column contains valid strings
            df['English'] = df['English'].fillna('')
            df['Processed_Text'] = df['English'].apply(lambda x: word_tokenize(x.lower()) if isinstance(x, str) else [])
        else:
            print("The 'English' column is not present in the dataset.")
            return None
        
        return df  # Return the entire DataFrame with all columns
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please provide a valid CSV file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Specify the file path (ensure it is correct, using raw string or double backslashes)
file_path = r"Datasets\Book1BLaan.csv"  # Use raw string for file path or double backslashes

# Call the preprocessing function
df = preprocess_data(file_path)

# Print the entire dataset if it was successfully processed
if df is not None:
    print(df)