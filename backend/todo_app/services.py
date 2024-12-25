import traceback
from todo_app.models import Task
from todo_app.serializers import TaskSerializer


class TaskSrv:
    
    def __init__(self,user,data=None):
        self.user = user
        self.data = data
    
    
    def create_record(self):
        try :
            out_data = []
            if self.data:
                self.data['user'] = self.user.id
                task_serializer = TaskSerializer(data=self.data)
                if task_serializer.is_valid():
                    task_serializer.save()
                    return task_serializer.data,"Record Saved SuccessFully.","1"
                out_data = task_serializer.errors
            return out_data,"Error while creating a task record.","S_01"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while creating a task record.","S_02"
    
    def get_all_records(self,status):
        try:
            all_task_queryset = Task.objects.filter(user_id=self.user.id)
            if status is not None and status != "all":
                status_val = status == 'completed'
                all_task_queryset = all_task_queryset.filter(is_completed=status_val)
            task_serializer = TaskSerializer(all_task_queryset,many=True)
            return task_serializer.data,"All Records fetched SuccessFully.","1"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while fetching all user task record.","S_03"
    
    
    def get_single_record(self,task_id):
        try:
            all_task_queryset = Task.objects.filter(id=task_id).first()
            task_serializer = TaskSerializer(all_task_queryset)
            return task_serializer.data,"Single Record fetched SuccessFully.","1"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while fetching single task record.","S_04"
        
    def update_record(self,task_id):
        try :
            out_data = []
            if self.data:
                task_obj = Task.objects.filter(id=task_id).first()
                if task_obj:
                    task_serializer = TaskSerializer(task_obj, data=self.data, partial=True)
                    if task_serializer.is_valid():
                        task_serializer.save()
                        return task_serializer.data,"Record Updated SuccessFully.","1"
                    out_data = task_serializer.errors
                else:
                    return "Task not found","Error while updating a task record.","S_05"
            return out_data,"Error while updating a task record.","S_06"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while updating a task record.","S_07"     
    
    def delete_record(self,task_id):
        try:
            task_obj = Task.objects.filter(id=task_id).first()
            if task_obj:
                task_obj.delete()
                return [],"Task deleted successfully.","1"
            else:
                return [],"Task not found.","S_09"
        except Exception as ex:
            print(traceback.format_exc())        
            return str(ex),"Error while deleting a task record.","S_10"