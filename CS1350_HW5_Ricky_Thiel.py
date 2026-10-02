Class Workout:
    def __init__(self, name="Cycling", duration_minutes=90, date="2026-10-05"):
        self.name = name
        self._duration_minutes = 0
        self.duration_minutes = duration_minutes
        self.date = date
def __init__(self, name="Cycling", duration_minutes=90, date="2026-10-05"):
        self.name = name
        self._duration_minutes = 0
        self.duration_minutes = duration_minutes
        self.date = date

    @property
    def duration_minutes(self):
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value):
        if value > 0:
            self._duration_minutes = value
        else:
            print("Invalid duration. Please enter a positive number.")

    def calories_burned(self):
        if self.name.lower() == "cycling":
            return 600
        return 0

    def __str__(self):
        return f"{self.name} ({self.duration_minutes} minutes) - {self.date}"

if __name__ == "__main__":
    workout = Workout()
    print(workout)

class CardioWorkout(Workout):
    def __init__(self, name="Running", duration_minutes=60, date="2026-10-05", avg_heart_rate=140):
        super().__init__(name, duration_minutes, date)
        self.avg_heart_rate = avg_heart_rate

    def calories_burned(self):
        return self.duration_minutes * (self.avg_heart_rate / 100) * 5

    @property
    def intensity(self):
        if self.avg_heart_rate >= 150:
            return "High"
        elif self.avg_heart_rate >= 120:
            return "Moderate"
        else:
            return "Low"
class StrengthWorkout(Workout):
    def __init__(self, name="Strength Training", duration_minutes=90, date="2026-10-05", sets=3, reps_per_set=12, weight_lbs=160):

        super().__init__(name, duration_minutes, date)
        self.sets = sets
        self.reps_per_set = reps_per_set
        self.weight_lbs = weight_lbs

    def calories_burned(self):
        return self.sets * self.reps_per_set * (self.weight_lbs / 160) * 3

    @property
    def total_volume(self):
        return self.sets * self.reps_per_set * self.weight_lbs
if __name__ == "__main__":
    cardio = CardioWorkout("Morning Run", 30, "2026-02-23", 155)
    strength = StrengthWorkout("Bench Press", 45, "2026-02-24", 4, 10, 135)
    print(cardio)
    print(f"Calories burned: {cardio.calories_burned():.0f}, Intensity: {cardio.intensity}")
    print(strength)
    print(f"Calories burned: {strength.calories_burned():.0f}, Total Volume: {strength.total_volume} lbs")

class WeeklyLog:
    def __init__(self, week_label):
        self.week_label = week_label
        self._workouts = []

    def add_workout(self, workout):
        self._workouts.append(workout)
@property
def total_minutes(self):
    return sum(workout.duration_minutes for workout in self._workouts)
@property
def total_minutes(self):
    return sum(workout.duration_minutes for workout in self._workouts)
@property
def total_calories(self):
    return sum(workout.calories_burned() for workout in self._workouts)
def summary(self):
    print(f"Weekly Log: {self.week_label}")
    print(f"Total Workouts: {len(self._workouts)}")
    print(f"Total Minutes: {self.total_minutes}")
    print(f"Total Calories Burned: {self.total_calories:.0f}")
    pass
def hardest_workout(self):
    pass

if __name__ == "__main__":

    log = WeeklyLog("Week 7")
run = CardioWorkout("Morning Run", 30, "2026-02-23", 155)
lift = StrengthWorkout("Bench Press", 45, "2026-02-24", 4, 10, 135)
bike = CardioWorkout("Cycling", 60, "2026-02-25", 130)
log.add_workout(run)
log.add_workout(lift)
log.add_workout(bike)
class WeeklyLog:
    def __init__(self, week_label):
        self.week_label = week_label
        self._workouts = []

    def add_workout(self, workout):
        self._workouts.append(workout)

    @property
    def total_minutes(self):
        return sum(workout.duration_minutes for workout in self._workouts)

    @property
    def total_calories(self):
        return sum(workout.calories_burned() for workout in self._workouts)

    def summary(self):
        print(f"Weekly Log: {self.week_label}")
        print(f"Total Workouts: {len(self._workouts)}")
        print(f"Total Minutes: {self.total_minutes}")
        print(f"Total Calories Burned: {self.total_calories:.0f}")

    def hardest_workout(self):
        return max(self._workouts, key=lambda w: w.calories_burned(), default=None)

log = WeeklyLog("Week 7")
log.add_workout(run)
log.add_workout(lift)
log.add_workout(bike)
log.summary()
print(f"\nRun intensity: {run.intensity}")
print(f"Bench press volume: {lift.total_volume} lbs")
hardest = log.hardest_workout()
print(f"Hardest workout: {hardest.name} ({hardest.calories_burned():.0f} cal)")
