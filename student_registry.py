class Student:
    
    _instance_counter = 0
    
    def __init__(self, name:str, age:int = 13, grade:str = "12th") -> "Student":
        self.name = name
        self.age = age
        self.grade = grade
        Student._instance_counter += 1
        self.instance_id = Student._instance_counter
        
    @property
    def name(self) -> str: # naming should match from initializer
        return self._name
    
    @name.setter
    def name(self, name_val:str) -> None:
        if not isinstance(name_val, str):
            #raise TypeError("Name must be a string")
            pass
        
        elif len(name_val) < 3:
            #raise ValueError("Name must 3 or more characters")
            pass
        
        elif not name_val.isalnum():
            #raise ValueError("Name must be only alphanumeric")
            pass
        
        else:
            self._name = name_val.strip().title()
        
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, age_val:int) -> None:
        if not isinstance(age_val, int):
            #raise TypeError("Age must be an interger")
            pass
        
        elif age_val not in range(12, 18):
            #raise ValueError("Age has to be between 12 - 17")
            pass
        
        else:
            self._age = age_val
        
    @property
    def grade(self) -> str:
        return self._grade
    
    @grade.setter
    def grade(self, grade_val:str) -> None:
        if not isinstance(grade_val, str):
            # raise TypeError("Grade must be an string")
            pass
        
        elif not grade_val.endswith("th"):
            # raise TypeError("Grade must end with th")
            pass
        
        elif int(grade_val.strip("th")) not in range(9,13):
            # raise ValueError("Grade must be between 9th and 12th")
            pass
        
        else:
            self._grade = grade_val
        
    def __str__ (self) -> str:
        return f"Student {self.instance_id}: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

caroline = Student("Caroline", 15, "11th")
francisco = Student("francisco", 17, "10th")
james = Student("james", 17, "12th")

print(caroline)
print(francisco)
print(james)