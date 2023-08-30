class Plan:
    def __init__(self):
        self.no_flores = 0
        self.no_rooms = 0
    def plan1(self,flores,rooms):
        self.no_flores = flores
        self.no_rooms = rooms
    def __str__(self):
        return f'No.of.flores={self.no_flores}\nNo.of.rooms="{self.no_rooms}'

B1 = Plan()
B1.plan1(5,25)
print(B1)