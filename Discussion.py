import random

# Define a list of random names for students
names = ["Samiya Rahaman", "Fardeen Khan", "Alice Johnson", "John Doe", "Sarah Ahmed",
         "Mohammed Ali", "Emma Watson", "Isabella Smith", "Liam Brown", "Noah Davis"]


# Function to generate a random student ID
def generate_student_id():
    return f"2024{random.randint(100000, 999999)}"


# Function to randomly generate student data ensuring GPA if degree is present
def generate_student():
    has_bachelor = random.choice([True, False])
    has_graduate = random.choice([True, False])

    # Ensure GPA is assigned if the student has a degree
    undergraduate_gpa = round(random.uniform(2.0, 4.0), 2) if has_bachelor else None
    graduate_gpa = round(random.uniform(2.0, 4.0), 2) if has_graduate else None

    return {
        "id": generate_student_id(),
        "name": random.choice(names),
        "has_bachelor_degree": has_bachelor,
        "has_graduate_degree": has_graduate,
        "undergraduate_gpa": undergraduate_gpa,
        "graduate_gpa": graduate_gpa
    }


# Generate a list of random students
students = [generate_student() for _ in range(10)]


# Function to check eligibility and print result
def print_admission_status(student):
    # Determine eligibility using `or` condition
    if (student["has_bachelor_degree"] and student["undergraduate_gpa"] is not None and student[
        "undergraduate_gpa"] >= 3.0) or \
            (student["has_graduate_degree"] and student["graduate_gpa"] is not None and student["graduate_gpa"] >= 3.0):
        status = "is eligible for regular admission"
    elif student["has_bachelor_degree"] and student["undergraduate_gpa"] is not None and student[
        "graduate_gpa"] is not None and \
            student["undergraduate_gpa"] < 3.0 and student["graduate_gpa"] < 3.0:
        status = "is eligible for provisional admission"
    else:
        status = "is not eligible for graduate admission"

    # Prepare degree information for output
    if student["has_bachelor_degree"]:
        degree_info = f"with undergraduate degree and GPA {student['undergraduate_gpa']}"
    elif student["has_graduate_degree"]:
        degree_info = f"with graduate degree and GPA {student['graduate_gpa']}"
    else:
        degree_info = "with no degree"

    # Print student status
    print(f"ID: {student['id']} {student['name']} {degree_info} {status}.")


# Simplified loop to print results for all students
for student in students:
    print_admission_status(student)
