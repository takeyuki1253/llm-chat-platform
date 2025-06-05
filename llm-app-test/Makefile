.PHONY: help install dev test build lint format clean docker-up docker-down db-init db-migrate db-reset

# Default target
help:
	@echo "Available commands:"
	@echo "  install       Install all dependencies"
	@echo "  dev          Start development environment"
	@echo "  test         Run all tests"
	@echo "  build        Build production images"
	@echo "  lint         Run all linters"
	@echo "  format       Format all code"
	@echo "  clean        Clean up containers and volumes"
	@echo "  docker-up    Start Docker containers"
	@echo "  docker-down  Stop Docker containers"
	@echo "  db-init      Initialize database"
	@echo "  db-migrate   Run database migrations"
	@echo "  db-reset     Reset database"

# Install dependencies
install:
	@echo "Installing dependencies..."
	npm install
	cd frontend && npm install
	@echo "✅ Dependencies installed"

# Development environment
dev: docker-up
	@echo "🚀 Development environment started"
	@echo "Frontend: http://localhost:3000"
	@echo "Backend API: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"

# Start Docker containers
docker-up:
	@echo "Starting Docker containers..."
	docker-compose up -d
	@echo "✅ Docker containers started"

# Stop Docker containers
docker-down:
	@echo "Stopping Docker containers..."
	docker-compose down
	@echo "✅ Docker containers stopped"

# Run tests
test: test-frontend test-backend
	@echo "✅ All tests completed"

test-frontend:
	@echo "Running frontend tests..."
	cd frontend && npm run test

test-backend:
	@echo "Running backend tests..."
	cd backend && python -m pytest

# Build production images
build:
	@echo "Building production images..."
	docker-compose -f docker-compose.prod.yml build
	@echo "✅ Production images built"

# Lint all code
lint: lint-frontend lint-backend
	@echo "✅ All linting completed"

lint-frontend:
	@echo "Linting frontend..."
	cd frontend && npm run lint

lint-backend:
	@echo "Linting backend..."
	cd backend && python -m black --check . && python -m isort --check . && python -m flake8

# Format all code
format: format-frontend format-backend
	@echo "✅ All code formatted"

format-frontend:
	@echo "Formatting frontend..."
	cd frontend && npm run format

format-backend:
	@echo "Formatting backend..."
	cd backend && python -m black . && python -m isort .

# Database operations
db-init:
	@echo "Initializing database..."
	docker-compose exec backend python -c "from src.config.database import engine, Base; import asyncio; asyncio.run(Base.metadata.create_all(bind=engine))"
	@echo "✅ Database initialized"

db-migrate:
	@echo "Running database migrations..."
	docker-compose exec backend alembic upgrade head
	@echo "✅ Database migrations completed"

db-reset:
	@echo "Resetting database..."
	docker-compose down -v
	docker-compose up -d db redis
	sleep 10
	$(MAKE) db-init
	@echo "✅ Database reset completed"

# Clean up
clean:
	@echo "Cleaning up..."
	docker-compose down -v --remove-orphans
	docker system prune -f
	@echo "✅ Cleanup completed"

# Production deployment
deploy-prod:
	@echo "Deploying to production..."
	docker-compose -f docker-compose.prod.yml up -d
	@echo "✅ Production deployment completed"

# Logs
logs:
	docker-compose logs -f

logs-backend:
	docker-compose logs -f backend

logs-frontend:
	docker-compose logs -f frontend

# Health checks
health:
	@echo "Checking service health..."
	@curl -f http://localhost:8000/health || echo "❌ Backend unhealthy"
	@curl -f http://localhost:3000 || echo "❌ Frontend unhealthy"
	@echo "✅ Health checks completed"

# Database backup
db-backup:
	@echo "Creating database backup..."
	docker-compose exec db pg_dump -U user llm_chat > backup_$(shell date +%Y%m%d_%H%M%S).sql
	@echo "✅ Database backup created"

# Database restore
db-restore:
	@echo "Restoring database from backup..."
	@read -p "Enter backup file path: " backup_file; \
	docker-compose exec -T db psql -U user -d llm_chat < "$$backup_file"
	@echo "✅ Database restored"

# Development shell access
shell-backend:
	docker-compose exec backend bash

shell-db:
	docker-compose exec db psql -U user -d llm_chat

shell-redis:
	docker-compose exec redis redis-cli

# Install pre-commit hooks
install-hooks:
	@echo "Installing pre-commit hooks..."
	cd frontend && npx husky install
	@echo "✅ Pre-commit hooks installed"

# Generate API documentation
docs:
	@echo "Generating API documentation..."
	cd backend && python -c "from src.main import app; import json; print(json.dumps(app.openapi(), indent=2))" > ../docs/api.json
	@echo "✅ API documentation generated"