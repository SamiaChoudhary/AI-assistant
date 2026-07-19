import os
import speech_recognition as sr
from config import INPUT_AUDIO_PATH

def transcribe_audio(audio_file_path=INPUT_AUDIO_PATH):
    """
    Converts audio file to text using free Google Speech Recognition.
    """
    if not os.path.exists(audio_file_path):
        print(f"❌ Error: Audio file '{audio_file_path}' not found!")
        return None

    print("🤖 Transcribing audio to text (Using Free Engine)...")
    
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file_path) as source:
            # Load the audio into memory
            audio_data = recognizer.record(source)
            
            # Convert speech to text (Supports English, Hindi, Urdu automatically)
            text = recognizer.recognize_google(audio_data)
            print(f"📝 User Said: {text}")
            return text

    except sr.UnknownValueError:
        print("❌ Error: Could not understand the audio clearly.")
        return None
    except sr.RequestError as e:
        print(f"❌ Error: Free service unavailable; {e}")
        return None
    except Exception as e:
        print(f"❌ Transcription error: {e}")
        return None

if __name__ == "__main__":
    # Test your transcription
    transcribe_audio()