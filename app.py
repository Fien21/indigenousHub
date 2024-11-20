from flask import Flask, render_template
import data  # Import the functions or data from data.py

app = Flask(__name__)

@app.route('/')
def index():
    # Call the function or access the data from data.py
    words = data.get_blaan_words()  # Assuming this is a function that returns a list of words
    return render_template('Blaan_BasicLevel.html', words=words)

if __name__ == '__main__':
    app.run(debug=True)
