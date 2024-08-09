import pyttsx3

print('Welcome to Robo Speaker 1.0')
speak = input("Enter what you want to speak: ")

engine = pyttsx3.init()
engine.say(speak)
engine.runAndWait()

