# dibarayan
In this project, we first create an ssh connection and send a configuration file to the desired client, then run the desired docker client (mock), the executed docker sends data to the server asynchronously, which we use redis And celery receives this data and stores it in the database.
## Dependencies
- Django
- Python
- Celery
- Redis

