from flask import render_template
import base64
from detectPaper import detectPaper
import numpy as np

def post(invoice):
    byteString = base64.b64decode(invoice['image'])
    img = np.frombuffer(byteString, np.uint8)

    invoiceImg = detectPaper(img)

    scannedInvoice = {}
    scannedInvoice["id"] = 1
    scannedInvoice["test"] = "blabla"
    scannedInvoice["image"] = base64.b64encode(invoiceImg)

    return scannedInvoice

def get(id) :
    return

def search() :
    return