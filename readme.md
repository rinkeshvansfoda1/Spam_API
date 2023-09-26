Open restapi folder in your VSCode Editor or any other.,
then type python manage.py runserver in the terminal

127.0.0.1:8000 is my local server
and most of the cases local server are on localhost or 127.0.0.1, and if any changes is there then it will be only of port number.

Endpoints:
it is global contact data:
contacts/
eg., http://127.0.0.1:8000/api/contacts/

it is used to search contact with particular id
contacts/<int:pk>/
eg., http://127.0.0.1:8000/api/contacts/35/

it is used to search contact with name
search/
eg., http://127.0.0.1:8000/api/search/?query=Daniel

it is used to search contact with number
search/phone/
eg., http://127.0.0.1:8000/api/search/phone/?query=0764573371

