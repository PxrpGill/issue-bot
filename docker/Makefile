.PHONY: build up down logs restart shell clean

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

restart: down up

shell:
	docker-compose exec main sh

clean:
	docker-compose down --rmi all -v
