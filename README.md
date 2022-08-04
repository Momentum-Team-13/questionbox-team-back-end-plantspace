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


## Running a local PostgreSQL database

### Clone the API repository:
```bash
git clone https://github.com/Momentum-Team-13/questionbox-team-back-end-plantspace.git
```

### Install project dependencies
This project uses [Python 3.10](https://www.python.org/).

Use [pipenv](https://pypi.org/project/pipenv/) to run a virtual enviroment with all the project dependencies.

Activate a vitual enviroment:
```bash
pipenv shell
```

Install the dependencies:
```bash
pipenv install
```

### Create a local PostgreSQL database
This project uses [PostgreSQL 14.4](https://www.postgresql.org/).
```bash
brew install postgresql
```

Run PostgreSQL:
```bash
brew services start postgresql
```

Create a local instance of a database. It is generally considered good practice to use the same name for username and database name.

Create a user:
```bash
createuser -d <username>
```

Create a database:
```bash
createdb -U <username> <dbname>
```

### Configure Django to connect to your local database
Install a Python PostgreSQL adapter:
```bash
pipenv install psycopg2-binary
```

Create a .env file in /core directory:
```bash
touch ./core/.env
```

Refer to .env.sample for how to configure your local copy of .env. Configure the database url in the following manner:
```bash
DATABASE_URL=postgres://<username>:@127.0.0.1:5432/<dbname>
```

### Run your local server
```bash
python manage.py runserver
```

[Postico](https://eggerapps.at/postico/) or [Dbeaver](https://dbeaver.io/) are great tools to that provide a GUI to interact with your database. [Insomnia](https://insomnia.rest/products/insomnia) is a great way to query your server, whether local or remote. All three are available on Homebrew.
