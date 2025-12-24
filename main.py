import logging
import os
from dotenv import load_dotenv
from livekit.agents import WorkerOptions, cli
from src.agent_worker import entrypoint  # This imports the logic we just wrote

# 1. Load the .env file so we can access Groq, Sarvam, and LiveKit keys
load_dotenv()

# 2. Setup logging so we can see what the agent is thinking in the terminal
logger = logging.getLogger("voice-agent")
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    # 3. cli.run_app starts the worker process.
    # WorkerOptions tells LiveKit which function is the main entry point (entrypoint).
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
        )
    )