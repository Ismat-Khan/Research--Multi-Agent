import time
import streamlit as st

from crew import create_crew


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Research Lab | Multi-Agent AI",
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

    /* ---------- GLOBAL ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(91, 83, 255, 0.14),
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 20%,
                rgba(0, 194, 255, 0.10),
                transparent 25%
            ),
            #070a13;
        color: #f5f7ff;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* ---------- TEXT ---------- */

    .eyebrow {
        color: #8f9bb8;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 0.7rem;
    }

    .hero-title {
        font-size: clamp(2.6rem, 6vw, 5rem);
        line-height: 0.98;
        font-weight: 800;
        letter-spacing: -0.055em;
        margin: 0;
        color: #ffffff;
    }

    .hero-title span {
        background: linear-gradient(
            100deg,
            #ffffff 0%,
            #9ea7ff 45%,
            #63dcff 100%
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        color: #9aa6c2;
        font-size: 1.05rem;
        line-height: 1.7;
        max-width: 720px;
        margin-top: 1.25rem;
        margin-bottom: 2rem;
    }

    /* ---------- HERO BADGE ---------- */

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 7px 12px;
        border: 1px solid rgba(130, 143, 255, 0.25);
        border-radius: 999px;
        background: rgba(105, 91, 255, 0.08);
        color: #aeb6ff;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-bottom: 1rem;
    }

    .badge-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #65e6a4;
        box-shadow: 0 0 12px rgba(101, 230, 164, 0.8);
    }

    /* ---------- GLASS CARD ---------- */

    .glass-card {
        background: rgba(16, 21, 35, 0.72);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 22px;
        padding: 24px;
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.035);
    }

    /* ---------- SECTION ---------- */

    .section-label {
        color: #7f8aa7;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }

    .section-title {
        color: #f5f7ff;
        font-size: 1.35rem;
        font-weight: 750;
        letter-spacing: -0.02em;
        margin-bottom: 0.3rem;
    }

    .section-description {
        color: #7f8aa7;
        font-size: 0.88rem;
    }

    /* ---------- AGENT CARDS ---------- */

    .agent-card {
        min-height: 165px;
        padding: 20px;
        border-radius: 20px;
        background: rgba(15, 20, 33, 0.82);
        border: 1px solid rgba(255, 255, 255, 0.07);
        transition:
            transform 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease;
    }

    .agent-card:hover {
        transform: translateY(-3px);
        border-color: rgba(132, 143, 255, 0.25);
        box-shadow: 0 18px 45px rgba(0, 0, 0, 0.25);
    }

    .agent-card.active {
        border-color: rgba(99, 220, 255, 0.45);
        box-shadow:
            0 0 0 1px rgba(99, 220, 255, 0.08),
            0 20px 55px rgba(32, 139, 255, 0.12);
    }

    .agent-card.complete {
        border-color: rgba(101, 230, 164, 0.22);
    }

    .agent-icon {
        font-size: 1.7rem;
        margin-bottom: 12px;
    }

    .agent-name {
        color: #f4f6ff;
        font-size: 0.98rem;
        font-weight: 750;
        margin-bottom: 5px;
    }

    .agent-role {
        color: #78849f;
        font-size: 0.77rem;
        line-height: 1.5;
        min-height: 36px;
    }

    .agent-status {
        margin-top: 15px;
        font-size: 0.7rem;
        font-weight: 800;
        letter-spacing: 0.09em;
        text-transform: uppercase;
    }

    .status-working {
        color: #63dcff;
    }

    .status-complete {
        color: #65e6a4;
    }

    .status-waiting {
        color: #69758f;
    }

    .pulse {
        display: inline-block;
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #63dcff;
        margin-right: 6px;
        box-shadow: 0 0 0 0 rgba(99, 220, 255, 0.7);
        animation: pulse 1.6s infinite;
    }

    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(99, 220, 255, 0.7);
        }

        70% {
            box-shadow: 0 0 0 9px rgba(99, 220, 255, 0);
        }

        100% {
            box-shadow: 0 0 0 0 rgba(99, 220, 255, 0);
        }
    }

    .check {
        color: #65e6a4;
        margin-right: 6px;
    }

    /* ---------- WORKING PANEL ---------- */

    .working-panel {
        padding: 18px 20px;
        border-radius: 18px;
        background:
            linear-gradient(
                110deg,
                rgba(78, 68, 255, 0.13),
                rgba(41, 184, 255, 0.07)
            );
        border: 1px solid rgba(99, 220, 255, 0.18);
    }

    .working-label {
        color: #72809d;
        font-size: 0.68rem;
        font-weight: 800;
        letter-spacing: 0.13em;
        text-transform: uppercase;
    }

    .working-agent {
        color: #ffffff;
        font-size: 1.12rem;
        font-weight: 750;
        margin-top: 5px;
    }

    .working-message {
        color: #8e9ab5;
        font-size: 0.82rem;
        margin-top: 3px;
    }

    /* ---------- METRICS ---------- */

    .metric-card {
        text-align: center;
        padding: 18px 12px;
        border-radius: 18px;
        background: rgba(15, 20, 33, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .metric-number {
        color: #ffffff;
        font-size: 1.45rem;
        font-weight: 800;
    }

    .metric-label {
        color: #737f99;
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 4px;
    }

    /* ---------- REPORT ---------- */

    .report-header {
        padding: 24px;
        border-radius: 22px;
        background:
            linear-gradient(
                120deg,
                rgba(75, 65, 255, 0.16),
                rgba(32, 183, 255, 0.08)
            );
        border: 1px solid rgba(125, 135, 255, 0.18);
    }

    .report-kicker {
        color: #65e6a4;
        font-size: 0.7rem;
        font-weight: 800;
        letter-spacing: 0.13em;
        text-transform: uppercase;
    }

    .report-title {
        color: white;
        font-size: 1.55rem;
        font-weight: 800;
        margin-top: 6px;
    }

    /* ---------- SOURCE TAG ---------- */

    .source-tag {
        display: inline-block;
        padding: 6px 10px;
        margin: 3px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.07);
        color: #8995af;
        font-size: 0.7rem;
    }

    /* ---------- STREAMLIT INPUTS ---------- */

    div[data-testid="stTextInput"] input {
        background: rgba(13, 18, 30, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 15px;
        padding: 16px;
        min-height: 52px;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: rgba(99, 220, 255, 0.5);
        box-shadow: 0 0 0 1px rgba(99, 220, 255, 0.12);
    }

    div[data-testid="stButton"] button {
        border-radius: 14px;
        min-height: 50px;
        font-weight: 750;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: linear-gradient(
            100deg,
            #5147e8,
            #227bd8
        );
        color: white;
        transition: all 0.2s ease;
    }

    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(56, 96, 255, 0.22);
    }

    /* ---------- DIVIDER ---------- */

    .soft-divider {
        height: 1px;
        background: rgba(255, 255, 255, 0.06);
        margin: 30px 0;
    }

    /* ---------- MOBILE ---------- */

    @media (max-width: 768px) {

        .block-container {
            padding: 1.2rem;
        }

        .hero-title {
            font-size: 2.7rem;
        }

        .hero-description {
            font-size: 0.95rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "research_started" not in st.session_state:
    st.session_state.research_started = False

if "research_result" not in st.session_state:
    st.session_state.research_result = None

if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="hero-badge">
        <span class="badge-dot"></span>
        MULTI-AGENT RESEARCH SYSTEM
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-title">
        Research that goes<br>
        <span>deeper than search.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-description">
        Give your research question to a team of specialized AI agents.
        They investigate background knowledge, academic evidence,
        source verification, and final synthesis — all in one workflow.
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RESEARCH INPUT
# ============================================================

st.markdown(
    """
    <div class="glass-card">
        <div class="section-label">Research Brief</div>
        <div class="section-title">What should the research team investigate?</div>
        <div class="section-description">
            Enter a topic, question, technology, theory, or research problem.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

input_col, button_col = st.columns([5, 1], vertical_alignment="bottom")

with input_col:
    topic = st.text_input(
        "Research topic",
        value=st.session_state.research_topic,
        placeholder="Example: Impact of artificial intelligence on higher education",
        label_visibility="collapsed",
    )

with button_col:
    start = st.button(
        "✦  Start Research",
        use_container_width=True,
    )


# ============================================================
# AGENT INFORMATION
# ============================================================

st.write("")
st.markdown(
    """
    <div class="section-label">Your Research Team</div>
    <div class="section-title">Four specialists. One research workflow.</div>
    <div class="section-description">
        Each agent has a dedicated responsibility and research tool.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

agent_columns = st.columns(4)

agent_information = [
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

for column, agent in zip(agent_columns, agent_information):

    icon, name, role, tool = agent

    with column:

        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-icon">{icon}</div>
                <div class="agent-name">{name}</div>
                <div class="agent-role">{role}</div>

                <div style="
                    margin-top: 14px;
                    color: #69758f;
                    font-size: 0.68rem;
                ">
                    TOOL
                </div>

                <div style="
                    color: #a4aec5;
                    font-size: 0.72rem;
                    margin-top: 2px;
                ">
                    {tool}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# START RESEARCH
# ============================================================

if start:

    if not topic.strip():

        st.warning("Please enter a research topic first.")

    else:

        st.session_state.research_topic = topic.strip()
        st.session_state.research_started = True
        st.session_state.research_result = None

        st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

        # ----------------------------------------------------
        # LIVE RESEARCH HEADER
        # ----------------------------------------------------

        progress_placeholder = st.empty()

        progress_placeholder.markdown(
            """
            <div class="working-panel">
                <div class="working-label">Research Status</div>
                <div class="working-agent">
                    <span class="pulse"></span>
                    Research team is starting
                </div>
                <div class="working-message">
                    Preparing agents and research tools...
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        # ----------------------------------------------------
        # PIPELINE
        # ----------------------------------------------------

        pipeline_status = st.status(
            "🔬 Research pipeline",
            expanded=True,
        )

        try:

            pipeline_status.write(
                "🔎 Research Scout is preparing the research..."
            )

            progress_placeholder.markdown(
                """
                <div class="working-panel">
                    <div class="working-label">Working Now</div>
                    <div class="working-agent">
                        <span class="pulse"></span>
                        🔎 Research Scout
                    </div>
                    <div class="working-message">
                        Establishing background context and key concepts.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # ------------------------------------------------
            # CREATE CREW
            # ------------------------------------------------

            crew = create_crew()

            pipeline_status.write(
                "⚡ CrewAI team initialized."
            )

            pipeline_status.write(
                "🔎 Research Scout → Wikipedia research"
            )

            time.sleep(0.3)

            pipeline_status.write(
                "🎓 Academic Researcher → academic literature"
            )

            time.sleep(0.3)

            pipeline_status.write(
                "🔍 Evidence Reviewer → source verification"
            )

            time.sleep(0.3)

            pipeline_status.write(
                "✍️ Research Writer → final synthesis"
            )

            # ------------------------------------------------
            # RUN CREW
            # ------------------------------------------------

            progress_placeholder.markdown(
                """
                <div class="working-panel">
                    <div class="working-label">Working Now</div>
                    <div class="working-agent">
                        <span class="pulse"></span>
                        🤖 CrewAI Research Team
                    </div>
                    <div class="working-message">
                        Agents are executing the research workflow...
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            result = crew.kickoff(
                inputs={
                    "topic": topic.strip()
                }
            )

            st.session_state.research_result = result

            # ------------------------------------------------
            # COMPLETE
            # ------------------------------------------------

            pipeline_status.update(
                label="✓ Research completed",
                state="complete",
                expanded=False,
            )

            progress_placeholder.markdown(
                """
                <div class="working-panel">
                    <div class="working-label">Research Status</div>
                    <div class="working-agent">
                        ✓ Research complete
                    </div>
                    <div class="working-message">
                        All four agents completed their workflow.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        except Exception as error:

            pipeline_status.update(
                label="Research failed",
                state="error",
                expanded=True,
            )

            progress_placeholder.empty()

            st.error(
                f"Research could not be completed.\n\n{error}"
            )

            st.stop()


# ============================================================
# FINAL RESULT
# ============================================================

if st.session_state.research_result is not None:

    result = st.session_state.research_result

    st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="report-header">
            <div class="report-kicker">
                ✓ Research Complete
            </div>

            <div class="report-title">
                Your Research Report
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    metric_1, metric_2, metric_3, metric_4 = st.columns(4)

    with metric_1:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">04</div>
                <div class="metric-label">AI Agents</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_2:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">04</div>
                <div class="metric-label">Research Tools</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_3:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">01</div>
                <div class="metric-label">Research Topic</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with metric_4:
        st.markdown(
            """
            <div class="metric-card">
                <div class="metric-number">✓</div>
                <div class="metric-label">Completed</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # --------------------------------------------------------
    # TOPIC
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="section-label">Research Topic</div>

        <div style="
            font-size: 1.4rem;
            font-weight: 750;
            color: white;
            margin-bottom: 20px;
        ">
            {st.session_state.research_topic}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # REPORT
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-label">
            Final Analysis
        </div>
        """,
        unsafe_allow_html=True,
    )

    if hasattr(result, "raw"):
        report = result.raw
    else:
        report = str(result)

    st.markdown(report)

    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    st.write("")

    st.download_button(
        label="↓  Download Research Report",
        data=report,
        file_name="research_report.txt",
        mime="text/plain",
        use_container_width=True,
    )


# ============================================================
# FOOTER
# ============================================================

st.write("")
st.markdown(
    """
    <div style="
        text-align: center;
        color: #4f5a72;
        font-size: 0.72rem;
        padding-top: 30px;
    ">
        Powered by CrewAI · Groq GPT-OSS 120B · Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)
