import os
import tempfile

import whisper
import sounddevice as sd
import soundfile as sf
import cohere
import pyttsx3

from dotenv import load_dotenv

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))

print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper loaded successfully!")

# -----------------------------
# Text To Speech
# -----------------------------
tts = pyttsx3.init()

tts.setProperty("rate", 170)

voices = tts.getProperty("voices")

if len(voices) > 0:
    tts.setProperty("voice", voices[0].id)


# -----------------------------
# Record Audio
# -----------------------------
def record_audio(filename, duration=5, samplerate=16000):

    print("\nSpeak now...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    sf.write(filename, audio, samplerate)

    print("Recording finished.")


# -----------------------------
# Speech To Text
# -----------------------------
def speech_to_text(filename):

    result = model.transcribe(filename)

    return result["text"].strip()


# -----------------------------
# Ask Cohere
# -----------------------------
def ask_bot(text):

    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Always answer only in English."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.message.content[0].text


# -----------------------------
# Speak
# -----------------------------
def speak(text):

    tts.say(text)
    tts.runAndWait()


# -----------------------------
# Main Program
# -----------------------------
def main():

    print("=" * 50)
    print(" AI Voice Chatbot ")
    print("=" * 50)

    while True:

        command = input(
            "\nPress ENTER to record\nType exit to quit\n> "
        ).strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp:

            filename = temp.name

        record_audio(filename)

        text = speech_to_text(filename)

        os.remove(filename)

        if text == "":
            print("No speech detected.")
            continue

        print("\nYou:", text)

        if text.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_bot(text)

        print("\nBot:", answer)

        speak(answer)


if __name__ == "__main__":
    main()