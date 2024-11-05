import requests
import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import threading

# Request details
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

# Helper functions
def format_timestamp(timestamp):
    dt_obj = datetime.utcfromtimestamp(timestamp / 1000)
    return dt_obj.strftime('%d %b, %Y %H:%M:%S %p')

def choose_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Locate the CSV file.",
        filetypes=[("CSV Files", ".csv")]
    )
    if file_path:
        file_label.config(text=f"Selected: {file_path}")
    else:
        file_label.config(text="No file selected")

def add_to_table(plate_no,result):
    # Get the output
    plate = plate_no
    issue_date = result.get('Issue Date')
    start_date = result.get('Start Date')
    end_date = result.get('End Date')
    error = result.get('Error')
    # inserting the values into the table
    tree.insert("", "end", values=(plate,issue_date,start_date,end_date,error))
    
def check_registration(plate_number):
    data = {
        "paramType": 2,
        "searchParam": plate_number
    }
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

def process_file():
    results = []
    try:
        with open(file_path, mode='r', newline='') as file:
            messagebox.showinfo("Processing","You can grab some coffee as you wait.\nPlease press okay to start processing")
            reader = csv.DictReader(file)
            for row in reader:
                plate_number = row['Reg No']
                result = check_registration(plate_number)
                results.append(result)
                add_to_table(plate_number,result)
                print(f"Plate: {plate_number}, Issue Date: {result.get('Issue Date')}, Start Date: {result.get('Start Date')}, End Date: {result.get('End Date')}")
    except:
        messagebox.showerror('Error','No file has been selected')
        return
    # Save the results to a new CSV file
    output_file = 'registration_results_filtered.csv'
    try:    
        with open(output_file, mode='w', newline='') as file:
            fieldnames = ['Plate', 'Issue Date', 'Start Date', 'End Date', 'Error']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
    except:
            messagebox.showerror("Error",f"It seems that {output_file} is opened by another app!\nDue to that failed to save the data Please close the program then try again :)")


    messagebox.showinfo("Success", f"Results saved to {output_file}")

    

# Thread function for non-blocking processing
try:
    def process_file_thread():
        # Run the process_file function in a separate thread
        threading.Thread(target=process_file).start()
except:
    messagebox.showerror('Error','No file has been selected!')

# UI Setup
root = tk.Tk()
root.title("Car Insurance ID Checker")
root.geometry("800x500")
root.resizable(False,False)
root.config(bg="#FFFFFF")  


style = ttk.Style()
# Title label
title_label = ttk.Label(root, text="Car Insurance ID Checker", font=("Segoe UI", 16, "bold"),background="#FFFFFF")
title_label.pack(pady=10)

# File selection
choose_file_button = ttk.Button(root, text="Choose CSV File", command=choose_file, style="TButton")
choose_file_button.pack(pady=10)

# Display selected file path
file_label = ttk.Label(root, text="No file selected", wraplength=450, font=("Segoe UI", 10), foreground="#555")
file_label.pack(pady=5)

heading_label = ttk.Label(root, text="See Real-time-results")

# creating the Frame to hold the tree and scrollbar
table_frame = ttk.Frame(root)
table_frame.pack(pady=20,fill="both", expand=True)

tree = ttk.Treeview(table_frame)

# Define columns
tree["columns"] = ("Plate", "Issue Date", "Start Date", "End Date", "Error")

# Format columns
tree.column("#0", width=0, stretch=tk.NO)  # Hide tree structure column
tree.column("Plate", anchor=tk.W, width=80)
tree.column("Issue Date", anchor=tk.CENTER, width=150)
tree.column("Start Date", anchor=tk.CENTER, width=150)
tree.column("End Date", anchor=tk.CENTER, width=150)
tree.column("Error", anchor=tk.CENTER, width=180)

# Create column headings
tree.heading("Plate",text="Plate", anchor=tk.CENTER)
tree.heading("Issue Date",text="Issue date", anchor=tk.CENTER)
tree.heading("Start Date",text="Start date", anchor=tk.CENTER)
tree.heading("End Date",text="End date", anchor=tk.CENTER)
tree.heading("Error",text="Error", anchor=tk.CENTER)


# Create Vertical Scrollbar
vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

# Pack the Scrollbar and Treeview
vsb.pack (side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)

# Button to process the file
process_button = ttk.Button(root, text="Process File", command=process_file_thread, style="TButton")
process_button.pack(pady=20,side="right",padx=20)

# Add some padding between elements
root.grid_columnconfigure(0, weight=1)
try:
    root.iconbitmap('logo.ico')
except:
    print("Icon not found!")
# Main loop
root.mainloop()
