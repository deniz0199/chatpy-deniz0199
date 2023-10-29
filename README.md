# Simple chatting application on localhost

## Introduction
This application allows users to send and receive messages from one another on host localhost and port 8765. This is achieved by using the websockets library, and using a server and client script simultaneously. The server also archives all of the exchanges, and when each user joined in its own terminal.

## Manual
In order to run this application, one must first run server.py. Then, corresponding to the number of users that will be chatting, different terminals must be opened. Afterwards, each user needs to connect to ws://localhost:8765/. This can be achieved by running python3 -m websockets ws://localhost:8765/ on the terminals. Note that this script is only functional so long as the server and clients are all connected to ws://localhost:8765/. Afterwards, the clients are free to enter their messages to their respective terminals, and the server will allow them to receive broadcasts of other messages.

## Safety concerns
As this application only allows text to be broadcast, it doesn't pose a great threat to its users. However, if chatting with untrusted clients, it is advised to not be immediately trusting of the links they share through this application in case they are malicious.
