from voice.listen import listen
from voice.speak import speak
from voice.wake_word import detect_wake_word
from core.pipeline import run_pipeline

def run_assistant():
    speak("Brahmastra is ready")

    while True:
        text = listen()

        if not text:
            continue

        # Wake word check
        if detect_wake_word(text):
            speak("Yes, tell me command")

            command = listen()

            if command:
                response = run_pipeline(command)
                speak(response)