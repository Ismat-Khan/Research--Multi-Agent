import re
from urllib.parse import quote

import requests

from crewai.tools import BaseTool


class WikipediaSearchTool(BaseTool):
    name: str = "Wikipedia Search"
    description: str = (
        "Search Wikipedia for reliable background information about a research topic. "
        "Use this tool to find definitions, history, important concepts, and general context."
    )

    def _run(self, query: str) -> str:
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 5,
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            return "No Wikipedia results found."

        output = []

        for item in results:
            title = item.get("title", "")
            snippet = re.sub("<.*?>", "", item.get("snippet", ""))

            page_url = (
                "https://en.wikipedia.org/wiki/"
                + quote(title.replace(" ", "_"))
            )

            output.append(
                f"Title: {title}\n"
                f"Summary: {snippet}\n"
                f"Source: {page_url}"
            )

        return "\n\n".join(output)


class OpenAlexSearchTool(BaseTool):
    name: str = "OpenAlex Academic Search"
    description: str = (
        "Search OpenAlex for academic research papers and scholarly works. "
        "Use this tool to find academic evidence related to the research topic."
    )

    def _run(self, query: str) -> str:
        url = "https://api.openalex.org/works"

        params = {
            "search": query,
            "per-page": 5,
        }

        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()

        data = response.json()

        results = data.get("results", [])

        if not results:
            return "No academic results found."

        output = []

        for item in results:
            title = item.get("title", "Unknown title")
            publication_year = item.get("publication_year", "Unknown")

            doi = item.get("doi")
            landing_page = item.get("primary_location", {}).get(
                "landing_page_url"
            )

            source = doi or landing_page or item.get("id", "")

            output.append(
                f"Title: {title}\n"
                f"Year: {publication_year}\n"
                f"Source: {source}"
            )

        return "\n\n".join(output)


class CrossrefSearchTool(BaseTool):
    name: str = "Crossref Evidence Search"
    description: str = (
        "Search Crossref for scholarly publication metadata. "
        "Use this tool to verify academic publication titles, authors, years, and DOI information."
    )

    def _run(self, query: str) -> str:
        url = "https://api.crossref.org/works"

        params = {
            "query.bibliographic": query,
            "rows": 5,
        }

        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()

        data = response.json()

        items = data.get("message", {}).get("items", [])

        if not items:
            return "No Crossref results found."

        output = []

        for item in items:
            title_list = item.get("title", [])
            title = title_list[0] if title_list else "Unknown title"

            authors = item.get("author", [])

            author_names = []

            for author in authors[:4]:
                given = author.get("given", "")
                family = author.get("family", "")

                name = f"{given} {family}".strip()

                if name:
                    author_names.append(name)

            year = "Unknown"

            date_parts = item.get("published", {}).get(
                "date-parts", []
            )

            if date_parts and date_parts[0]:
                year = date_parts[0][0]

            doi = item.get("DOI", "")

            output.append(
                f"Title: {title}\n"
                f"Authors: {', '.join(author_names)}\n"
                f"Year: {year}\n"
                f"DOI: {doi}"
            )

        return "\n\n".join(output)


class CitationAuditTool(BaseTool):
    name: str = "Citation Audit"
    description: str = (
        "Inspect a research draft and identify URLs and DOI references "
        "that should be checked before producing the final report."
    )

    def _run(self, text: str) -> str:
        urls = re.findall(
            r"https?://[^\s\]\)]+",
            text
        )

        dois = re.findall(
            r"10\.\d{4,9}/[-._;()/:A-Z0-9]+",
            text,
            flags=re.IGNORECASE,
        )

        result = []

        result.append(f"URLs found: {len(urls)}")

        for url in urls[:15]:
            result.append(f"- {url}")

        result.append(f"DOIs found: {len(dois)}")

        for doi in dois[:15]:
            result.append(f"- https://doi.org/{doi}")

        if not urls and not dois:
            result.append(
                "No obvious URLs or DOIs were found. "
                "The final report should clearly identify sources from the research context."
            )

        return "\n".join(result)
