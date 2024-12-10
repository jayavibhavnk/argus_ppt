import streamlit as st

# Page configuration
st.set_page_config(page_title="ARGUS - AI Regulatory and Governance", page_icon=":shield:", layout="wide")

# Main title and subtitle
st.title("ARGUS")
st.subheader("AI Regulatory and Governance for Unbiased and Safe LLM Systems")

# Introduction
st.markdown(
    """
    ARGUS is an Agentic Pipeline designed to enhance safety and reliability of AI-generated content. It integrates advanced models to address critical challenges like prompt safety, bias, and hallucinations.
    """
)

# Methodology Section
st.header("Methodology")
st.markdown(
    """
    Our ARGUS pipeline ensures safe, unbiased, and reliable AI-generated content through key components:

    - **Agent Controller**: Dynamically refines pipeline to ensure safe outputs.
    - **LLM Judge**: Detects and mitigates bias and hallucinations, regenerating outputs when necessary.
    - **Prompt Injection Detection**: Screens inputs using a DistilBERT classifier to ensure safety.
    - **Feedback Loop**: Iteratively improves prompts and outputs, enhancing adaptability.

    **Models used:**
    - LLM Judge: NomicAI GPT4ALL 70B
    - Agent Controller: Llama 3.1 8B
    - Prompt Injection: Custom DistilBERT
    - Text Generation: Llama 3.1 8B
    - Vector Database: FAISS
    """
)

# Results Section
st.header("Results")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Prompt Injection Detection")
    st.markdown("Accuracy: **97.7%**")

    st.subheader("Bias Reduction (Modified BEAD Dataset)")
    st.markdown("""
    - Llama 3.1 8B: **54%**
    - Llama 3.1 13B: **62.3%**
    - ARGUS (Llama 3.1 8B): **82.7%**
    """
)

with col2:
    st.subheader("Hallucination Reduction (HalEval Dataset)")
    st.markdown("Reduction: **52.0%**")

    st.subheader("RAG Evaluation (RAGBench)")
    st.markdown("""
    - Perturbations: **15.4% improvement**
    - Answer Accuracy: **19.1% improvement**
    - ARGUS Overall: **44.1% evaluation success**
    """
)

# Demo Links
st.header("Demo")
st.markdown("""
- [Demo 1: ARGUS Prompt Injection Detection](#)
- [Demo 2: ARGUS Bias Mitigation](#)
- [Demo 3: ARGUS RAG Evaluation](#)
""")

# Contact Us Section
st.header("Contact Us")
st.markdown("""
- **Jayavibhav Niranjan Kogundi**: [Email](mailto:jniranja@usc.edu), [LinkedIn](#)
- **Dhruv Shetty**: [Email](mailto:ddshetty@usc.edu)
""")
