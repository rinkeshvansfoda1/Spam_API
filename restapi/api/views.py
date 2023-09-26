from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer,ContactSerialized
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# Creating Different View for Viewing on the server

# Creting the ContactList having id,name,mobile_no and accessing data from the database
class ContactListCreateView(generics.ListCreateAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerialized

# Creting the ContactDetailsView and accessing data from the database by giving id
class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer

# Creting the ContactSearchView and accessing data from the database by giving name of the contact
class SearchContactView(APIView):
    def get(self,request,*args,**kwargs):
        search_query=self.request.query_params.get('query','')

        if search_query:
            contacts_starts=Contact.objects.filter(name__istartswith=search_query)
            contacts_contains=Contact.objects.filter(name__icontains=search_query).exclude(name__istartswith=search_query)

            results=contacts_starts | contacts_contains
            serializer=ContactSerializer(results,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response([],status=status.HTTP_200_OK)
        

# Creting the ContactSearch Via Phone No and accessing data from the database by giving mobile no of the contact
class SearchContactPhoneView(APIView):
    def get(self,request,*args,**kwargs):
        search_query=self.request.query_params.get('query','')

        registered_contact = Contact.objects.filter(mobile_no=search_query).first()

        if registered_contact:
            serializer=ContactSerializer(registered_contact)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            contact_match=Contact.objects.filter(mobile_no=search_query)
            serializer=ContactSerializer(contact_match,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
