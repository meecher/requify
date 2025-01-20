#!include imports in pyscript.toml
#Based on https://pyscript.com/@adec3dd4-c366-46d3-9d45-84d3b0996a43/chatgpt-demo/latest
import js

import os
import csv
import requests
import pandas as pd
from js import Uint8Array, File, URL, document
from datetime import datetime
from pyodide.ffi.wrappers import add_event_listener 
from js import window

import pyodide_http

# Patch the Requests library so it works with Pyscript
pyodide_http.patch_all()


explist = [[1, 0], [2, 0], [3, 1], [4, 0], [5, 1], [6, 0], [7, 0], [8, 1], [9, 0], [10, 0], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 0], [17, 0], [18, 0], [19, 0], [20, 1], [21, 0], [22, 1], [23, 0], [24, 0], [25, 1], [26, 1], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0], [32, 0], [33, 1], [34, 1], [35, 1], [36, 0], [37, 1], [38, 1], [39, 1], [40, 0], [41, 1], [42, 1], [43, 1], [44, 0], [45, 0], [46, 1], [47, 0], [48, 1], [49, 1], [50, 1], [51, 0], [52, 1], [53, 1], [54, 0], [55, 0], [56, 0], [57, 1], [58, 1], [59, 0], [60, 1], [61, 1], [62, 1], [63, 0], [64, 1], [65, 1], [66, 0], [67, 0], [68, 0], [69, 1], [70, 0], [71, 1], [72, 1], [73, 0], [74, 0], [75, 0], [76, 1], [77, 1], [78, 0], [79, 0], [80, 1]]


def send():
    userElement = js.document.getElementById('userInput')
    message = userElement.value
    print(message)

    for i in explist:
        if i[0] == int(message):
            if i[1] == 0:
                window.location.href = "expnormal.html"
            elif i[1] == 1:
                window.location.href = "expai.html"

    
   