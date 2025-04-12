class Employee:
    max_hour = 176
    cnt = 0
    
    def __init__(self, name: str, dep: str):
        self._name = name
        self._dep = dep
        self._id = Employee.cnt
        Employee.cnt += 1

        
    def compute_payment(self, hour):
        return 0

    


class FullTimeEmployee(Employee):
    def __init__(self, name: str, dep: str, salary: int):
        super().__init__(name, dep)
        self._salary = salary
        
    def compute_payment(self, hour):
        if hour > Employee.max_hour - 20:
            return self._salary
        
        return self._salary * (hour / Employee.max_hour)

    
class PartTimeEmployee(Employee):
    def __init__(self, name: str, dep: str, wage: int):
        super().__init__(name, dep)
        self._wage = wage
        
    def compute_payment(self, hour):
        return self._wage * hour
