"""Calculate GPA from comma-separated letter grades on a 4.0 scale."""

grade_points = {
	"A": 4.0,
	"A-": 3.7,
	"B+": 3.3,
	"B": 3.0,
	"B-": 2.7,
	"C+": 2.3,
	"C": 2.0,
	"C-": 1.7,
	"D+": 1.3,
	"D": 1.0,
	"D-": 0.7,
	"F": 0.0,
}

grades_input = input("Enter your grades separated by commas (for example, A, B+, C): ")
grades = [grade.strip().upper() for grade in grades_input.split(",")]
invalid_grades = [grade for grade in grades if grade not in grade_points]

if not grades_input.strip():
	print("Please enter at least one grade.")
elif invalid_grades:
	print("Invalid grade(s):", ", ".join(invalid_grades))
else:
	total_points = 0
	for grade in grades:
		total_points += grade_points[grade]

	gpa = total_points / len(grades)
	print(f"Your GPA is: {gpa:.2f}")
