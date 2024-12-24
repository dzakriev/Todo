## Start:
```
docker image pull dzakriev/todo-service
docker run -d -p 8000:80 -v app/data dzakriev/todo-service:latest
```