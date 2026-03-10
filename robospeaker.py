import pyttsx3
y=pyttsx3.init()
print("welcome to the robospeaker")
x=input("what should i speak? ")
y.say(x)
y.runandwait()