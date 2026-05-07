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

# ---------- METHOD 1 TEXT (using a list to avoid triple-quote issues) ----------
method1_lines = [
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

method2_lines = [
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

# ---------- DISPLAY METHODS ----------
with st.expander("📌 Method 1 – Safe Mode with Command Prompt"):
    st.markdown("\n".join(method1_lines))

with st.expander("📌 Method 2 – Windows Installation Media (Utilman Trick)"):
    st.markdown("\n".join(method2_lines))

# ---------- HELPFUL REMINDER ----------
st.markdown("---")
st.subheader("💾 Before you start – save your work!")
st.markdown("""
Both methods require a reboot. Your open documents will be closed.  
➡️ **Save all your files now** (Ctrl+S) and close any important applications.  
Your documents will **not** be deleted – only the reboot is needed.
""")

st.success("🔒 Once you regain admin access, consider setting a strong password and documenting it for future repairs.")
st.caption("© GlobalInternet.py – Authorized IT repair educational tools")
