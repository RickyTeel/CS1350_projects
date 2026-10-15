# Midterm_Problem_1
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, copies):
        self.books[isbn] = {
            "title": title,
            "author": author,
            "copies": copies
        }

    def find_author(self, author):
        target = author.lower()

        return [
            book["title"]
            for book in self.books.values()
            if book["author"].lower() == target
        ]

    def inventory_value(self, prices):
        total = 0

        for isbn, book in self.books.items():
            if isbn in prices:
                total += book["copies"] * prices[isbn]

        return total

    def low_stock(self, threshold):
        return {
            isbn: book["copies"]
            for isbn, book in self.books.items()
            if book["copies"] < threshold
        }
# Midterm_Problem_2
class Session:
    def __init__(self, title):
        self.title = title
        self.attendees = set()

    def register(self, name):
        self.attendees.add(name)

    def unregister(self, name):
        self.attendees.discard(name)

    def attendee_count(self):
        return len(self.attendees)


def attended_all(sessions):
    if not sessions:
        return set()

    result = set(sessions[0].attendees)

    for s in sessions[1:]:
        result &= s.attendees

    return result


def attended_exactly_one(sessions):
    counts = {}

    for s in sessions:
        for person in s.attendees:
            counts[person] = counts.get(person, 0) + 1

    return {
        person
        for person, n in counts.items()
        if n == 1
    }


def no_shows(registered, sessions):
    attended = set()

    for s in sessions:
        attended |= s.attendees

    return registered - attended


def summary(sessions):
    everyone = set()

    for s in sessions:
        print(f"{s.title}: {s.attendee_count()} attendees")
        everyone |= s.attendees

    print(f"Distinct attendees: {len(everyone)}")
# Midterm_Problem_3
import json

def process_orders(in_file, json_file, big_file, threshold):
    """
    Summarize orders per customer into a JSON file
    and list big orders.

    Returns:
        number of lines written to big_file
    """

    summary_data = {}
    big_count = 0

    with open(in_file, "r") as f_in, open(big_file, "w") as f_big:

        for line in f_in:
            line = line.strip()

            # skip blank lines
            if not line:
                continue

            order_id, customer, amount = line.split(",")
            amount = float(amount)

            # create customer record if needed
            if customer not in summary_data:
                summary_data[customer] = {
                    "orders": 0,
                    "total": 0.0,
                    "largest": 0.0
                }

            summary_data[customer]["orders"] += 1
            summary_data[customer]["total"] += amount

            if amount > summary_data[customer]["largest"]:
                summary_data[customer]["largest"] = amount

            # write big orders
            if amount >= threshold:
                f_big.write(f"{order_id} {customer} {amount:.2f}\n")
                big_count += 1

    with open(json_file, "w") as f_json:
        json.dump(summary_data, f_json, indent=2)

    return big_count
#Midterm_Problem_4
from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, number, nights):
        self.number = number
        self.nights = nights

    @abstractmethod
    def cost(self):
        pass

    def receipt(self):
        return f"Room {self.number} ({self.nights} nights): ${self.cost():.2f}"

    @staticmethod
    def validate_nights(nights):
        if nights <= 0:
            raise ValueError("Nights must be positive")


class StandardRoom(Room):
    def __init__(self, number, nights, rate=100.0):
        super().__init__(number, nights)
        self.rate = rate

    def cost(self):
        return self.nights * self.rate


class DeluxeRoom(StandardRoom):
    def __init__(self, number, nights, rate=100.0, breakfast=15.0):
        super().__init__(number, nights, rate)
        self.breakfast = breakfast

    def cost(self):
        return super().cost() + self.nights * self.breakfast


class Suite(Room):
    def __init__(self, number, nights, rate=250.0, discount_pct=0.10):
        super().__init__(number, nights)
        self.rate = rate
        self.discount_pct = discount_pct

    def cost(self):
        total = self.nights * self.rate

        if self.nights >= 3:
            total *= (1 - self.discount_pct)

        return total


def invoice(rooms):
    total = 0

    for room in rooms:
        print(room.receipt())
        total += room.cost()

    print(f"Total: ${total:.2f}")
    return total
# Midterm_Problem_5
class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds

    def _normalized(self):
        h, rem = divmod(self.total_seconds, 3600)
        m, s = divmod(rem, 60)
        return h, m, s

    def __str__(self):
        h, m, s = self._normalized()
        return f"{h}:{m:02d}:{s:02d}"

    def __repr__(self):
        h, m, s = self._normalized()
        return f"Duration({h}, {m}, {s})"

    def __len__(self):
        return self.total_seconds

    def __getitem__(self, unit):
        h, m, s = self._normalized()

        if unit == "hours":
            return h
        elif unit == "minutes":
            return m
        elif unit == "seconds":
            return s
        else:
            raise KeyError(unit)

    def __bool__(self):
        return self.total_seconds > 0

    def __add__(self, other):
        result = Duration()
        result.total_seconds = self.total_seconds + other.total_seconds
        return result

    def __sub__(self, other):
        result = self.total_seconds - other.total_seconds

        if result < 0:
            raise ValueError("Negative duration")

        d = Duration()
        d.total_seconds = result
        return d

    def __mul__(self, n):
        d = Duration()
        d.total_seconds = self.total_seconds * n
        return d

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds
