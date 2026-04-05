import datetime

class Solution:

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return Solution.days[datetime.date(year, month, day).weekday()]