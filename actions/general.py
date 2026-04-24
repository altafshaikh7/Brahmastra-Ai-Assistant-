import wikipedia

def wikipedia_search(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "No result found"

def greet():
    return "Hello, I am Brahmastra AI"

def fallback():
    return "Sorry, I didn't understand"