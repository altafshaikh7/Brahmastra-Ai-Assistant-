import pywhatkit as kit

def send_whatsapp(number, message):
    try:
        kit.sendwhatmsg_instantly(number, message)
        return "Message sent on WhatsApp"
    except:
        return "Failed to send message"