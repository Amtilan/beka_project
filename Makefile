DC = docker-compose
APP_FILE = docker_compose/app.yaml
ENV=--env-file .env

.PHONY: start
start:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: drop
drop:
	${DC} -f ${APP_FILE} down

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} logs -f