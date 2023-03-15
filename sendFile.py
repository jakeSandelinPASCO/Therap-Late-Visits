from tkinter import filedialog
from tkinter.filedialog import askdirectory
import pandas as pd
import requests


proc_path = filedialog.askopenfilename(title = "Select the Therap Basic ISP File")
df = pd.read_excel(r'C:\Users\JakeSa\Downloads\ISP_Data_Basic_Report (20230120134pm).xlsx')

json_data = df.to_json()

response = requests.post('http://localhost:5000/ISPUpload', json=json_data)
print(response)