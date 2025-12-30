students = {}
n = int(input("Enter the number of students: "))

# We need the total working days to calculate percentage
total_working_days = int(input("Enter the total number of working days in the semester: "))

# 1. Accept Data
for i in range(n):
    roll = input(f"Enter roll number of student {i+1}: ")
    absent = int(input(f"Enter the number of days absent for student {i+1}: "))
    students[roll] = absent

print("\n--- Eligibility Check (Minimum 85% Attendance) ---")

noneligible = {}

# 2. Process Data
for roll, absent in students.items():
    # Calculate days present
    present = total_working_days - absent
    
    # Calculate percentage
    # Formula: (Present Days / Total Days) * 100
    percentage = (present / total_working_days) * 100
    
    # Check eligibility condition
    if percentage < 85:
        noneligible[roll] = absent

# 3. Output Results
if noneligible:
    print("Non-eligible students:")
    print("-" * 30)
    print(f"{'Roll Number':<15} {'Days Absent':<15} {'Percentage':<10}")
    print("-" * 30)
    for roll, absent in noneligible.items():
        # Recalculate percentage just for display purposes
        present = total_working_days - absent
        pct = (present / total_working_days) * 100
        print(f"{roll:<15} {absent:<15} {pct:.2f}%")
else:
    print("No non-eligible students found. Everyone is eligible!")
