# lifegoals

1. Create a user

    $ curl 'http://localhost:8000/users/'\
         -H 'Accept: application/json; indent=4'\
         -H 'Content-Type: application/json'\
         -X POST -d '{
                    "username": "shiprashalini",
                    "first_name": "Shipra",
                    "last_name": "Shalini",
                    "password": "x5tw73bfqo9w",
                    "email": "shiprashalini@example.com",
                    "is_active": "true"
                }'

2. Sign in and note the token returned.

    $ curl 'http://localhost:8000/signin/'\
         -H 'Accept: application/json; indent=4'\
         -H 'Content-Type: application/json'\
         -X POST -d '{
                    "username": "shiprashalini",
                    "password": "x5tw73bfqo9w"
                }'

3. Create a goal with token as a header

    $ curl 'http://localhost:8000/goals/'\
         -H 'Accept: application/json; indent=4'\
         -H 'Content-Type: application/json'\
         -H 'Authorization: Token <token>'\
         -X POST -d '{
                "title": "Go to Alps",
                "description": "",
                "end_date": "2018-01-01 00:00:00"
            }'
