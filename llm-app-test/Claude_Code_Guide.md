# LLMチャットプラットフォーム - Claude Code開発ガイド

## プロジェクト概要

### 目的
複数のLLMプロバイダー（OpenAI、Google、Anthropic）に同時にクエリを送信し、結果を比較・評価できるチャットツールの開発

### 主要機能
- **マルチLLMチャット**: 複数のLLMに同時クエリ送信と結果比較
- **評価システム**: ユーザー評価と自動評価による品質分析
- **ダッシュボード**: 統計情報と利用状況の可視化
- **ユースケース管理**: 定期実行可能なテストケース管理

## 技術スタック

### フロントエンド
- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **UI**: Tailwind CSS + Material-UI
- **State Management**: Redux Toolkit
- **HTTP Client**: Axios
- **WebSocket**: Socket.io

### バックエンド
- **Framework**: FastAPI + Python 3.9+
- **Database**: PostgreSQL + SQLAlchemy
- **Cache**: Redis
- **Task Queue**: Celery
- **Migration**: Alembic

### インフラ（Azure）
- **Frontend**: Azure Static Web Apps
- **Backend**: Azure Container Instances / AKS
- **Database**: Azure Database for PostgreSQL
- **Cache**: Azure Cache for Redis
- **Monitoring**: Azure Application Insights

## プロジェクト構成

```
llm-chat-platform/
├── frontend/              # React TypeScript
├── backend/              # FastAPI Python
├── infrastructure/       # Azure IaC
├── docs/                # Documentation
├── scripts/             # Dev/Ops scripts
└── shared/              # Shared resources
```

### フロントエンド構成
```
frontend/
├── src/
│   ├── components/      # 再利用可能コンポーネント
│   │   ├── chat/       # チャット関連
│   │   ├── dashboard/  # ダッシュボード
│   │   ├── evaluation/ # 評価機能
│   │   └── common/     # 汎用コンポーネント
│   ├── pages/          # ページコンポーネント
│   ├── hooks/          # カスタムフック
│   ├── services/       # API通信
│   ├── store/          # Redux状態管理
│   └── types/          # TypeScript型定義
```

### バックエンド構成
```
backend/src/
├── api/                # APIエンドポイント
│   └── v1/            # API v1
├── services/          # ビジネスロジック
│   ├── llm/          # LLM統合
│   ├── evaluation/   # 評価機能
│   ├── dashboard/    # 分析機能
│   └── usecase/      # ユースケース管理
├── models/           # SQLAlchemyモデル
├── schemas/          # Pydanticスキーマ
├── tasks/            # Celeryタスク
└── utils/            # ユーティリティ
```

## Claude Code セットアップ手順

### 1. プロジェクト初期化

```bash
# プロジェクトディレクトリ作成
mkdir llm-chat-platform && cd llm-chat-platform

# Git初期化
git init
```

**Claude Code コマンド:**
```bash
claude-code "Initialize a monorepo structure for a full-stack LLM chat platform with the following requirements:
- Frontend: React TypeScript with Vite, Tailwind CSS, Redux Toolkit
- Backend: FastAPI with Poetry, SQLAlchemy, Alembic
- Development tools: ESLint, Prettier, pytest
- Docker support for development and production
- GitHub Actions CI/CD setup
- Create package.json with workspace configuration
- Create basic directory structure as specified in the project layout"
```

### 2. 基盤環境構築

#### フロントエンド初期化
```bash
claude-code "Setup React TypeScript project in frontend/ directory with:
- Vite configuration
- Tailwind CSS integration
- Redux Toolkit store setup
- Axios HTTP client configuration
- Socket.io client setup
- ESLint and Prettier configuration
- Basic routing with React Router
- Material-UI integration
- Environment variables setup (.env.example)"
```

#### バックエンド初期化
```bash
claude-code "Setup FastAPI project in backend/ directory with:
- Poetry dependency management (pyproject.toml)
- SQLAlchemy database models
- Alembic migration setup
- Pydantic schemas for API validation
- JWT authentication system
- CORS middleware configuration
- Environment configuration with Pydantic Settings
- Database connection pool setup
- Redis client configuration
- Celery task queue setup
- pytest configuration with fixtures"
```

### 3. 開発環境設定

