import datetime
class RedFlagModel():

    flags = []
    
    def __init__ (self, CreatedBy, Location, Status, Comment):
        self.CreatedBy = CreatedBy
        self.Location = Location
        self.Status = Status
        self.Comment = Comment
       # flags = RedFlagModel.flags

        #Generate Flag id incrementaly 
        self.Id = len(RedFlagModel.flags)+1
        

    def view(self):
        return RedFlagModel.flags

    def viewOne(Id):
        flag = next(filter(lambda flag:flag['Id'] == Id, RedFlagModel.flags),None)
        return flag

    def deleteOne(Id):
        flag = next(filter(lambda flag:flag['Id'] == Id, RedFlagModel.flags),None)
        RedFlagModel.flags.remove(flag)
        return 


   
       

    