import pyttsx3

text_speech = pyttsx3.init()
blog=''''''
text_speech.setProperty('rate',130)
text_speech.say(blog)
text_speech.runAndWait()
