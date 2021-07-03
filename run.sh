#! /usr/bin/bash

echo "installing requirements..."
pip install -r requirements.txt

cd ./todo
echo "migrating database..."
python3 manage.py migrate


echo "running server..."
python3 manage.py runserver