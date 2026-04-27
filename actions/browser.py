import webbrowser
import pywhatkit as kit

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def play_song(song):
    clean_song = song.lower().replace("play", "").replace("song", "").strip()
    
    if not clean_song:
        return "Konsa song play karu?"
    
    kit.playonyt(clean_song)
    return f"Playing {clean_song}"