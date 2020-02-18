from textblob import TextBlob
from flask import Flask, render_template

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

data = [12,13,14,14,13,11]

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run(debug = True)