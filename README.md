# Student Performance Analytics Dashboard

The Student Performance Analytics Dashboard is an interactive Power BI dashboard designed to analyze and visualize student performance data efficiently. It helps educators track individual and section-wide performance, identify trends, and make data-driven decisions.

## Features
- **Section Overview**: Insights on average marks, pass/fail rates, and subject performance.
- **Individual Performance**: Student-specific analysis with SGPA trends, subject marks, and result breakdowns.
- **CIE vs. SEE Analysis**: Visual comparison of Continuous Internal Evaluation (CIE) and Semester End Examination (SEE) scores.
- **Dynamic Slicers**: Filter data by Batch, Semester, USN, and Subjects.
- **Real-time Data Updates**: Data updates automatically when new records are added.

## Tech Stack
- **Power BI**: Interactive dashboards and data visualizations.
- **MySQL**: Data storage and retrieval.
- **Python (Pandas, SQLAlchemy)**: Data preprocessing and automation.
- **Streamlit**: UI for CSV uploads to MySQL.
- **GitHub**: Version control and collaboration.

## Installation
### Steps:
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/student-performance-dashboard.git && cd student-performance-dashboard
   ```
2. **Set up MySQL database:**
   - Import the provided SQL schema and ensure correct table relationships.
3. **Run the Streamlit upload interface (if applicable):**
   ```sh
   pip install -r requirements.txt && streamlit run app.py
   ```
4. **Open the Power BI dashboard:**
   - Load the `.pbix` file in Power BI Desktop and update data source settings.

## Data Schema
### Tables:
- **student_details**
  - **Key Columns**: `USN`, `Name`, `Batch`
  - **Description**: Stores student personal details.
- **student_semester**
  - **Key Columns**: `USN`, `Semester`, `SGPA`
  - **Description**: Stores student SGPA per semester.
- **subject_marks**
  - **Key Columns**: `USN`, `Subject_ID`, `CIE_Marks`, `SEE_Marks`, `Total_Marks`
  - **Description**: Stores marks per subject.
- **subjects**
  - **Key Columns**: `Subject_ID`, `Subject_Name`
  - **Description**: Stores subject details.
  - 
## License
This project is licensed under the **MIT License**.

