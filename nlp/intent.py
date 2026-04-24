import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def predict_intent(text):
    text = preprocess(text)

    # 🎵 SONG PLAY (TOP PRIORITY 🔥)
    if "play" in text or "song" in text:
        return "play_song"

    # 🎥 YOUTUBE
    elif "youtube" in text:
        return "open_youtube"

    # 🔍 GOOGLE SEARCH
    elif "search" in text or "google" in text:
        return "search_google"

    # ⏰ TIME
    elif "time" in text:
        return "get_time"

    # 🔊 VOLUME
    elif "volume up" in text or "increase volume" in text:
        return "volume_up"

    elif "volume down" in text or "decrease volume" in text:
        return "volume_down"

    # 📁 FILE
    elif "file" in text or "open file" in text:
        return "open_file"

    # 💬 WHATSAPP
    elif "whatsapp" in text or "send message" in text:
        return "send_whatsapp"

    # 📚 WIKIPEDIA
    elif "who is" in text or "what is" in text or "tell me about" in text:
        return "wiki"

    # 👋 GREETING
    elif "hello" in text or "hi" in text or "hey" in text:
        return "greet"

    # 🌐 GENERAL FALLBACK
    elif "open" in text:
        return "search_google"

    else:
        return "unknown"