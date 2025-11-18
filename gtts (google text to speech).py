import os
# gTTS for converting text to speech.
from gtts import gTTS

# Takes input from the user to convert into audio.
text=input('Enter the text:')

# Converts the input text to speech in English (lang='en').
# slow=False makes the voice read at normal speed.
voice=gTTS(text=text,lang='en',slow=False)

# Saves the generated speech as Audio.mp3.
voice.save('Audio.mp3')

# In windows Plays the audio file using the default media player.
os.system('start Audio.mp3')