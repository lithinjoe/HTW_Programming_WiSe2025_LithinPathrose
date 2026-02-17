class Person:
    def __init__(self, n, a):
        self.name, self.age = n, a
class Student(Person):
    def __init__(self, n, a, sid):
        super().__init__(n, a)
        self.sid = sid
    def info(self):
        return f"Student: {self.name}, ID: {self.sid}"
print(Student("Marco", 21, "12345").info())
