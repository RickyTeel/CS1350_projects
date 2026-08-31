# my_info
my_info = dict(name="Ricky Thiel", age=19, major="Information Systems")
print(my_info)
# menu_info
menu_info= dict(Hamburger=4.99, Cheeseburger=5.24, Fries=2.85, Soda=1.87)
print(menu_info)
# Course_Credits
course_credits = dict(CS1350=3, CS2500=3, IS2180=3,MA2025=3)
print(course_credits)
# weekly_temps
weekly_temps = dict(Mon=76, Tue=80, Wed=84, Thu=83, Fri=82, Sat=84, Sun=87)
print(weekly_temps)
#pet info
pet_info = dict(name="Buddy", type="Dog", age="3")
print(pet_info)
print(dict.get(pet_info, "Color", "Brown"))
# grade_info


course_grade = {
    "Alex": "Passing",
    "Jacob": "Passing",
    "Ricky": "passing",
    "Sol": "Passing",
    "John": "Failing"
}
print(course_grade.get("Ricky"))
#product_info
product_info = {
    "Computer": 1500, 
    "Monitor": 500, 
    "Mouse": 56
}
print(product_info)
# inventry_info
inventory_info = { 
    "lettuce": 3.85,
    "protein_bar": 4.95,
    "soup": 2.68}
print(inventory_info)
# score_info
score_info = {
    "Team_A": 45, 
    "Team_B": 52, 
    "Team_C": 41
    }
print(score_info)
removed = score_info.pop("Team_A")
print(removed) # 45
print(score_info) # {"Team_A":45}
# Shopping_cart
shopping_cart = {}
## Adding Items
shopping_cart["Rice"] = 2.85
shopping_cart["Beans"] = 3.59
shopping_cart["Crackers"] = 4.87
print("After adding:", shopping_cart)
## Updating Item Price
shopping_cart["Crackers"] = 3.58 ##Crackers reduced
print("After update:", shopping_cart)
## Removing Item 
dropped = shopping_cart.pop("Beans")
print(f"Beans dropped with price: {dropped}")
print ("Final Shopping Cart:", shopping_cart)
# Valid Dictionary Keys
## a) Yes, it is a string
## b) No, it is a list
## c) Yes, it is a number
## d) Yes, It is a tuple
## e) No, it is a dictionary
## f) Yes, it is a Frozenset
# Fixing Code
## 1. locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}
locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}
## 2. data = {"a": 1, "b": 2, "a": 3, "b":4}
## print(data)
## print(len(data))
## It will print the last two values of "a" & "b"
data = {"a": 1, "b": 2, "a": 3, "b":4}
print(data)
print(len(data))
## 3. Hash value of "Ricky" & "100"
print(hash("Ricky"))
## 1632552399997345257
print(hash(100))
## -2935539518565956557
# Game High Scores
High_Scores = {
    "Josh, football": 150,
    "Alice, basketball": 200,
    "Bob, baseball": 250
}
print(High_Scores)
# Big_Dicitionary
import time
big_dict = {i: i for i in range(100000)}
start = time.time()
result = 100000 in big_dict
dict_time = time.time() - start
print(f"Dict search: {dict_time:.6f} seconds")
big_list = list(range(100000))
start = time.time()
result = 100000 in big_list
list_time = time.time() - start
print(f"List search: {list_time:.6f} seconds")
big_dict = {i: i for i in range(100000)}
start = time.time()
result = 100000 in big_dict
dict_time = time.time() - start
print(f"Dict search: {dict_time:.6f} seconds")
big_list = list(range(100000))
start = time.time()
result = 100000 in big_list
list_time = time.time() - start
print(f"List search: {list_time:.6f} seconds")
print(f"Dict is {list_time / dict_time:.0f}x faster!")
# Weather Data
temps = {
    "Monday": 72,
    "Tuesday": 75,
    "Wednesday": 68
}
print(f"keys types: {type(temps.keys())}")
print(f"values type: {type (temps.values())}")
print(f"items type: {type(temps.items())}")
max(temps.values())
print(max(temps.values()))
print(min(temps.values()))
if "Friday" in temps:
    print("Friday is in the dictionary")
else:
    print("friday is not in the dictionary")
