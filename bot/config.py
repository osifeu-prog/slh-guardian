import os

# Core
ENV = os.getenv("ENV", "production").lower()
MODE = os.getenv("MODE", "polling").lower()
# Railway deployments historically used TOKEN_GUARDIAN/BOT_TOKEN while the
# Guardian code expected TELEGRAM_TOKEN. Keep one runtime identity.
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN") or os.getenv("TOKEN_GUARDIAN") or os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Admin
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
ADMIN_IDS = os.getenv("ADMIN_IDS")

# Infra
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

# SLH / Wallets (optional)
FOUNDER_WALLET = os.getenv("FOUNDER_WALLET")
TON_WALLET = os.getenv("TON_WALLET")
SLH_TOKEN_ADDRESS = os.getenv("SLH_TOKEN_ADDRESS")
ZUZ_TOKEN_ADDRESS = os.getenv("ZUZ_TOKEN_ADDRESS")

# AI (optional)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Payments (MVP)
DONATE_URL = os.getenv("DONATE_URL")
