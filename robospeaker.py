import pyttsx3
engine=pyttsx3.init()
print("welcome to the robospeaker")
x=input("what should i speak? ")
engine.say(x)
engine.runAndWait()