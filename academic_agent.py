from crewai import Agent

from llm import get_llm
from tools import OpenAlexSearchTool


def create_academic_researcher():
    return Agent(
        role="Academic Researcher",
        goal=(
            "Find relevant academic studies and scholarly evidence "
            "that can support the research topic."
        ),
        backstory=(
            "You are an academic research specialist. "
            "You look beyond general web information and identify scholarly "
            "works, publication years, and useful academic evidence."
        ),
        llm=get_llm(),
        tools=[OpenAlexSearchTool()],
        allow_delegation=False,
        verbose=True,
    )
