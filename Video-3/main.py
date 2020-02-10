from textblob import TextBlob
from flask import Flask

def get_sentiment(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score > 0:
        if score > 0.5:
            return "This sentence is highly positive."
        else:
            return "This sentence is positive."
    elif score == 0:
        return "This sentence is neutral."
    else:
        if score < -0.5:
            return "This sentence is highly negative." # -0.9
        else:
            return "This sentence is negative." # -0.3

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>A Flask Application</h1>"

if __name__ == "__main__":
    app.run(debug = True)