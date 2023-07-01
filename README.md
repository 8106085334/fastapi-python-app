# fastapi-python-app
Basic app using fastapi that can perform CRUD operations

**To create a virtual environment for python:**

python3 -m venv env

**Active your env for linux/bash:**

/path/to/venv/bin/activate

**Install dependencies:**

pip3 install fastapi
pip3 install "uvicorn[standard]"

**App in action:**

uvicorn main:app --reload
http://localhost:8000
