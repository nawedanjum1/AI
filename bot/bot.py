import aiml
import sys
import os
os.chdir("C:/Users/MD/Desktop/aiml-files")
mybot = aiml.Kernel()
mybot.setBotPredicate("name","AskMe")
mybot.learn('startup.xml')
mybot.respond('load aiml b')
mybot.saveBrain('standard.brn')
while True:
  print (mybot.respond(input("Enter input >")))
