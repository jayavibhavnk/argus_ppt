import streamlit as st
import base64
import os

def get_image_base64(path):
    """
    Convert image to base64 for embedding
    """
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return ""

def local_css(file_name):
    """
    Load local CSS for custom styling
    """
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def display_pdf(pdf_path):
    """
    Display PDF using base64 encoding
    """
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_base64 = base64.b64encode(pdf_file.read()).decode("utf-8")
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="800" type="application/pdf"></iframe>',
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.error(f"Error displaying PDF: {e}")

def argus_landing_page():
    # Page Configuration
    st.set_page_config(
        page_title="ARGUS | AI Governance",
        page_icon="🛡️",
        layout="wide"
    )

    # Custom CSS
    local_css("styles.css")

    # Main Title
    st.markdown('<div class="main-title">ARGUS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI REGULATORY AND GOVERNANCE FOR UNBIASED AND SAFE LLM SYSTEMS</div>', unsafe_allow_html=True)

    # Spacer
    st.markdown("<br>", unsafe_allow_html=True)

    # About ARGUS
    st.header("About ARGUS")
    st.write("ARGUS is an Agentix Pipeline designed to enhance safety and reliability of AI generated content. It integrates advanced models to address critical challenges like prompt safety, bias and hallucinations.")

    # Methodology
    st.header("Methodology")
    st.write("Our ARGUS pipeline ensures safe, unbiased, and reliable AI-generated content through key components:")
    st.markdown("""
    - **Agent Controller**: Dynamically refines pipeline to ensure safe outputs.
    - **LLM Judge**: Detects and mitigates bias and hallucinations, regenerating outputs when necessary.
    - **Prompt Injection Detection**: Screens inputs using a DistilBERT classifier to ensure safety.
    - **Feedback Loop**: Iteratively improves prompts and outputs, enhancing adaptability.
    - **Models Used**:
        - LLM Judge: Nanoron 708
        - Agent Controller: Llama 3.1 BB
        - Prompt Injection: Custom DistilBERT
        - Text Generation: Llama 3.1 BB
        - Vector database: FAISS
    """, unsafe_allow_html=True)

    # Results
    st.header("Results")
    st.image("poster.png", use_column_width=True)

    # PDF Display
    st.header("Project Overview")
    display_pdf("31_Adventures_of_Dh2_and_JV.pdf")

    # Contact Section
    st.markdown('<div class="contact-section">', unsafe_allow_html=True)
    st.markdown('<div class="contact-title">Contact Our Team</div>', unsafe_allow_html=True)

    # Contact Details
    contact_info = {
        "Dr. Emily Rodriguez": {
            "LinkedIn": "https://www.linkedin.com/in/example1",
            "Email": "emily.rodriguez@argus.ai"
        },
        "Alex Chen": {
            "GitHub": "https://github.com/example2",
            "Twitter": "https://twitter.com/example2"
        }
    }
    for name, links in contact_info.items():
        st.markdown(f"**{name}**")
        for platform, link in links.items():
            st.markdown(f"- {platform}: [{link}]({link})")
        st.markdown("---")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    argus_landing_page()
