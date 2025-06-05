# LLMチャットツール ディレクトリ構成

## 全体構成（モノレポ構成）

```
llm-chat-platform/
├── README.md
├── .gitignore
├── .env.example
├── docker-compose.yml
├── docker-compose.prod.yml
├── Makefile
├── package.json                    # ルートレベルのスクリプト管理
├── .github/                        # GitHub Actions CI/CD
│   ├── workflows/
│   │   ├── frontend-ci.yml
│   │   ├── backend-ci.yml
│   │   ├── e2e-tests.yml
│   │   └── deploy-azure.yml
│   └── ISSUE_TEMPLATE/
├── docs/                           # プロジェクト関連ドキュメント
│   ├── api/                       # API仕様書
│   ├── architecture/              # アーキテクチャ設計書
│   ├── deployment/                # デプロイメント手順
│   └── user-guide/               # ユーザーガイド
├── scripts/                       # 開発・運用スクリプト
│   ├── setup/                     # 環境セットアップ
│   ├── migration/                 # データベースマイグレーション
│   ├── backup/                    # バックアップスクリプト
│   └── monitoring/               # 監視スクリプト
├── infrastructure/                # Azure Infrastructure as Code
│   ├── terraform/                # Terraform設定
│   ├── bicep/                    # Azure Bicep テンプレート
│   ├── kubernetes/               # K8sマニフェスト
│   └── helm/                     # Helmチャート
├── frontend/                      # React/TypeScript フロントエンド
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── .eslintrc.js
│   ├── .prettierrc
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── manifest.json
│   ├── src/
│   │   ├── main.tsx               # アプリケーションエントリーポイント
│   │   ├── App.tsx               # メインアプリコンポーネント
│   │   ├── types/                # TypeScript型定義
│   │   │   ├── api.ts           # APIレスポンス型
│   │   │   ├── chat.ts          # チャット関連型
│   │   │   ├── user.ts          # ユーザー関連型
│   │   │   ├── llm.ts           # LLM関連型
│   │   │   └── dashboard.ts     # ダッシュボード関連型
│   │   ├── components/           # 再利用可能なコンポーネント
│   │   │   ├── common/          # 汎用コンポーネント
│   │   │   │   ├── Button/
│   │   │   │   ├── Modal/
│   │   │   │   ├── LoadingSpinner/
│   │   │   │   ├── ErrorBoundary/
│   │   │   │   └── Layout/
│   │   │   ├── chat/            # チャット関連コンポーネント
│   │   │   │   ├── ChatInterface/
│   │   │   │   ├── MessageList/
│   │   │   │   ├── MessageInput/
│   │   │   │   ├── LLMResponseCard/
│   │   │   │   ├── ModelSelector/
│   │   │   │   └── ResponseComparison/
│   │   │   ├── dashboard/       # ダッシュボードコンポーネント
│   │   │   │   ├── StatisticsPanel/
│   │   │   │   ├── UsageChart/
│   │   │   │   ├── EvaluationMetrics/
│   │   │   │   ├── CostAnalysis/
│   │   │   │   └── PerformanceGraph/
│   │   │   ├── evaluation/      # 評価関連コンポーネント
│   │   │   │   ├── RatingWidget/
│   │   │   │   ├── FeedbackForm/
│   │   │   │   ├── ComparisonTool/
│   │   │   │   └── EvaluationHistory/
│   │   │   ├── usecase/         # ユースケース管理コンポーネント
│   │   │   │   ├── UseCaseEditor/
│   │   │   │   ├── UseCaseList/
│   │   │   │   ├── TemplateManager/
│   │   │   │   ├── ScheduleConfig/
│   │   │   │   └── ResultsViewer/
│   │   │   └── auth/            # 認証関連コンポーネント
│   │   │       ├── LoginForm/
│   │   │       ├── RegisterForm/
│   │   │       ├── UserProfile/
│   │   │       └── ApiKeyManager/
│   │   ├── pages/               # ページコンポーネント
│   │   │   ├── HomePage/
│   │   │   ├── ChatPage/
│   │   │   ├── DashboardPage/
│   │   │   ├── EvaluationPage/
│   │   │   ├── UseCasePage/
│   │   │   ├── SettingsPage/
│   │   │   ├── LoginPage/
│   │   │   └── AdminPage/       # 将来の管理機能
│   │   ├── hooks/               # カスタムフック
│   │   │   ├── useAuth.ts
│   │   │   ├── useChat.ts
│   │   │   ├── useLLM.ts
│   │   │   ├── useWebSocket.ts
│   │   │   ├── useEvaluation.ts
│   │   │   └── useLocalStorage.ts
│   │   ├── services/            # API通信・外部サービス
│   │   │   ├── api/
│   │   │   │   ├── client.ts    # APIクライアント基盤
│   │   │   │   ├── auth.ts      # 認証API
│   │   │   │   ├── chat.ts      # チャットAPI
│   │   │   │   ├── llm.ts       # LLM API
│   │   │   │   ├── evaluation.ts # 評価API
│   │   │   │   ├── dashboard.ts # ダッシュボードAPI
│   │   │   │   └── usecase.ts   # ユースケースAPI
│   │   │   ├── websocket/
│   │   │   │   ├── client.ts
│   │   │   │   └── handlers.ts
│   │   │   └── storage/
│   │   │       ├── localStorage.ts
│   │   │       └── sessionStorage.ts
│   │   ├── store/               # 状態管理（Redux Toolkit）
│   │   │   ├── index.ts         # ストア設定
│   │   │   ├── slices/
│   │   │   │   ├── authSlice.ts
│   │   │   │   ├── chatSlice.ts
│   │   │   │   ├── llmSlice.ts
│   │   │   │   ├── evaluationSlice.ts
│   │   │   │   ├── dashboardSlice.ts
│   │   │   │   └── uiSlice.ts
│   │   │   └── middleware/
│   │   │       ├── authMiddleware.ts
│   │   │       └── persistMiddleware.ts
│   │   ├── utils/               # ユーティリティ関数
│   │   │   ├── constants.ts
│   │   │   ├── helpers.ts
│   │   │   ├── formatters.ts
│   │   │   ├── validators.ts
│   │   │   ├── dateUtils.ts
│   │   │   └── analytics.ts
│   │   ├── styles/              # スタイル定義
│   │   │   ├── globals.css
│   │   │   ├── components.css
│   │   │   └── themes/
│   │   │       ├── default.ts
│   │   │       └── dark.ts
│   │   └── __tests__/           # フロントエンドテスト
│   │       ├── components/
│   │       ├── pages/
│   │       ├── hooks/
│   │       ├── services/
│   │       └── utils/
│   ├── public/
│   └── dist/                    # ビルド出力
├── backend/                     # Python/FastAPI バックエンド
│   ├── pyproject.toml          # Poetry設定
│   ├── poetry.lock
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── alembic.ini             # データベースマイグレーション設定
│   ├── src/
│   │   ├── main.py             # FastAPIアプリケーションエントリーポイント
│   │   ├── config/             # 設定管理
│   │   │   ├── __init__.py
│   │   │   ├── settings.py     # アプリケーション設定
│   │   │   ├── database.py     # データベース設定
│   │   │   ├── redis.py        # Redis設定
│   │   │   └── logging.py      # ログ設定
│   │   ├── core/               # コア機能
│   │   │   ├── __init__.py
│   │   │   ├── security.py     # セキュリティ機能
│   │   │   ├── deps.py         # 依存性注入
│   │   │   ├── exceptions.py   # カスタム例外
│   │   │   └── middleware.py   # カスタムミドルウェア
│   │   ├── models/             # データベースモデル（SQLAlchemy）
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── user.py
│   │   │   ├── chat.py
│   │   │   ├── message.py
│   │   │   ├── evaluation.py
│   │   │   ├── usecase.py
│   │   │   └── audit.py        # 監査ログ
│   │   ├── schemas/            # Pydanticスキーマ
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── chat.py
│   │   │   ├── message.py
│   │   │   ├── llm.py
│   │   │   ├── evaluation.py
│   │   │   ├── dashboard.py
│   │   │   └── usecase.py
│   │   ├── api/                # APIルーター
│   │   │   ├── __init__.py
│   │   │   ├── deps.py         # API依存性
│   │   │   ├── v1/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py     # 認証エンドポイント
│   │   │   │   ├── chat.py     # チャットエンドポイント
│   │   │   │   ├── llm.py      # LLMエンドポイント
│   │   │   │   ├── evaluation.py # 評価エンドポイント
│   │   │   │   ├── dashboard.py # ダッシュボードエンドポイント
│   │   │   │   ├── usecase.py  # ユースケースエンドポイント
│   │   │   │   └── admin.py    # 管理機能エンドポイント
│   │   │   └── websocket/      # WebSocketエンドポイント
│   │   │       ├── __init__.py
│   │   │       ├── chat.py
│   │   │       └── notifications.py
│   │   ├── services/           # ビジネスロジック
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── chat_service.py
│   │   │   ├── llm/            # LLM関連サービス
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py     # LLMプロバイダー基底クラス
│   │   │   │   ├── openai_service.py
│   │   │   │   ├── google_service.py
│   │   │   │   ├── anthropic_service.py
│   │   │   │   ├── coordinator.py # マルチLLM調整
│   │   │   │   └── rate_limiter.py
│   │   │   ├── evaluation/     # 評価関連サービス
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user_evaluation.py
│   │   │   │   ├── auto_evaluation.py
│   │   │   │   ├── metrics.py
│   │   │   │   └── comparison.py
│   │   │   ├── dashboard/      # ダッシュボードサービス
│   │   │   │   ├── __init__.py
│   │   │   │   ├── statistics.py
│   │   │   │   ├── analytics.py
│   │   │   │   └── reporting.py
│   │   │   ├── usecase/        # ユースケース管理サービス
│   │   │   │   ├── __init__.py
│   │   │   │   ├── manager.py
│   │   │   │   ├── executor.py
│   │   │   │   ├── scheduler.py
│   │   │   │   └── template.py
│   │   │   └── notification/   # 通知サービス
│   │   │       ├── __init__.py
│   │   │       ├── email.py
│   │   │       ├── webhook.py
│   │   │       └── realtime.py
│   │   ├── utils/              # ユーティリティ
│   │   │   ├── __init__.py
│   │   │   ├── helpers.py
│   │   │   ├── validators.py
│   │   │   ├── formatters.py
│   │   │   ├── crypto.py       # 暗号化機能
│   │   │   ├── cache.py        # キャッシュ機能
│   │   │   └── monitoring.py   # 監視機能
│   │   ├── tasks/              # バックグラウンドタスク（Celery）
│   │   │   ├── __init__.py
│   │   │   ├── celery_app.py
│   │   │   ├── chat_tasks.py
│   │   │   ├── evaluation_tasks.py
│   │   │   ├── usecase_tasks.py
│   │   │   ├── report_tasks.py
│   │   │   └── cleanup_tasks.py
│   │   └── db/                 # データベース関連
│   │       ├── __init__.py
│   │       ├── session.py      # セッション管理
│   │       ├── migrations/     # Alembicマイグレーション
│   │       └── seeds/          # 初期データ
│   ├── tests/                  # バックエンドテスト
│   │   ├── __init__.py
│   │   ├── conftest.py        # pytest設定
│   │   ├── unit/              # ユニットテスト
│   │   │   ├── test_services/
│   │   │   ├── test_models/
│   │   │   └── test_utils/
│   │   ├── integration/       # 統合テスト
│   │   │   ├── test_api/
│   │   │   ├── test_llm/
│   │   │   └── test_database/
│   │   └── e2e/              # E2Eテスト
│   │       ├── test_chat_flow/
│   │       └── test_evaluation_flow/
│   └── logs/                  # ログファイル
├── shared/                    # フロントエンドとバックエンドで共有するファイル
│   ├── types/                 # 共通型定義
│   │   ├── api.ts
│   │   ├── entities.ts
│   │   └── constants.ts
│   ├── schemas/              # APIスキーマ（OpenAPI）
│   │   ├── openapi.json
│   │   └── postman/          # Postmanコレクション
│   └── docs/                 # 共通ドキュメント
├── monitoring/               # 監視・運用関連
│   ├── prometheus/           # Prometheus設定
│   │   ├── prometheus.yml
│   │   └── rules/
│   ├── grafana/             # Grafana設定
│   │   ├── dashboards/
│   │   └── provisioning/
│   ├── loki/               # ログ集約
│   │   └── config.yml
│   └── alerts/             # アラート設定
│       ├── slack.yml
│       └── email.yml
├── data/                   # 開発・テスト用データ
│   ├── fixtures/          # テストフィクスチャ
│   ├── migrations/        # データマイグレーション
│   └── backups/          # バックアップファイル
├── tools/                 # 開発ツール
│   ├── code-generators/   # コード生成ツール
│   │   ├── api-generator.py
│   │   └── component-generator.js
│   ├── validators/        # 各種バリデーター
│   │   ├── api-validator.py
│   │   └── schema-validator.js
│   └── performance/       # パフォーマンステスト
│       ├── load-test/
│       └── stress-test/
└── security/             # セキュリティ関連
    ├── ssl/              # SSL証明書
    ├── secrets/          # シークレット管理（Git管理外）
    └── compliance/       # コンプライアンス文書
        ├── gdpr/
        ├── security-audit/
        └── penetration-test/
```

