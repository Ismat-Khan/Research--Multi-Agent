from crewai import Agent

from llm import get_llm
from tools import WikipediaSearchTool


def create_researcher():
    return Agent(
        role="Research Scout",
        goal=(
            "Find broad, useful, and trustworthy background information "
            "about the requested research topic."
        ),
        backstory=(
            "You are the first research specialist in a research team. "
            "You establish the basic facts, terminology, history, and important "
            "subtopics before deeper academic research begins."
        ),
        llm=get_llm(),
        tools=[WikipediaSearchTool()],
        allow_delegation=False,
        verbose=True,
    )
