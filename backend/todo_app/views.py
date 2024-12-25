import json
import logging 
import traceback
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from todo_app.services import TaskSrv

log = logging.getLogger(__name__)

# @permission_classes((IsAuthenticated,))
@csrf_exempt
@api_view(['POST','GET','PATCH','DELETE'])
def task(request,id=None):
    error_msg = ""
    error_code = ""
    if request.method == "GET":    
        try:
            if id is not None:
                pass
                srv = TaskSrv(request.user)
                resp_data,msg,code = srv.get_single_record(id)
                return  JsonResponse({"response_data":resp_data,"response_msg":msg,"response_code":code})
            else:
                srv = TaskSrv(request.user)
                resp_data,msg,code = srv.get_all_records()
                return  JsonResponse({"response_data":resp_data,"response_msg":msg,"response_code":code})
                
        except Exception as ex:
            log.error(traceback.format_exc())
            error_msg = f"there are some issue in GET task view.{ex}"
            error_code = "V_01"
            return  JsonResponse({"response_data":[],"response_msg":error_msg,"response_code":error_code})
    elif request.method == "POST":
        try:
            data = json.loads(request.body)    
            srv = TaskSrv(request.user,data)
            resp_data,msg,code = srv.create_record()
            return  JsonResponse({"response_data":resp_data,"response_msg":msg,"response_code":code})
        except Exception as ex:
            log.error(traceback.format_exc())
            error_msg = f"there are some issue in POST task view.{ex}"
            error_code = "V_02"
            return  JsonResponse({"response_data":[],"response_msg":error_msg,"response_code":error_code})
    elif request.method == "PATCH":
        if id is not None:
            try:
                data = json.loads(request.body)
                srv = TaskSrv(request.user,data)
                resp_data,msg,code = srv.update_record(id)
                return  JsonResponse({"response_data":resp_data,"response_msg":msg,"response_code":code})                
            except Exception as ex:
                log.error(traceback.format_exc())
                error_msg = f"there are some issue in UPDATE/PATCH task view.{ex}"
                error_code = "V_03"
                return  JsonResponse({"response_data":[],"response_msg":error_msg,"response_code":error_code})                            
        else:
            return  JsonResponse({"response_data":resp_data,"response_msg":"task id not given update request.","response_code":"V_04"})
    elif request.method == "DELETE":
        if id is not None:
            try:
                srv = TaskSrv(request.user)
                resp_data,msg,code = srv.delete_record(id)
                return  JsonResponse({"response_data":resp_data,"response_msg":msg,"response_code":code})                
            except Exception as ex:
                log.error(traceback.format_exc())
                error_msg = f"there are some issue in DELETE task view.{ex}"
                error_code = "V_05"
                return  JsonResponse({"response_data":[],"response_msg":error_msg,"response_code":error_code})                            
        else:
            return  JsonResponse({"response_data":resp_data,"response_msg":"task id not given in delete request.","response_code":"V_06"})
    else:
        return  JsonResponse({"response_data":resp_data,"response_msg":"invalid request method.","response_code":"V_07"})