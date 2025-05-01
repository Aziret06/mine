
# Turistan Backend

## 1. Клонирование репозитория

```bash
git clone https://gitlab.geeks.kg/turistan/turistan_backend.git
```

## 2. Создание виртуальной среды

```bash
python -m venv <name>  # например: python -m venv .venv
```

## 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

## 4. Создание файла `.env` (не для продакшена)

Создайте файл `.env` в корне проекта и вставьте туда следующее:

```env
SECRET_KEY=django-insecure-qpbc%8hmt1)&$k-!c%#p(=9_2*adi-vj9*qm(&^l97rfbqgdhf
DEBUG=True
PROD=False

POSTGRES_DB=touristan
POSTGRES_USER=hotel
POSTGRES_PASSWORD=sudotouristan
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

## 5. Работа с ветками

Создайте ветку с названием вашего таска и перейдите в неё:

```bash
git branch <task-name>
git checkout <task-name>
```

## 6. Обновление вашей ветки с dev

```bash
git rebase dev
```

## 7. Стиль коммитов (Conventional Commit)

Используйте следующие типы коммитов:

- `fix:` — если вы что-то исправили
- `feat:` — если добавили новый функционал
- `refactor:` — если изменили структуру или расположение кода

### Примеры:

```text
fix: fixed api of url about_us
feat: added search for project
refactor: moved model of room ahead of model info
```

Можно использовать комбинированные типы:

```text
fix-feat: fixed and added search feature
fix-refactor: fixed bugs and refactored structure
```