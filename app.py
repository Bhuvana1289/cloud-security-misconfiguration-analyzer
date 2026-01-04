from flask import Flask, render_template, request
import json
from analyzer import analyze_config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    issues = []
    recommendations = []

    if request.method == "POST":
        file = request.files["file"]
        if file:
            config = json.load(file)
            issues, recommendations = analyze_config(config)

    return render_template(
        "analyzer.html",
        issues=issues,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
