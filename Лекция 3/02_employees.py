"""Практика 1 (слайд 33): наследование и расчёт зарплаты."""


class Employee:
    def __init__(self, name, base_salary):
        if base_salary < 0:
            raise ValueError("Оклад не может быть отрицательным.")
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, team_size, bonus_per_employee):
        super().__init__(name, base_salary)
        if (
            type(team_size) is not int
            or team_size < 0
            or bonus_per_employee < 0
        ):
            raise ValueError(
                "Размер команды и премия должны быть неотрицательными."
            )
        self.team_size = team_size
        self.bonus_per_employee = bonus_per_employee

    def calculate_salary(self):
        return (
            super().calculate_salary()
            + self.team_size * self.bonus_per_employee
        )


class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, hourly_rate):
        super().__init__(name, base_salary)
        if overtime_hours < 0 or hourly_rate < 0:
            raise ValueError(
                "Часы переработки и ставка должны быть неотрицательными."
            )
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return (
            super().calculate_salary() + self.overtime_hours * self.hourly_rate
        )


if __name__ == "__main__":
    employees = [
        Employee("Анна", 50000),
        Manager("Иван", 80000, 5, 3000),
        Developer("Степан", 100000, 8, 1500),
    ]
    for employee in employees:
        print(f"{employee.name}: {employee.calculate_salary():.2f} руб.")
