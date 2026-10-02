import time
import streamlit as st

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
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       GLOBAL
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(82, 82, 255, 0.10),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(0, 180, 255, 0.08),
                transparent 28%
            ),
            #070b14;
        color: #f5f7ff;
    }

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* =========================
       HERO
       ========================= */

    .hero {
        padding: 45px 10px 35px 10px;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 13px;

        border: 1px solid rgba(130, 145, 255, 0.25);
        border-radius: 999px;

        background: rgba(90, 100, 255, 0.08);

        color: #aeb7ff;

        font-size: 11px;
        font-weight: 700;

        letter-spacing: 1.5px;
    }

    .hero-title {
        margin-top: 18px;

        font-size: clamp(40px, 6vw, 72px);
        line-height: 1.02;

        font-weight: 800;

        letter-spacing: -3px;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #bfc8ff,
                #7bdcff
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        max-width: 760px;

        margin-top: 18px;

        color: #8f9ab3;

        font-size: 17px;
        line-height: 1.7;
    }


    /* =========================
       SECTION HEADERS
       ========================= */

    .section-header {
        margin-top: 35px;
        margin-bottom: 18px;
    }

    .section-eyebrow {
        color: #7783a2;

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

        color: #78849e;

        font-size: 13px;
    }


    /* =========================
       RESEARCH INPUT
       ========================= */

    .input-card {
        padding: 25px;

        background: rgba(16, 22, 36, 0.75);

        border: 1px solid rgba(130, 145, 180, 0.16);

        border-radius: 20px;

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.18);
    }


    /* =========================
       AGENT CARDS
       ========================= */

    .agent-card {
        width: 100%;
        min-height: 175px;

        padding: 20px;

        box-sizing: border-box;

        background: rgba(18, 24, 40, 0.78);

        border: 1px solid rgba(130, 145, 180, 0.18);

        border-radius: 18px;

        transition: all 0.25s ease;
    }

    .agent-card:hover {
        transform: translateY(-4px);

        border-color: rgba(130, 145, 255, 0.40);

        box-shadow:
            0 12px 35px rgba(0, 0, 0, 0.25);
    }

    .agent-icon {
        font-size: 28px;
        line-height: 1;

        margin-bottom: 18px;
    }

    .agent-name {
        color: #f4f7ff;

        font-size: 16px;
        font-weight: 700;

        line-height: 1.3;

        margin-bottom: 6px;
    }

    .agent-role {
        color: #8f9bb5;

        font-size: 12px;

        line-height: 1.4;
    }

    .agent-tool-label {
        margin-top: 20px;

        color: #69758f;

        font-size: 9px;

        font-weight: 700;

        letter-spacing: 1.5px;
    }

    .agent-tool {
        margin-top: 4px;

        color: #aab4c9;

        font-size: 11px;

        line-height: 1.4;
    }


    /* =========================
       WORKING CARD
       ========================= */

    .working-card {
        margin-top: 25px;

        padding: 20px 22px;

        background:
            linear-gradient(
                135deg,
                rgba(35, 45, 85, 0.75),
                rgba(14, 20, 35, 0.85)
            );

        border: 1px solid rgba(120, 140, 255, 0.22);

        border-radius: 18px;
    }

    .working-label {
        color: #7f8cac;

        font-size: 10px;
        font-weight: 700;

        letter-spacing: 1.8px;
    }

    .working-agent {
        margin-top: 7px;

        color: #ffffff;

        font-size: 20px;
        font-weight: 700;
    }

    .working-description {
        margin-top: 5px;

        color: #8995ae;

        font-size: 12px;
    }


    /* =========================
       METRICS
       ========================= */

    .metric-card {
        padding: 20px;

        background: rgba(15, 21, 35, 0.7);

        border: 1px solid rgba(120, 135, 170, 0.13);

        border-radius: 16px;

        text-align: center;
    }

    .metric-number {
        color: #f5f7ff;

        font-size: 26px;
        font-weight: 800;
    }

    .metric-label {
        margin-top: 5px;

        color: #737f99;

        font-size: 10px;

        letter-spacing: 1px;
    }


    /* =========================
       REPORT
       ========================= */

    .report-card {
        padding: 30px;

        background: rgba(14, 20, 34, 0.85);

        border: 1px solid rgba(130, 145, 180, 0.16);

        border-radius: 20px;

        line-height: 1.8;
    }


    /* =========================
       BUTTON
       ========================= */

    .stButton > button {
        width: 100%;

        min-height: 48px;

        border: none;

        border-radius: 12px;

        background:
            linear-gradient(
                135deg,
                #6674ff,
                #4d9cff
            );

        color: white;

        font-size: 14px;

        font-weight: 700;

        box-shadow:
            0 10px 25px rgba(80, 100, 255, 0.20);

        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 14px 32px rgba(80, 100, 255, 0.30);
    }


    /* =========================
       TEXT AREA
       ========================= */

    textarea {
        background: #0d1321 !important;

        color: #f5f7ff !important;

        border: 1px solid rgba(130, 145, 180, 0.18) !important;

        border-radius: 14px !important;
    }


    /* =========================
       DOWNLOAD BUTTON
       ========================= */

    .stDownloadButton > button {
        width: 100%;

        border-radius: 12px;

        background: #111a2c;

        color: #dce3f5;

        border: 1px solid rgba(130, 145, 180, 0.20);
    }


    /* =========================
       FOOTER
       ========================= */

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

        <div class="hero-badge">
            MULTI-AGENT RESEARCH LAB
        </div>

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
    placeholder=(
        "Example: The impact of artificial intelligence "
        "on modern education"
    ),
    height=120,
    label_visibility="collapsed",
)


