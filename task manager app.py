class Task:
    def __init__(self, description, priority=5):
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"Task(description={self.description!r}, priority={self.priority})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority=5):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Added: {task}")

    def remove_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print(f"Removed: {task}")
                return
        print(f"Task not found: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Current tasks:")
            for task in self.tasks:
                print(task)

    def prioritize_task(self, description, new_priority):
        for task in self.tasks:
            if task.description == description:
                task.priority = new_priority
                print(f"Updated priority: {task}")
                return
        print(f"Task not found: {description}")

    def recommend_task(self, keyword):
        recommendations = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        if not recommendations:
            print(f"No tasks found with keyword: {keyword}")
        else:
            print(f"Tasks with keyword '{keyword}':")
            for task in recommendations:
                print(task)

def main():
    task_manager = TaskManager()

    while True:
        print("\nOptions: add, remove, list, prioritize, recommend, exit")
        action = input("Choose an action: ").strip().lower()

        if action == "add":
            description = input("Task description: ").strip()
            priority = int(input("Task priority (1-10): ").strip())
            task_manager.add_task(description, priority)

        elif action == "remove":
            description = input("Task description to remove: ").strip()
            task_manager.remove_task(description)

        elif action == "list":
            task_manager.list_tasks()

        elif action == "prioritize":
            description = input("Task description to prioritize: ").strip()
            new_priority = int(input("New priority (1-10): ").strip())
            task_manager.prioritize_task(description, new_priority)

        elif action == "recommend":
            keyword = input("Keyword for recommendation: ").strip()
            task_manager.recommend_task(keyword)

        elif action == "exit":
            print("Exiting the task manager.")
            break

        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
