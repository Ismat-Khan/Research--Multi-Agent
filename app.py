import streamlit as st
import time

from crew import create_crew


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Research Lab",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(88, 80, 255, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(0, 180, 255, 0.09),
                transparent 30%
            ),
            #070b14;
        color: #f5f7ff;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    header {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* HERO */

    .hero {
        padding: 45px 10px 35px 10px;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        border: 1px solid rgba(130, 145, 255, 0.28);
        background: rgba(80, 90, 255, 0.10);
        color: #adb7ff;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
    }

    .hero-title {
        margin-top: 18px;
        font-size: clamp(42px, 6vw, 72px);
        line-height: 1.02;
        font-weight: 800;
        letter-spacing: -3px;
        background: linear-gradient(
            90deg,
            #ffffff,
            #c5cbff,
            #7bdcff
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        max-width: 780px;
        margin-top: 18px;
        color: #909bb4;
        font-size: 17px;
        line-height: 1.7;
    }

    /* SECTION */

    .section-header {
        margin-top: 35px;
        margin-bottom: 20px;
    }

    .section-eyebrow {
        color: #75819e;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 2px;
    }

    .section-title {
        margin-top: 7px;
        color: #f5f7ff;
        font-size: 25px;
        font-weight: 750;
    }

    .section-subtitle {
        margin-top: 6px;
        color: #78849d;
        font-size: 13px;
    }

    /* AGENTS */

    .agent-card {
        min-height: 180px;
        padding: 21px;
        background: rgba(18, 24, 40, 0.82);
        border: 1px solid rgba(130, 145, 180, 0.18);
        border-radius: 18px;
        box-sizing: border-box;
        transition: 0.25s ease;
    }

    .agent-card:hover {
        transform: translateY(-4px);
        border-color: rgba(125, 140, 255, 0.42);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25);
    }

    .agent-icon {
        font-size: 28px;
        margin-bottom: 17px;
    }

    .agent-name {
        color: #f5f7ff;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .agent-role {
        color: #8d99b3;
        font-size: 12px;
    }

    .agent-tool-label {
        margin-top: 21px;
        color: #66728c;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 1.5px;
    }

    .agent-tool {
        margin-top: 4px;
        color: #aab4c8;
        font-size: 11px;
    }

    /* WORKING */

    .working-card {
        margin-top: 25px;
        padding: 22px;
        border-radius: 18px;
        background: linear-gradient(
            135deg,
            rgba(38, 48, 90, 0.75),
            rgba(14, 20, 35, 0.90)
        );
        border: 1px solid rgba(120, 140, 255, 0.22);
    }

    .working-label {
        color: #7d89a5;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 1.7px;
    }

    .working-agent {
        margin-top: 7px;
        color: #ffffff;
        font-size: 20px;
        font-weight: 700;
    }

    .working-description {
        margin-top: 5px;
        color: #8995ad;
        font-size: 12px;
    }

    /* REPORT */

    .report-box {
        padding: 25px;
        margin-top: 15px;
        background: rgba(14, 20, 34, 0.85);
        border: 1px solid rgba(130, 145, 180, 0.16);
        border-radius: 18px;
    }

    /* METRICS */

    .metric-card {
        padding: 20px;
        background: rgba(15, 21, 35, 0.75);
        border: 1px solid rgba(120, 135, 170, 0.14);
        border-radius: 16px;
        text-align: center;
    }

    .metric-number {
        color: #f5f7ff;
        font-size: 27px;
        font-weight: 800;
    }

    .metric-label {
        margin-top: 5px;
        color: #737f99;
        font-size: 10px;
        letter-spacing: 1px;
    }

    /* INPUT */

    textarea {
        background: #0d1321 !important;
        color: #f5f7ff !important;
        border: 1px solid rgba(130, 145, 180, 0.20) !important;
        border-radius: 14px !important;
    }

    /* BUTTON */

    .stButton > button {
        width: 100%;
        min-height: 48px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(
            135deg,
            #6674ff,
            #4d9cff
        );
        color: white;
        font-weight: 700;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
    }

    /* DOWNLOAD */

    .stDownloadButton > button {
        width: 100%;
        border-radius: 12px;
        background: #111a2c;
        color: #dce3f5;
        border: 1px solid rgba(130, 145, 180, 0.20);
    }

    /* FOOTER */

    .footer {
        margin-top: 55px;
        padding-top: 20px;
        border-top: 1px solid rgba(130, 145, 180, 0.10);
        text-align: center;
        color: #56617a;
        font-size: 11px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">MULTI-AGENT RESEARCH LAB</div>

        <div class="hero-title">
            Research that goes<br>
            deeper than search.
        </div>

        <div class="hero-subtitle">
            A CrewAI-powered research team where specialized AI agents
            discover information, find scholarly evidence, verify sources,
            and produce a structured research report.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RESEARCH INPUT
# ============================================================

st.markdown(
    """
    <div class="section-header">
        <div class="section-eyebrow">
            START A RESEARCH SESSION
        </div>

        <div class="section-title">
            What do you want to research?
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


topic = st.text_area(
    "Research topic",
    placeholder="Example: The impact of artificial intelligence on modern education",
    height=120,
    label_visibility="collapsed",
)


start_research = st.button(
    "🚀 Start Research",
    width="stretch",
)


# ============================================================
# AGENT TEAM
# ============================================================

st.markdown(
    """
    <div class="section-header">

        <div class="section-eyebrow">
            RESEARCH TEAM
        </div>

        <div class="section-title">
            Your AI Research Team
        </div>

        <div class="section-subtitle">
            Four specialized agents working together to research,
            verify, and synthesize your topic.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


agents = [
    (
        "🔎",
        "Research Scout",
        "Background Intelligence",
        "Wikipedia Search",
    ),
    (
        "🎓",
        "Academic Researcher",
        "Scholarly Intelligence",
        "OpenAlex Search",
    ),
    (
        "🔍",
        "Evidence Reviewer",
        "Evidence Verification",
        "Crossref Search",
    ),
    (
        "✍️",
        "Research Writer",
        "Research Synthesis",
        "Citation Audit",
    ),
]


agent_columns = st.columns(4)

for column, agent in zip(agent_columns, agents):

    icon, name, role, tool = agent

    with column:

        st.markdown(
            f"""
            <div class="agent-card">

                <div class="agent-icon">{icon}</div>

                <div class="agent-name">
                    {name}
                </div>

                <div class="agent-role">
                    {role}
                </div>

                <div class="agent-tool-label">
                    TOOL
                </div>

                <div class="agent-tool">
                    {tool}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# RUN RESEARCH
# ============================================================

if start_research:

    if not topic.strip():

        st.warning("Please enter a research topic first.")

    else:

        st.markdown(
            """
            <div class="working-card">

                <div class="working-label">
                    CURRENT ACTIVITY
                </div>

                <div class="working-agent">
                    🔎 Research team is working...
                </div>

                <div class="working-description">
                    The agents are processing your research topic.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        progress = st.progress(0)

        status = st.status(
            "🔬 Starting research...",
            expanded=True,
        )

        try:

            status.write(
                "🔎 Research Scout is gathering background information..."
            )

            progress.progress(15)

            time.sleep(0.3)

            status.write(
                "🎓 Academic Researcher is finding scholarly sources..."
            )

            progress.progress(30)

            time.sleep(0.3)

            status.write(
                "🔍 Evidence Reviewer is checking evidence..."
            )

            progress.progress(45)

            time.sleep(0.3)

            status.write(
                "✍️ Research Writer is preparing the final synthesis..."
            )

            progress.progress(60)

            # -----------------------------------------------
            # RUN CREW
            # -----------------------------------------------

            crew = create_crew()

            result = crew.kickoff(
                inputs={
                    "topic": topic.strip()
                }
            )

            # -----------------------------------------------
            # SAFELY CONVERT RESULT TO TEXT
            # -----------------------------------------------

            if result is None:

                result_text = (
                    "The research team completed the process, "
                    "but no report was returned."
                )

            else:

                result_text = str(result).strip()

                if not result_text:

                    result_text = (
                        "The research team completed the process, "
                        "but the generated report was empty."
                    )

            # -----------------------------------------------
            # SAVE RESULT
            # -----------------------------------------------

            st.session_state["research_result"] = result_text
            st.session_state["research_topic"] = topic.strip()

            progress.progress(100)

            status.update(
                label="✅ Research completed",
                state="complete",
                expanded=False,
            )

        except Exception as error:

            status.update(
                label="❌ Research failed",
                state="error",
                expanded=True,
            )

            st.error(
                "The research process failed."
            )

            st.code(
                str(error),
                language="text",
            )


# ============================================================
# FINAL REPORT
# ============================================================

if "research_result" in st.session_state:

    st.markdown(
        """
        <div class="section-header">

            <div class="section-eyebrow">
                FINAL OUTPUT
            </div>

            <div class="section-title">
                Research Report
            </div>

            <div class="section-subtitle">
                Synthesized from the work of the complete
                research agent team.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    report = st.session_state.get(
        "research_result",
        "",
    )

    # Make absolutely sure download data is a string.
    if report is None:
        report = ""

    report = str(report)

    st.markdown(
        '<div class="report-box">',
        unsafe_allow_html=True,
    )

    st.markdown(report)

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    st.write("")

    # --------------------------------------------------------
    # SAFE DOWNLOAD
    # --------------------------------------------------------

    if report.strip():

        st.download_button(
            label="⬇️ Download Research Report",
            data=report.encode("utf-8"),
            file_name="research_report.txt",
            mime="text/plain",
            key="download_research_report",
            width="stretch",
        )


# ============================================================
# SYSTEM OVERVIEW
# ============================================================

st.markdown(
    """
    <div class="section-header">

        <div class="section-eyebrow">
            SYSTEM OVERVIEW
        </div>

        <div class="section-title">
            Research Pipeline
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


metric_columns = st.columns(4)


metrics = [
    ("04", "AI AGENTS"),
    ("04", "RESEARCH TOOLS"),
    ("01", "RESEARCH TOPIC"),
    (
        "✓" if "research_result" in st.session_state else "—",
        "STATUS",
    ),
]


for column, (number, label) in zip(
    metric_columns,
    metrics,
):

    with column:

        st.markdown(
            f"""
            <div class="metric-card">

                <div class="metric-number">
                    {number}
                </div>

                <div class="metric-label">
                    {label}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Built with Streamlit · CrewAI · Groq · Research Tools
    </div>
    """,
    unsafe_allow_html=True,
)
