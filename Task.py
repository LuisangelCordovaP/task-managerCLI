from datetime import datetime


class Task:
    #Status Constants
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


    def __init__(self, id, description, status=TODO, createdAt=None, updatedAt=None):

        self.id = id
        self.description = description
        self.status = status
        

        if createdAt is None and updatedAt is None:
            #Store the current date when a task is created
            now = datetime.now()
            self.createdAt = self.updatedAt = now.strftime("%Y-%m-%d %H:%M")
        else:
            self.createdAt = createdAt
            self.updatedAt = updatedAt
        
    
    def __str__(self):
        return f"{self.id}\t{self.description}\t{self.status}\t{self.createdAt}\t{self.updatedAt}"
    
    def updateDescription(self, newDescription):

        #Validating description is blank
        if not newDescription and newDescription.strip() == "":
            print("Tasks must have a description....")
            return
        
        self.description = newDescription

    def updateStatus(self, newStatus):
        validStatus = [self.DONE, self.TODO, self.IN_PROGRESS]

        if newStatus not in validStatus:
            return print("Invalid status....")
        
        self.status = newStatus
        #Setting time when it was updated
        now = datetime.now()
        self.updatedAt = now.strftime("%Y-%m-%d %H:%M")
    
    def toDict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }