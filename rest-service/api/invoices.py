from flask import render_template
import base64
from detectPaper import *
import numpy as np
import copy
from pymongo import MongoClient

import json
from bson import json_util

client = MongoClient('localhost', 27017)
db = client['detect-paper-sheet']


def post(invoice):
    byteString = base64.b64decode(invoice['image'])
    img = np.frombuffer(byteString, np.uint8)

    invoiceImg = detectPaper(img, MODE_MEMORY_BUFFER)
    invoiceImgBase64 = base64.b64encode(invoiceImg[1]).decode('ascii')

    scannedInvoice = {}
    scannedInvoice["test"] = "blabla"
    scannedInvoice["image"] = invoiceImgBase64

    db.invoices.insert_one(scannedInvoice)

    #return scannedInvoice
    return json.loads(json.dumps(scannedInvoice, default=json_util.default))
    
def get(id) :
    db.invoices.find_one({'test': 'Bill'})
    return

def search() :
    return