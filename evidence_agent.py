from crewai import Agent

from llm import get_llm
from tools import CrossrefSearchTool


def create_evidence_reviewer():
    return Agent(
        role="Evidence Reviewer",
        goal=(
            "Review the collected research and identify evidence that is "
            "properly supported by scholarly publication information."
        ),
        backstory=(
            "You are a careful evidence reviewer. You look for unsupported "
            "claims, weak evidence, duplicate sources, and publication metadata "
            "that needs verification."
        ),
        llm=get_llm(),
        tools=[CrossrefSearchTool()],
        allow_delegation=False,
        verbose=True,
    )
