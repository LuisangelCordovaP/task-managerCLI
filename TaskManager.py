from Task import Task
import json, os
from tabulate import tabulate

class TaskManager:
    def __init__(self, filePath):
        self.filePath = filePath
        self.tasks = self.loadTasks()
    
    def loadTasks(self):
        if not os.path.exists(self.filePath):
            return []
        
        with open(self.filePath, "r") as f:
            data = json.load(f)
            return [Task(**item) for item in data]
    
    def saveTasks(self):
        if not self.tasks:
            return
        
        #open or create the file where the tasks going to be stored
        with open(self.filePath, 'w') as f:

            #Tranforming each task object to a list and saving it 
            json.dump([task.toDict() for task in self.tasks], f, indent=2)
    
    def addTask(self, description):
        #Starting id if theres no tasks yet
        nextId = 1

        if self.tasks:
            #Searching the last id created
            nextId = max(task.id for task in self.tasks) + 1
            
        
        self.tasks.append(Task(nextId,description))
        self.saveTasks()
        print(f"Task added successfully (ID: {nextId})")
    
    def updateTask(self,id,newDescription):
        isFound = False
        for task in self.tasks:
            if task.id == id:
                task.updateDescription(newDescription)
                self.saveTasks()
                isFound = True
        
        if not isFound:
            print('This id does not exist...')
    
    def updateTaskStatus(self,id,newStatus):
        isFound = False
        for task in self.tasks:
            if task.id == id:
                task.updateStatus(newStatus)
                self.saveTasks()
                isFound = True
        
        if not isFound:
            print('This id does not exist...') 
    
    def listTasks(self, statusFilter=None):
        if statusFilter is None:
            filtered_list = [
                [task.id, task.description, task.status, task.createdAt, task.updatedAt]
                for task in self.tasks 
                if task.status != Task.DELETED
            ]
            
        else:
            filtered_list = [
                [task.id, task.description, task.status, task.createdAt, task.updatedAt]
                for task in self.tasks 
                if task.status == statusFilter
            ]
        
        if filtered_list:
            print(tabulate(filtered_list, headers=['ID','DESCRIPTION','STATUS','CREATED AT','UPDATED AT']))
        else:
            print("No tasks to show yet")
