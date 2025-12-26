from src.logic.task_manager import TaskManager
from src.ui.console import (
    display_menu,
    get_menu_choice,
    display_message,
    get_task_input,
    get_task_id_input,
    display_tasks,
    get_update_task_input
)

def main():
    """
    Main function to run the To-Do Application.
    """
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == '1':
            task_details = get_task_input()
            try:
                if not task_details["title"]:
                    display_message("Task title cannot be empty.", is_error=True)
                    continue
                task = task_manager.add_task(task_details["title"], task_details["description"])
                display_message(f"Task '{task.title}' (ID: {task.id}) added.")
            except ValueError as e:
                display_message(str(e), is_error=True)

        elif choice == '2':
            tasks = task_manager.get_all_tasks()
            display_tasks(tasks)

        elif choice == '3':
            task_id = get_task_id_input("Enter the ID of the task to update: ")
            if task_id is None:
                display_message("Invalid Task ID.", is_error=True)
                continue

            task_to_update = task_manager.get_task_by_id(task_id)
            if not task_to_update:
                display_message(f"Task with ID {task_id} not found.", is_error=True)
                continue

            update_details = get_update_task_input()
            try:
                updated_task = task_manager.update_task(
                    task_id,
                    new_title=update_details["title"],
                    new_description=update_details["description"]
                )
                if updated_task:
                    display_message(f"Task ID {task_id} updated successfully.")
                else:
                    display_message(f"Task with ID {task_id} not found during update.", is_error=True)
            except ValueError as e:
                display_message(str(e), is_error=True)

        elif choice == '4':
            task_id = get_task_id_input("Enter the ID of the task to delete: ")
            if task_id is None:
                display_message("Invalid Task ID.", is_error=True)
                continue

            if task_manager.delete_task(task_id):
                display_message(f"Task ID {task_id} deleted successfully.")
            else:
                display_message(f"Task with ID {task_id} not found.", is_error=True)

        elif choice == '5':
            task_id = get_task_id_input("Enter the ID of the task to toggle completion: ")
            if task_id is None:
                display_message("Invalid Task ID.", is_error=True)
                continue

            task = task_manager.toggle_task_completion(task_id)
            if task:
                status = "completed" if task.completed else "incomplete"
                display_message(f"Task ID {task_id} marked as {status}.")
            else:
                display_message(f"Task with ID {task_id} not found.", is_error=True)

        elif choice == '6':
            display_message("Exiting To-Do App. Goodbye!")
            break

        else:
            display_message("Invalid choice. Please enter a number between 1 and 6.", is_error=True)

if __name__ == "__main__":
    main()
