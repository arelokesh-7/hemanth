# Simple To-Do List Application

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the to-do list."""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        """Remove a task from the to-do list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        """View all tasks in the to-do list."""
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View all tasks")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1-4.")

if __name__ == "__main__":
    main()
``
