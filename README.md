# Ryde

[Ryde](https://ryde-app.herokuapp.com/) is a web app for organizing and joining carpools. It was created for Project 3 at General Assembly, WDI-17 and is hosted on Heroku at:


---
## Technologies Used

- HTML5 / CSS3
- JavaScript
- Jquery
- Materialize
- Python
- Django
- D3
- Nvd3
- PostgresSql


## Routes
[to the top](https://github.com/ScoRoc/Ryde#ryde)

| CRUD   | ROUTE                           | FUNCTIONALITY
|--------|---------------------------------|--------------
| GET    | /                               | Home page.
| POST   | /auth/signup                    | Sign up.
| POST   | /auth/login                     | Log in.
| POST   | /auth/me/from/token                  | Lift login from token.
| POST   | /ryde                           | Post a dryve.




## Models

#### User
    -Django's built in User Model

#### Money
    - User
    - cash
    - wage
    -


## APIs Used
[to the top](https://github.com/ScoRoc/Ryde#ryde)
- [Avatar API](https://www.avatarapi.com)

## User Stories
[to the top](https://github.com/ScoRoc/Ryde#ryde)

1. As a daily commuter, I'd prefer to carpool over taking public transportation or driving my own car to work every day. Commuting is cheaper, more pleasant than riding the bus, and is better for the environment.
2. My friends and I are going to a music festival, but none of us have a car! We'd love to carpool
if someone else going has a few extra seats.
3. I'm looking for something to do this weekend, and want to find trips that are leaving from my area. Maybe I'll make some new friends on the way!

## About the project
[to the top](https://github.com/ScoRoc/Ryde#ryde)

Ryde was originally inspired by the traffic and difficult commutes prevalent in Seattle. Organizing carpools at scale could reduce the number of cars on the road, helping to clear room and reduce travel times at peak hours.

Once we started thinking about it, however, we realized that the opportunity for Ryde was even larger than daily commutes. Carpooling can help save money and provide access in a number of situations, including remote weekend activities (like skiing), traveling to popular destinations (Sasquatch music festival), and more.

## Wireframes
[to the top](https://github.com/ScoRoc/Ryde#ryde)

![Landing page wireframe](readme-images/1.jpg)
![List search](readme-images/2.jpg)
![Expandable result card](readme-images/3.jpg)
![Login and signup](readme-images/4.jpg)


## Next Steps
[to the top](https://github.com/ScoRoc/Ryde#ryde)

- Improve ReadMe.md
- Add payments API integration
- Improve security
- Clean and standardize code.
- Consolidate BigSearch and MiniSearch server routes.
