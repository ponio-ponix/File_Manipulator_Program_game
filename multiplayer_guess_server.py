import asyncio
import random
import websockets

# Dictionary to store game state per client
# Each client gets its own random number and guess count

CLIENTS = {}

async def handle_client(websocket):
    # Generate a random number for this client
    number = random.randint(1, 100)
    guesses = 0
    CLIENTS[websocket] = number
    await websocket.send("Welcome to Guess the Number! Guess a number between 1 and 100.")
    try:
        async for message in websocket:
            try:
                guess = int(message.strip())
            except ValueError:
                await websocket.send("Please send a valid integer.")
                continue

            guesses += 1
            if guess < number:
                await websocket.send("Higher")
            elif guess > number:
                await websocket.send("Lower")
            else:
                await websocket.send(f"Correct! It took you {guesses} guesses. Starting a new round...")
                number = random.randint(1, 100)
                guesses = 0
                CLIENTS[websocket] = number
    finally:
        CLIENTS.pop(websocket, None)

async def main(host="0.0.0.0", port=8765):
    async with websockets.serve(handle_client, host, port):
        print(f"Server started on {host}:{port}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
