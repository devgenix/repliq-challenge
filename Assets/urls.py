# Django imports
from django.urls import path

# Own Imports
from Assets import views

urlpatterns = [
    # Company urls
    path('company/create', views.CompanyView.as_view(), name='create_company'), # POST method to create a company by a superuser
    path('company/<int:pk>', views.CompanyView.as_view(), name='retrieve_company'), # GET method to get details about a company by a company_admin/superuser
    path('company/<int:pk>/update', views.CompanyView.as_view(), name='update_company'), # PATCH method to update a company by a company_admin/superuser
    path('company/<int:pk>/delete', views.CompanyView.as_view(), name='delete_company'), # DELETE method to delete a compnay by a superuser
    path('company/list', views.AllListView.as_view(), name='list_company'), # GET method to get a list of companies by superuser
    
    # Deveice urls
    path('device/create', views.DeviceView.as_view(), name='create_device'), # POST method to create a device
    path('device/<int:pk>', views.DeviceView.as_view(), name='retrieve_device'), # GET method to get details about a device
    path('device/<int:pk>/update', views.DeviceView.as_view(), name='update_device'), # PATCH method to update details about a device
    path('device/<int:pk>/delete', views.DeviceView.as_view(), name='delete_device'), # DELETE method to delete a device
    path('device/list/<str:company_name>', views.AllListView.as_view(), name='list_device'), # GET method to get a list of a company's devices by a company_admin/superuser
    
    # Employee urls
    path('employee/create', views.EmployeeView.as_view(), name='create_employee'), # POST method to create an Employee by a company_admin
    path('employee/<int:pk>', views.EmployeeView.as_view(), name='retrieve_employee'), # GET method to retrieve an Employees' data by a super_admin 
    path('employee/<int:pk>/update', views.EmployeeView.as_view(), name='update_employee'), # PATCH method to update an Employee's data by a company_admin
    path('employee/<int:pk>/delete', views.EmployeeView.as_view(), name='delete_employee'), # DELETE method to delete an Employee by a company_admin
    path('employee/list', views.AllListView.as_view(), name='list_employee'), # GET method to get a list of a company's employees by a company_admin/superuser
    
    # Checkout urls
    path('checkout/create', views.CheckoutView.as_view(), name='create_checkout'), # POST method to assign a device to an employee by a company_admin/superuser
    path('checkout/<int:pk>', views.CheckoutView.as_view(), name='retrieve_checkout'), # GET method to get details about a checkout record by a company_admin/superuser
    path('checkout/<int:pk>/update', views.CheckoutView.as_view(), name='update_checkout'), # PATCH method to update details about a checkout record by a company_admin/superuser
    path('checkout/<int:pk>/delete', views.CheckoutView.as_view(), name='delete_checkout'), # DELETE method to delete a checkout record by a company_admin/superuser
    path('checkout/list/<str:company_name>', views.AllListView.as_view(), name='list_checkout'), # GET method to get a list of a company's recent transactions by a company_admin/superuser
    
    
    # path('checkout/employee/<int:pk>', views.RetrieveEmployeeCheckoutView.as_view(), name='retrieve_employee_checkout'),
    # path('checkout/device/<int:pk>', views.RetrieveDeviceCheckoutView.as_view(), name='retrieve_device_checkout'),
    # path('checkout/company/<int:pk>', views.RetrieveCompanyCheckoutView.as_view(), name='retrieve_company_checkout'),
    # path('checkout/employee/<int:pk>/list', views.ListEmployeeCheckoutView.as_view(), name='list_employee_checkout'),
    # path('checkout/device/<int:pk>/list', views.ListDeviceCheckoutView.as_view(), name='list_device_checkout'),
    # path('checkout/company/<int:pk>/list', views.ListCompanyCheckoutView.as_view(), name='list_company_checkout'),
    # path('checkout/employee/<int:pk>/history', views.RetrieveEmployeeCheckoutHistoryView.as_view(), name='retrieve_employee_checkout_history'),
    # path('checkout/device/<int:pk>/history', views.RetrieveDeviceCheckoutHistoryView.as_view(), name='retrieve_device_checkout_history'),
    # path('checkout/company/<int:pk>/history', views.RetrieveCompanyCheckoutHistoryView.as_view(), name='retrieve_company_checkout_history'),
    
    # path('checkout/employee/<int:pk>/history/list', views.ListEmployeeCheckoutHistoryView.as_view(), name='list_employee_checkout_history'),
    
    # path('checkout/device/<int:pk>/history/list', views.ListDeviceCheckoutHistoryView.as_view(), name='list_device_checkout_history'),
    
    # path('checkout/company/<int:pk>/history/list', views.ListCompanyCheckoutHistoryView.as_view(), name='list_company_checkout_history'),
    
    # path('checkout/employee/<int:pk>/history/active/return', views.ReturnEmployeeCheckoutActiveHistoryView.as_view(), name='return_employee_checkout_active_history'),
    # path('checkout/device/<int:pk>/history/active/return', views.ReturnDeviceCheckoutActiveHistoryView.as_view(), name='return_device_checkout_active_history'),
    # path('checkout/company/<int:pk>/history/active/return', views.ReturnCompanyCheckoutActiveHistoryView.as_view(), name='return_company_checkout_active_history'),

]
