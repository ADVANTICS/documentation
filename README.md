# Advantics documentations

Main documentation site, build out of this repository:

**https://documentation.advantics.fr**

## Local execution

Create a virtual environment and install the requirements.txt.

If you want to use uv:

```
uv venv --python 3.12
uv pip install -r requirements.txt
```

You can choose which product you want to work on and spin up the dev server, for example:

```
cd products/ADB-PC-DC01 && ENABLE_PROD=False mkdocs serve --dev-addr localhost:8000
```

Then, goto http://localhost:8000/ADB-PC-DC01
