# Flask CRUD Application
The objective of this assignment is to apply the basic CRUD operations on a list of users.
The end user of this application should be able to 
- Create New user
- Read user
- Update existing user
- Delete a user

### Software Requirements
- Python 3.9.1
- Flask 1.1.2
- Werkzeug 1.0.1
- pyjwt-2.3.0
- sqlite3

### User Interface
CRUD operations can be carried out with help of GUI and command line

#### Running the Application

- python App.py

#### GUI
The Application GUI can be accessed at 127.0.0.1:5000 after executing ```python App.py```

#### Login
The Login page accepts username and password which are validated against the user stored in the database. If the user 
does not have a login they can create one with the register tab

![127.0.0.1:5000](images/login.PNG)

#### Register
To Register the user hits the Sign Up button and a modal form pos up where the user can choose a username, password and 
create a profile.Username along with a hashed password is stored in the database.

![127.0.0.1:5000](images/signup.PNG)

#### Home Page

![127.0.0.1:5000](images/home.PNG)

Amongst the CRUD operations the Read, Update, Delete are protected and hence require a JWT token generated at login. 
We ceate a WT token at login and pass it to these protected URLS as a part of session headers.

Note: For convenience, I am using the username as the JWT secret key. Also a SECRET key is set up in the app config file
for the user session   

##### Create User
On clicking 'Add User' Button ,we use a pop up form to Input user fields like Id, Name, Age, Occupation, Email and Phone. 
On submit the user is refected on the user list on home page. In the backend the user is  written to the JSON file 
and displayed on the home page

##### Read 
On successful login, 
All the users are read from the backend json file and displayed in the user list on home page

##### Update Users
On clicking ' Edit' button next to each user ,we use a pop up form to edit the user details and it is updated in the 
backend JSON file on submit. The updates made are refected in the user list on home page

##### Delete Users
There is a button provided on the GUI to delete the user from the JSON user file. A confirmation pop up is displayed

##### Notes
All the Routes used for thr GUI are in the routes.py file

#### Command line access with CURL

All the CRUD operations can be carried out by command line as well.
The Read, Update and Delete operations are protected with a JWT token, whereas the Create operation can be carried out 
without a token

##### Token access
On running the app the JWT token can be accessed with the following command on your browser

```127.0.0.1:5000/auth_cmd/token```

![127.0.0.1:5000](images/authorize.PNG)

On entering credentials

![127.0.0.1:5000](images/token.PNG)

##### CREATE
To create a user we do not need JWT Authorization

- Call and Response
``` curl 127.0.0.1:5000/cmd/create -d "{\"Id\": \"4\", \"Name\": \"Four\", \"Age\": \"30\", \"Occupation\": \"occupation\", \"Email\": \"email\"```
```,\"Phone\": \"number\"}" -H "Content-Type:application/json"```

- Response

``` On Server ```
```127.0.0.1 - - [22/Oct/2021 12:58:41] "POST /cmd/create HTTP/1.1" 200 -```

```On terminal - Request Processed```

##### READ
- Call

``` curl "127.0.0.1:5000/cmd/read/1?token=<JWT Token>" ```
![127.0.0.1:5000](images/read.PNG)

##### UPDATE
- Call

```curl "127.0.0.1:5000/cmd/update/1?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoibml0eWEuZ3VkaSIsImV4cCI6MTYzNTM0MDExMX0.Wi4bAUZyHaRDvacKoaEPDAc1cvK5cl0aFKH9DNmTK1Y"  -d "{\"Id\": \"1\", \"Name\": \"First User\", \"Age\": \"31\", \"Occupation\": \"Engineer\", \"Email\": \"first@first\",\"Phone\": \"4088160593\"}" -H "Content-Type:application/json```

![127.0.0.1:5000](images/update.PNG)

##### DELETE
- Call
```curl "127.0.0.1:5000/cmd/delete/4?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoibml0eWEuZ3VkaSIsImV4cCI6MTYzNTM0MDExMX0.Wi4bAUZyHaRDvacKoaEPDAc1cvK5cl0aFKH9DNmTK1Y" ```

![127.0.0.1:5000](images/delete.PNG)



If JWT token is not passwd with the calls for Read,Update , Delete operations the following response is thrown
![127.0.0.1:5000](images/tokenmiss.PNG)