#### Docker環境
```bash
claude-code "Create Docker development environment with:
- Multi-stage Dockerfile for frontend (Node.js build + nginx serve)
- Multi-stage Dockerfile for backend (Python with Poetry)
- docker-compose.yml for development with:
  - PostgreSQL database
  - Redis cache
  - Frontend hot reload
  - Backend auto-reload
  - Shared volumes for development
- docker-compose.prod.yml for production deployment
- .dockerignore files for optimization"
```

#### 開発ツール設定
```bash
claude-code "Create development automation with:
- Makefile with commands for install, dev, test, build, lint, format
- package.json scripts for monorepo management
- Pre-commit hooks for code quality
- VS Code workspace configuration
- GitHub Actions workflows for CI/CD:
  - Frontend tests and build
  - Backend tests and lint
  - E2E tests with Playwright
  - Azure deployment pipeline"
```

## コア機能実装

### 1. 認証システム

```bash
claude-code "Implement JWT authentication system with:

Backend (FastAPI):
- User model with SQLAlchemy (id, email, hashed_password, api_keys, settings)
- JWT token generation and validation
- Password hashing with bcrypt
- OAuth2 scheme implementation
- API endpoints: /auth/register, /auth/login, /auth/me, /auth/refresh
- Dependency injection for authenticated routes
- API key encryption for LLM providers

Frontend (React):
- Authentication context and provider
- Login/Register forms with validation
- Protected route wrapper component
- Token storage and automatic refresh
- API key management interface
- Logout functionality with token cleanup"
```

### 2. チャット機能基盤

```bash
claude-code "Implement chat system foundation with:

Backend:
- Chat session model (id, user_id, title, tags, created_at)
- Message model (id, session_id, content, type, responses, timestamp)
- WebSocket connection manager for real-time chat
- Chat service for session management
- API endpoints for chat CRUD operations

Frontend:
- Chat interface layout with sidebar and main area
- WebSocket hook for real-time messaging
- Chat session list component
- Message list with auto-scroll
- Message input with send functionality
- Chat history persistence in Redux store"
```

### 3. LLM統合サービス

```bash
claude-code "Create LLM integration layer with:

Backend:
- Base LLM provider abstract class with standard interface
- OpenAI service implementation with GPT-4/3.5 support
- Google service implementation with Gemini/PaLM support  
- Anthropic service implementation with Claude models
- LLM coordinator for parallel requests
- Rate limiting and error handling
- Response time and token usage tracking
- Cost calculation for each provider

Key features:
- Async/await pattern for parallel processing
- Retry mechanism with exponential backoff
- Streaming response support
- Model parameter configuration (temperature, max_tokens)
- API quota monitoring and alerts"
```

### 4. 評価システム

```bash
claude-code "Implement evaluation system with:

Backend:
- Evaluation model for storing user ratings and feedback
- Auto-evaluation service for response analysis:
  - Response time metrics
  - Token efficiency calculation
  - Response length analysis
  - Similarity comparison between LLM responses
- Evaluation aggregation and statistics
- API endpoints for rating submission and statistics

Frontend:
- Rating widget component (1-5 stars for multiple criteria)
- Feedback form for detailed comments
- Response comparison interface
- Evaluation history viewer
- Statistics dashboard with charts"
```

### 5. ダッシュボード機能

```bash
claude-code "Create analytics dashboard with:

Backend:
- Statistics service for data aggregation
- Analytics queries for:
  - Usage statistics by model and time period
  - Cost analysis and optimization suggestions
  - Response time trends
  - User evaluation summaries
  - Error rate monitoring
- Report generation service
- Data export functionality

Frontend:
- Dashboard layout with grid system
- Chart components using Recharts:
  - Usage timeline charts
  - Model comparison charts
  - Cost breakdown pie charts
  - Performance metrics gauges
- Filter controls for date range and model selection
- Export functionality for reports"
```

### 6. ユースケース管理

```bash
claude-code "Implement use case management system with:

Backend:
- UseCase model (id, name, description, prompt_template, expected_output, schedule)
- Template engine for dynamic prompt generation
- Scheduler service using Celery for automated execution
- Results tracking and comparison over time
- Batch execution for multiple use cases

Frontend:
- Use case editor with rich text prompt editing
- Template variable management
- Schedule configuration interface
- Results viewer with timeline
- Comparison tools for tracking performance changes
- Import/export functionality for use case libraries"
```

