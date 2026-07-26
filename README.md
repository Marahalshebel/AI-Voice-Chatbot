# AI Voice Chatbot
This project implements an AI-powered voice chatbot using Python. The chatbot records the user's speech through the microphone, converts it into text using OpenAI Whisper, generates an AI response using the Cohere API, and finally converts the generated response into speech.

## Features
- Speech-to-Text using OpenAI Whisper
- AI-generated responses using Cohere API
- Text-to-Speech using pyttsx3
- English voice conversation
- Microphone-based voice input

- ## Output
The following screenshot demonstrates the chatbot execution after converting speech to text, generating an AI response, and displaying the conversation.
![Voice Chatbot Output](images/output.png)

## Technologies
- Python 3.11
- OpenAI Whisper
- Cohere API
- pyttsx3
- SoundDevice
- SoundFile
- NumPy
- SciPy
- FFmpeg

## Project Structure
```text
VoiceChatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── images/
    └── output.png
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd VoiceChatbot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## How It Works

1. The application records the user's speech through the microphone.
2. Whisper converts the recorded speech into text.
3. The recognized text is sent to the Cohere API.
4. Cohere generates an AI response.
5. The generated response is converted into speech and played back to the user.
