# Trybe Backend README

## Install Dependencies
1. pip install -r requirements.txt


## Database Migrations 
1. python manage.py makemigrations
2. python manage.py migrate


## Connect to Server
1. Local: python manage.py runserver

## Running Requests Using Postman

Download and install the Postman API platform: https://www.postman.com/downloads/

Run the following requests using curl from the command line:

### Create a User

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
 
### Login:
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

### Create a Goal:

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


### See Goals:
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

### Invite Supporter:

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

### Registration for Supporter:

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

### Login for Supporter:

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

8. **Connect to Goal**
curl --location --request POST 'http://127.0.0.1:8000/supporters/connect/' \
--header 'Authorization: Token auth_token' \
--form 'supporter_email=supporter@support.com' \
--form 'supporter_id=1'

**Returns**

[
    {
        "id": 1,
        "goal_id": 1,
        "supporter_email": "supporter@support.com",
        "supporter_id": 1
    }
]

9. **Send a supportive message**
curl --location --request POST 'http://127.0.0.1:8000/goals/1/messages/' \
--header 'Authorization: Token auth_token' \
--form 'message="Good show lad keep going!"'

**Returns**

{
    "id": 4,
    "goal_id": 1,
    "sender_id": 2,
    "sender_username": "supporter",
    "message": "And again",
    "created_at": "2022-07-13T15:43:16.841716+01:00"
}

10. **Goal owner can see goal with supportive message(s)**
curl --location --request GET 'http://127.0.0.1:8000/goals/1/messages/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Token auth_token'

**Returns**

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

11. **Goal owner can edit goal**

curl --location --request PATCH 'http://127.0.0.1:8000/goals/1/' \
--header 'Authorization: Token a8353fc692c629d7f6e828929ec1ea35b3003de1' \
--form 'goal_description="Patterned"' \
--form 'progress="1.0"'


**Returns**

{
    "id": 5,
    "goal_description": "Getting there",
    "created_at": "2022-07-12T17:12:15.769108+01:00",
    "owner": 3,
    "progress": "0.50"
}