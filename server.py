from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Bot läuft ✅"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "").lower()

    if "salam" in message:
        answer = "Wa alaikum salam mein Freund. Wie kann ich dir helfen🤲"
    elif "allah" in message:
        answer = "Allah ist der Schöpfer von allem und der einzige Gott im Islam ☝️"
    elif "gebet" in message:
        answer = "Muslime beten 5 mal am Tag und es gibt auch Extra Gebete die heißen Sunna Gebete 🕌"
    elif "koran" in message:
        answer = "Der Koran ist das heilige Buch im Islam und enthält die Worte Allahs📖"
    else:
        answer = "Weiß ich leider noch nicht frag den Istaz"

    return {"answer": answer}