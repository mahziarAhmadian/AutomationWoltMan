from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from WoltMan.Serializers.WaterMeterSerializer import WaterMeterSerializer
from WoltMan.Views import result_creator


@csrf_exempt
class WaterMeterView:
    @csrf_exempt
    def Add_WaterMeter_View(self, request):
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")

        fields = ["waterMeter_data", "other_information"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        waterMeter_data = input_data["waterMeter_data"]
        other_information = input_data["other_information"]
        result, data = WaterMeterSerializer.Add_WaterMeter_Serializer(waterMeter_data=waterMeter_data,
                                                                      other_information=other_information)
        if result:
            return result_creator()
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])

    @csrf_exempt
    def Admin_GetAll_WaterMeters_View(self, request):
        try:
            input_data = json.loads(request.body)
        except:
            return result_creator(status="failure", code=406, farsi_message="وارد نشده است json",
                                  english_message="invalid JSON error")
        if "Token" in request.headers:
            token = request.headers["Token"]
        else:
            token = ''
        fields = ["page", "count"]
        for field in fields:
            if field not in input_data:
                return result_creator(status="failure", code=406, farsi_message=f".وارد نشده است {field}",
                                      english_message=f"{field} is Null.")
        page = input_data["page"]
        count = input_data["count"]
        result, data = WaterMeterSerializer.Admin_GetAll_WaterMeters_Serializer(token=token,
                                                                                page=page, count=count)
        if result:
            data = {
                "water_meters": data
            }
            if data['water_meters'].__len__() > 0:
                return result_creator(data)
            else:
                return result_creator(status="failure", code=406, farsi_message="هیچ موردی پیدا نشد",
                                      english_message="don't find anything")
        else:
            return result_creator(status="failure", code=403, farsi_message=data["farsi_message"],
                                  english_message=data["english_message"])
