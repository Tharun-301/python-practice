import pickle

class Student:
    def __init__(self, stud_id, name, marks):
        self.stud_id = stud_id
        self.name = name
        self.marks = marks

    def __repr__(self):
        return f"{self.name} ({self.stud_id}) - Marks: {self.marks}"


def save_students(student_list, filename='students.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(student_list, f)


def load_students(filename='students.pkl'):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


if __name__ == "__main__":
    students = [
        Student('S001', 'Tharun', {'Math': 75, 'Science': 80}),
        Student('S002', 'Jason', {'Math': 68, 'Science': 74}),
        Student('S003', 'Jonas', {'Math': 95, 'Science': 86})
    ]

    save_students(students)

    loaded_students = load_students()

    print("Student Records:")
    for student in loaded_students:
        print(student)