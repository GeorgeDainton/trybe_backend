# TRYBE Backend

<img src="./images/theApp.png" width="200" alt="picture of the app">

## Team

[Luiza](https://github.com/LGretzk) <br>
[Kieran](https://github.com/K-Carty) <br>
[George](https://github.com/GeorgeDainton) <br>
[Luke](https://github.com/lukestorey95) <br>
[Gawain](https://github.com/gawainhewitt) <br>

## <u> Introduction </u> 



Welcome to Trybe. This is our [Makers Academy](https://makers.tech/) final project which we have built in 8 days. <br>

Trybe is an app that helps to build and manage a community in the supporting of achieving bespoke goals. The idea is a group of friends, your TRYBE (TM) will help motivate you with encouragement, while the app also allows you to track and share progress. We concieved it as a type of inverse to the Strava style of tracking, in that your network is small and private, and goals can range from things you would be proud to share, to things you may want to stay discreet about.
<br>


## <u> Design, concept and build </u>


Trybe backend is built using a Python based web framework called the Django Rest Framework. It's sister frontend project can be found [here](https://github.com/lukestorey95/trybe-prod)

## <u> Install Dependencies </u>
1. pip install -r requirements.txt


## <u> Database Migrations </u>
1. python manage.py makemigrations
2. python manage.py migrate


## <u> Connect to Server </u>
1. Local: python manage.py runserver

## <u> Running Requests Using Curl </u>

Run the following requests using curl from the command line:

#### 1. Create a User

```
curl -X POST "http://127.0.0.1:8000/auth/users/" \
--data 'username=goalhaver&email=goals@goal.com&password=inneedofsupport'
```

Returns:

```
    {
    "email": "goalhaver@goal.com",
    "username": "goalhaver",
    "id": 1
    }
```
 
#### 2. Login:
```
  curl -X POST "http://127.0.0.1:8000/auth/token/login/" \
   --data 'username=goalhaver&password=inneedofsupport'
```

Returns:

```
{
    "auth_token": "d671adc4f70d1024aa6b1f80a9c84ef0278f404c"
}
```

  
**This will return an authorization token which needs to be used in every logged in request, referred to hereafter as auth_token**

#### 3. Create a Goal:

```
curl "http://127.0.0.1:8000/goals/" \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Token auth_token" \
-d '{"goal_description":"Goal"}'
```

Returns:
```

{
  "id": 1,
  "goal_description": "Goal",
  "created_at": "2022-07-13T15:35:21.045728+01:00",
  "owner": 1,
  "progress": "0.01"
}
```


#### 4. See Goals:
```
curl -X GET 'http://127.0.0.1:8000/goals/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token auth_token'
```

Returns:
```

[
  {
    "id": 1,
    "goal_description": "Goal",
    "created_at": "2022-07-13T15:35:21.045728+01:00",
    "owner": 1,
    "progress": "0.01"
  }
]
```

#### 5. Invite Supporter:

```
curl --location --request POST 'http://127.0.0.1:8000/supporters/add/' \
--header 'Authorization: Token auth_token' \
--data 'goal_id=1' \
--data 'supporter_email=supporter@support.com'
```
Returns:
```

{
    "id": 1,
    "goal_id": 1,
    "supporter_email": "supporter@support.com"
}
```

#### 6. Registration for Supporter:

```
curl --location --request POST 'http://127.0.0.1:8000/auth/users/' \
--form 'username=supporter' \
--form 'email=supporter@support.com' \
--form 'password=iwanttohelpyou'
```

Returns:

```

{
    "email": "supporter@support.com",
    "username": "supporter",
    "id": 2
}

```

#### 7. Login for Supporter:

```
curl --location --request POST 'http://127.0.0.1:8000/auth/token/login/' \
--form 'username=supporter' \
--form 'password=iwanttohelpyou'
```

Returns:

```
{
    "auth_token": "34e85c6c711dea327f4f67df545c6912ac2cfad9"
}
```


#### 8. Connect to Goal
```
curl --location --request POST 'http://127.0.0.1:8000/supporters/connect/' \
--header 'Authorization: Token auth_token' \
--form 'supporter_email=supporter@support.com' \
--form 'supporter_id=1'
```

Returns
```
[
    {
        "id": 1,
        "goal_id": 1,
        "supporter_email": "supporter@support.com",
        "supporter_id": 1
    }
]
```

### 9. Send a supportive message
```
curl --location --request POST 'http://127.0.0.1:8000/goals/1/messages/' \
--header 'Authorization: Token auth_token' \
--form 'message="Good show lad keep going!"'
```

Returns
```
{
    "id": 4,
    "goal_id": 1,
    "sender_id": 2,
    "sender_username": "supporter",
    "message": "And again",
    "created_at": "2022-07-13T15:43:16.841716+01:00"
}
```

### 10. Goal owner can see goal with supportive message(s)
```
curl --location --request GET 'http://127.0.0.1:8000/goals/1/messages/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token auth_token'
```
Returns
```
[
    {
        "id": 1,
        "goal_id": 1,
        "sender_id": 2,
        "sender_username": "supporter",
        "message": "Good show lad keep going!",
        "created_at": "2022-07-13T15:39:33.191782+01:00"
    },
    {
        "id": 2,
        "goal_id": 1,
        "sender_id": 2,
        "sender_username": "supporter",
        "message": "Bravo Bravo",
        "created_at": "2022-07-13T15:41:54.810063+01:00"
    },
    {
        "id": 3,
        "goal_id": 1,
        "sender_id": 2,
        "sender_username": "supporter",
        "message": "Another one",
        "created_at": "2022-07-13T15:43:00.994097+01:00"
    },
    {
        "id": 4,
        "goal_id": 1,
        "sender_id": 2,
        "sender_username": "supporter",
        "message": "And again",
        "created_at": "2022-07-13T15:43:16.841716+01:00"
    }
]
```

#### 11. Goal owner can see supporters on their goal

```
curl -X GET 'http://127.0.0.1:8000/goals/1/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token auth_token'
```

Returns
```
{
    "goal": {
        "id": 1,
        "goal_description": "goal",
        "created_at": "2022-07-14T16:20:21.949504+01:00",
        "owner": 1,
        "progress": "0.01"
    },
    "supporters": [
        {
            "id": 2,
            "username": "supporter",
            "email": "supporter@support.com"
        }
    ]
}
```

#### 12. Goal owner can edit goal
```
curl --location --request PATCH 'http://127.0.0.1:8000/goals/1/' \
--header 'Authorization: Token a8353fc692c629d7f6e828929ec1ea35b3003de1' \
--form 'goal_description="Patterned"' \
--form 'progress="1.0"'
```

Returns
```
{
    "id": 5,
    "goal_description": "Getting there",
    "created_at": "2022-07-12T17:12:15.769108+01:00",
    "owner": 3,
    "progress": "0.50"
}
```

### 13. Goal owner can delete goal
```
curl --location --request DELETE 'http://127.0.0.1:8000/goals/1/' \
--header 'Authorization: Token a8353fc692c629d7f6e828929ec1ea35b3003de1'
```

Returns:
```
{
    "response": "Goal Deleted",
    "goal_id": 1
}
```

## Impact Effort Assessment

![impact effor assessment graph](./images/impact_effort.jpg)

## Wireframe

![sketch wireframe of design](./images/wireframe.jpg)

## Video of app working 

[![Video of Trybe](./images/videoLinkImage.jpg)](https://www.youtube.com/watch?v=qts_DSZA9IA "Trybe Video")

