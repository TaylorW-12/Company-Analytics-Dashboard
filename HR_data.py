import pandas as pd
import numpy as np
import random

# Define lists for random selections
states = ["Alabama", "Arizona", "Arkansas", "California", "Florida", "Georgia",
          "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
          "Massachusetts", "Michigan", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
           "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

departments = ["Finance", "Training", "Support", "Business Development", "Quality", "Engineering", "Marketing", "Sales", "Product Management", "Human Resources", "Legal"]

job_titles = [
    "Business Analyst I", "Business Analyst II", "Accountant I", "Accountant II", "Software Engineer I", "Software Engineer II", "HR Manager",
    "Marketing Specialist", "Sales Associate", "Quality Analyst", "Product Manager", "Senior Product Manager", "Legal Advisor",
    "Training Coordinator", "Support Specialist", "Data Scientist", "Data Analyst", "Engineering Manager", "Operations Manager",
    "DevOps Engineer", "UX Designer", "UI Developer", "Legal Associate", "Finance Specialist", "HR Specialist", "Customer Success Manager",
    "Marketing Coordinator", "Senior Engineer", "Technical Lead"
]

genders = ["Male", "Female", "Non-binary"]
races = ["White", "Black or African American", "Asian", "Hispanic or Latino", "Native American", "Two or More Races"]

# Generate Employee Data
num_employees = 4000
employee_data = {
    "Employee_ID": range(1, num_employees + 1),
    "Location": random.choices(states, k=num_employees),
    "Department": random.choices(departments, k=num_employees),
    "Job_Title": random.choices(job_titles, k=num_employees),
    "Years_with_Company": np.random.randint(0, 30, size=num_employees),
    "Age": np.random.randint(21, 65, size=num_employees),
    "Left_Company": np.random.choice(["Yes", "No"], size=num_employees, p=[0.2, 0.8]),
    "Salary": [
        np.random.randint(50_000, 120_000) if "I" in title else np.random.randint(80_000, 200_000)
        for title in random.choices(job_titles, k=num_employees)
    ],
    "Work_Type": np.random.choice(["In-Person", "Remote"], size=num_employees, p=[0.6, 0.4]),
    "Gender": random.choices(genders, k=num_employees),
    "Race": random.choices(races, k=num_employees),
    "Environment_Score": np.random.randint(1, 6, size=num_employees),
    "Wellbeing_Score": np.random.randint(1, 6, size=num_employees),
    "Inclusion_Score": np.random.randint(1, 6, size=num_employees),
    "Hire_Date": pd.to_datetime(np.random.choice(pd.date_range(start="2000-01-01", end="2024-01-01"), size=num_employees)),
}

# Add Leave Date for employees who left the company
employee_data["Leave_Date"] = [
    hire_date + pd.Timedelta(days=np.random.randint(1, max(365, 365 * employee_data["Years_with_Company"][i])))
    if left == "Yes" else pd.NaT
    for i, (hire_date, left) in enumerate(zip(employee_data["Hire_Date"], employee_data["Left_Company"]))
]


employee_df = pd.DataFrame(employee_data)

# Ensure at least 40 new hires between 2020-2024
new_hires = employee_df[employee_df["Hire_Date"] >= "2020-01-01"]
if new_hires.shape[0] < 40:
    additional_hires = 40 - new_hires.shape[0]
    for _ in range(additional_hires):
        new_hire = {
            "Employee_ID": employee_df["Employee_ID"].max() + 1,
            "Location": random.choice(states),
            "Department": random.choice(departments),
            "Job_Title": random.choice(job_titles),
            "Years_with_Company": 0,
            "Age": np.random.randint(21, 65),
            "Left_Company": "No",
            "Salary": np.random.randint(50_000, 300_000),
            "Work_Type": random.choice(["In-Person", "Remote"]),
            "Gender": random.choice(genders),
            "Race": random.choice(races),
            "Environment_Score": np.random.randint(1, 6),
            "Wellbeing_Score": np.random.randint(1, 6),
            "Inclusion_Score": np.random.randint(1, 6),
            "Hire_Date": pd.to_datetime(np.random.choice(pd.date_range(start="2020-01-01", end="2024-01-01"))),
            "Leave_Date": pd.NaT,
        }
        employee_df = pd.concat([employee_df, pd.DataFrame([new_hire])], ignore_index=True)

# Save the data to CSV files
employee_df.to_csv("INDGO_Employee_Data_with_Survey.csv", index=False)

print("Employee data with survey scores and hire dates generated successfully!")
