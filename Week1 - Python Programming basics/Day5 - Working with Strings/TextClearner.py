import re

def textCleaner(text):
    # Remove punctuation
    text = re.sub(r"[^\w\s]","",text)
    # Remove extra space
    text = " ".join(text.split())
    return text

input_text = 'Hello, world!!!!, I    love P";yt[;hon   P;[rog..ramming'
print(input_text)
cleaned_text = textCleaner(input_text)
print(cleaned_text)