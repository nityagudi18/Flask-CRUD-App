# Flask CRUD Application
The objective of this assignment is to apply the basic CRUD operations on a list of users.
The end user of this application should be able to 
- create New user
- Read user
- Update existing user
- Delete a user

### Software Requirements
- Python 3.9.1
- Flask 1.1.2
- Werkzeug 1.0.1

### User Interface
CRUD operations can be carried out with help of GUI and command line

#### Running the Application
- python App.py

#### GUI
The Application GUI can be accessed at 127.0.0.1:5000 after executing ```python App.py```


![127.0.0.1:5000](home.PNG)


##### Create User
On clicking 'Add User' Button ,we use a pop up form to Input user fields like Id, Name, Age, Occupation, Email and Phone. 
On submit the user is refected on the user list on home page. In the backend the user is  written to the JSON file 
and displayed on the home page

##### Read 
All the users are read from the backend json file and displayed in the user list on home page

##### Update Users
On clicking ' Edit' button next to each user ,we use a pop up form to edit the user details and it is updated in the 
backend JSON file on submit. The updates made are refected in the user list on home page

##### Delete Users
There is a button provided on the GUI to delete the user from the JSON user file. A confirmation pop up is displayed

##### Notes
All the Routes used for thr GUI are in the routes.py file

#### Command line access with curl

All the CRUD operations can be carried out by command line as well. 

##### CREATE
- Call

``` curl 127.0.0.1:5000/cmd/create -d "{\"Id\": \"4\", \"Name\": \"Four\", \"Age\": \"30\", \"Occupation\": \"occupation\", \"Email\": \"email\"```
```,\"Phone\": \"number\"}" -H "Content-Type:application/json"```

- Response

``` On Server ```
```127.0.0.1 - - [22/Oct/2021 12:58:41] "POST /cmd/create HTTP/1.1" 200 -```

```On terminal - Request Processed```

##### READ
- Call

``` curl 127.0.0.1:5000/cmd/read/<Id> ```

- Response

```On Terimal -  {"Age":"30","Email":"first@first.com","Id":"1","Name":"First User","Occupation":"Engineer","Phone":"1234567890"}```
```On Server - 127.0.0.1 -  [22/Oct/2021 13:00:46] "GET /cmd/read/1 HTTP/1.1" 200 -```
##### UPDATE
- Call

```curl 127.0.0.1:5000/cmd/update/<Id> -d "{\"Id\": \"4\", \"Name\": \"Four\", \"Age\": \"30\", \"Occupation\": \"occupation\", \"Email\": \"email\"```
```,\"Phone\": \"number\"}" -H "Content-Type:application/json"```

- Response

```On Server - 127.0.0.1 - - [22/Oct/2021 13:07:26] "POST /cmd/update/1 HTTP/1.1" 200 -```
```On Terminal - User Updated```
##### DELETE
- Call
```curl 127.0.0.1:5000/cmd/delete/<id>```
- Response

``` On Server - 127.0.0.1 - - [22/Oct/2021 13:16:33] "GET /cmd/delete/1 HTTP/1.1" 200 -```
``` On Terminal - User Deleted```

#### Directory Structure