## 開発フロー

### 1. 機能開発サイクル

```bash
# 1. 新機能ブランチ作成
git checkout -b feature/new-feature

# 2. Claude Codeで実装
claude-code "Implement [specific feature] following the existing patterns"

# 3. テスト実行
make test

# 4. コード品質チェック
make lint && make format

# 5. プルリクエスト作成
```

### 2. デバッグとトラブルシューティング

```bash
claude-code "Debug the following issue in the [component/service]:
[Error description or unexpected behavior]

Please:
1. Analyze the error logs
2. Identify potential root causes
3. Provide fix recommendations
4. Add appropriate error handling
5. Include unit tests for the fix"
```

### 3. パフォーマンス最適化

```bash
claude-code "Optimize performance for [specific component/endpoint]:
- Analyze current bottlenecks
- Implement caching strategies
- Add database query optimization
- Reduce API response times
- Add performance monitoring
- Create benchmarks for comparison"
```

## デプロイメント

### Azure環境構築

```bash
claude-code "Create Azure infrastructure as code using Terraform:
- Resource group for the application
- Azure Database for PostgreSQL with backup configuration
- Azure Cache for Redis
- Azure Container Registry
- Azure Kubernetes Service or Container Instances
- Azure Application Gateway with SSL termination
- Azure Key Vault for secrets management
- Azure Monitor and Application Insights
- GitHub Actions deployment pipeline with proper environment variables"
```

### 本番環境設定

```bash
claude-code "Configure production deployment with:
- Environment-specific configuration management
- Database migration pipeline
- Blue-green deployment strategy
- Health check endpoints
- Monitoring and alerting setup
- Backup and disaster recovery procedures
- Security hardening (HTTPS, CORS, rate limiting)
- Performance optimization (CDN, caching, compression)"
```

## テスト戦略

### 自動テスト実装

```bash
claude-code "Implement comprehensive testing strategy:

Backend Tests:
- Unit tests for all services using pytest
- Integration tests for API endpoints
- Database tests with test fixtures
- Mock tests for external LLM APIs
- Performance tests for concurrent requests

Frontend Tests:
- Unit tests for components using Jest/React Testing Library
- Integration tests for user flows
- Mock service worker for API testing
- Accessibility tests
- Visual regression tests

E2E Tests:
- Critical user journey tests with Playwright
- Cross-browser compatibility tests
- Performance testing under load
- Security testing for authentication flows"
```

## 運用・監視

### ログとモニタリング

```bash
claude-code "Implement production monitoring with:
- Structured logging with correlation IDs
- Application metrics collection
- Error tracking and alerting
- Performance monitoring dashboards
- User analytics and usage patterns
- Security audit logging
- Cost monitoring and optimization alerts
- SLA monitoring and reporting"
```

## セキュリティ

### セキュリティ実装

```bash
claude-code "Implement security best practices:
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- CSRF protection
- Rate limiting and DDoS protection
- API key rotation mechanism
- Data encryption at rest and in transit
- Security headers configuration
- Vulnerability scanning integration
- Compliance documentation (GDPR, privacy policies)"
```

## 拡張計画

### 将来機能の準備

```bash
claude-code "Prepare architecture for future enhancements:
- Plugin system for custom LLM providers
- Multi-language support (i18n)
- Advanced AI agent capabilities
- Real-time collaboration features
- Mobile app API readiness
- Enterprise features (SSO, RBAC, audit trails)
- API versioning strategy
- Microservices migration path"
```

## 開発開始コマンド

実際に開発を開始する際は、以下の順序でClaude Codeコマンドを実行してください：

```bash
# 1. プロジェクト初期化
claude-code [プロジェクト初期化コマンド]

# 2. 開発環境構築
claude-code [フロントエンド初期化コマンド]
claude-code [バックエンド初期化コマンド]
claude-code [Docker環境コマンド]

# 3. 認証システム実装
claude-code [認証システムコマンド]

# 4. チャット基盤実装
claude-code [チャット機能基盤コマンド]

# 5. LLM統合
claude-code [LLM統合サービスコマンド]

# 以降、機能を順次追加
```

このガイドに従って開発を進めることで、スケーラブルで保守性の高いLLMチャットプラットフォームを効率的に構築できます。