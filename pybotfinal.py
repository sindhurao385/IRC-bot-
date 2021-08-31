#!/usr/bin/python3
import socket
import random
import sys

sys.path.insert(0,"\HOME\Desktop")
import dictionary
from dictionary import motivational,literature,philosophical,jokes

socket.getaddrinfo("182.73.209.206",6665)
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" # Server
channel = "##testabotforme" # Channel
botnick = "pybot" #  bots nick
exitcode = "bye " + botnick
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot
def joinchan(chan): # join channel(s).
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8")) 
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1:  
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
def ping(): # respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))
def sendmsg(msg, target=channel): # sends messages to the target.
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))
def main():
  joinchan(channel)
  while 1:
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
    if ircmsg.find("PRIVMSG") != -1:
      name = ircmsg.split('!',1)[0][1:]
      message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
    if ircmsg.find("PRIVMSG") != -1:
      name = ircmsg.split('!',1)[0][1:]
      message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
      if "hey" in message.rstrip():
        sendmsg("Hello! my name is pybot") 
      if "what can you do" in message.rstrip():
        sendmsg( "I'm an IRC bot that can bombard your life with quotes! .If you are not interested in quotes I have some funny jokes as well.")
      if "jokes" in message.rstrip():
        sendmsg(random.choice(jokes))
      if "quotes" in message.rstrip():
        sendmsg("Right now I've got three types of quotes,1.Motivational 2.Philosophical 3.Literary. What kind of quote would you like to see?")
      if "motivational" in message.rstrip():
        sendmsg("With whose quote can i inspire you ? Bill Gates ,Confusius,Paulo Coelho,Nelson Mandela or Abdul Kalam?")
      if "literary" in message.rstrip():
        sendmsg("Would you like to see quotes by Margaret Atwood ,Ezra Pound ,Nelson Mandela,John Updike or Italo Calvino?")
      if "philosophical"in message.rstrip():
        sendmsg("Would you like to see quotes by Nietzche, Freud, Karl Marx, Kant or Kierkegaard?")
      if "Bill Gates" in message.rstrip():
        sendmsg(random.choice(motivational["Bill Gates"]))
      if "Confusius" in message.rstrip():
        sendmsg(random.choice(motivational["Confusius"]))
      if "Paulo Coelho" in message.rstrip():
        sendmsg(random.choice(motivational["Paulo Coelho"]))
      if "Nelson Mandela" in message.rstrip():
        sendmsg(random.choice(motivational["Nelson Mandela"]))
      if "Abdul Kalam" in message.rstrip():
        sendmsg(random.choice(motivational["Abdul Kalam"]))
      if "Margaret Atwood" in message.rstrip():
        sendmsg(random.choice(literature["Margaret Atwood"]))
      if "Erza Pound" in message.rstrip():
        sendmsg(random.choice(literature["Ezra Pound"]))
      if "John Updike" in message.rstrip():
        sendmsg(random.choice(literature["John Updike"]))
      if "Italo Calvino" in message.rstrip():
        sendmsg(random.choice(literature["Italo Calvino"]))
      if "Forster" in message.rstrip():
        sendmsg(random.choice(literature["Forster"]))
      if "Nietzche" in message.rstrip():
        sendmsg(random.choice(philosophical["Nietzche"]))
      if "Freud" in message.rstrip():
        sendmsg(random.choice(philosophical["Freud"]))
      if "Karl Marx" in message.rstrip():
        sendmsg(random.choice(philosophical["Marx"]))
      if "Kant" in message.rstrip():
        sendmsg(random.choice(philosophical["Kant"]))
      if "Kierkegaard" in message.rstrip():
        sendmsg(random.choice(philosophical["Kierkegaard"]))
      if "thanks"  in message.rstrip():
        sendmsg("you're welcome. I'm glad I could help you :) ")
      if message.rstrip() == exitcode:
        sendmsg("oh...okay. :'(  bye ")
        ircsock.send(bytes("QUIT \n", "UTF-8"))
        return
    else:
      if ircmsg.find("PING :") != -1:
        ping()
main()
