"""Setup at app startup"""
from app import routes
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-cgrq7r9mbg5e4khr5ej0-a.oregon-postgres.render.com",
    database="todo_wfs3",
    user="todo_wfs3_user",
    password="igBDB6j71JranM8mFwaH7BXbVd2RokLs")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
