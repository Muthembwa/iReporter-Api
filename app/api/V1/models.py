class IncidenceModel():
    flags= [{
            "Id":1,
            "Comment": "dfffsfsfdsfsdfsdfdsfdfsdffdffdfdfffsdffffdf",
            "CreatedBy": "CreatedBy",
            "IncidenceType": "red-flags",
            "Location": "Thika",
            "Status": "pending"
        },
        {
            "Id":2,
            "Comment": "dfffsfsfdsfsdfsdfdsfdfsdffdffdfdfffsdffffdf",
            "CreatedBy": "CreatedBy",
            "IncidenceType": "red-flags",
            "Location": "Thika",
            "Status": "pending"
        },
        {
            "Id":3,
            "Comment": "dfffsfsfdsfsdfsdfdsfdfsdffdffdfdfffsdffffdf",
            "CreatedBy": "CreatedBy",
            "IncidenceType": "red-flags",
            "Location": "Thika",
            "Status": "pending"
        }]
    
    def __init__ (self):
        self.db=IncidenceModel.flags
        if len(self.db)==0:
            self.id=1
        else:
            self.id = len(self.db)+1
    def save ( self, CreatedBy, IncidenceType, Location, Status, Comment ):
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

    def view(self):
        return self.db

    def viewOne(self, Id):
        flag=list(filter(lambda flag:flag['Id'] == Id, self.db))
        return flag

    def editOne():
        pass

    def deleteOne():
        pass

   