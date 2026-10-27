"""Практика 4 (слайд 36): симулятор космического корабля."""


class CrewMember:
    def __init__(self, name, role, skills, health=100):
        if not 0 <= health <= 100:
            raise ValueError("Здоровье должно быть от 0 до 100.")
        self.name = name
        self.role = role
        self.skills = set(skills)
        self.health = health

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным.")
        self.health = max(0, self.health - amount)

    def heal(self, amount):
        if amount < 0:
            raise ValueError("Лечение не может быть отрицательным.")
        self.health = min(100, self.health + amount)


class SpaceShip:
    def __init__(self, name, fuel=100, hull=100, speed=0):
        if fuel < 0 or speed < 0 or not 0 <= hull <= 100:
            raise ValueError("Недопустимые параметры корабля.")
        self.name = name
        self.fuel = fuel
        self.hull = hull
        self.speed = speed
        self.crew = []

    def add_crew(self, member):
        if member not in self.crew:
            self.crew.append(member)

    def refuel(self, amount):
        if amount <= 0:
            raise ValueError("Количество топлива должно быть положительным.")
        self.fuel += amount

    def accelerate(self, delta):
        if delta <= 0:
            raise ValueError("Прирост скорости должен быть положительным.")
        if self.hull <= 0:
            raise ValueError("Корабль разрушен.")
        if not any(m.role == "пилот" and m.health > 0 for m in self.crew):
            raise ValueError("Нужен здоровый пилот.")
        fuel_cost = delta * 0.5
        if fuel_cost > self.fuel:
            raise ValueError("Недостаточно топлива.")
        self.fuel -= fuel_cost
        self.speed += delta

    def brake(self, delta):
        if delta <= 0:
            raise ValueError("Снижение скорости должно быть положительным.")
        self.speed = max(0, self.speed - delta)

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным.")
        self.hull = max(0, self.hull - amount)
        if self.hull == 0:
            self.speed = 0

    def status(self):
        return (
            f"{self.name}: топливо {self.fuel:g}, корпус {self.hull:g}%, "
            f"скорость {self.speed:g} км/с"
        )


class Mission:
    def __init__(self, name, objectives, resources):
        if not objectives:
            raise ValueError("У миссии должна быть хотя бы одна цель.")
        if any(
            type(value) is not int or value < 0 for value in resources.values()
        ):
            raise ValueError(
                "Количество ресурсов должно быть целым и неотрицательным."
            )
        self.name = name
        self.objectives = list(objectives)
        self.completed_objectives = set()
        self.resources = dict(resources)
        self.events = []

    def complete_objective(self, objective, ship):
        if ship.hull <= 0:
            raise ValueError("Разрушенный корабль не может выполнить цель.")
        if objective not in self.objectives:
            raise ValueError("Неизвестная цель миссии.")
        self.completed_objectives.add(objective)

    @property
    def completed(self):
        return set(self.objectives) <= self.completed_objectives

    def handle_event(self, event, ship):
        if ship.hull <= 0:
            raise ValueError("Корабль разрушен.")
        if event == "астероиды":
            ship.take_damage(25)
            message = "Встреча с астероидами: корпус повреждён на 25%."
        elif event == "авария":
            ship.take_damage(10)
            for member in ship.crew:
                member.take_damage(5)
            message = "Авария: корпус -10%, здоровье экипажа -5."
        elif event == "ремонт":
            engineer = any(
                m.role == "инженер" and "ремонт" in m.skills and m.health > 0
                for m in ship.crew
            )
            if not engineer or self.resources.get("запчасти", 0) < 1:
                raise ValueError("Для ремонта нужны инженер и запчасть.")
            self.resources["запчасти"] -= 1
            ship.hull = min(100, ship.hull + 20)
            message = "Ремонт: восстановлено до 20% корпуса."
        else:
            raise ValueError("Неизвестное событие.")
        self.events.append(message)
        return message


if __name__ == "__main__":
    ship = SpaceShip("Восток")
    ship.add_crew(CrewMember("Анна", "пилот", ["навигация"]))
    ship.add_crew(CrewMember("Иван", "инженер", ["ремонт"]))
    mission = Mission(
        "Разведка", ["Достичь орбиты", "Собрать данные"], {"запчасти": 2}
    )
    ship.accelerate(30)
    print(ship.status())
    for event in ["астероиды", "авария", "ремонт"]:
        print(mission.handle_event(event, ship))
    for objective in mission.objectives:
        mission.complete_objective(objective, ship)
    ship.brake(30)
    print(ship.status())
    print("Ресурсы:", mission.resources)
    print("Миссия выполнена:", mission.completed)
