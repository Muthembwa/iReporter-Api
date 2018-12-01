

class IncidenceModel():
    flags=[]

    def __init__ (self):
        self.db=IncidenceModel.flags
        if len(self.db)==0:
            self.id=1
        else:
            self.id = len(self.db)+1
    def save( self, CreatedBy, IncidenceType, Location, Status, Comment ):
        data = {
            "Id" : self.id,
            "CreatedBy" : CreatedBy,
            "IncidenceType": IncidenceType,
            "Location" : Location,
            "Status" : Status,
            "Comment" : Comment
            }
        self.db.append(data)
        return self.db

    def View(self):
        return self.db
    def Delete(self):
        for incident in flags:
            data =incident
        res=self.db.remove(data),None
        return self.db
    def edit():
        pass