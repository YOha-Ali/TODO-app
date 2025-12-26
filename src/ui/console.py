from typing import Optional, List, Dict, Any
from src.model.task import Task

def display_message(message: str, is_error: bool = False):
    """
    Displays a message to the console.

    Args:
        message (str): The message to display.
        is_error (bool): If True, indicates an error message (can be used for styling).
    """
    if is_error:
        print(f"ERROR: {message}")
    else:
        print(message)

def get_task_input(prompt_title: str = "Enter task title: ", prompt_description: str = "Enter task description (optional): ") -> Dict[str, str]:
    """
    Prompts the user for task details.

    Args:
        prompt_title (str): The prompt for the task title.
        prompt_description (str): The prompt for the task description.

    Returns:
        Dict[str, str]: A dictionary containing 'title' and 'description'.
    """
    title = input(prompt_title).strip()
    description = input(prompt_description).strip()
    return {"title": title, "description": description}

def get_update_task_input() -> Dict[str, Optional[str]]:
    """
    Prompts the user for new title and description for an existing task.
    Allows for optional input for either field.

    Returns:
        Dict[str, Optional[str]]: A dictionary containing 'title' and 'description',
                                  where None indicates no change for that field.
    """
    print("\nEnter new task details (leave blank to keep current value):")
    new_title = input("New Title: ").strip()
    new_description = input("New Description: ").strip()

    return {
        "title": new_title if new_title else None,
        "description": new_description if new_description else None
    }


def get_task_id_input(prompt: str) -> Optional[int]:
    """
    Prompts the user for a task ID and validates the input.

    Args:
        prompt (str): The prompt message to display.

    Returns:
        Optional[int]: The validated task ID, or None if invalid input.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return None
        try:
            task_id = int(user_input)
            if task_id <= 0:
                display_message("Task ID must be a positive integer.", is_error=True)
            else:
                return task_id
        except ValueError:
            display_message("Invalid input. Please enter a number for the Task ID.", is_error=True)

def display_tasks(tasks: List[Task]):
    """
    Displays a list of tasks to the console.

    Args:
        tasks (List[Task]): The list of Task objects to display.
    """
    if not tasks:
        display_message("No tasks found.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "[✓]" if task.completed else "[✗]"
        desc = f" ({task.description})" if task.description else ""
        print(f"{status} ID: {task.id} | Title: {task.title}{desc}")
    print("------------------")

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n--- To-Do App Menu ---")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Toggle task completion")
    print("6. Exit")
    print("----------------------")

def get_menu_choice() -> Optional[str]:
    """
    Prompts the user for their menu choice.

    Returns:
        Optional[str]: The user's choice as a string, or None if empty.
    """
    choice = input("Enter your choice: ").strip()
    return choice