#!/bin/bash

# Setup script for LLM Chat Platform
set -e

echo "🚀 Setting up LLM Chat Platform development environment..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

# Create environment files if they don't exist
if [ ! -f "frontend/.env" ]; then
    echo "📝 Creating frontend .env file..."
    cp frontend/.env.example frontend/.env
fi

if [ ! -f "backend/.env" ]; then
    echo "📝 Creating backend .env file..."
    cp backend/.env.example backend/.env
fi

# Install dependencies
echo "📦 Installing dependencies..."
make install

# Start development environment
echo "🐳 Starting development environment..."
make dev

echo "✅ Setup completed!"
echo ""
echo "🌐 Application URLs:"
echo "  Frontend: http://localhost:3000"
echo "  Backend API: http://localhost:8000"
echo "  API Documentation: http://localhost:8000/docs"
echo ""
echo "🛠️  Useful commands:"
echo "  make help           - Show all available commands"
echo "  make logs           - View application logs"
echo "  make docker-down    - Stop development environment"
echo "  make clean          - Clean up containers and volumes"
echo ""
echo "Happy coding! 🎉"