import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Corrige 1 : le secret vient de l environnement, plus du code source
API_KEY = os.environ.get("API_KEY", "")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/ping")
def ping():
    hote = request.args.get("host", "localhost")
    # Corrige 2 : liste d arguments sans shell, et validation de l entree
    if not hote.replace(".", "").replace("-", "").isalnum():
        return {"erreur": "nom d hote invalide"}, 400
    try:
        resultat = subprocess.check_output(
            ["ping", "-c", "1", hote], shell=False, timeout=5
        )
    except subprocess.SubprocessError:
        return {"erreur": "echec du ping"}, 500
    return {"resultat": resultat.decode()}

if __name__ == "__main__":
    # Corrige 3 : debug desactive, pilote par variable d environnement
    app.run(host="0.0.0.0", port=5000, debug=False)
