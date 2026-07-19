import time
from audio import record_audio
from speech_to_text import transcribe_audio
from text_to_speech import speak_text

def run_voice_assistant():
    print("🤖 Welcome to your AI Voice Assistant! 🤖")
    # Step 1: Record your voice
    # It will use the default duration from config.py (5 seconds)
    record_audio()
    
    # Step 2: Convert the recorded audio to text
    print("\nProcessing your audio...")
    user_text = transcribe_audio()
    
    if not user_text:
        print("❌ Could not process any text from your voice. Exiting.")
        speak_text("I'm sorry, I couldn't hear or understand your recording.")
        return

    # Step 3: Handle the response logic 
    # (Since LLM keys are bypassed, we handle conversational matching or custom rules)
    print(f"\nAnalyzing what you said: '{user_text}'")
    
    user_text_lower = user_text.lower()
    if "hello" in user_text_lower or "hi" in user_text_lower:
        ai_reply = "Hello there! I am your local voice assistant. How can I help you today?"
    elif "time" in user_text_lower:
        current_time = time.strftime("%I:%M %p")
        ai_reply = f"The current time is approximately {current_time}."
    elif "your name" in user_text_lower:
        ai_reply = "I am a custom voice assistant built completely with Python."
    else:
        ai_reply = f"You said: {user_text}. Your voice processing and speaker systems are perfectly integrated!"

    print(f"\n🤖 Assistant Response: {ai_reply}")
    
    # Step 4: Speak the response out loud
    speak_text(ai_reply)
    print("🎉 Loop Complete! Your assistant works beautifully.")

if __name__ == "__main__":
    run_voice_assistant()