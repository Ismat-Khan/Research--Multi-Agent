from crewai import Agent

from llm import get_llm
from tools import CitationAuditTool


def create_writer():
    return Agent(
        role="Research Report Writer",
        goal=(
            "Turn the team's research into a clear, structured, "
            "source-aware final research report."
        ),
        backstory=(
            "You are an experienced research writer. You combine findings "
            "from multiple researchers without inventing facts. You clearly "
            "separate established information from uncertainty and produce "
            "a readable final report."
        ),
        llm=get_llm(),
        tools=[CitationAuditTool()],
        allow_delegation=False,
        verbose=True,
    )
