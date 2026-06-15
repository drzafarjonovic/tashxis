-- Tashxis bot — Supabase Postgres sxemasi (v1.1)
-- Bot ishga tushganda avtomatik bajariladi (idempotent).
-- Qo'lda qo'llash uchun: Supabase Dashboard → SQL Editor → bu faylni ishga tushiring.

CREATE TABLE IF NOT EXISTS bot_users (
    telegram_id BIGINT PRIMARY KEY,
    lang        TEXT        NOT NULL DEFAULT 'uz',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_seen   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS diagnoses (
    id           BIGSERIAL   PRIMARY KEY,
    telegram_id  BIGINT      NOT NULL REFERENCES bot_users(telegram_id) ON DELETE CASCADE,
    lang         TEXT        NOT NULL DEFAULT 'uz',
    category     TEXT        NOT NULL,
    disease_id   TEXT,
    diagnosis    TEXT,
    confidence   REAL,
    uncertain    BOOLEAN     NOT NULL DEFAULT FALSE,
    symptoms     JSONB       NOT NULL DEFAULT '{}'::jsonb,
    alternatives JSONB       NOT NULL DEFAULT '[]'::jsonb,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_diagnoses_telegram_id ON diagnoses(telegram_id);
CREATE INDEX IF NOT EXISTS idx_diagnoses_created_at  ON diagnoses(created_at);
CREATE INDEX IF NOT EXISTS idx_diagnoses_disease_id  ON diagnoses(disease_id);
