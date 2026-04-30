from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

DATA_FILE = "data/data.json"

# Charger données
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Sauvegarder données
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Page accueil
@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()

    if request.method == "POST":
        name = request.form["name"]
        study = request.form["study"]
        score = request.form["score"]

        data.append({
            "name": name,
            "study": float(study),
            "score": float(score)
        })

        save_data(data)
        return redirect("/")

    return render_template("index.html", data=data)

# Page graphique
@app.route("/charts")
def charts():
    data = load_data()
    return render_template("charts.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)