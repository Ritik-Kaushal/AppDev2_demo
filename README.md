# AppDev2_demo - IITM
## PLEASE NOTE
### Do not copy code from this repository. It is purely for understanding purpose. If copied, it might lead to plagiarism which would lead to serious consequences.

# Command to run the server

1. Celery Worker : celery -A main.cel worker --loglevel=info
2. Celery Beat : celery -A main.cel beat --loglevel=info
3. Redis : sudo service redis-server start
4. To check if redis is running : redis-cli ping
	If it return PONG, means redis is runnning
	
