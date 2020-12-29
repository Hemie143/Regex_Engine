class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @staticmethod
    def from_string(time_string):
        hour, minute = time_string.split(":")
        return Time(hour, minute)
