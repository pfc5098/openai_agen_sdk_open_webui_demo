import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from openai_agents import Runner
from .agent.agent import get_agent
from .agent.session_manager import get_session

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Initialize the agent and single session
agent = get_agent()
session = get_session()

@app.post("/chat")
async def chat(payload: dict):
    """
    Chat endpoint that accepts a JSON payload with a 'message' field.
    It streams the agent's response back to the client.
    """
    message = payload.get("message")
    if not message:
        raise HTTPException(status_code=400, detail="message field is required")

    async def token_generator():
        # Use the OpenAI Agents SDK to stream responses token by token
        async for token in Runner.run_stream(agent, message, session=session):
            # Yield plain text tokens
            yield token

    return StreamingResponse(token_generator(), media_type="text/plain")
