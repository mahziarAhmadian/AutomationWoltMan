from WoltMan.models import WaterMeters, Admins
from WoltMan.TokenManager import user_id_to_token, token_to_user_id
from WoltMan.Serializers import wrong_token_result, status_success_result, wrong_data_result, wrong_result
from WoltMan.Serializers.AdminsSerializer import AdminsSerializer


class WaterMeterSerializer():

    @staticmethod
    def Add_WaterMeter_Serializer(waterMeter_data,other_information):
        fields = {
            "waterMeter_data": (waterMeter_data, str)
        }
        result = wrong_result(fields)
        if result == None:
            water_meter = WaterMeters()
            water_meter.waterMeter_data = waterMeter_data
            water_meter.other_information = other_information
            water_meter.save()
            return True, status_success_result
        else:
            wrong_data_result["farsi_message"] = "لطفا دیتا را به صورت رشته ارسال کنید"
            wrong_data_result["english_message"] = "data most be string"
            return False, wrong_data_result

    @staticmethod
    def Admin_GetAll_WaterMeters_Serializer(token, page, count):

        token_result = token_to_user_id(token)
        if token_result["status"] == "OK":
            admin_id = token_result["data"]["user_id"]
            if AdminsSerializer.admin_check_permission(admin_id, 'Admin'):
                fields = {
                    "page": (page, int),
                    "count": (count, int),
                }
                field_result = wrong_result(fields)
                if field_result == None:
                    offset = int((page - 1) * count)
                    limit = int(count)
                    all_water_meters = WaterMeters.objects.all().order_by(
                        '-waterMeter_create_date')[offset:offset + limit]

                    tableCount = (WaterMeters.objects.count())
                    all_water_meters = [water_meter.as_dict() for water_meter in all_water_meters]
                    result = {
                        "wattermeters":all_water_meters,
                        "all_data":tableCount
                    }
                    return True, result
                else:
                    return field_result
            else:
                return False, wrong_token_result
