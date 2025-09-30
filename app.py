import streamlit as st
import os

# Title of the app
st.title("Abhishek")

# --- IMPORTANT CHANGE: Use relative path AND the new parameter ---

# 1. Ensure 'FRESHERS PARTY.jpeg' is in the same folder as this Python script.
image_filename = "FRESHERS PARTY.jpeg"

import streamlit as st
import os

# Title of the app
st.title("ABhishek")

# --- IMPORTANT: Ensure the image file is in the same directory as this script ---
image_filename = "FRESHERS PARTY.jpeg"

if os.path.exists(image_filename):
    st.image(
        image_filename,
        caption="Hosted Image",
        # CORRECTED: Replaced use_column_width with use_container_width
        use_container_width=True
    )
else:
    st.error(f"Error: Image file '{image_filename}' not found. Make sure it is in the same directory as your app script.")