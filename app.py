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
    - LLM Judge: Nemotron 70B
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

# Links
st.header("Links")
st.markdown("""
- [BEAD Dataset](https://huggingface.co/datasets/shainar/BEAD)
- [HaluEval Dataset](https://github.com/RUCAIBox/HaluEval)
- [RagBench Dataset](https://huggingface.co/datasets/rungalileo/ragbench)
""")

# Contact Us Section
st.header("Contact Us")
st.markdown("""
- **Jayavibhav Niranjan Kogundi**: [Email](mailto:jniranja@usc.edu), [Portfolio](https://jayavibhav.netlify.app/), [HuggingFace](https://huggingface.co/jayavibhav)
- **Dhruv Shetty**: [Email](mailto:ddshetty@usc.edu)
""")

st.markdown(
    """
    ## Other Projects Developed by Us:
    - [Small LLMs for SQL using COT](https://huggingface.co/jayavibhav/llama3.2_1b_sql)
    - [Llama 3.2 1B COT](https://huggingface.co/jayavibhav/llama3.2_1b_CoT)
    - [Llama 3.2 11B Vision - Finetuned for Geometry and Maths](https://huggingface.co/jayavibhav/llama3.2_11B_Vision_Maths_Geometry)
    - [Llama 3.2 1B Function Calling](https://huggingface.co/jayavibhav/Llama3.2_1B_Cot_LoRa)
    - [Graph Retrieval for RAG (Python Library)](https://pypi.org/project/MultimodalGraphRetrieval/)
    """
)

