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
