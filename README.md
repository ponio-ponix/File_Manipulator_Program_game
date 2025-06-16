# Guess The Number Game Server

This repository contains a simple interactive game and a WebSocket server
implementation that allows multiple players to play a "guess the number"
 game simultaneously.

## Files

- `guess_the_number_game.py` – original command line version.
- `multiplayer_guess_server.py` – asynchronous WebSocket server.
- `client.html` – basic browser client for connecting to the server.

## Running the Server

Install the required dependency:

```bash
pip install websockets
```

Start the server with:

```bash
python multiplayer_guess_server.py
```

Then open `client.html` in a web browser to play.
