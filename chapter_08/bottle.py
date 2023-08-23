class Bottle:
    def __init__(self, capacity, fill_level, material_type) -> None:
        self.cap = capacity
        self.fill = fill_level
        self.type = material_type

    def check_liqud_lvl(self) -> str:
        status = self.fill + ' of ' + self.cap
        return status

fanta = Bottle('330 ml', '300 ml', 'aluminium')

print(fanta)
print(fanta.check_liqud_lvl())
print(fanta.type)