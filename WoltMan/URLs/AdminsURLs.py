from django.urls import path
from WoltMan.Views.AdminsView import AdminsView

admins_view = AdminsView()

urlpatterns = [
    path('admin/login', admins_view.login_admin),
    path('admin/setProfile', admins_view.admin_set_profile),
    path('admin/getProfile', admins_view.admin_get_profile),
    path('admin/getOne', admins_view.admin_get_one_admin),
    path('admin/changePassword', admins_view.admin_change_password),
    path('admin/add', admins_view.admin_create_new_admin),
    path('admin/getAll', admins_view.admin_get_all_admins),
    path('admin/edit', admins_view.admin_edit_other_admin),
    path('admin/remove', admins_view.admin_remove_other_admin),
]
