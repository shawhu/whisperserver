# save this as app.py
from flask import Flask, request
from markupsafe import escape
import whisper


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if request.method == "POST":
        file = request.files["file"]

        try:
            language = request.form["language"]
        except:
            language = ""

        file.save("d:/temp/voicedemo.m4a")
        return do_the_transcribe(
            "d:/temp/voicedemo.m4a", request.form["model"], language
        )
    else:
        return "Only POST is accepted"


mainmodel = whisper.load_model("small")


def do_the_transcribe(f, model, language):
    # load the entire audio file
    audio = whisper.load_audio(f)

    if language:  # check if language is not empty
        options = {
            "language": language,  # input language
            "task": "transcribe",  # translate or "transcribe"
        }
    else:
        options = {
            "task": "transcribe",  # translate or "transcribe"
        }
    result = whisper.transcribe(mainmodel, audio, **options)
    print(result["text"])
    return {"text": result["text"]}
