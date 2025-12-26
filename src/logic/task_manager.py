from typing import List, Optional
from src.model.task import Task

class TaskManager:
    """
    Manages a collection of Task objects in memory.
    Handles adding, viewing, updating, deleting, and toggling completion status.
    """
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Adds a new task to the manager.

        Args:
            title (str): The title of the new task.
            description (str, optional): The description of the new task. Defaults to "".

        Returns:
            Task: The newly created task object.
        """
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieves all tasks currently managed.

        Returns:
            List[Task]: A list of all task objects.
        """
        return self._tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a task by its unique ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            Optional[Task]: The task object if found, otherwise None.
        """
        return next((task for task in self._tasks if task.id == task_id), None)

    def update_task(self, task_id: int, new_title: Optional[str] = None, new_description: Optional[str] = None) -> Optional[Task]:
        """
        Updates an existing task's title or description.

        Args:
            task_id (int): The ID of the task to update.
            new_title (Optional[str], optional): The new title for the task. If None, title is not changed.
            new_description (Optional[str], optional): The new description for the task. If None, description is not changed.

        Returns:
            Optional[Task]: The updated task object if found, otherwise None.
        """
        task = self.get_task_by_id(task_id)
        if task:
            if new_title is not None:
                if not new_title:
                    raise ValueError("Task title cannot be empty.")
                task.title = new_title
            if new_description is not None:
                task.description = new_description
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task from the manager.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            bool: True if the task was deleted, False if not found.
        """
        initial_count = len(self._tasks)
        self._tasks = [task for task in self._tasks if task.id != task_id]
        return len(self._tasks) < initial_count

    def toggle_task_completion(self, task_id: int) -> Optional[Task]:
        """
        Toggles the completion status of a task.

        Args:
            task_id (int): The ID of the task to toggle.

        Returns:
            Optional[Task]: The updated task object if found, otherwise None.
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = not task.completed
        return task