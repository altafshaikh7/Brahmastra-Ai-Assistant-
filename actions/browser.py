import pywhatkit as kit

def play_song(song):
    try:
        song = song.lower().replace("play", "").replace("song", "").strip()
        kit.playonyt(song)
        return f"Playing {song}"
    except Exception as e:
        print("Error:", e)
        return "Song play nahi ho paya"