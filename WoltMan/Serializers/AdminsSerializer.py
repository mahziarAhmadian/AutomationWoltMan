from WoltMan.models import Admins
from WoltMan.TokenManager import user_id_to_token, token_to_user_id
from WoltMan.Serializers import wrong_token_result, status_success_result


class AdminsSerializer:

    @staticmethod
    def admin_check_permission(admin_id, permission):
        admin = Admins.objects.get(admin_id=admin_id)
        if permission in admin.admin_permissions:
            return True
        else:
            return False

    @staticmethod
    def admin_login_serializer(admin_phone, admin_password):
        try:
            admin = Admins.objects.get(admin_phone=admin_phone, admin_password=admin_password)
            admin_id = str(admin.admin_id)
            permissions = admin.admin_permissions
            token = user_id_to_token(admin_id, True, token_level="Admin")
            result = {
                "permissions": permissions,
                "token": token
            }
            return True, result
        except:
            return False, None

    @staticmethod
    def admin_set_profile_serializer(token, admin_name, admin_lastname, other_information):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Self'):
                admin = Admins.objects.get(admin_id=admin_id)
                admin.admin_name = admin_name
                admin.admin_lastname = admin_lastname
                admin.other_information = other_information
                admin.save()
                return True, status_success_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def admin_get_profile_serializer(token):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Self'):
                admin = Admins.objects.get(admin_id=admin_id)
                profile_result = {
                    "admin_id": admin.admin_id,
                    "admin_name": admin.admin_name,
                    "admin_lastname": admin.admin_lastname,
                    "admin_permissions": admin.admin_permissions,
                    "other_information": admin.other_information,
                    "admin_phone": admin.admin_phone
                }
                return True, profile_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def admin_get_other_admin(token, other_admin_id):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Admin'):
                admin = Admins.objects.get(admin_id=other_admin_id)
                profile_result = {
                    "admin_id": admin.admin_id,
                    "admin_name": admin.admin_name,
                    "admin_lastname": admin.admin_lastname,
                    "admin_permissions": admin.admin_permissions,
                    "other_information": admin.other_information,
                    "admin_phone": admin.admin_phone
                }
                return True, profile_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def admin_change_password_serializer(token, new_password):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Self'):
                admin = Admins.objects.get(admin_id=admin_id)
                admin.admin_password = new_password
                admin.save()
                return True, status_success_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def admin_create_new_admin_serializer(token, admin_name, admin_phone, admin_lastname, admin_password,
                                          admin_permissions, other_information):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Admin'):
                admin = Admins()
                admin.admin_name = admin_name
                admin.admin_phone = admin_phone
                admin.admin_lastname = admin_lastname
                admin.admin_password = admin_password
                admin.admin_permissions = admin_permissions
                admin.other_information = other_information
                admin.save()
                return True, status_success_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def get_all_admins_serializer(token, admin_name, admin_lastname, admin_phone):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Admin'):
                all_admins = Admins.objects.filter(admin_name__contains=admin_name,
                                                   admin_lastname__contains=admin_lastname,
                                                   admin_phone__contains=admin_phone)
                all_admins = [admin.as_dict() for admin in all_admins]
                return True, all_admins
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def admin_edit_others_serializer(token, other_admin_id, admin_name, admin_lastname,
                                     admin_permissions, other_information):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Admin'):
                admin = Admins.objects.get(admin_id=other_admin_id)
                admin.admin_name = admin_name
                admin.admin_lastname = admin_lastname
                admin.admin_permissions = admin_permissions
                admin.other_information = other_information
                admin.save()
                return True, status_success_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result

    @staticmethod
    def admin_remove_other_serializer(token, other_admin_id):
        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Admin'):
                admin = Admins.objects.get(admin_id=other_admin_id)
                admin.delete()
                return True, status_success_result
            else:
                return False, wrong_token_result
        else:
            return False, wrong_token_result
