import unittest
import os, json
from TaskManager import TaskManager
from Task import Task

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_tasks.json'
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


    def test_load_task_file_not_exists(self):
        manager = TaskManager(self.test_file)
        
        self.assertEqual(manager.tasks, [])
    
    def test_load_task_file(self):
        tasks = [
            {
                "id": 1,
                "description": "Test Task 1",
                "status": "todo",
                "createdAt": "2025-05-12 21:49",
                "updatedAt": "2025-05-12 21:49"
            },
            {
                "id": 2,
                "description": "Test Task 2",
                "status": "in-progress",
                "createdAt": "2025-05-12 22:49",
                "updatedAt": "2025-05-12 22:49"
            },
        ]

        with open(self.test_file,'w') as f:
            json.dump(tasks, f)
        
        manager = TaskManager(self.test_file)

        self.assertEqual(len(manager.tasks), 2)
        self.assertIsInstance(manager.tasks[0], Task)
        self.assertEqual(manager.tasks[0].description, 'Test Task 1')

    def test_add_task(self):
        manager =  TaskManager(self.test_file)

        manager.addTask('Test task')

        self.assertEqual(len(manager.tasks), 1)
        self.assertIsInstance(manager.tasks[0],Task)
        self.assertEqual(manager.tasks[0].description, 'Test task')
    
    def test_update_task(self):
        manager = TaskManager(self.test_file)

        manager.addTask('test task')
        manager.updateTask(1, 'test task updated')

        manager.addTask('test task 2')
        manager.updateTaskStatus(2, Task.IN_PROGRESS)

        self.assertEqual(manager.tasks[0].description, 'test task updated')
        self.assertEqual(manager.tasks[0].status, Task.TODO)

        self.assertEqual(manager.tasks[1].description, 'test task 2')
        self.assertEqual(manager.tasks[1].status, Task.IN_PROGRESS)
    
    def test_list_tasks(self):
        manager = TaskManager(self.test_file)

        manager.addTask('todo task 1')

        manager.addTask('in-progress task 1')
        manager.updateTaskStatus(2,Task.IN_PROGRESS)
        manager.addTask('in-progress task 2')
        manager.updateTaskStatus(3,Task.IN_PROGRESS)

        manager.addTask('done task 1')
        manager.updateTaskStatus(4,Task.DONE)

        all_tasks = manager.listTasks(None,returnOnly=True)
        todo_tasks = manager.listTasks(Task.TODO, returnOnly=True)
        inprogress_tasks = manager.listTasks(Task.IN_PROGRESS, returnOnly=True)
        done_tasks = manager.listTasks(Task.DONE, returnOnly=True)

        self.assertEqual(len(all_tasks), 4)

        self.assertEqual(len(todo_tasks), 1)
        self.assertTrue(todo_tasks[0][2] == Task.TODO)

        self.assertEqual(len(inprogress_tasks), 2)
        self.assertTrue(all(row[2] == Task.IN_PROGRESS for row in inprogress_tasks))

        self.assertEqual(len(done_tasks), 1)
        self.assertTrue(done_tasks[0][2] == Task.DONE)


if __name__ == '__main__':
    unittest.main()