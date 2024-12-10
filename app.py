import streamlit as st
import base64

def get_image_base64(path):
    """
    Convert image to base64 for embedding
    (Note: Replace with actual image path when deploying)
    """
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except:
        return ""

def local_css(file_name):
    """
    Load local CSS for custom styling
    """
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def argus_landing_page():
    # Page Configuration
    st.set_page_config(
        page_title="ARGUS | AI Governance",
        page_icon="🛡️",
        layout="wide"
    )

    # Custom CSS
    st.markdown("""
    <style>
    .main-title {
        font-size: 4em;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #34495e;
        text-align: center;
        margin-bottom: 40px;
    }
    .contact-section {
        background-color: #f4f6f7;
        padding: 20px;
        border-radius: 10px;
        margin-top: 40px;
    }
    .contact-title {
        font-size: 1.8em;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main Title
    st.markdown('<div class="main-title">ARGUS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI REGULATORY AND GOVERNANCE FOR UNBIASED AND SAFE LLM SYSTEMS</div>', unsafe_allow_html=True)

    # Spacer
    st.markdown("<br>", unsafe_allow_html=True)

    # Presentation Section
    st.header("Our Approach")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Bias Detection", "99.5%")
        st.write("Advanced algorithms to identify and mitigate AI bias")
    
    with col2:
        st.metric("Compliance", "ISO 27001")
        st.write("Rigorous governance frameworks and standards")
    
    with col3:
        st.metric("Safety Scoring", "Real-time")
        st.write("Continuous monitoring of LLM ethical performance")

    # Presentation Details
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mock Presentation Embedding (you'd replace this with actual presentation link)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

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

# Run the landing page
if __name__ == "__main__":
    argus_landing_page()
