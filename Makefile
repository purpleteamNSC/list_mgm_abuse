app:
	@docker compose exec backend bash

down:
	@docker compose down

up:
	@docker compose --env-file .env up -d