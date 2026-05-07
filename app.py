import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Admin Access Methods | IT Repair",
    page_icon="🛠️",
    layout="wide"
)

# ---------- CUSTOM CSS FOR READABILITY AND COLOR ----------
st.markdown("""
<style>
    /* Main app background gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f3460 0%, #1a1a2e 100%);
        border-right: 2px solid #e94560;
    }
    /* Sidebar text color */
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label {
        color: #ffffff !important;
    }
    /* Buttons */
    .stButton button {
        background-color: #e94560 !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        transition: 0.2s;
    }
    .stButton button:hover {
        background-color: #ff6b6b !important;
        transform: scale(1.02);
    }
    /* Login card */
    .login-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    /* Success and info text */
    .stAlert {
        background-color: rgba(0,0,0,0.7) !important;
        color: white !important;
    }
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #0f3460 !important;
        color: white !important;
        border-radius: 10px;
    }
    .streamlit-expanderContent {
        background-color: rgba(15,52,96,0.5) !important;
        border-radius: 0 0 10px 10px;
    }
    /* Title and headers */
    h1, h2, h3 {
        color: #ffd966 !important;
    }
    p, li {
        color: #ffffff !important;
    }
    /* Code blocks */
    code {
        background-color: #1e1e2e !important;
        color: #ffaa66 !important;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR SPINNING GLOBE LOGO ----------
st.sidebar.markdown("""
<style>
.spin-globe {
    font-size: 80px;
    animation: spin 4s linear infinite;
    display: inline-block;
    text-align: center;
}
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
</style>
<div style="text-align: center;">
    <div class="spin-globe">🌍</div>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("## **GlobalInternet.py**")
st.sidebar.markdown("### Authorized IT Repair Tools")
st.sidebar.markdown("---")
st.sidebar.markdown("**Built by Gesner Deslandes** – Technology Coordinator")
st.sidebar.markdown("---")
st.sidebar.markdown("📞 **Phone:** (509)-47385663")
st.sidebar.markdown("✉️ **Email:** deslandes78@gmail.com")
st.sidebar.markdown("---")
st.sidebar.markdown("**🌐 Website:**")
st.sidebar.markdown("[https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
st.sidebar.markdown("---")

# ---------- PRICING SECTION (Competitive for IP software sale) ----------
st.sidebar.markdown("### 💰 Software Pricing (One‑time License)")
st.sidebar.markdown("""
| Package | Price (USD) |
|---------|-------------|
| **Single‑User License** | $99 |
| **Campus / School License** | $499 |
| **Enterprise / Global License** | $1,999 |
| **Source Code + Resell Rights** | $4,999 |
""")
st.sidebar.info("✅ Includes full educational content, updates for 1 year, and email support.")
st.sidebar.markdown("---")
st.sidebar.caption("© GlobalInternet.py – Secure, alive, and ready for IT pros.")

# ---------- LOGIN/LOGOUT STATE ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------- LOGOUT BUTTON (if logged in) ----------
def logout():
    st.session_state.authenticated = False
    st.rerun()

# ---------- LOGIN PAGE ----------
def show_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>🔧 Admin Access Methods</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Enter the secure password to access the IT repair guide.</p>", unsafe_allow_html=True)
        password = st.text_input("Password", type="password")
        if st.button("Login", use_container_width=True):
            if password == "20082010":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password. Access denied.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- MAIN EDUCATIONAL CONTENT ----------
def show_educational_content():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h1>🔧 Windows Administrator Access Methods</h1>", unsafe_allow_html=True)
        st.markdown("### For authorized IT repair – preserve all your files")
        st.info("💡 Both methods **do not delete or damage your documents**. Your files remain safe.")
    
    with col2:
        if st.button("🔓 Logout", use_container_width=True):
            logout()
    
    # Method 1
    method1_text = [
        "**When to use:** You have physical access to the laptop and it boots normally, but you don't know the admin password.",
        "",
        "**What this does:** Enables the hidden built‑in Administrator account.",
        "",
        "### Step‑by‑step:",
        "1. **Restart** the laptop.",
        "2. As soon as the Dell logo appears, repeatedly press **F8** until the **Advanced Boot Options** menu appears.",
        "   - *Alternative (Windows 10/11):* Hold **Shift** while clicking Restart → Troubleshoot → Advanced Options → Startup Settings → Restart → press **6** for Safe Mode with Command Prompt.",
        "3. Select **Safe Mode with Command Prompt** and press Enter.",
        "4. A Command Prompt window will open **as SYSTEM** (highest privilege).",
        "5. Type the following command and press Enter:",
        "   ```",
        "   net user administrator /active:yes",
        "   ```",
        "6. (Optional) Set a password for the administrator account:",
        "   ```",
        "   net user administrator *",
        "   ```",
        "7. **Restart** the laptop normally.",
        "8. Log in using the **Administrator** account.",
        "",
        "✅ **Result:** You now have full admin access. Your personal files remain untouched.",
        "",
        "⚠️ **Note:** If the built‑in admin account is disabled by Group Policy, this method may not work. Use Method 2 instead."
    ]
    
    with st.expander("📌 Method 1 – Safe Mode with Command Prompt"):
        st.markdown("\n".join(method1_text))
    
    # Method 2
    method2_text = [
        "**When to use:** Method 1 fails, or you have a Windows USB/DVD available.",
        "",
        "**What this does:** Replaces the Ease of Access tool with a Command Prompt to enable admin.",
        "",
        "### Prerequisites:",
        "- A **Windows installation USB** (any version matching the installed OS)",
        "- Physical access to the laptop",
        "",
        "### Step‑by‑step:",
        "1. **Insert the Windows USB** and restart the laptop.",
        "2. Boot from the USB (usually press **F12** at Dell logo, select USB drive).",
        "3. At the language selection screen, press **Shift + F10** – a Command Prompt will open.",
        "4. Find your Windows drive letter (usually `C:` or `D:`). Type:",
        "   ```",
        "   dir C:\\\\",
        "   ```",
        "   If you see folders like `Windows`, `Users`, `Program Files`, it's the correct drive.",
        "5. **Back up the original Utilman.exe** (Ease of Access tool):",
        "   ```",
        "   move C:\\\\Windows\\\\System32\\\\utilman.exe C:\\\\Windows\\\\System32\\\\utilman.exe.bak",
        "   ```",
        "6. **Replace it with cmd.exe**:",
        "   ```",
        "   copy C:\\\\Windows\\\\System32\\\\cmd.exe C:\\\\Windows\\\\System32\\\\utilman.exe",
        "   ```",
        "7. **Restart** the laptop normally (remove the USB).",
        "8. On the login screen, click the **Ease of Access** icon (bottom‑right, looks like a clock with a person).",
        "   - A Command Prompt will open with **SYSTEM privileges**.",
        "9. Type the following to enable the admin account:",
        "   ```",
        "   net user administrator /active:yes",
        "   ```",
        "10. (Optional) Set a password:",
        "    ```",
        "    net user administrator *",
        "    ```",
        "11. Close the Command Prompt and log in as **Administrator**.",
        "",
        "### 🔁 **To restore normal behaviour (recommended after repair):**",
        "1. Repeat steps 1–4 (boot from USB, open Command Prompt).",
        "2. Restore Utilman:",
        "   ```",
        "   move C:\\\\Windows\\\\System32\\\\utilman.exe.bak C:\\\\Windows\\\\System32\\\\utilman.exe",
        "   ```",
        "3. Restart normally.",
        "",
        "✅ **Result:** You gain admin access, and after restoration, the login screen behaves normally again.",
        "",
        "⚠️ **Important:** If BitLocker is enabled, you will need the recovery key before using this method."
    ]
    
    with st.expander("📌 Method 2 – Windows Installation Media (Utilman Trick)"):
        st.markdown("\n".join(method2_text))
    
    # Reminder
    st.markdown("---")
    st.subheader("💾 Before you start – save your work!")
    st.markdown("""
    Both methods require a reboot. Your open documents will be closed.  
    ➡️ **Save all your files now** (Ctrl+S) and close any important applications.  
    Your documents will **not** be deleted – only the reboot is needed.
    """)
    
    st.success("🔒 Once you regain admin access, consider setting a strong password and documenting it for future repairs.")
    st.caption("© GlobalInternet.py – Authorized IT repair educational tools")

# ---------- ROUTING ----------
if not st.session_state.authenticated:
    show_login()
else:
    show_educational_content()
