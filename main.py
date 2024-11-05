import requests
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

url = "https://tiramis.tira.go.tz/covernote/api/public/portal/verify"

headers = {
    "Host": "tiramis.tira.go.tz",
    "Sec-Ch-Ua": '"Not;A=Brand";v="24", "Chromium";v="128"',
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "https://tiramis.tira.go.tz",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://tiramis.tira.go.tz/",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def format_timestamp(timestamp):
    dt_obj = datetime.utcfromtimestamp(timestamp / 1000)
    return dt_obj.strftime('%d %b, %Y %H:%M:%S %p')

def choose_file():
    file_path = filedialog.askopenfilename(
        title="Locate the csv file.",
        filetypes=[("CSV Files", ".csv")]
        )
    if file_path:
        file_label.config(text=f"Selected: {file_path}")
    else:
        file_label.config(text="No file selected")
            
def check_registration(plate_number):
    data = {
        "paramType": 2,
        "searchParam": plate_number
    }

    # Send POST request
    response = requests.post(url, json=data, headers=headers, verify=False)

    if response.status_code == 200:
        result = response.json()
        if result['code'] == 1000 and result['data']:
            data = result['data'][0]
            issue_date = format_timestamp(data['issueDate'])
            start_date = format_timestamp(data['coverNoteStartDate'])
            end_date = format_timestamp(data['coverNoteEndDate'])

            return {
                'Plate': plate_number,
                'Issue Date': issue_date,
                'Start Date': start_date,
                'End Date': end_date
            }
        else:
            return {'Plate': plate_number, 'Error': 'No valid data found'}
    else:
        return {'Plate': plate_number, 'Error': f"Failed to check {plate_number}"}

data = pd.read_csv(f'{file_path}')
carplates = data['Reg No'].tolist()

results = []
for plate in carplates:
    result = check_registration(plate)
    results.append(result)
    print(f"Plate: {plate}, Issue Date: {result.get('Issue Date')}, Start Date: {result.get('Start Date')}, End Date: {result.get('End Date')}")

output = pd.DataFrame(results)
output.to_csv('registration_results_filtered.csv', index=False)

windwow = tk.Tk()
window.title("Car insurance id")
window.geometry("400x300")

choose_file_button = tk.button(rooe, text="Choose File", command=choose_file)
choose_file_button.pack(pady=20)

file_label = tk.Label(root,text="No file selected", wraplength=350)
file_path.pack()

window.mainloop()