start_research = st.button(
    "🚀 Start Research",
    use_container_width=True,
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
    {
        "icon": "🔎",
        "name": "Research Scout",
        "role": "Background Intelligence",
        "tool": "Wikipedia Search",
    },
    {
        "icon": "🎓",
        "name": "Academic Researcher",
        "role": "Scholarly Intelligence",
        "tool": "OpenAlex Search",
    },
    {
        "icon": "🔍",
        "name": "Evidence Reviewer",
        "role": "Evidence Verification",
        "tool": "Crossref Search",
    },
    {
        "icon": "✍️",
        "name": "Research Writer",
        "role": "Research Synthesis",
        "tool": "Citation Audit",
    },
]


cols = st.columns(4)

for col, agent in zip(cols, agents):

    with col:

        st.markdown(
            f"""
            <div class="agent-card">

                <div class="agent-icon">
                    {agent["icon"]}
                </div>

                <div class="agent-name">
                    {agent["name"]}
                </div>

                <div class="agent-role">
                    {agent["role"]}
                </div>

                <div class="agent-tool-label">
                    TOOL
                </div>

                <div class="agent-tool">
                    {agent["tool"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# RESEARCH EXECUTION
# ============================================================

if start_research:

    if not topic.strip():

        st.warning(
            "Please enter a research topic before starting."
        )

    else:

        st.markdown(
            """
            <div class="working-card">

                <div class="working-label">
                    RESEARCH STATUS
                </div>

                <div class="working-agent">
                    🤖 Research team is working...
                </div>

                <div class="working-description">
                    Your topic is being processed by the
                    multi-agent research pipeline.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        progress = st.progress(0)

        status = st.status(
            "🔬 Research pipeline is starting...",
            expanded=True,
        )

        try:

            status.write(
                "🔎 Research Scout is gathering background information..."
            )

            progress.progress(15)

            time.sleep(0.5)

            status.write(
                "🎓 Academic Researcher is finding scholarly sources..."
            )

            progress.progress(35)

            time.sleep(0.5)

            status.write(
                "🔍 Evidence Reviewer is checking research evidence..."
            )

            progress.progress(60)

            time.sleep(0.5)

            status.write(
                "✍️ Research Writer is synthesizing the final report..."
            )

            progress.progress(80)

            crew = create_crew()

            result = crew.kickoff(
                inputs={
                    "topic": topic.strip()
                }
            )

            progress.progress(100)

            status.update(
                label="✅ Research completed successfully",
                state="complete",
                expanded=False,
            )

            # Store result
            st.session_state["research_result"] = str(result)
            st.session_state["research_topic"] = topic.strip()

        except Exception as e:

            status.update(
                label="❌ Research failed",
                state="error",
                expanded=True,
            )

            st.error(
                f"Research failed: {str(e)}"
            )


# ============================================================
# RESULTS
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

    result = st.session_state["research_result"]

    st.markdown(
        '<div class="report-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        result
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    st.write("")

    st.download_button(
        label="⬇️ Download Research Report",
        data=result,
        file_name="research_report.txt",
        mime="text/plain",
        use_container_width=True,
    )


# ============================================================
# METRICS
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


metric_cols = st.columns(4)

metrics = [
    ("04", "AI AGENTS"),
    ("04", "RESEARCH TOOLS"),
    ("01", "RESEARCH TOPIC"),
    (
        "✓" if "research_result" in st.session_state else "—",
        "STATUS",
    ),
]


for col, (number, label) in zip(metric_cols, metrics):

    with col:

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
        Built with Streamlit · CrewAI · Groq · Specialized Research Tools
    </div>
    """,
    unsafe_allow_html=True,
)