## 主要ディレクトリの説明

### フロントエンド（/frontend）
- **components/**: 機能別に分類された再利用可能なコンポーネント
- **pages/**: ルーティングに対応するページコンポーネント
- **services/**: API通信、WebSocket、ストレージなどの外部サービス
- **store/**: Redux Toolkit による状態管理
- **hooks/**: カスタムフック（ビジネスロジックの抽象化）

### バックエンド（/backend）
- **api/**: APIエンドポイントの定義（バージョニング対応）
- **services/**: ビジネスロジックの実装（LLM、評価、ダッシュボード等）
- **models/**: SQLAlchemyデータベースモデル
- **schemas/**: Pydanticスキーマ（API入出力の型定義）
- **tasks/**: Celeryバックグラウンドタスク

### 拡張性を考慮した設計

#### LLMプロバイダー拡張
- `/backend/src/services/llm/`に新しいプロバイダークラスを追加
- 基底クラス（`base.py`）を継承することで統一インターフェース

#### 新機能追加時の拡張ポイント
- **新しいページ**: `/frontend/src/pages/`に追加
- **新しいAPI**: `/backend/src/api/v1/`に追加
- **新しいサービス**: `/backend/src/services/`に追加
- **新しいバックグラウンド処理**: `/backend/src/tasks/`に追加

#### 将来の機能拡張例
- **AI エージェント機能**: `/backend/src/services/agent/`
- **多言語対応**: `/shared/i18n/`
- **プラグインシステム**: `/plugins/`
- **API v2**: `/backend/src/api/v2/`

## 開発環境の起動コマンド例

### 開発環境セットアップ
```bash
# 依存関係インストール
make install

# データベースセットアップ
make db-setup

# 開発サーバー起動
make dev

# テスト実行
make test

# フォーマット・リント
make format
make lint
```

この構成により、機能の拡張や新しい技術の導入が容易になり、チーム開発での保守性も向上します。