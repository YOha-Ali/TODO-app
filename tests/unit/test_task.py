import unittest
from src.model.task import Task

class TestTask(unittest.TestCase):
    """
    Unit tests for the Task class.
    """

    def test_task_creation(self):
        """
        Tests that a Task can be created with a title.
        """
        task = Task(id=1, title="Buy milk")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Buy milk")
        self.assertEqual(task.description, "")
        self.assertFalse(task.completed)

    def test_task_creation_with_description(self):
        """
        Tests that a Task can be created with a title and description.
        """
        task = Task(id=1, title="Buy milk", description="Get 2% milk")
        self.assertEqual(task.description, "Get 2% milk")

    def test_task_creation_with_completed_status(self):
        """
        Tests that a Task can be created with a completed status.
        """
        task = Task(id=1, title="Buy milk", completed=True)
        self.assertTrue(task.completed)

    def test_task_creation_with_empty_title_raises_error(self):
        """
        Tests that creating a Task with an empty title raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Task(id=1, title="")

    def test_task_representation(self):
        """
        Tests the string representation of a Task.
        """
        task = Task(id=1, title="Buy milk", description="Get 2% milk")
        self.assertEqual(repr(task), "[✗] #1: Buy milk - Get 2% milk")

        task.completed = True
        self.assertEqual(repr(task), "[✓] #1: Buy milk - Get 2% milk")

if __name__ == '__main__':
    unittest.main()
