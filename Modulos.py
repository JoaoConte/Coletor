from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
from pathlib import Path
import tkinter as tk
import sqlite3
import webbrowser
import os
import pyodbc
import sys
import cx_Oracle
import babel.numbers
import numpy as np
import pandas as pd



