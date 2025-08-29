
build:
    mkdocs build --clean --strict
serve:
    ENABLE_PROD=False mkdocs serve --dev-addr localhost:8000
install:
  uv sync --locked --no-install-project
