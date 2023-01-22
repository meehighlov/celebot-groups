.PHONY: up stop build

up:
	docker compose up -d

stop:
	docker compose down

build:
	docker compose build

.PHONY:
	start

start: build up
