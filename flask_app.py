from flask import Flask, render_template, jsonify
from tester.runner import run_all_tests
from storage import save_run, list_runs

app = Flask(__name__)

# Page d'accueil : tes consignes
@app.get("/")
def consignes():
    return render_template("consignes.html")

# Lancer un run de tests
@app.get("/run")
def run_tests():
    result = run_all_tests()
    save_run(result)
    return jsonify(result)

# Dashboard HTML
@app.get("/dashboard")
def dashboard():
    runs = list_runs()
    return render_template("dashboard.html", runs=runs)

# Healthcheck
@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # utile en local uniquement
    app.run(host="0.0.0.0", port=5000, debug=True)
