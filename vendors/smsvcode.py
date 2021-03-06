# coding: utf-8
# cython: language_level=3, boundscheck=False

import os
import re
import csv

def get(smsFile, phoneNumber, lastVcode=None, match=None):
    if not os.path.isfile(smsFile):
        return False

    if match == None:
        match = r'\d{5,8}'

    phoneNumberCol = 3
    textCol = 4

    with open(smsFile, 'r') as f:
        reader = list(csv.reader(f))

    flag = False

    for sms in reader[:-3:-1]:
        if sms[phoneNumberCol] != phoneNumber:
            continue

        vcode = re.findall(match, sms[4])
        if vcode:
            if vcode[0] != lastVcode:
                return vcode[0]
            else:
                break

    return None
