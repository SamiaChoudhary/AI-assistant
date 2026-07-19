import os

# Paste your Groq API key here (the one starting with AQ. or gsk_ if you get a fresh one)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "AQ.Ab8RN6JKPwUWqvXvcv4Yu87KqrF6TzLiLAQ0ab5F1YVAzGBJJQ")

# Directory Configurations
RECORDINGS_DIR = "recordings"
OUTPUT_DIR = "output"

# Audio File Paths
INPUT_AUDIO_PATH = os.path.join(RECORDINGS_DIR, "input.wav")
OUTPUT_AUDIO_PATH = os.path.join(OUTPUT_DIR, "output.wav")

# Audio Settings
SAMPLE_RATE = 44100
DURATION = 5  # default recording duration in seconds