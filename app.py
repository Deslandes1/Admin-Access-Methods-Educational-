import streamlit as st

st.set_page_config(
    page_title="Admin Access Methods | IT Repair",
    page_icon="🛠️",
    layout="wide"
)

# ---------- SIDEBAR WITH DISCLAIMER ----------
with st.sidebar:
    st.markdown("""
    <style>
    .spin-logo {
        font-size: 60px;
        animation: spin 4s linear infinite;
        display: inline-block;
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    </style>
    <div style="text-align: center;">
        <div class="spin-logo">🛠️</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("## **Admin Access Tools**")
    st.markdown("---")
    st.markdown("**Built by Gesner Deslandes** – Technology Coordinator")
    st.markdown("📞 (509)-47385663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("---")
    st.error("""
    ⚠️ **DISCLAIMER**  
    These methods are for **authorized repair and maintenance only** on devices you own or are responsible for.  
    Using them on others' devices without permission is illegal and unethical.  
    The author assumes no liability for misuse.
    """)

st.title("🔧 Windows Administrator Access Methods")
st.markdown("### For authorized IT repair – preserve all your files")

st.info("💡 Both methods **do not delete or damage your documents**. Your files remain safe.")

# ---------- METHOD 1 ----------
with st.expander("📌 Method 1 – Safe Mode with Command Prompt", expanded=False):
    st.markdown("""
    **When to use:** You have physical access to the laptop and it boots normally, but you don't know the admin password.
    
    **What this does:** Enables the hidden built‑in Administrator account.
    
    ### Step‑by‑step:
    1. **Restart** the laptop.
    2. As soon as the Dell logo appears, repeatedly press **F8** until the **Advanced Boot Options** menu appears.
       - *Alternative (Windows 10/11):* Hold **Shift** while clicking Restart → Troubleshoot → Advanced Options → Startup Settings → Restart → press **6** for Safe Mode with Command Prompt.
    3. Select **Safe Mode with Command Prompt** and press Enter.
    4. A Command Prompt window will open **as SYSTEM** (highest privilege).
    5. Type the following command and press Enter:
       ```cmd
       net user administrator /active:yes
