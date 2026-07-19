import os
from gtts import gTTS
import sounddevice as sd
import soundfile as sf
from config import OUTPUT_AUDIO_PATH, OUTPUT_DIR

def speak_text(text, lang='en'):
    """
    Converts text to an audio file using free Google TTS and plays it.
    """
    if not text:
        return

    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print(f"🔊 Speaking: {text}")

    try:
        # Generate speech using gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        temp_mp3 = os.path.join(OUTPUT_DIR, "temp.mp3")
        tts.save(temp_mp3)

        # Convert and read the file to play it via sounddevice
        # (This avoids launching external media players on your system)
        data, fs = sf.read(temp_mp3)
        sd.play(data, fs)
        sd.wait() # Wait until audio finishes playing

        # Clean up temporary mp3 file
        if os.path.exists(temp_mp3):
            os.remove(temp_mp3)

    except Exception as e:
        print(f"❌ Text-to-Speech Error: {e}")

if __name__ == "__main__":
    # Test the Text-to-Speech module independently
    speak_text("Hello! This is a test of your free text to speech module. It works completely offline from key boundaries.")