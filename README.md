# How to Create 400 Fake Users

I created a Python script to make fake user accounts to practice Identity Access Management (IAM) skills such as provisioning/deprovisioning, role-based access controls (RBAC), Single Sign-On (SSO), Multi-factor Authentication (MFA), and syncing Active Directory to Azure/Entra ID.

Here are the steps of how I was able to do it.

**Duration:** 15 minutes

Running Python scripts can seem daunting if you're new to programming, but with a step-by-step approach, you can get up and running smoothly. Below is a comprehensive guide to help you install Python, set up your environment, and execute the provided script to generate your CSV file with 400 users.

## 1. Install Python

### For Windows:

#### **Download Python:**

1. Visit the [official Python website](https://www.python.org/downloads/).
2. Click on the **"Download Python X.X.X"** button (where `X.X.X` is the latest version).

#### **Run the Installer:**

1. Locate the downloaded installer (`python-X.X.X.exe`) in your Downloads folder and double-click to run it.

#### **Customize Installation:**

1. **Important:** Check the box that says **"Add Python X.X to PATH"** at the bottom of the installer window. This allows you to run Python from the command line.
2. Click on **"Customize installation"** for more options or **"Install Now"** for default settings.

#### **Complete Installation:**

1. Wait for the installation to complete and click **"Close"**.

### For macOS:

#### **Check Pre-installed Python:**

macOS often comes with Python 2.x pre-installed. However, it's recommended to install the latest Python 3.x version.

#### **Download Python:**

1. Go to the [Python downloads page](https://www.python.org/downloads/) and download the **macOS installer** for the latest Python 3.x version.

#### **Run the Installer:**

1. Open the downloaded `.pkg` file and follow the on-screen instructions to install Python.

#### **Verify Installation:**

1. Open **Terminal** and type:
    ```bash
    python3 --version
    ```
    You should see the Python version you installed.

### For Linux:

#### **Check Python Installation:**

Most Linux distributions come with Python pre-installed. To check, open the terminal and type:
```bash
python3 --version
```
#### **Install Python (if not installed):**

Debian/Ubuntu:
```bash
sudo apt update
sudo apt install python3 python3-pip
```
Fedora:
```bash
sudo dnf install python3 python3-pip
```

Arch Linux:
```bash
sudo pacman -S python python-pip
```

## 2. Install Required Python Libraries
The script provided earlier uses two Python libraries: Faker and Pandas (optional but recommended for better CSV handling).

Open Command Prompt / Terminal:

Windows: Press ```Win``` + ```R```, type ```cmd```, and press ```Enter```.
macOS/Linux: Open the Terminal application.
Install Libraries Using pip:

Ensure pip is installed by checking its version:

```bash
pip --version
```
If pip is not recognized, you might need to use pip3 instead:

```bash
pip3 --version
```
Install Faker:

```bash
pip install Faker
```
Or, if using pip3:

```bash
pip3 install Faker
```
Install Pandas (Optional but Recommended):

```bash
pip install pandas
```
Or:

```bash
pip3 install pandas
```
Verify Installation:

You can verify that the libraries are installed by listing installed packages:
```bash
pip list
```

Look for Faker and pandas in the list.

## 3. Create the Python Script

Open a Text Editor or IDE:

Text Editors: Notepad (Windows), TextEdit (macOS), or any other plain text editor.
IDEs: Visual Studio Code, PyCharm, Sublime Text, etc. (Recommended for better experience)
Copy the Script:

Use the Python script provided in the previous message. Here's the script again for convenience:
```python
import csv
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Configuration
NUM_USERS = 400
DOMAIN = "yourdomain.com"
DEPARTMENTS = ['Marketing', 'IT', 'Finance', 'Human Resources', 'Sales', 'Research & Development', 'Customer Support']
JOB_TITLES = {
    'Marketing': ['Marketing Manager', 'Content Strategist', 'SEO Specialist', 'Social Media Manager'],
    'IT': ['Developer', 'System Administrator', 'Network Engineer', 'IT Support Specialist'],
    'Finance': ['Financial Analyst', 'Accountant', 'Controller', 'Finance Manager'],
    'Human Resources': ['HR Manager', 'Recruiter', 'HR Coordinator'],
    'Sales': ['Sales Manager', 'Account Executive', 'Sales Representative'],
    'Research & Development': ['R&D Engineer', 'Product Developer', 'Research Scientist'],
    'Customer Support': ['Customer Support Representative', 'Support Manager', 'Technical Support Specialist']
}
USAGE_LOCATIONS = ['US', 'GB', 'CA', 'AU', 'DE', 'FR', 'JP']

def generate_password():
    """Generates a secure password."""
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

def generate_users(num_users):
    users = []
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        display_name = f"{first_name} {last_name}"
        user_principal = f"{first_name.lower()}.{last_name.lower()}@{DOMAIN}"
        email = f"{user_principal}"
        department = random.choice(DEPARTMENTS)
        job_title = random.choice(JOB_TITLES[department])
        usage_location = random.choice(USAGE_LOCATIONS)
        password = generate_password()

        user = {
            'UserPrincipalName': user_principal,
            'DisplayName': display_name,
            'FirstName': first_name,
            'LastName': last_name,
            'Email': email,
            'JobTitle': job_title,
            'Department': department,
            'Password': password,
            'UsageLocation': usage_location
        }
        users.append(user)
    return users

def save_to_csv(users, filename='users.csv'):
    headers = ['UserPrincipalName', 'DisplayName', 'FirstName', 'LastName', 'Email', 'JobTitle', 'Department', 'Password', 'UsageLocation']
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for user in users:
            writer.writerow(user)
    print(f"CSV file '{filename}' with {len(users)} users has been created successfully.")

if __name__ == "__main__":
    users = generate_users(NUM_USERS)
    save_to_csv(users)
```
Customize the Script (Optional):

```NUM_USERS```: Keep at 400 or change to any amount you desire.

```DOMAIN```: Replace "yourdomain.com" with your actual domain if needed.
Departments and Job Titles: Adjust the DEPARTMENTS and JOB_TITLES lists to match your organization's structure.
Save the Script:

Filename: Save the file with a .py extension, e.g., generate_users.py.
Location: Choose a directory you can easily navigate to via the command line (e.g., Desktop, Documents).

## 4. Run the Python Script
Step-by-Step Instructions:
Open Command Prompt / Terminal:

Windows: Press ```Win```+ ```R```, type ```cmd```, and press ```Enter```.
macOS/Linux: Open the Terminal application.
Navigate to the Script Directory:

Use the cd (change directory) command to navigate to the folder where you saved ```generate_users.py```.

Example:

If you saved the script on your Desktop:
Windows:
```bash

cd Desktop
```
macOS/Linux:
```bash
cd ~/Desktop
```
Run the Script:

Execute the script using Python.

For Python 3.x:

```bash
python generate_users.py
```
Or, if python points to Python 2.x, use:

```bash
python3 generate_users.py
```
Expected Output:

```plaintext
CSV file 'users.csv' with 400 users has been created successfully.
```
Verify the CSV File:

After running the script, a file named ```users.csv``` should appear in the same directory.

Open the file using Microsoft Excel, Google Sheets, or any text editor to view the generated user data.

## **5. Troubleshooting Common Issues** 

#### **a. Python Command Not Found**
- Symptom: When you type ```python``` or ```python3```, you receive an error like ```'python' is not recognized as an internal or external command```.

- Solution:

  - Ensure Python is Installed: Follow the installation steps above.

  - Add Python to PATH:
    - Windows:
      - Re-run the Python installer and ensure the "Add Python to PATH" option is checked.
      - Alternatively, manually add Python to the system PATH:
        1. Right-click on This PC or My Computer and select Properties.
        2. Click on Advanced system settings.
        3. Click on Environment Variables.
        4. Under System variables, find and select the Path variable, then click Edit.
        5. Click New and add the path to your Python installation (e.g., ```C:\Python39\ and C:\Python39\Scripts\```).
        6. Click OK to save changes.

  - macOS/Linux:
    - Python is typically added to PATH automatically. If not, you can add it by editing your shell profile (e.g., ```.bash_profile```, ```.zshrc```).

#### **b. Module Not Found Error**
- Symptom: Errors like ```ModuleNotFoundError: No module named 'Faker'```.
- Solution:
  - Ensure Libraries Are Installed:
      - Run:
        ```bash
        pip install Faker
        pip install pandas
        ```
        Or, if using ```pip3```:
        ```bash
        pip3 install Faker
        pip3 install pandas
        ```
  - Check for Virtual Environments:

    - If you're using a virtual environment, ensure it's activated before installing packages and running the script.

#### c. Permission Denied Error

- Symptom: Errors related to file writing permissions.
- Solution:
    - Run Command Prompt/Terminal as Administrator:

- Windows: Right-click on Command Prompt and select ```Run``` as administrator.
- macOS/Linux: Use ```sudo``` if necessary, though for writing to your user directories, this typically isn't required.

Change Directory Permissions: Ensure you have write permissions to the directory where you're trying to create the CSV file.
#### d. Script Errors or Unexpected Behavior
- Solution:
    - Double-Check the Script: Ensure there are no syntax errors or typos.
    - Print Debug Statements: Add print statements in the script to debug and understand where it might be failing.
    - Refer to Error Messages: Python error messages are usually descriptive. Read them carefully to identify the issue.
## 6. Additional Tips
a. Using an Integrated Development Environment (IDE)
Recommended IDEs:

Visual Studio Code: Free, lightweight, and highly customizable.
PyCharm: Offers both free (Community) and paid (Professional) versions with powerful features.
Sublime Text: Fast and flexible with numerous plugins.
Benefits:

Syntax Highlighting: Makes code easier to read.
Integrated Terminal: Run scripts without switching windows.
Debugging Tools: Identify and fix issues efficiently.
b. Virtual Environments
Purpose: Isolate project dependencies to prevent conflicts between different projects.

### Creating a Virtual Environment:

````bash
python -m venv myenv
````
#### Activating the Virtual Environment:

##### Windows:
```bash
myenv\Scripts\activate
```
##### macOS/Linux:
```bash
source myenv/bin/activate
```
#### Installing Libraries Within Virtual Environment:

```bash
pip install Faker pandas
```
Deactivating the Virtual Environment:

````bash
deactivate
````

Installation:
````bash
pip install notebook
````
Running Jupyter Notebook:
````bash
jupyter notebook
````
## 7. Alternative Approach: Using Online Python Environments
If installing Python locally isn't an option, you can use online platforms to run your Python scripts.

a. Google Colab
Access Google Colab:

Go to Google Colab.
Create a New Notebook:

Click on "New Notebook".
Install Required Libraries:

In the first cell, install Faker:
````python
!pip install Faker
Run the cell by pressing Shift + Enter.
````
Copy and Paste the Script:

In a new cell, paste the Python script.
Modify the save_to_csv function to save the CSV file to Google Drive or download it directly.
Download the CSV:

Use the following code snippet to download the CSV:
````python
from google.colab import files
files.download('users.csv')
````
b. Repl.it
Visit Repl.it:

Go to Repl.it.
Create a New Python Repl:

Click on "Create", select Python, and name your project.
Install Libraries:

In the shell or terminal within Repl.it, run:
````bash
pip install Faker
````
Paste and Run the Script:

Add the Python script to the main file and run it.
Download the generated users.csv from the file explorer.

## 8. Final Verification
After successfully running the script, ensure that the generated users.csv file contains the expected data.

#### Open the CSV File:

Use Microsoft Excel, Google Sheets, or any text editor.
Verify Columns:

Ensure all the required headers are present:
````UserPrincipalName
DisplayName
FirstName
LastName
Email
JobTitle
Department
Password
UsageLocation
````
Check Data Integrity:

Review a few entries to ensure that the data looks realistic and follows the correct format.
Use in Your Application:

Now that your CSV is ready, you can use it to import users into Active Directory or Microsoft Entra ID as needed.

### Summary
Running a Python script involves several steps, but by following this guide, you can:

- Install Python on your operating system.
- Install necessary libraries using pip.
- Create and customize the Python script to generate your CSV file.
- Execute the script via the command line to produce the users.csv file.
- Verify and utilize the generated CSV as required.

Remember, practice makes perfect! Don't hesitate to experiment with the script to better understand how it works and to tailor it to your specific needs.

If you encounter any issues or have further questions, feel free to ask!

