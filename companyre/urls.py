
from django.urls import path
from companyre.views import CompanyList,CompanyDetails

urlpatterns = [
    path('details/',CompanyList.as_view()),
    path('details/<int:pk>',CompanyDetails.as_view()),
 
]