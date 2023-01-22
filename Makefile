.PHONY: up down build

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build

.PHONY:
	start

start: build up
