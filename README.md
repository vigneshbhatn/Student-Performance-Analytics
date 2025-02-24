# Student Performance Analytics Dashboard

project:
  name: Student Performance Analytics Dashboard
  description: >
    The Student Performance Analytics Dashboard is an interactive Power BI dashboard
    designed to analyze and visualize student performance data efficiently.
    It helps educators track individual and section-wide performance, identify trends,
    and make data-driven decisions.

features:
  - Section Overview: Insights on average marks, pass/fail rates, and subject performance.
  - Individual Performance: Student-specific analysis with SGPA trends, subject marks, and result breakdowns.
  - CIE vs. SEE Analysis: Visual comparison of Continuous Internal Evaluation (CIE) and Semester End Examination (SEE) scores.
  - Dynamic Slicers: Filter data by Batch, Semester, USN, and Subjects.
  - Real-time Data Updates: Data updates automatically when new records are added.

tech_stack:
  - Power BI: Interactive dashboards and data visualizations.
  - MySQL: Data storage and retrieval.
  - Python (Pandas, SQLAlchemy): Data preprocessing and automation.
  - Streamlit: UI for CSV uploads to MySQL.
  - GitHub: Version control and collaboration.

installation:
  steps:
    - Clone the repository:
      command: git clone https://github.com/your-username/student-performance-dashboard.git && cd student-performance-dashboard
    - Set up MySQL database:
      description: Import the provided SQL schema and ensure correct table relationships.
    - Run the Streamlit upload interface (if applicable):
      command: pip install -r requirements.txt && streamlit run app.py
    - Open the Power BI dashboard:
      description: Load the .pbix file in Power BI Desktop and update data source settings.

data_schema:
  tables:
    - name: student_details
      key_columns: [USN, Name, Batch]
      description: Stores student personal details.
    - name: student_semester
      key_columns: [USN, Semester, SGPA]
      description: Stores student SGPA per semester.
    - name: subject_marks
      key_columns: [USN, Subject_ID, CIE_Marks, SEE_Marks, Total_Marks]
      description: Stores marks per subject.
    - name: subjects
      key_columns: [Subject_ID, Subject_Name]
      description: Stores subject details.

issues:
  - Batch and Semester Slicer Issues: Ensure slicers are properly formatted and not cross-filtering unintentionally.
  - Incorrect Aggregation in Charts: Verify relationships in Power BI’s data model.

contributing:
  guidelines:
    - Fork the repository.
    - Create a new branch.
    - Commit changes and push.
    - Submit a Pull Request.

license:
  type: MIT
  description: This project is licensed under the MIT License.

authors:
  - name: Your Name
  - name: Team Member 1
  - name: Team Member 2
  - name: Team Member 3
