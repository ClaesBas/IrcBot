# -*- coding: utf-8 -*-
# File: IrcBot.py

import sys
import socket
import string
import datetime

from IrcBotSettings import *

s=socket.socket( )
s.connect((HOST, PORT))
if PASS:
    s.send("PASS %s\r\n" % PASS) 
s.send("NICK %s\r\n" % NICK)
s.send("USER %s 0 * :%s\r\n" % (NICK, REALNAME))
s.send("JOIN %s\r\n" % ','.join(LOG_CHANNELS))

readbuffer = ""
do_loop = True

while do_loop:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop()

    for line in temp:
        
        line=string.rstrip(line)
        
        if DEBUG:
            print line
        
        line=string.split(line)

        if(line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])

        if(line[1] == "PRIVMSG"):
            
            sender = line[0][1:].split("!")[0]
            channel = line[2]
            command_str = ""
            parameters = []
            
            if(len(line) > 3):
                   
                admin = line[0][1:] in ADMINS

		# Any request to the "Bot"?
                if(channel == NICK):
                    
                    command_str = line[3][1:].lower()

		    # "Private" commands without parameters
                    if(len(line) == 4):
           
                        #Admin commands
                        if admin:
			    # Should we quit?
                            if(command_str == QUIT_CMD_STR):
                                s.send("QUIT :%s\r\n" % QUIT_MSG)
                                do_loop = False

                    else:
                        parameters = line[4:]   
                    
                elif((line[3] == ":" + NICK + ":") and (len(line) > 4)):
                    
                    command_str = line[4].lower()
                    if(len(line) > 5):
                        parameters = line[5:]

                    
                if(DEBUG and command_str):
                   print "command_str|" + command_str + \
                       "|parameters:" + ' '.join(parameters)

                if((command_str == "echo") and parameters):
                    if(channel == NICK):
                        destination = sender
                    else:
                        destination = channel
                    s.send( \
                        "PRIVMSG %s :%s\r\n" % \
                        (destination, ' '.join(parameters)) \
                    )
                    
            # Skall vi "logga"?
            if(channel in LOG_CHANNELS):
                
                time = datetime.datetime.now()
                msg = ' '.join(line[3:])[1:]
                
                if DEBUG:
                    print "%s|%s|%s|%s" % (time, sender, channel, msg)

                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		# And here we should push the message to Postgres or something
                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# That's all folks!
