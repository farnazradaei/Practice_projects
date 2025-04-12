class Student:

    def __init__(self, student: str, score: int):
        self.__student = student
        self.__score = score

    def get_student(self) ->str:
        return self.__student
    
    def set_student(self, student: str):
        self.__student = student 

    def get_score(self):
        return self.__score

    def set_score(self, score: int):
        self.__score = score

    def compare_scores(self, other):
        """
        Compare the scores of this student with another student.
        Prints the higher score and the corresponding student's name.
        """
    
        if self.__score > other.get_score():
            print(self.__student, self.__score) 
        elif other.get_score() > self.__score:
            print(other.get_student(), other.get_score())
        else:
            print("The students' scores are equal.")
        if not isinstance(other, Student):
            raise ValueError("Comparison must be between two Student objects.")


s1 = Student("Alice", 100)
s2 = Student("Bob", 100)
s1.compare_scores(s2)