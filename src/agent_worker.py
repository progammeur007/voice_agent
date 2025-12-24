import logging
from dotenv import load_dotenv

load_dotenv()

from livekit.agents import JobContext, llm, Agent, AgentSession
from livekit.plugins import groq, sarvam, silero

from src.prompts import SYSTEM_PROMPT
from src.tools import search_schemes, search_web, check_eligibility

logger = logging.getLogger("voice-agent")

async def entrypoint(ctx: JobContext):
    await ctx.connect()
    logger.info(f"Connected to room: {ctx.room.name}")

  
    maitra_agent = Agent(
        instructions=SYSTEM_PROMPT,
        tools=[search_schemes, search_web, check_eligibility],
    )

    session = AgentSession(
        llm=groq.LLM(model="llama-3.3-70b-versatile"),
        stt=sarvam.STT(language="mr-IN"),
        tts=sarvam.TTS(target_language_code="mr-IN"),
        vad=silero.VAD.load(),
    )


    @session.on("user_input_transcribed")
    def _on_user_input(event):
        print(f"\n📥 [CONVERSATION STATE] User said: {event.transcript}")

    @session.on("tool_call_completed")
    def _on_tool_call(tool_call):
        print(f"🛠️  [REASONING] LLM used tool: {tool_call.tool_name}")

    await session.start(room=ctx.room, agent=maitra_agent)

    await session.say(
        "नमस्कार, मी मैत्र आहे. मी तुमची काय मदत करू शकतो?",
        allow_interruptions=True
    )