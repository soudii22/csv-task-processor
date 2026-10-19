import csv
import json


class Task:
    def __init__(self, id, title, status, priority):
        self.id = id
        self.title = title
        self.status = status
        self.priority = priority


tasks = []

try:
    with open("tasks.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            # Validate
            if not row["id"].isdigit():
                print("Invalid ID. Skipping task.")
                continue

            if row["title"].strip() == "":
                print("Missing title. Skipping task.")
                continue

            if row["status"] not in ["pending", "done"]:
                print("Invalid status. Skipping task.")
                continue

            if row["priority"] not in ["low", "medium", "high"]:
                print("Invalid priority. Skipping task.")
                continue

            # Create object
            task = Task(
                int(row["id"]),
                row["title"],
                row["status"],
                row["priority"]
            )

            tasks.append(task)

except FileNotFoundError:
    print("tasks.csv was not found.")


# Convert objects to dictionaries
data = []

for task in tasks:
    data.append({
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "priority": task.priority
    })


# Save JSON
with open("tasks.json", "w") as file:
    json.dump(data, file, indent=4)

print("Done!")