# Team Fennec Foxes: PlantSpace API
### Backend Engineers: Amanda McMullin & Yuriy Golota

This repository is the API for a React web application called PlantSpace. The API was built using Django and Django REST Framework, and allows users to create questions and answers to questions. 

## API Endpoints

Base URL: [https://plantspace-fennec-foxes.herokuapp.com](https://plantspace-fennec-foxes.herokuapp.com)


| URL                             |    Method    |                               Function |
| :------------------------------ | :----------: | -------------------------------------: |
| /auth/users/                    |     POST     |                            Create User |
| /auth/token/login/              |     POST     |                                  Login |
| /auth/token/logout/             |     POST     |                                 Logout |
| /api/questions/                 |     GET      |                          All Questions |
| /api/questions/new/             |     POST     |                        Create Question |
| /api/questions/<int:pk>/answer/ |  GET, POST   |            List Answers, Create Answer |
| /api/questions/<int:pk>/details |     GET      |                       Question Details |
| /api/questions/<int:pk>/star    | POST, DELETE |         Star Question, Unstar Question |
| /api/questions/<int:pk>/trash   |    DELETE    |                        Delete Question |
| /api/answers/<int:pk>/star      | POST, DELETE |             Star Answer, Unstar Answer |
| /api/myquestions/               |     GET      | List User's Questions and Answers |



### Register
> /auth/users/
- Method: POST
- Data JSON:

```python
{
    "username": "<username>",
    "password": "<password>"
}
```

- Response: User JSON Object


### Login
> /auth/token/login/
- Method: POST
- Data JSON:

```python
{ 
	"username": "<username>", 
	"password": "<password>" 
}
```

- Response: Example Authentication Token

```python
{
	"auth_token": "a0b8f9382584861a9ad9bc54cd63649f8df4f3c9"
}
```


### Logout
> /auth/token/logout/
- Method: POST

- Data: Authentication Token (See Example Authentication Token in Login section)

- Response: No Data


### List All Questions
> /api/questions/
- Method: GET
- Response: 200_OK, Array of all questions


### Create Question
> /api/questions/new/
- Method: POST
- Data JSON: Example

```
{
	"category": 2,
	"title": "Help",
	"body": "How can I ensure my plants survive the heat?"	
}
```

Response: 201_Created


### List Answers / Create Answer
> /api/questions/int:pk/answer/
- List Answers:
  - Method: GET
  - The URL pk identifies the question whose answers will return
  - Response: 200_OK, Array of answers for question specified in URL

- Create Answer:
  - Method: POST
  - The URL pk identifies the question being answered
  - Data JSON: Example

```
{
"answer_body": "your sample answer here"	
}
```
_
  - Response: 201_Created


### Question Detail
> /api/questions/int:pk/details
- Method: GET
- The URL pk identifies the question for which to return details
- Response: 200_OK, Array of details for question specified in URL


### Star Question / Unstar Question
> /api/questions/int:pk/star
- Methods: star- POST, unstar - DELETE


### Delete Question
> /api/questions/int:pk/trash
- Method: DELETE 
- The pk in the URL above identifies the question you wish to delete
- Response: 204_NO_CONTENT


### Star Answer / Unstar Answer
> /api/answers/int:pk/star
- Methods: star- POST, unstar - DELETE


### List All User Created Questions and Answers
> /api/myquestions/
- Method: GET
- Response: 200_OK, Array of all questions and answers created by specific user