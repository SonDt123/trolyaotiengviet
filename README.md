# trolyaotiengviet
install packet
import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
import pyautogui
import urllib.request as urllib2
from random import choice #phần random ngẫu nhiên một câu nói
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#Đóng gói ứng dụng
$ py2applet --make-setup MyApplication.py
#Wrote setup.py
$ python setup.py py2app -A
