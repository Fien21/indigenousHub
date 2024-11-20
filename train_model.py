import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from data_preprocessing import preprocess_data  # Import from the separate file

def train_model(data_path="Datasets\Book1BLaan.csv", model_dir="models"):
    # Load and preprocess the data
    df = preprocess_data(data_path)
    
    if df is not None:
        # Check for the required columns in the preprocessed DataFrame
        if 'Processed_Text' not in df.columns or 'Label' not in df.columns:
            print("Error: Required columns 'Processed_Text' and 'Label' are missing.")
            return
        
        # Vectorize the text using TF-IDF (Transform Text to feature vectors)
        vectorizer = TfidfVectorizer(analyzer=lambda x: x)  # Using tokenized text directly
        X = vectorizer.fit_transform(df['Processed_Text'])
        y = df['Label']  # Labels (target variable)
        
        # Split data into training and test sets (80% train, 20% test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model (Logistic Regression)
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy}")
        
        # Save the trained model and vectorizer to disk
        joblib.dump(model, f"{model_dir}/model.pkl")
        joblib.dump(vectorizer, f"{model_dir}/vectorizer.pkl")
        print("Model and vectorizer saved.")
    else:
        print("Data preprocessing failed, training aborted.")

if __name__ == "__main__":
    train_model()