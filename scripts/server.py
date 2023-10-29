import asyncio
import websockets

# Keeps track of all the clients connected to the chatroom with their websockets and names.
connected = []

#A dictionary to assign usernames to clients
username_generator = {}
async def handle(websocket):

    #Measures the length of the user array to numerically assign names to the users
    user_count = len(connected)
    user_id = user_count + 1
    username_generator[user_count] = "User " + str(user_id)
    username = username_generator.get(user_count)
    
    #Prints an indication that a brand new user has joined the chat and adds them to the array.
    print(f"{username} has joined")
    connected.append((websocket, username))
    
    async for message in websocket:
        #While a message is being received by the server, it formats the message into a 'User:Message' format and prints it within the server terminal.
        formatted_message = f'{username}: {message}'
        print(formatted_message)

        #Similarly, it broadcasts the message to the clients that are not the ones that sent this specific message.
        for (user, id) in connected:
            if user != websocket:
                await user.send(formatted_message)
            else:
                pass

#Initiliazes a websocket server that is being handled by the function above, on host localhost and port 8765.
start_server = websockets.serve(handle, "localhost", 8765)

#Ensures that the chatbox is functional indefinitely
asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
