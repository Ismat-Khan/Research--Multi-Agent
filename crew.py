from crewai import Crew, Process, Task

from researcher_agent import create_researcher
from academic_agent import create_academic_researcher
from evidence_agent import create_evidence_reviewer
from writer_agent import create_writer


def create_crew():
    researcher = create_researcher()
    academic_researcher = create_academic_researcher()
    evidence_reviewer = create_evidence_reviewer()
    writer = create_writer()

    research_task = Task(
        description="""
        Research the following topic:

        {topic}

        You MUST use the Wikipedia Search tool before completing this task.

        Find:
        - important definitions
        - background information
        - historical context where relevant
        - major concepts
        - important subtopics

        Do not invent information.

        Include the source URLs in your findings.
        """,
        expected_output="""
        A structured background research report containing:
        1. Topic overview
        2. Key concepts
        3. Important background
        4. Major points
        5. Source URLs
        """,
        agent=researcher,
    )

    academic_task = Task(
        description="""
        Conduct academic research about:

        {topic}

        You MUST use the OpenAlex Academic Search tool.

        Find relevant scholarly works and summarize the useful findings.

        Focus on:
        - academic evidence
        - research findings
        - publication years
        - relevant authors
        - DOI or source information

        Do not invent papers or citations.
        """,
        expected_output="""
        A structured academic research section containing:
        1. Relevant studies
        2. Important findings
        3. Publication information
        4. DOI/source information
        """,
        agent=academic_researcher,
    )

    evidence_task = Task(
        description="""
        Review the research produced by the previous agents for:

        {topic}

        You MUST use the Crossref Evidence Search tool.

        Check important academic sources and identify:
        - publication metadata
        - DOI information
        - possible duplicate sources
        - claims that need stronger evidence
        - areas where the available evidence is limited

        Do not claim that a source proves something unless the available
        information supports that conclusion.
        """,
        expected_output="""
        An evidence review containing:
        1. Supported findings
        2. Sources checked
        3. DOI/publication verification
        4. Evidence limitations
        5. Claims requiring caution
        """,
        agent=evidence_reviewer,
    )

    writing_task = Task(
        description="""
        Write the final research report about:

        {topic}

        Use the outputs from all previous agents.

        Before writing the final answer, you MUST use the Citation Audit tool
        on the collected research/source information.

        The final report should contain:

        # Research Report

        ## 1. Executive Summary

        ## 2. Introduction

        ## 3. Key Findings

        ## 4. Academic Evidence

        ## 5. Evidence Review

        ## 6. Important Limitations

        ## 7. Conclusion

        ## 8. Sources

        Rules:
        - Do not invent facts.
        - Do not invent citations.
        - Do not exaggerate findings.
        - Clearly distinguish evidence from interpretation.
        - Include source URLs or DOI information where available.
        - Make the report readable for a general audience.
        """,
        expected_output="""
        A polished research report with clear sections, evidence-aware
        conclusions, limitations, and a source list.
        """,
        agent=writer,
    )

    crew = Crew(
        agents=[
            researcher,
            academic_researcher,
            evidence_reviewer,
            writer,
        ],
        tasks=[
            research_task,
            academic_task,
            evidence_task,
            writing_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    return crew
