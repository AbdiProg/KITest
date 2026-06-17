from openai import OpenAI
import requests
import base64

import fitz

from transformers import pipeline
from PIL import Image
import requests
import torch

import io

client = OpenAI(
    api_key="sk-hmb6GIEX2f_-TD6PVdiTPQ",
    base_url="https://litellm.s.studiumdigitale.uni-frankfurt.de/v1/"
)

with open("assets/Vorlesung_1_OraleMedizinUndSystemischeAspekte/13.png", "rb") as f:
    bild_base64 = base64.b64encode(f.read()).decode("utf-8")

with open("assets/Vorlesung_1_OraleMedizinUndSystemischeAspekte/14.png", "rb") as f:
    bild_base64_2 = base64.b64encode(f.read()).decode("utf-8")

"""
response = requests.get(
    "https://litellm.s.studiumdigitale.uni-frankfurt.de/v1/model/info",
    headers={"x-litellm-api-key": "sk-hmb6GIEX2f_-TD6PVdiTPQ"}
)
"""
"""
for modell in response.json()["data"]:
    name = modell["model_name"]
    vision = modell.get("model_info", {}).get("supports_vision", False)
    print(f"{name}: Vision={vision}")

"""


def pdf_zu_text(pfad):
    doc = fitz.open(pfad)
    return "\n".join([seite.get_text() for seite in doc])


text = pdf_zu_text("assets/IMPPPrüfziele/IMPPPrüfziele_OraleMedizinUndSystemischeAspekte.pdf")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": [{"type": "text", "text": "Du bist ein Dozent der Zahnmedizin"}]
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "Zu welchem IMPP Prüfziel passt das Bild? Insbesondere wegen dem Thema von Diabetes."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{bild_base64}"}
                         },
                        {"type": "text", "text": text}]
        }],
    model="medgemma-27b-it",  # Beispiel-Modell
    temperature=0.7
)

print(chat_completion.choices[0].message.content)
