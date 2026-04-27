import pywhatkit as kit
import time

def send_whatsapp(number, message):
    try:
        # Ensure number format
        if not number.startswith("+"):
            return "Please include country code (e.g. +91...)"

        kit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        
        time.sleep(5)  # thoda wait for send
        
        return "Message sent on WhatsApp"
    
    except Exception as e:
        return f"Failed to send message: {str(e)}"