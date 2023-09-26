from django.urls import path
from .views import ContactListCreateView, ContactDetailView, SearchContactView,SearchContactPhoneView


# Here I had mentioned the api endpoints from where we can access the data, and each and every endpoints mechanism and work is different though they give same output

urlpatterns=[
    path('contacts/',ContactListCreateView.as_view(),name='contact-list-create'),
    path('contacts/<int:pk>/',ContactDetailView.as_view(),name='contact-details'),
    path('search/',SearchContactView.as_view(),name='contact-search'),
    path('search/phone/',SearchContactPhoneView.as_view(),name='search-phone-number'),
]
