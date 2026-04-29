import os
import pandas as pd

base_folder = "data/new_dataset"

df_list = []

for file in os.listdir(base_folder):
    print("Checking:", file)

    if file.endswith(".csv"):
        file_path = os.path.join(base_folder, file)
        print("Reading:", file_path)

        df = pd.read_csv(file_path)

        # 🔥 Extract label from filename
        if "Benign" in file:
            label = "Benign"
        elif "DDoS" in file:
            label = "DDoS"
        elif "DoS" in file:
            label = "DoS"
        elif "Recon" in file:
            label = "Recon"
        else:
            label = "Attack"

        df['label'] = label
        df_list.append(df)

print("Total files loaded:", len(df_list))

combined = pd.concat(df_list, ignore_index=True)
combined.to_csv("data/combined_dataset.csv", index=False)

print("Combined dataset saved successfully!")