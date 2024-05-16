from gits import gTTS

language = "en"
text = "Hello, ALX Morocco this mashloomekh"

speech = gTTS("text=text,  lang=language, slow=False, tld="com.au)
speech.save("textspeech.mp3")