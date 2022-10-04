import os

from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# app.jinja_env.filters["usd"] = usd

db = SQL("sqlite:///prayer.db")


@app.route("/")
def index():
  row = db.execute("SELECT * FROM times WHERE ")
  return render_template("index.html")
