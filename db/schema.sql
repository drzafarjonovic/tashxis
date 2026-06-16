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


-- ════════════════════════════════════════════════════════════════
--  V2.0 — Clinical Data Collection Platform
--  Maqsad: real klinik ma'lumot to'plash → priorlarni yangilash →
--  ML modelni o'qitish → kalibrlash zanjiri uchun asos.
-- ════════════════════════════════════════════════════════════════

-- Eski diagnoses jadvaliga demografiya/joylashuv ustunlarini qo'shish
ALTER TABLE diagnoses ADD COLUMN IF NOT EXISTS age_group TEXT;
ALTER TABLE diagnoses ADD COLUMN IF NOT EXISTS sex       TEXT;
ALTER TABLE diagnoses ADD COLUMN IF NOT EXISTS location  JSONB NOT NULL DEFAULT '{}'::jsonb;

-- Diagnostik sessiya (bitta to'liq seans)
CREATE TABLE IF NOT EXISTS diagnosis_sessions (
    session_id     BIGSERIAL   PRIMARY KEY,
    telegram_id    BIGINT      REFERENCES bot_users(telegram_id) ON DELETE SET NULL,
    lang           TEXT        NOT NULL DEFAULT 'uz',
    age_group      TEXT,
    sex            TEXT,
    category       TEXT,
    location       JSONB       NOT NULL DEFAULT '{}'::jsonb,
    question_count INTEGER     NOT NULL DEFAULT 0,
    top1_disease   TEXT,
    top1_conf      REAL,
    top2_disease   TEXT,
    top3_disease   TEXT,
    uncertain      BOOLEAN     NOT NULL DEFAULT FALSE,
    started_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at   TIMESTAMPTZ
);

-- Sessiyadagi har bir savol-javob (ML feature extraction uchun)
CREATE TABLE IF NOT EXISTS session_answers (
    id          BIGSERIAL   PRIMARY KEY,
    session_id  BIGINT      NOT NULL REFERENCES diagnosis_sessions(session_id) ON DELETE CASCADE,
    question_id TEXT        NOT NULL,
    answer      BOOLEAN     NOT NULL,
    step        INTEGER,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Shifokor tasdig'i (eng qimmatli ma'lumot — kalibrlash va prior yangilash uchun)
CREATE TABLE IF NOT EXISTS doctor_feedback (
    id              BIGSERIAL   PRIMARY KEY,
    session_id      BIGINT      REFERENCES diagnosis_sessions(session_id) ON DELETE CASCADE,
    final_diagnosis TEXT,
    confirmed       BOOLEAN,
    notes           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Kasallik statistikasi (Self-Learning Prior Update manbai)
CREATE TABLE IF NOT EXISTS disease_statistics (
    disease_id      TEXT        PRIMARY KEY,
    predicted_count BIGINT      NOT NULL DEFAULT 0,
    confirmed_count BIGINT      NOT NULL DEFAULT 0,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- O'rganilgan prior overrides (statik tier'lar ustidan qo'llanadi)
CREATE TABLE IF NOT EXISTS priors (
    disease_id TEXT        PRIMARY KEY,
    multiplier REAL        NOT NULL DEFAULT 1.0,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ML/kalibrovka model versiyalari
CREATE TABLE IF NOT EXISTS model_versions (
    id         BIGSERIAL   PRIMARY KEY,
    kind       TEXT        NOT NULL,      -- 'bayes' | 'ml' | 'calibration'
    version    TEXT        NOT NULL,
    notes      TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_sessions_telegram ON diagnosis_sessions(telegram_id);
CREATE INDEX IF NOT EXISTS idx_sessions_created  ON diagnosis_sessions(started_at);
CREATE INDEX IF NOT EXISTS idx_answers_session   ON session_answers(session_id);
CREATE INDEX IF NOT EXISTS idx_feedback_session  ON doctor_feedback(session_id);
