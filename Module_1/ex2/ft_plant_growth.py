class Plant:
    def	__init__(self, name: str, height: int, age: int, growth: float):
        self.name: str = name.capitalize()
        self.height: int = height
        self.age_days: int = age
        self.growth: float = growth

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def age(self, day: int) -> None:
        self.age += day