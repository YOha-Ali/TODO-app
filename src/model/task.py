class Task:
    """
    Represents a single task in the to-do list.
    """
    def __init__(self, id: int, title: str, description: str = "", completed: bool = False):
        """
        Initializes a new Task.

        Args:
            id (int): The unique identifier for the task.
            title (str): The title of the task.
            description (str, optional): A detailed description of the task. Defaults to "".
            completed (bool, optional): The completion status of the task. Defaults to False.
        """
        if not title:
            raise ValueError("Task title cannot be empty.")

        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self) -> str:
        """
        Returns a string representation of the Task.
        """
        status = "✓" if self.completed else "✗"
        return f"[{status}] #{self.id}: {self.title} - {self.description}"
    
