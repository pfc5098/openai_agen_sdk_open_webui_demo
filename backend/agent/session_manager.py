from openai_agents import Session

# Create a single global session for the agent (single user)
_session = Session()

def get_session() -> Session:
    """Return the global session for maintaining conversation state."""
    return _session
