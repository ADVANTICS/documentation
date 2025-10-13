
# product should be the folder name of the product to build
build product:
    cd products/{{product}} && mkdocs build --clean

build-all:
    for dir in $(ls -d products/ | grep -v 'site\|assets'); do \
        cd $$dir && mkdocs build --clean --strict; \
        cd ..; \
    done

serve product:
    cd products/{{product}} && ENABLE_PROD=False mkdocs serve --dev-addr localhost:8000

install:
  uv sync --locked --no-install-project

build-landing:
    cd landing && pnpm run build
