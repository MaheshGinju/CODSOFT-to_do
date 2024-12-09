class TodoApp:
    def __init__(self):
        self.tasks = []  # Store tasks as a list
    def show_menu(self):
        print("\n--- To-Do List Menu ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        return choice

    def add_task(self):
        task = input("Enter the task: ")
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
            return
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")

    def remove_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Enter the task number to remove: "))
            if 1 <= task_id <= len(self.tasks):
                removed_task = self.tasks.pop(task_id - 1)
                print(f"Task '{removed_task['task']}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def mark_task_completed(self):
        self.view_tasks()
        try:
            task_id = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_id <= len(self.tasks):
                self.tasks[task_id - 1]["completed"] = True
                print(f"Task '{self.tasks[task_id - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                self.mark_task_completed()
            elif choice == "5":
                print("Exiting the To-Do List app. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

# Main Program
if __name__ == "__main__":
    todo_app = TodoApp()
    todo_app.run()
