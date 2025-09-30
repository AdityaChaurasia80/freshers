import streamlit as st
import os




import streamlit as st
import os

# Title of the app
st.title("We look forward to seeing you at the FRESHERS PARTY! on 4th October")

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
