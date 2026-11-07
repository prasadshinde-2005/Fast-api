
data = {
    "STU001": {
        "name": "Aarav Sharma",
        "age": 20,
        "course": "Computer Engineering",
        "year": 3,
        "city": "Pune",
        "marks": 85.5
    },
    "STU002": {
        "name": "Priya Patel",
        "age": 21,
        "course": "Information Technology",
        "year": 4,
        "city": "Mumbai",
        "marks": 91.0
    },
    "STU003": {
        "name": "Rahul Verma",
        "age": 19,
        "course": "Electronics and Telecommunication",
        "year": 2,
        "city": "Nashik",
        "marks": 78.0
    }
}

for student_id, info in data.items():
    print(info["course"]=="Computer Engineering")
