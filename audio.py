import os
import sounddevice as sd
import soundfile as sf
from config import INPUT_AUDIO_PATH, RECORDINGS_DIR, SAMPLE_RATE, DURATION

def record_audio(duration=DURATION, sample_rate=SAMPLE_RATE):
    """
    Records audio from the microphone and saves it as a WAV file.
    """
    # Ensure the recordings directory exists
    if not os.path.exists(RECORDINGS_DIR):
        os.makedirs(RECORDINGS_DIR)
        
    print(f"🎤 Recording started... speak for {duration} seconds...")
    
    # Record audio (channels=1 for mono audio)
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()  # Wait until the recording is finished
    
    print("🛑 Recording finished! Saving file...")
    
    # Save the audio file
    sf.write(INPUT_AUDIO_PATH, recording, sample_rate)
    print(f"💾 Audio successfully saved to: {INPUT_AUDIO_PATH}")
    return INPUT_AUDIO_PATH

if __name__ == "__main__":
    # Test recording
    record_audio()