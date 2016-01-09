# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from flask import Flask, request, session, redirect, url_for, abort, render_template, jsonify
import sys, os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

app = Flask(__name__)
from config.db import Product


@app.route("/")
def home():
	p = Product.query.all()
	return render_template("index.html",products=p)

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
		