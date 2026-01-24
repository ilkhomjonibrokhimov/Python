import json
import csv

filename = '/Users/macbook/Python/Lesson-9/Homework-9/tasks.json'

with open(filename, 'r') as file:
    data = json.load(file)
    print('Total num of tasks:', len(data))
    
    completed = sum(1 for d in data if d["completed"])
    print('Completed:', completed)

    pending = sum(1 for d in data if not d["completed"])
    print('Pending:', pending)

    average_priority = sum(d["priority"] for d in data) / len(data)
    print('Average priority:', round(average_priority, 2))


csv_file = '/Users/macbook/Python/Lesson-9/Homework-9/tasks.csv'

with open(filename, 'r') as file:
    tasks = json.load(file)

with open(csv_file, 'w') as file:
    fieldnames = ['id', 'task', "completed", "priority"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(tasks)





