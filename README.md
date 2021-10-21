# Flask CRUD Application
The objective of this assignment is to apply the basic CRUD operations on a list of users.
The end user of this application should be able to 
- create New user
- Read all users, Read Single User
- Update existing user
- Delete a user

### Software Requirements
- Python 3.9.1
- Flask 1.1.2
- Werkzeug 1.0.1

### User Interface
The Application GUI can be accessed at 127.0.0.1:5000.
The user can be created using the Add User button.
Each user created will have a 'Edit' and 'Delete' button to its right so users can be updated and deleted respectively.
The data is stored in the JSON file at the backend. 

#####Create User
On clicking 'Add User' Button ,we use a pop up form to Input user fields. On submit these are written to the JSON file 
and displayed on the home page

#####Read single User
Reading a single user is tested with command line call
Call :    ``` curl -v http://127.0.0.1:5000/read/2 ```
  
Response:
> HTTP/1.0 200 OK
> Content-Type: application/json
> Content-Length: 142
> Server: Werkzeug/1.0.1 Python/3.9.1
> Date: Thu, 21 Oct 2021 10:35:18 GMT

>{
  "Age": "30",
  "Email": "different@gmail.com",
  "Id": "2",
  "Name": "Bhanu",
  "Occupation": "designer",
  "Phone": "7406591911"
}
>Closing connection 0

#####Read All Users
The index.html displays all the users from the JSON file

#####Update Users
On clicking ' Edit' ,We use a form to edit the user details and it is updated in the back JSON file on submit

#####Delete Users
There is a button provided on the GUI to delete the user from the JSON user file, 
also can be done with curl command
Call: ```curl http://127.0.0.1:5000/delete/1```

Response:
The user is deleted successfully but the page is redirected to Index.html
><!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
><title>Redirecting...</title>
><h1>Redirecting...</h1>
><p>You should be redirected automatically to target URL: <a href="/">/</a>.  If not click the link.

####Running the Application
- python App.py
- GUI Access: http://127.0.0.1:5000/