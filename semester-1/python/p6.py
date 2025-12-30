students = {}
n = int(input("Enter the number of students: "))
total_working_days = int(input("Enter the total number of working days: "))

# 1. Accept Data
for i in range(n):
    roll = input(f"Enter roll number of student {i+1}: ")
    absent = int(input(f"Enter the number of days absent for student {i+1}: "))
    students[roll] = absent

print("\n--- Eligibility Check (Minimum 85% Attendance) ---")

noneligible = {}

# 2. Process Data (Calculate ONCE)
for roll, absent in students.items():
    present = total_working_days - absent
    percentage = (present / total_working_days) * 100
    
    # Check eligibility
    if percentage < 85:
        # OPTIMIZATION: Store both absent days AND percentage together
        # We use a tuple: (absent_days, calculated_percentage)
        noneligible[roll] = (absent, percentage) 

# 3. Output Results (No Recalculation)
if noneligible:
    print("Non-eligible students:")
    print("-" * 45) # Adjusted width for cleaner look
    print(f"{'Roll Number':<15} {'Days Absent':<15} {'Percentage':<10}")
    print("-" * 45)
    
    # We unpack the tuple directly here
    for roll, (absent, pct) in noneligible.items():
        print(f"{roll:<15} {absent:<15} {pct:.2f}%")
else:
    print("No non-eligible students found. Everyone is eligible!")
