# Team Fennec Foxes
### Backend Engineers: Amanda McMullin & Yuriy Golota

This repository is the API for a React web application called PlantSpace.

## Endpoints

URL          | Method | Function
:-------------|:--------:|--------------------:
/auth/users/ |  POST  | Create User 
/auth/token/login/ | POST | Login
/auth/token/logout/ | POST | Logout
/api/questions/ | GET | All questions
/api/questions/new/ | POST | Create Question
/api/questions/<int:pk>/answer/ | POST | Answer Question
/api/questions/<int:pk>/details | GET | Question Details
/api/questions/<int:pk>/trash | DELETE | Delete Question


## Heroku URL

[https://plantspace-fennec-foxes.herokuapp.com](https://plantspace-fennec-foxes.herokuapp.com)