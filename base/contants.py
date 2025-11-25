# coding=utf-8
import os
import sys
import re
import platform
import datetime

file_path = os.path.abspath(__file__)
path_dir = os.path.dirname(file_path)

CONFIG_PATH = os.path.join(path_dir, '../config')