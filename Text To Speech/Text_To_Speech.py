from gtts import gTTS
import os



myText = "My Name is Aditya Singh"
language = 'en'
output = gTTS(text = myText,lang=language , slow=False)

# file name
output.save('speech.mp3')

os.system('start speech.mp3')
