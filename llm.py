from groq import Groq
from config import GROQ_API_KEY

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_ai_response(user_text):
    """
    Generates a text response using Llama-3 via Groq.
    """
    if not user_text:
        return "I didn't catch that. Could you please repeat?"

    print("🤖 AI is thinking via Groq Llama-3...")
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful, concise voice assistant. Respond naturally and keep answers short."},
                {"role": "user", "content": user_text}
            ],
            model="llama3-8b-8192",
        )
        
        ai_reply = chat_completion.choices[0].message.content
        print(f"🤖 AI Reply: {ai_reply}")
        return ai_reply

    except Exception as e:
        print(f"❌ Error generating response: {e}")
        return "I am having trouble processing that right now."

if __name__ == "__main__":
    # Test the Groq LLM independently
    generate_ai_response("Hello! Who are you?")