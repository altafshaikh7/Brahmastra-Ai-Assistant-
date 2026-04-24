from actions.browser import open_youtube, search_google
from actions.browser import play_song   # 🔥 ADD
from actions.system import get_time, volume_up, volume_down
from actions.files import open_file
from actions.whatsapp import send_whatsapp
from actions.general import wikipedia_search, greet, fallback

def dispatch_action(intent, text):

    if intent == "open_youtube":
        return open_youtube()

    elif intent == "search_google":
        return search_google(text)

    elif intent == "play_song":   # 🔥 ADD
        return play_song(text)

    elif intent == "get_time":
        return get_time()

    elif intent == "volume_up":
        return volume_up()

    elif intent == "volume_down":
        return volume_down()

    elif intent == "open_file":
        return open_file(text)

    elif intent == "send_whatsapp":
        return send_whatsapp("+919999999999", "Hello from Brahmastra")

    elif intent == "wiki":
        return wikipedia_search(text)

    elif intent == "greet":
        return greet()

    else:
        return fallback()