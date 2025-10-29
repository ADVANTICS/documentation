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
cd products/adb-pc-dc01 && ENABLE_PROD=False mkdocs serve --dev-addr localhost:8000
```

Then, goto http://localhost:8000/adb-pc-dc01

## Windows users

Try the following:
- Install Python

run the following in the terminal (you might need to run it as admin, depending on how you installed your Python)

```
pip install -r requirements.txt
```

Try to run the documentation server (choose a directory that has the product you want to work on)

```
cd products/adb-pc-dc01
mkdocs serve --dev-addr localhost:8000
```

If you get en error like libgobject-2.0-0 not found, install the GTK runtime library:
https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/tag/2022-01-04
And then try again
```
mkdocs serve --dev-addr localhost:8000
```
