import joblib
from nltk.tokenize import word_tokenize
import os

# Load the saved model and vectorizer with relative paths
model_path = os.path.join("..", "models", "model.pkl")
vectorizer_path = os.path.join("..", "models", "vectorizer.pkl")
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Function to preprocess a single text (tokenize)
def preprocess_text(text):
    # Tokenize and convert to lowercase
    return word_tokenize(text.lower())

# Function to make predictions
def predict_new_text(text):
    # Preprocess the input text (tokenize)
    processed_text = preprocess_text(text)
    
    # Vectorize the tokenized text
    vectorized_text = vectorizer.transform([processed_text])
    
    # Predict the label using the trained model
    prediction = model.predict(vectorized_text)
    return prediction[0]

# Example usage
if __name__ == "__main__":
    # Provide new text (for prediction)
    new_text = "This is an example Bla'an sentence."
    predicted_label = predict_new_text(new_text)
    print(f"Predicted Label: {predicted_label}")