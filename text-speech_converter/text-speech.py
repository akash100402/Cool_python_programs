import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1.0)  # Volume level

# Convert text to speech
text = "Hello, how are you today?"
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()