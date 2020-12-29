class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    # create the method
    def __add__(self, other):
        desc = f"{self.description}\n{other.description}"
        team = f"{self.team}, {other.team}"
        return Task(desc, team)
