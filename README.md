# Speech-to-Text Converter using SpeechRecognition
**This project is a simple speech-to-text conversion tool built with Python's SpeechRecognition library. It allows users to input an audio file (WAV, AIFF, FLAC) and receive the transcribed text using the Google Web Speech API.

This tool demonstrates the basic usage of speech recognition in Python and can be extended for voice assistant apps, transcription services, audio note-taking tools, or accessibility solutions.**

## 🔧 Features
    🎙️ Transcribes audio files into text using Google Web Speech API
    📁 Supports formats: WAV, AIFF, AIFF-C, FLAC
    ⚠️ Handles errors like inaudible input or network issues gracefully
    🧪 Easily extendable for live mic input or batch processing

## 🧠 Technologies Used
    Python 3.9+
    SpeechRecognition – for handling speech-to-text processing
    Google Web Speech API – used under the hood by the library

## How to use?
 1) Install dependencies
    Make sure you have Python 3.9+ installed, then run:
    ````
    pip install SpeechRecognition
    ````

3) Place your audio file
    * Supported formats: .wav, .aiff, .aifc, .flac
    * Save your file in the project directory or provide the full path.

4) Run the script
````
from speech_to_text import transcribe_audio_speechrecognition
path = "your_audio_file.wav"
transcript = transcribe_audio_speechrecognition(path)
print(transcript)
````
# ❗ Notes
* Requires an active internet connection (Google API is cloud-based).
* Longer or poor-quality audio may reduce accuracy.
* For offline or large-scale applications, consider using models like Whisper.

