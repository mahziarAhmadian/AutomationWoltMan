from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from WoltMan.Serializers.AdminsSerializer import AdminsSerializer
from WoltMan.Views import result_creator


@csrf_exempt
class AdminsView:
    @csrf_exempt
    def login_admin(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        admin_phone = input_data["admin_phone"]
        admin_password = input_data["admin_password"]
        result, data = AdminsSerializer.admin_login_serializer(admin_phone=admin_phone, admin_password=admin_password)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message="شماره موبایل و رمز عبور مطابقت ندارند.",
                                  english_message="Wrong phone number or password.")

    @csrf_exempt
    def admin_set_profile(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        admin_name = input_data["admin_name"]
        admin_lastname = input_data["admin_lastname"]
        other_information = input_data["other_information"]
        result, data = AdminsSerializer.admin_set_profile_serializer(token=token, admin_name=admin_name,
                                                                     admin_lastname=admin_lastname,
                                                                     other_information=other_information)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_get_profile(self, request):
        if request.method.lower() == "options":
            return result_creator()
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        result, data = AdminsSerializer.admin_get_profile_serializer(token=token)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_get_one_admin(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        other_admin_id = input_data["other_admin_id"]
        result, data = AdminsSerializer.admin_get_other_admin(token=token, other_admin_id=other_admin_id)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_change_password(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        admin_password = input_data["admin_password"]
        result, data = AdminsSerializer.admin_change_password_serializer(token=token, new_password=admin_password)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_create_new_admin(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        admin_name = input_data["admin_name"]
        admin_phone = input_data["admin_phone"]
        admin_lastname = input_data["admin_lastname"]
        admin_password = input_data["admin_password"]
        admin_permissions = input_data["admin_permissions"]
        other_information = input_data["other_information"]
        result, data = AdminsSerializer.admin_create_new_admin_serializer(token=token, admin_name=admin_name,
                                                                          admin_phone=admin_phone,
                                                                          admin_lastname=admin_lastname,
                                                                          admin_password=admin_password,
                                                                          admin_permissions=admin_permissions,
                                                                          other_information=other_information)
        if result:
            return result_creator()
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_get_all_admins(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        admin_name = input_data["admin_name"]
        admin_phone = input_data["admin_phone"]
        admin_lastname = input_data["admin_lastname"]
        result, data = AdminsSerializer.get_all_admins_serializer(token=token, admin_name=admin_name,
                                                                  admin_lastname=admin_lastname,
                                                                  admin_phone=admin_phone)
        if result:
            return result_creator(data=data)
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_edit_other_admin(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        other_admin_id = input_data["other_admin_id"]
        admin_name = input_data["admin_name"]
        admin_lastname = input_data["admin_lastname"]
        admin_permissions = input_data["admin_permissions"]
        other_information = input_data["other_information"]
        result, data = AdminsSerializer.admin_edit_others_serializer(token, other_admin_id, admin_name,
                                                                     admin_lastname,
                                                                     admin_permissions, other_information)
        if result:
            return result_creator()
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def admin_remove_other_admin(self, request):
        if request.method.lower() == "options":
            return result_creator()
        input_data = json.loads(request.body)
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        other_admin_id = input_data["other_admin_id"]
        result, data = AdminsSerializer.admin_remove_other_serializer(token, other_admin_id)
        if result:
            return result_creator()
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])
