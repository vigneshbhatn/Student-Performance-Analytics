import pandas as pd
import os

# Define the correct path to the 'data' folder
data_folder = r"C:\Users\Vignesh\Documents\GitHub\Student-Performance-Analytics\data"
output_folder = r"C:\Users\Vignesh\Documents\GitHub\Student-Performance-Analytics\processed data"  # Output folder

csv_files = ["SEE3rd22.csv"]

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

for file in csv_files:
    file_path = os.path.join(data_folder, file)  # Construct full path
    df = pd.read_csv(file_path)  # Read CSV file
    df["File_Name"] = file  # Track source file
    
    # Save with the same name as the input CSV in the output folder
    output_path = os.path.join(output_folder, file)
    df.to_csv(output_path, index=False)

    print(f"✅ Processed file saved as: {output_path}")
