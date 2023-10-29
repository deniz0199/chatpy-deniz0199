import asyncio
import websockets
import aioconsole

#Handles message receiving. While a message is being broadcast from the server, it asynchronously prints the message on the terminal.
async def received_message_handler(websocket):
    while True:
        message = await websocket.recv()
        await aioconsole.aprint(message)

#Handles sending messages to the server. When an input is entered, the websocket sends the message for the server to broadcast to other servers.
async def sent_message_handler(websocket):
    while True:
        message = await aioconsole.ainput()
        await websocket.send(message)


async def main():
    #The address that the users need to be connected to communicate.
    link = "ws://localhost:8765"
    print("Greetings.")

    #Connects to the server associated with the link
    async with websockets.connect(link) as websocket:
        #Ensures that the programme is executed when these two functions are both complete.
        await asyncio.gather(
            received_message_handler(websocket),
            sent_message_handler(websocket)
        )

asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop.run_forever()
