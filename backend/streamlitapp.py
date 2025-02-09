# streamlit_app.py
import streamlit as st
import pandas as pd
import requests
import io

def main():
    st.title("Student Performance Data Upload")
    
    # File upload widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Show preview of the data
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the data:")
        st.dataframe(df.head())
        
        # Count of records
        st.write(f"Total number of records: {len(df)}")
        
        # Upload button
        if st.button("Upload and Process Data"):
            # Reset file pointer
            uploaded_file.seek(0)
            
            # Create files dict for requests
            files = {
                'file': ('data.csv', uploaded_file, 'text/csv')
            }
            
            try:
                # Send to Flask backend
                response = requests.post('http://localhost:5000/upload', files=files)
                
                if response.status_code == 200:
                    st.success("Data processed successfully!")
                    result = response.json()
                    st.write("Processing details:", result['details'])
                else:
                    st.error(f"Error: {response.json()['error']}")
                    
            except Exception as e:
                st.error(f"Error connecting to server: {str(e)}")

if __name__ == "__main__":
    main()