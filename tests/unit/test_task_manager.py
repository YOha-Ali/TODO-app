import unittest
from src.logic.task_manager import TaskManager
from src.model.task import Task

class TestTaskManager(unittest.TestCase):
    """
    Unit tests for the TaskManager class.
    """
    def setUp(self):
        """
        Set up a new TaskManager instance before each test.
        """
        self.task_manager = TaskManager()

    def test_add_task(self):
        """
        Tests adding a single task.
        """
        task = self.task_manager.add_task("Test Task 1", "Description 1")
        self.assertIsInstance(task, Task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task 1")
        self.assertEqual(task.description, "Description 1")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.task_manager.get_all_tasks()), 1)

    def test_add_multiple_tasks_and_ids(self):
        """
        Tests adding multiple tasks and verifies unique ID assignment.
        """
        task1 = self.task_manager.add_task("Task One")
        task2 = self.task_manager.add_task("Task Two")
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(len(self.task_manager.get_all_tasks()), 2)

    def test_get_all_tasks_empty(self):
        """
        Tests retrieving all tasks when the manager is empty.
        """
        self.assertEqual(self.task_manager.get_all_tasks(), [])

    def test_get_all_tasks_with_data(self):
        """
        Tests retrieving all tasks when there is data.
        """
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].title, "Task 1")
        self.assertEqual(tasks[1].title, "Task 2")
    
    def test_get_task_by_id_found(self):
        """
        Tests retrieving a task by a valid ID.
        """
        self.task_manager.add_task("Task A")
        task_b = self.task_manager.add_task("Task B")
        found_task = self.task_manager.get_task_by_id(task_b.id)
        self.assertIsNotNone(found_task)
        self.assertEqual(found_task.title, "Task B")

    def test_get_task_by_id_not_found(self):
        """
        Tests retrieving a task by an invalid ID.
        """
        self.task_manager.add_task("Task C")
        found_task = self.task_manager.get_task_by_id(99)
        self.assertIsNone(found_task)

    def test_update_task_title(self):
        """
        Tests updating a task's title.
        """
        task = self.task_manager.add_task("Original Title")
        updated_task = self.task_manager.update_task(task.id, new_title="New Title")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(self.task_manager.get_task_by_id(task.id).title, "New Title")

    def test_update_task_description(self):
        """
        Tests updating a task's description.
        """
        task = self.task_manager.add_task("Title", "Original Description")
        updated_task = self.task_manager.update_task(task.id, new_description="New Description")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.description, "New Description")
        self.assertEqual(self.task_manager.get_task_by_id(task.id).description, "New Description")

    def test_update_task_both(self):
        """
        Tests updating both title and description.
        """
        task = self.task_manager.add_task("Title", "Description")
        updated_task = self.task_manager.update_task(task.id, new_title="New Title", new_description="New Description")
        self.assertIsNotNone(updated_task)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_update_task_not_found(self):
        """
        Tests updating a non-existent task.
        """
        updated_task = self.task_manager.update_task(99, new_title="Non Existent")
        self.assertIsNone(updated_task)

    def test_update_task_empty_title_raises_error(self):
        """
        Tests that updating a task with an empty title raises a ValueError.
        """
        task = self.task_manager.add_task("Valid Title")
        with self.assertRaises(ValueError):
            self.task_manager.update_task(task.id, new_title="")
    
    def test_delete_task_success(self):
        """
        Tests successful deletion of a task.
        """
        task = self.task_manager.add_task("Task to delete")
        initial_count = len(self.task_manager.get_all_tasks())
        result = self.task_manager.delete_task(task.id)
        self.assertTrue(result)
        self.assertEqual(len(self.task_manager.get_all_tasks()), initial_count - 1)
        self.assertIsNone(self.task_manager.get_task_by_id(task.id))

    def test_delete_task_not_found(self):
        """
        Tests deleting a non-existent task.
        """
        self.task_manager.add_task("Another Task")
        initial_count = len(self.task_manager.get_all_tasks())
        result = self.task_manager.delete_task(99)
        self.assertFalse(result)
        self.assertEqual(len(self.task_manager.get_all_tasks()), initial_count)

    def test_toggle_task_completion(self):
        """
        Tests toggling a task's completion status.
        """
        task = self.task_manager.add_task("Task to toggle")
        self.assertFalse(task.completed)

        toggled_task = self.task_manager.toggle_task_completion(task.id)
        self.assertIsNotNone(toggled_task)
        self.assertTrue(toggled_task.completed)
        self.assertTrue(self.task_manager.get_task_by_id(task.id).completed)

        toggled_task = self.task_manager.toggle_task_completion(task.id)
        self.assertIsNotNone(toggled_task)
        self.assertFalse(toggled_task.completed)
        self.assertFalse(self.task_manager.get_task_by_id(task.id).completed)

    def test_toggle_task_completion_not_found(self):
        """
        Tests toggling completion for a non-existent task.
        """
        toggled_task = self.task_manager.toggle_task_completion(99)
        self.assertIsNone(toggled_task)

if __name__ == '__main__':
    unittest.main()
