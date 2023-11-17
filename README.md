# fastapi_todo
To-do APi with FastAPI and SQLAlchemy


```sh
docker run --name fastapi_todo -d \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=fastapi_todo \
    -e MYSQL_USER=fastapi_todo \
    -e MYSQL_PASSWORD=fastapi_todo \
    -e MYSQL_DATABASE=fastapi_todo \
    mysql:latest
```

## Blog Post
[https://www.ktechhub.com/tutorials/building-a-todo-api-with-fastapi-and-sqlalchemy-a-step-by-step-guide](https://www.ktechhub.com/tutorials/building-a-todo-api-with-fastapi-and-sqlalchemy-a-step-by-step-guide)