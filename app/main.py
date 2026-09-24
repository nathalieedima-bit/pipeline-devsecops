import subprocess
from flask import Flask, request

app = Flask(__name__)

# Defaut 1 : secret en dur dans le code (detecte par Gitleaks et Semgrep)
API_KEY = "AKIAIOSFODNN7FAKEDEMO"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/ping")
def ping():
    hote = request.args.get("host", "localhost")
    # Defaut 2 : injection de commande, shell=True avec une entree utilisateur
    resultat = subprocess.check_output("ping -c 1 " + hote, shell=True)
    return {"resultat": resultat.decode()}

if __name__ == "__main__":
    # Defaut 3 : mode debug active en production
    app.run(host="0.0.0.0", debug=True)

