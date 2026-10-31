"""Site da Yasmim Almeida · Nail Designer (Jaguariúna-SP)

Como rodar:
    pip install -r requirements.txt
    python app.py          ->  http://127.0.0.1:5000
"""
import os
from urllib.parse import quote_plus
from flask import Flask, render_template

app = Flask(__name__)

# ---------- Dados editáveis do site ----------
WHATSAPP = "5519989900890"          # DDI + DDD + número, sem símbolos
INSTAGRAM = "yaa.naildesigner"
ENDERECO = "Rua Cap. Ulisses Masoti, 362 · Centro · Jaguariúna-SP"

# categorias: francesinha | glitter | escuras | artes
CATEGORIAS = [
    "glitter", "glitter", "francesinha", "francesinha", "artes", "escuras",
    "francesinha", "artes", "artes", "escuras", "escuras", "escuras",
    "artes", "glitter", "escuras", "glitter",
]
GALERIA = [
    {"arquivo": f"trabalho{i:02d}.jpg", "cat": cat}
    for i, cat in enumerate(CATEGORIAS, start=1)
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        galeria=GALERIA,
        whatsapp=WHATSAPP,
        instagram=INSTAGRAM,
        endereco=ENDERECO,
        maps_query=quote_plus(ENDERECO.replace("·", ",")),
    )


@app.route("/saude")
def saude():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