temps.setdefault("Thursday", 70)
print("After setdefault('Thursday', 70)")
print(f"After setdefult: {temps}")
print("\n=== Dynamic Views ===")
keys_view = temps.keys()
print(f"Before : {keys_view}")
temps["Saturday"] = 78
print(f"After adding 'Saturday': {keys_view}")
# Price_list
prices= {
    "Laptop": 999, 
    "Phone":699, 
    "Tablet":449, 
    "Watch": 299
}
sum(prices.values())
print(f"Total price: {sum(prices.values())}")
max(prices.values())
print(f"Max price: Laptop {max(prices.values())}")
min(prices.values())
print(f"Min price: Watch {min(prices.values())}")
print("\n=== Memory Usage ===")
import sys
prices.keys() = {i: i for i in range(100000)}
view = prices.keys()
as_lost = list(prices.keys())
print(f"View: {sys.getsizeof(view)} bytes")
print(f"List: {sys.getsizeof(as_list)} bytes")
prices= {
    "Laptop": 999, 
    "Phone":699, 
    "Tablet":449, 
    "Watch": 299
}
sum(prices.values())
print(f"Total price: {sum(prices.values())}")
max(prices.values())
print(f"Max price: Laptop {max(prices.values())}")
min(prices.values())
print(f"Min price: Watch {min(prices.values())}")
print("\n=== Memory Usage ===")
import sys
prices = {i: i for i in range(100000)}
view = prices.keys()
as_list = list(prices.keys())
print(f"View: {sys.getsizeof(view)} bytes")
as_list = list(prices.keys())
prices.update({
    "Mouse":58,
    "Keyboard":75,
    "Mouse_Pad":27
})
print(f"Prices after update: {prices}")
# Item_Description
colors = {
    "apple": "red",
    "banana": "yellow", 
    "grape": "purple"
}
for item, color in colors.items(): "The apple is red""
    print(f"{item}: {color}")
for item, color in colors.items(): "The banana is yellow""
    print(f"{item}: {color}")
for item, color in colors.items(): "The grape is purple""
    print(f"{item}: {color}")
## The apple is red, the banana is yellow, and the grape is purple
# Drink_Prices
drink_prices = {
    "Coffee": 4.50,
    "Tea": 3.00,
    "Juice": 5.25,
}
print("=== Price Tax ===")
tax_rate = .45
for drink, price in drink_prices.items():
    price_with_tax = price +tax_rate
    print(f"{drink}: ${price_with_tax:.2f}")  
    #Threshold price
    threshhold= 4.00
    ## Count items over threshold using iteration
    count= 0
    for drink, price in drink_prices.items():
        if price > threshhold:
            count +=1
            print(f"Number of items over ${threshhold}: {count}")
# Tiple unpacking
print("\n=== Unpacking ===")
#Swap values
x = 10
y = 20
x, y = y, x
print(f"x: {x}, y: {y}")
first, *rest = [1, 2, 3, 4, 5]
print(f"first={1}, rest={rest}")
last = rest[-1]
print(f"last={5}, rest={rest}")
print(f"middle={3}, rest={rest}")
# Score list
scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}
print("\n=== Finding Best Score ===")
name, score = max(scores.items(), key=lambda x: x[1])
print(f"Top student: {name} with {score}")
passed = dict()
failed = dict()
for student, grade in scores.items():
    if grade >=70:
        passed[student]= grade
    else:
        failed[student]= grade
        print("Passed:", passed)
        print("Failed:", failed)
        def calculate_class_average(scores_dict):
            if not scores_dict:
                return 0
            return sum(scores_dict.values()) / len(scores_dict)

        print("Class Average:", calculate_class_average(scores))
        data = {f"Key{i}": i for i in range (50_000)}
   def iterate_items ():
    """Iterate using dict.items()"""
    total = 0
    for k, v in data.items():
        total += v
        return total
    def iterate_keys_lookup():
        """Iterate using dict.keys() and then lookup"""
        total = 0
        for k in data.keys():
            total += data[k]
            return total
        ##Number of repeptitions for timint
        repeats = 5
        iterations = 100
        ##Measure execution times
        items_time = timeit.timeit("iterate_items()", globals=globals(), number=iterations)
        keys_time = timeit.timeit("iterate_keys_lookup()", globals=globals(), number=iterations)
        ##Print results
        print(f"Dictionary size: {len(data):,}")
        print(f"Iterations per test: {iterations}:)
              print (f"Repeats: {repeats} (averaged manually if needed)\n")
              print (f" items() iteration time: {items_time:.6f} seconds")
              print (f"keys() + lookup time: {keys_time:.6f} seconds")
              if keys_time !=0
              print(f"Speed ratio (keys/items): {keys_time / items_time:.2f}x slower")
