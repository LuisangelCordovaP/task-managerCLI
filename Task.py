from datetime import datetime



class Task:
    #Status Constants
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

    #Variable to set unique id for each task
    counter = 0

    def __init__(self, description):
        #Increment it before assigning to a task
        Task.counter =+ 1

        self.id = Task.counter
        self.status = Task.TODO
        self.description = description

        #Store the current date when a task is created
        now = datetime.now()
        self.createdAt = self.updatedAt = now.strftime("%Y-%m-%d %H:%M")
    
    def updateDescription(self, newDescription):

        #Validating description is blank
        if not newDescription and newDescription.strip() == "":
            print("Tasks must have a description....")
            return
        
        self.description = newDescription

    def updateStatus(self, newStatus):
        validStatus = [self.DONE, self.TODO, self.IN_PROGRESS]

        if newStatus not in validStatus:
            return print("Wrong status....")
        
        self.status = newStatus
    
    

