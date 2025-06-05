# LLM Chat Platform

A comprehensive multi-LLM chat platform that enables simultaneous querying of multiple AI providers (OpenAI, Google, Anthropic) with built-in evaluation, comparison, and analytics features.

## Features

- **Multi-LLM Chat**: Send queries to multiple LLMs simultaneously and compare responses
- **Evaluation System**: Rate and evaluate LLM responses with automated metrics
- **Analytics Dashboard**: Visualize usage statistics, costs, and performance metrics
- **Use Case Management**: Create and schedule automated test scenarios
- **Real-time Updates**: WebSocket-based live chat functionality
- **Enterprise Ready**: JWT authentication, role-based access control, and API key management

## Architecture

### Tech Stack

**Frontend:**
- React 18 with TypeScript
- Vite for fast development
- Tailwind CSS + Material-UI
- Redux Toolkit for state management
- Socket.io for real-time features

**Backend:**
- FastAPI with Python 3.9+
- PostgreSQL with SQLAlchemy ORM
- Redis for caching
- Celery for background tasks
- Alembic for database migrations

**Infrastructure:**
- Docker for containerization
- Azure cloud deployment ready
- GitHub Actions CI/CD

## Project Structure

```
llm-chat-platform/
├── frontend/              # React TypeScript application
├── backend/              # FastAPI Python application
├── infrastructure/       # Infrastructure as Code (Azure/Terraform)
├── docs/                # Documentation
├── scripts/             # Development and deployment scripts
└── shared/              # Shared resources and types
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm 9+
- Python 3.9+
- Docker and Docker Compose
- PostgreSQL 14+
- Redis 7+

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/takeyuki1253/llm-chat-platform.git
cd llm-chat-platform
```

2. Run the setup script:
```bash
./scripts/setup.sh
```

### Manual Setup

1. Install dependencies:
```bash
make install
```

2. Set up environment variables:
```bash
cp frontend/.env.example frontend/.env
cp backend/.env.example backend/.env
```

3. Start development environment:
```bash
make dev
```

### Development Commands

```bash
make help          # Show all available commands
make dev           # Start development environment
make test          # Run all tests
make lint          # Run linters
make format        # Format code
make logs          # View application logs
make clean         # Clean up containers and volumes
```

### Running Tests

```bash
npm run test        # Run all tests
npm run test:frontend  # Frontend tests only
npm run test:backend   # Backend tests only
```

### Code Quality

```bash
npm run lint        # Run linters
npm run format      # Format code
```

## API Documentation

Once the backend is running, API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Deployment

### Docker Production Build

```bash
docker-compose -f docker-compose.prod.yml up --build
```

### Azure Deployment

See [infrastructure/README.md](infrastructure/README.md) for Azure deployment instructions.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Claude Code assistance
- Inspired by the need for comprehensive LLM evaluation tools
- Community contributors and testers