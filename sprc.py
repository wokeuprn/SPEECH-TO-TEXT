import speech_recognition as sr

def transcribe_audio_speechrecognition(audio_file_path):
    """
    Transcribes audio using SpeechRecognition library (Google Web Speech API)
    
    Args:
        audio_file_path (str): Path to audio file (WAV, AIFF, AIFF-C, FLAC)
    
    Returns:
        str: Transcribed text
    """
    
    recognizer = sr.Recognizer()
    
    
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

