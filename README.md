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
| /api/questions/                 |     GET      |                          All questions |
| /api/questions/new/             |     POST     |                        Create Question |
| /api/questions/<int:pk>/answer/ |  GET, POST   |            List Answers, Create Answer |
| /api/questions/<int:pk>/details |     GET      |                       Question Details |
| /api/questions/<int:pk>/star    | POST, DELETE |         Star Question, Unstar Question |
| /api/questions/<int:pk>/trash   |    DELETE    |                        Delete Question |
| /api/answers/<int:pk>/star      | POST, DELETE |             Star Answer, Unstar Answer |
| /api/myquestions/               |     GET      | All User Created Questions and Answers |



### Create User
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
- Data JSON: Example

```
{
		"id": 1,
		"user": "admin",
		"category_name": "House Plants",
		"answers": [],
		"created_at": "2022-07-28T19:56:47.509638Z",
		"updated_at": "2022-08-01T17:22:28.750849Z",
		"title": "Does my plant need fertilizer?",
		"body": "HELP! My houseplant looks like it is on the way OUT. Does it need water? Does it need fertilizer? Does it need to be adopted by a better caretaker?",
		"category": 1,
		"image": null,
		"starred_by": []
	},
    {
		"id": 3,
		"user": "wannahavegreenthumb1",
		"category_name": "Vegetables",
		"answers": [],
		"created_at": "2022-07-28T20:03:48.500586Z",
		"updated_at": "2022-08-01T17:23:09.729538Z",
		"title": "Newbie here",
		"body": "How can I get started to make a vegetable patch in my backyard?",
		"category": 3,
		"image": null,
		"starred_by": []
	}
```
- Response: 200 OK


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

Response: 201 Created


### List Answers/Create Answer
> /api/questions/int:pk/answer/
- Methods: list - GET, create - POST


### Question Detail
> /api/questions/int:pk/details
- Method: GET
- The pk in the URL above identifies the question for which you want details
- Data JSON: Example

```
{
	"id": 125,
	"user": "dummy007",
	"category_name": "Vegetables",
	"answers": [],
	"created_at": "2022-08-03T18:02:59.279623Z",
	"updated_at": "2022-08-03T18:02:59.279648Z",
	"title": "Greenie beanies",
	"body": "Let's grow all the beans!",
	"category": 3,
	"image": null,
	"starred_by": [
		4
	]
}
```

Response: 200 OK


### Star Question/Unstar Question
> /api/questions/int:pk/star
- Methods: star- POST, unstar - DELETE


### Delete Question
> /api/questions/int:pk/trash
- Method: DELETE 
- The pk in the URL above identifies the question you wish to delete
- Response: 204 No Content


### Star Answer/Unstar Answer
> /api/answers/int:pk/star
- Methods: star- POST, unstar - DELETE


### List All User Created Questions and Answers
> /api/myquestions/
- Method: GET
- Data JSON: Example
  
```
{
	"questions": [
	    {
			"id": 10,
			"user": "FredTomato",
			"category_name": "Vegetables",
			"answers": [
				{
					"pk": 16,
					"user": "susan",
					"question": 10,
					"answer_body": "answer",
					"starred_by": [],
					"created_at": "2022-08-01T20:49:04.056605Z"
				}
			],
			"created_at": "2022-07-29T18:36:16.196469Z",
			"updated_at": "2022-08-01T17:23:48.173405Z",
			"title": "What is your favorite french radish variety?",
			"body": "Share your favorite french radish variety and provide a link to a seed distributor that carries it.",
			"category": 3,
			"image": null,
			"starred_by": []
	    }
    ],
    "answers": [
		{"pk": 4,
			"user": "FredTomato",
			"question": 13,
			"answer_body": "I forgot.....it also needs water.",
			"starred_by": [],
			"created_at": "2022-07-31T19:24:41.778900Z"
		},
        {
			"pk": 7,
			"user": "FredTomato",
			"question": 13,
			"answer_body": "Share your favorite french radish variety and provide a link to a seed distributor that carries it.",
			"starred_by": [],
			"created_at": "2022-08-01T17:28:19.876772Z"
		},
		{
			"pk": 8,
			"user": "FredTomato",
			"question": 13,
			"answer_body": "Just weed around it!",
			"starred_by": [],
			"created_at": "2022-08-01T17:28:43.228435Z"
		}
	]
}
```

- Response: 200 OK