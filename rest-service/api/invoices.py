from flask import render_template
import base64
from detectPaper import *
import numpy as np

def post(invoice):
    byteString = base64.b64decode(invoice['image'])
    img = np.frombuffer(byteString, np.uint8)

    invoiceImg = detectPaper(img, MODE_MEMORY_BUFFER)
    invoiceImgBase64 = base64.b64encode(invoiceImg[1]).decode('ascii')

    scannedInvoice = {}
    scannedInvoice["id"] = 1
    scannedInvoice["test"] = "blabla"
    scannedInvoice["image"] = invoiceImgBase64

    return scannedInvoice

def get(id) :
    return

def search() :
    return