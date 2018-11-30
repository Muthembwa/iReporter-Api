

class IncidenceModel():
    incidents=[]

    def __init__ (self):
        self.db=IncidenceModel.incidents
        if len(self.db)==0:
            self.id=1
        else:
            self.id = len(incidents)+1
    def Save(self, IncidenceType, Location, Status,Comment):
        data={
        "Id":self.id,
        "CreatedBy":CreatedBy,
        "IncidenceType":IncidenceType,
        "Location":Location,
        "Status":Status,
        "Comment":Comment 
        }
        self.db.append(data)
        return self.id
    def View(self):
        return self.db
    def Delete(self):
        for incident in incidents:
            data =incident
        res=self.db.remove(data),None
        return self.db
    def edit():
        pass