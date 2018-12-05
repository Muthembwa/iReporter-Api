import datetime
class RedFlagModel():

    flags = []
    
    def __init__ (self, CreatedBy, Location, Status, Comment):
       
        self.db=RedFlagModel.flags
        self.CreatedBy = CreatedBy
        self.Location = Location
        self.Status = Status
        self.Comment = Comment

        #Generate Flag id incrementaly 
       
        if len(self.db)==0:
            self.id=1
        else:
            self.id = len(self.db)+1 

    def save (self, new_flag):
        self.db.append(new_flag)
        return new_flag

    def view(self):
        return self.db

    def viewOne(self, Id):
        flag = next(filter(lambda flag:flag['Id'] == Id, self.db),None)
        return flag

    def deleteOne(self, Id):
        flag = next(filter(lambda flag:flag['Id'] == Id, self.db))
        self.db.remove(flag)
        return self.db

   
       

    