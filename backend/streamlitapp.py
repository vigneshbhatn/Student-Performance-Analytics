import streamlit as st
import pandas as pd
import os
import logging
from data_loader import process_csv_data  # Your existing data loading logic

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit UI
st.title("📂 CSV File Uploader")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        # Save the file temporarily
        file_path = os.path.join("uploads", uploaded_file.name)
        os.makedirs("uploads", exist_ok=True)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

        # Process the uploaded CSV file
        result = process_csv_data(file_path)

        # Display processing results (modify based on what your function returns)
        st.write("### 📊 Processing Results")
        st.json(result)

        # Remove the temporary file
        os.remove(file_path)

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        st.error(f"❌ Error: {str(e)}")
