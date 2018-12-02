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
        flag=next(filter(lambda flag:flag['Id'] == Id, self.db))
        return flag

    def editOne():
        pass

    def deleteOne(self, Id):
        flag=next(filter(lambda flag:flag['Id'] == Id, self.db))
        self.db.remove(flag)
        return self.db


#    def update_task(task_id):
#         task = [task for task in tasks if task['id'] == task_id]
#         if len(task) == 0 or not request.json:
#             abort(400)
#         if 'title' in request.json and type(request.json['title']) != unicode:
#             abort(400)
#         if 'description' in request.json and type(request.json['description']) is not unicode:
#             abort(400)
#         if 'done' in request.json and type(request.json['done']) is not bool:
#             abort(400)
#         task[0]['title'] = request.json.get('title', task[0]['title'])
#         task[0]['description'] = request.json.get('description', task[0]['description'])
#         task[0]['done'] = request.json.get('done', task[0]['done'])
#         return jsonify({'task': task})