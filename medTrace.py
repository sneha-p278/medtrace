import random
from flask import Flask, render_template, request, send_file, redirect, url_for, jsonify
import qrcode
import pyotp
import uuid
import os
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from werkzeug.utils import secure_filename
import re
from cryptography.fernet import Fernet
from pymongo import MongoClient
import smtplib
from PIL import Image, ImageDraw

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
