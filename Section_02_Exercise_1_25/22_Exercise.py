"""
Exercise No. 22

Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

Examples:
    get_student_names({
        "Student 1": "Steve",
        "Student 2": "Becky",
        "Student 3": "John"
    }) -> ["Steve", "John", "Steve"]

Notes:
    - Don't forget to return your result.
"""


def get_student_names(students):
    return sorted(students.values())


print(get_student_names({
        "Student 1": "Steve",
        "Student 2": "Becky",
        "Student 3": "John"
     }))
