#priority-based scheduling and task dependencies

import heapq

tasks = []
completed = set()
counter = 0

def add_task(name, priority, dependencies=None):
    global counter
    dependencies = dependencies or []
    heapq.heappush(tasks, (priority, counter, name, dependencies))
    counter += 1

def execute_tasks():
    while tasks:
        executed = False
        waiting = []

        while tasks:
            priority, order, name, dependencies = heapq.heappop(tasks)

            if all(dep in completed for dep in dependencies):
                print(f"Executing task: {name} (Priority {priority})")
                completed.add(name)
                executed = True
            else:
                waiting.append((priority, order, name, dependencies))

        for task in waiting:
            heapq.heappush(tasks, task)

        if not executed and tasks:
            print("Cannot execute remaining tasks. Check dependencies.")
            break

add_task("Download Data", 1)
add_task("Process Data", 2, ["Download Data"])
add_task("Generate Report", 3, ["Process Data"])
add_task("Send Notification", 1, ["Generate Report"])

execute_tasks()

#Round Robin scheduling


import time

tasks = [
    ("Task 1", 3),
    ("Task 2", 5),
    ("Task 3", 2),
    ("Task 4", 4),
    ("Task 5", 1),
    ("Task 6", 3)
]

workers = {
    "Worker 1": [],
    "Worker 2": []
}

# Assign tasks using Round Robin
worker_names = list(workers.keys())

for i, task in enumerate(tasks):
    workers[worker_names[i % 2]].append(task)

# Simulate task execution
counts = {"Worker 1": 0, "Worker 2": 0}

for worker, assigned_tasks in workers.items():
    print(f"\n{worker}:")

    for task_name, processing_time in assigned_tasks:
        start = time.time()
        time.sleep(processing_time * 0.1)
        completion_time = time.time() - start

        counts[worker] += 1

        print(
            f"{task_name} | Processing Time: {processing_time}s | "
            f"Completion Time: {completion_time:.2f}s"
        )

# Print task counts
print("\nNumber of tasks assigned:")
for worker, count in counts.items():
    print(f"{worker}: {count} tasks")
