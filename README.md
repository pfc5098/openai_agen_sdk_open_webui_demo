# OpenAI Agent SDK + Open WebUI Demo

This repository demonstrates a basic integration between the OpenAI Agents SDK and Open WebUI.

## Features

- A FastAPI backend that exposes a chat endpoint using the OpenAI Agents SDK and supports streaming responses.
- Built-in OpenAI web search tool and a custom crypto price tool using CoinGecko.
- Simple session management (single session) to preserve chat context.
- Example configuration guide for connecting Open WebUI to this backend.

## Setup

1. Clone this repository.
2. Install Python dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and set your OpenAI API key:

   ```
   cp .env.example .env
   ```

4. Start the backend server:

   ```
   uvicorn backend.app:app --reload
   ```

The server will be available at `http://localhost:8000`.

## Integrating with Open WebUI

See the instructions in `openwebui/config.md` for configuring Open WebUI to use this backend as a chat provider.
