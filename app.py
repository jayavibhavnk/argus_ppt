import streamlit as st

def argus_landing_page():
    # Page Configuration
    st.set_page_config(
        page_title="ARGUS | AI Governance",
        page_icon="🛡️",
        layout="wide"
    )

    # Custom CSS
    local_css("style.css")

    # Main Title
    st.markdown('<div class="main-title">ARGUS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI REGULATORY AND GOVERNANCE FOR UNBIASED AND SAFE LLM SYSTEMS</div>', unsafe_allow_html=True)

    # Introduction
    st.header("Introduction")
    st.write("ARGUS is an Agentic Pipeline designed to enhance the safety and reliability of AI-generated content. It integrates advanced models to address critical challenges like prompt safety, bias, and hallucinations.")

    # Methodology
    st.header("Methodology")
    st.write("The ARGUS pipeline ensures safe, unbiased, and reliable AI-generated content through key components:")
    st.markdown("- **Agent Controller**: Dynamically refines pipeline to ensure safe outputs")
    st.markdown("- **LLM Judge**: Detects and mitigates bias and hallucinations, regenerating outputs when necessary")
    st.markdown("- **Prompt Injection Detection**: Screens inputs using a DistilBERT classifier to ensure safety")
    st.markdown("- **Feedback Loop**: Iteratively improves prompts and outputs, enhancing adaptability")

    # Results
    st.header("Results")
    st.markdown("**Prompt Injection Detection:**")
    st.write("Achieved 97% accuracy on the test set.")
    st.markdown("**Bias Evaluation:**")
    st.write("Reduced bias by 37% compared to the base model.")
    st.markdown("**Hallucination Evaluation:**")
    st.write("52% reduction in hallucinations compared to the base model.")
    st.markdown("**RAG Evaluation:**")
    st.write("Showed improvements across different metrics.")

    # Contact Section
    st.markdown('<div class="contact-section">', unsafe_allow_html=True)
    st.markdown('<div class="contact-title">Contact Our Team</div>', unsafe_allow_html=True)

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

# Run the landing page
if __name__ == "__main__":
    argus_landing_page()
