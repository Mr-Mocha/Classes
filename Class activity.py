class Course:
    roster = []
    name = ""
    def __init__(self,n):
        self.roster = []
        self.name = n

    def Add(self):
        while True:
            name = input("Enter a name:  ")
            self.roster.append(name)
            option = input("Add another student? y or n" )
            if option == "n":
                break
    def Remove(self):
        print(self.roster)
        name = input("Enter a name:  ")
        self.roster.remove(name)

    def ShowStudents(self):
        print(f"{len(self.roster)} student(s)")
        self.roster.sort()
        for student in self.roster:
            print(student)

myCourse = Course("CSC 221")
myCourse.Add()
myCourse.Remove()
myCourse.ShowStudents()
