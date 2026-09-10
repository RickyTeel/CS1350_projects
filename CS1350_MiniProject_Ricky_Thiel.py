# Contact records: name -> dictionary of details
contact_book = {
 "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
 "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
 "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
 "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
 "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
 "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
 "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
 "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}
# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
 "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
 "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
 "Sister": {"Jan": 80, "Mar": 70},
 "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
 "Roommate": {"Feb": 15, "Mar": 25},
 "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
 "Professor": {"Feb": 20, "Mar": 35},
 "Dentist": {"Jan": 10},
}

#Phase 1 — Creating Contact Manager (30 points)
quick_contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Best Friend": "555-8888",
    "Pizza Place": "555-9999",
    "Work": "555-0000"
}
print(" - - - Access and Modify - - -")
print("Mom's Number:", quick_contacts["Mom"])
print(quick_contacts.get("Grandma", "Looking Up Grandma: Contact Not Found"))
quick_contacts["Dad"] = "555-4321"
quick_contacts["Dentist"] = "555-2222"
print("Updated Contacts:", quick_contacts)
print("- - - Delete and Analyze - - -")
del quick_contacts["Pizza Place"]
print("After deletion:", quick_contacts)
old_work = quick_contacts.pop("Work")
print("Removed Work Number:", old_work)
print("Contacts Remaining:",len(quick_contacts))
print("Contact names:", list(quick_contacts.keys()))
print("Phone Numbers:", list(quick_contacts.values()))

print("=== Contact Activity ===")
for name, months_data in call_log.items():
    months_called = len(months_data)
    total_minutes = sum(months_data.values())
    average_minutes = total_minutes / months_called
    busiest = max(months_data, key=months_data.get)
    print(f"{name}: {months_called} month(s), {total_minutes} min total, avg: {average_minutes:.2f}, busiest: {busiest} ({months_data[busiest]} min)")

print("=== Aggregations ===")

month_stats = {}
for contact, monthly_calls in call_log.items():
    for month, minutes in monthly_calls.items():
        if month not in month_stats:
            month_stats[month] = {"total_minutes": 0, "contacts": 0}
        month_stats[month]["total_minutes"] += minutes
        month_stats[month]["contacts"] += 1

for month in month_stats:
    month_stats[month]["avg"] = (
        month_stats[month]["total_minutes"] / month_stats[month]["contacts"]
    )

for month, stats in sorted(
    month_stats.items(), key=lambda item: item[1]["avg"], reverse=True
):
    print(
        f"{month}: {stats['total_minutes']} min total, "
        f"{stats['avg']:.2f} avg, {stats['contacts']} contacts"
    )

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for name, months_data in call_log.items():
    total_minutes = sum(months_data.values())

    category = contact_book[name]["category"]
    city = contact_book[name]["city"]

    minutes_by_category[category] = minutes_by_category.get(category, 0) + total_minutes
    minutes_by_city[city] = minutes_by_city.get(city, 0) + total_minutes

for info in contact_book.values():
    city = info["city"]
    contacts_per_city[city] = contacts_per_city.get(city, 0) + 1

print(f"Minutes by Category: {minutes_by_category}")
print(f"Minutes by City: {minutes_by_city}")
print(f"Contacts per City: {contacts_per_city}")

print("=== Comprehensions ===")

#Classify
phone_book = {name: info["phone"] for name, info in contact_book.items()}
local_contacts = {name: info["phone"] for name, info in contact_book.items() if info["city"] == "Fort Wayne"}
activity_level = {
    name: ("Frequent" if sum(month_minutes.values()) >= 200 else "Occasional")
    for name, month_minutes in call_log.items()
}
print('Phone book:', phone_book)
print('Local contacts:', local_contacts)
print('Activity level:', activity_level)
#Classify
def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze" 
    else:
        return "Inactive"

for name, months_data in call_log.items():
    total_minutes = sum(months_data.values())
    tier = get_tier(total_minutes)
    print(f"{name}: {total_minutes} minutes ({tier})")

print("--- Tier Distribution ---")

platinum = 0
gold = 0
silver = 0
bronze = 0
inactive = 0

for name, months_data in call_log.items():
    total_minutes = sum(months_data.values())
    tier = get_tier(total_minutes)
    if tier == "Platinum":
        platinum += 1
    elif tier == "Gold":
        gold += 1
    elif tier == "Silver":
        silver += 1
    elif tier == "Bronze":
        bronze += 1
    else:
        inactive += 1

print(f"Platinum: {platinum}")
print(f"Gold: {gold}")
print(f"Silver: {silver}")
print(f"Bronze: {bronze}")
print(f"Inactive: {inactive}")

print("--- Top and Bottom ---")
total_minutes_list = [(name, sum(months_data.values())) for name, months_data in call_log.items()]
top_contact = max(total_minutes_list, key=lambda x: x[1])
bottom_contact = min(total_minutes_list, key=lambda x: x[1])
average_minutes = sum(minutes for _, minutes in total_minutes_list) / len(total_minutes_list)
grand_total_minutes = sum(minutes for _, minutes in total_minutes_list)
print(f"Top Contact: {top_contact[0]} with {top_contact[1]} minutes")
print(f"Bottom Contact: {bottom_contact[0]} with {bottom_contact[1]} minutes")
print(f"Average Minutes: {average_minutes:.2f}")
print(f"Total Minutes: {grand_total_minutes}")

print("=== Contact Hub Report ===")
contacts = []
for name, months in call_log.items():
    total = sum(months.values())
    tier = "Platinum" if total >= 400 else ("Gold" if total >= 200 else "Silver" if total >= 100 else ("Bronze" if total >= 50 else "Inactive"))
    contacts.append({
        "name": name,
        "category": contact_book[name]["category"],
        "city": contact_book[name]["city"],
        "total": total,
        "tier": tier,
    })


sorted_contacts = sorted(contacts, key=lambda item: item["total"], reverse=True)

# Print table header
header = f"{'Name':<12} {'Category':<12} {'City':<12} {'Total':>8}   {'Tier':<8}"
print(header)
print("-" * len(header))

for c in sorted_contacts:
    print(f"{c['name']:<12} {c['category']:<12} {c['city']:<12} {c['total']:>8}   {c['tier']:<8}")

grand_total = sum(c["total"] for c in sorted_contacts)
avg_mins = grand_total / len(sorted_contacts)
print("----------------------------------------------------------------------------------------------------------------------")
print(f"{len(total_minutes_list)} contacts,| Total Minutes: {grand
