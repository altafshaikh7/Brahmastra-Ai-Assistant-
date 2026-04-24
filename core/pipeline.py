from nlp.intent import predict_intent
from actions.dispatcher import dispatch_action

def run_pipeline(text):
    intent = predict_intent(text)
    
    print("Intent:", intent)   # ✅ yahan likhna hai

    response = dispatch_action(intent, text)
    return response