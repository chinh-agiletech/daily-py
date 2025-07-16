import json
import os


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    _id_counter = 1

    def __init__(self, name, age, grades=None, student_id=None):
        super().__init__(name, age)
        self.grades = grades if grades else []

        if student_id is not None:
            self.student_id = student_id
            # giữ cho counter luôn lớn hơn ID lớn nhất
            if student_id >= Student._id_counter:
                Student._id_counter = student_id + 1
        else:
            self.student_id = Student._id_counter
            Student._id_counter += 1

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_rank(self):
        avg = self.get_average_grade()
        if avg >= 8:
            return "Giỏi"
        elif avg >= 6.5:
            return "Khá"
        else:
            return "Trung bình"

    def __str__(self):
        return (f"[ID: {self.student_id}] {self.name} - {self.age} tuổi | "
                f"Điểm: {self.grades} | TB: {self.get_average_grade():.2f} | Xếp loại: {self.get_rank()}")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(data):
        return Student(
            name=data["name"],
            age=data["age"],
            grades=data["grades"],
            student_id=data["student_id"]
        )


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    def save_students(self):
        data = [s.to_dict() for s in self.students]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_students(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.students = [Student.from_dict(item) for item in data]

    def add_student(self, name, age):
        student = Student(name, age)
        self.students.append(student)
        self.save_students()
        print("✅ Thêm học sinh thành công!")

    def remove_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                self.save_students()
                print("🗑️ Đã xoá học sinh.")
                return
        print("❌ Không tìm thấy học sinh.")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def show_all_students(self):
        if not self.students:
            print("⚠️ Danh sách học sinh trống.")
            return
        for s in self.students:
            print(s)

    def add_grade_for_student(self, student_id, grade):
        student = self.find_student(student_id)
        if student:
            student.add_grade(grade)
            self.save_students()
            print("✅ Đã thêm điểm.")
        else:
            print("❌ Không tìm thấy học sinh.")


# ----------------------
# Menu Console
# ----------------------

def main():
    manager = StudentManager()
1
    while True:
        print("\n🎓 Student Management System 🎓")
        print("1. Thêm học sinh")
        print("2. Xoá học sinh")
        print("3. Thêm điểm cho học sinh")
        print("4. Xem tất cả học sinh")
        print("5. Thoát")

        choice = input("👉 Nhập lựa chọn: ")

        if choice == "1":
            name = input("Tên học sinh: ")
            age = input("Tuổi: ")
            if not age.isdigit():
                print("❌ Tuổi phải là số.")
                continue
            manager.add_student(name, int(age))

        elif choice == "2":
            sid = input("Nhập ID học sinh cần xoá: ")
            if sid.isdigit():
                manager.remove_student(int(sid))
            else:
                print("❌ ID không hợp lệ.")

        elif choice == "3":
            sid = input("Nhập ID học sinh: ")
            grade = input("Nhập điểm: ")
            if sid.isdigit() and grade.replace(".", "", 1).isdigit():
                manager.add_grade_for_student(int(sid), float(grade))
            else:
                print("❌ ID hoặc điểm không hợp lệ.")

        elif choice == "4":
            manager.show_all_students()

        elif choice == "5":
            print("👋 Tạm biệt!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
