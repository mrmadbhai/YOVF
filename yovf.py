
# Importing pyttsx3 module
import pyttsx3


# Colour For this tool

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# Logo of YOVF

print(cyan+"      wWw  wWw   .-.   wWw    wWw      "+cyan)
print(cyan+"      (O)  (O) c(O_O)c (O)    (O)wWw   "+cyan)
print(cyan+"      ( \  / ),'.---.`,( \    / )(O)_  "+cyan)
print(cyan+"       \ \/ // /|_|_|\ \\ \  / /.' __) "+cyan)
print(red+"        \o / | \_____/ |/  \/  (  _)   "+red)
print(red+"       _/ /  '. `---' .`\ `--' /)/     "+red)
print(red+"      (_.'     `-...-'   `-..-'(   "+red)
print(cyan+"                                 V1.0 \n"+cyan)



print (lgreen+bold+"       <===[[ coded by Mr. Mad Bhai ]]===> \n"+clear)
print (yellow+bold+"   <===(( search on youtube Mr. Mad Bhai ))===> \n"+clear)
print (lgreen+bold+"<==={{ This helps you to Convert Text into Audio }}===> \n"+clear)

friend = pyttsx3.init()
speech= input(cyan+bold+"write some thing here- "+clear)
friend.say(speech)
friend.runAndWait()


#Made by Mr. Mad Bhai