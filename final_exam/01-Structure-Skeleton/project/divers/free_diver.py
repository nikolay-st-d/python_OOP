from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INIT_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, self.INIT_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        self.oxygen_level -= round(time_to_catch * 0.6)
        if self.oxygen_level < 0:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.INIT_OXYGEN_LEVEL

