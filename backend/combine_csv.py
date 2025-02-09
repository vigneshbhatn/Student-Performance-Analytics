import pandas as pd
import os

# Define the correct path to the 'data' folder
data_folder = r"C:\Users\Vignesh\Documents\GitHub\Student-Performance-Analytics\data"  # Move one directory up and into 'data'
csv_files = ["SEE3rd22.csv", "SEE4th22.csv", "SEE5th21.csv"]

dataframes = []

for file in csv_files:
    file_path = os.path.join(data_folder, file)  # Construct full path
    df = pd.read_csv(file_path)  # Read CSV file
    df["File_Name"] = file  # Track source file
    dataframes.append(df)

df_combined = pd.concat(dataframes, ignore_index=True)
print("CSV files loaded successfully!")
df_combined.to_csv("data/combined_output.csv", index=False)
