# -*- coding: utf-8 -*-
# File: IrcBotSettings.py

DEBUG = True

HOST = "irc.freenode.net"
PORT = 6667

NICK = "PythonSeBot"
IDENT = "PythonSeBot"
REALNAME = "Python Sverige Arkivbot"
#PASS = "XXXXXXXXXXXXXXXX"	# Only if/when we registered the Nick...

if DEBUG:
    LOG_CHANNELS = ["#onlyTestWithIrcBot",]
else:
    LOG_CHANNELS = [
	"#python-se",
        "#django",
        "#django-se",
        "#djangocon",
        "#django-dev",
        "#django-sprint",
        "#django-south",
    ]

QUIT_MSG = "God bye"
QUIT_CMD_STR= "quit"

ADMINS = ["ClaesBas!~ClaesBas@stock-zit3.8.cust.blixtvik.net",]
