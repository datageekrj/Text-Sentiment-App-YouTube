from textblob import TextBlob
from flask import Flask, render_template, request 

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
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form.get("text")
        sentiment = get_sentiment(content)
        return "The sentiment is: " + sentiment
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)