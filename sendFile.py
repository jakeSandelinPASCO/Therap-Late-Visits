from tkinter import filedialog
from tkinter.filedialog import askdirectory
import pandas as pd
import requests


#proc_path = filedialog.askopenfilename(title = "Select the Therap Basic ISP File")
df = pd.read_excel(r'C:\Users\JakeSa\Downloads\ISP_Data_Basic_Report (20230120134pm) v2.xlsx')

json_data = df.to_json()
#thePath = "C:/Users/JakeSa/Downloads/ISP_Data_Basic_Report (20230120134pm) v2.xlsx"
thePath = "C:\\Users\\JakeSa\Downloads\\ISP_Data_Basic_Report (20230120134pm) v2.xlsx"
#response = requests.get("http://127.0.0.1:3000/ISPUpload/" + thePath) #Use this for testing w/o Docker
response = requests.get("http://localhost:80/ISPUpload/" + thePath) #Use this for testing w/ Docker
#response = requests.post('http://localhost:80/ISPUpload', json=json_data)
#response = requests.post('http://127.0.0.1:3000/ISPUpload/:' + thePath)


#http://127.0.0.1:3000/
print(response)
