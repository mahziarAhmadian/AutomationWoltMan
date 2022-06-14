from django.urls import path
from WoltMan.Views.WaterMeterView import WaterMeterView

watermeter_view = WaterMeterView()

urlpatterns = [

    path('add', watermeter_view.Add_WaterMeter_View),
    path('admin/getAll', watermeter_view.Admin_GetAll_WaterMeters_View)

]
