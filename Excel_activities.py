import os

# requirements.txt
# openpyxl==3.0.10
import pandas as pd
import openpyxl

print("openpyxl is installed successfully.")

folder_path = r"C:\Users\acer\Desktop\New folder"
# file list
file_list = os.listdir(folder_path)
cly = [
    "class1",
    "class1",
    "class1",
    "class1",
    "class1",
    "class1",
    "class1",
    "class1",
]
df = pd.DataFrame({"Filenames": file_list, "Type": cly})
df.to_excel("file_list.xlsx", index=False)
