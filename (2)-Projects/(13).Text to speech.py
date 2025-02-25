import gtts
import playsound
import googletrans
print(googletrans.LANGUAGES)
text=input("\n\nEnter the text: ")
language=input("Enter the language: ")
sound=gtts.gTTS(text, language)
sound.save("Soundbox-1.mp3")
playsound.playsound("Soundbox-1.mp3")