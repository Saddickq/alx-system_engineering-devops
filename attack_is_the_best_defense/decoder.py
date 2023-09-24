#!/usr/bin/python3
""" A python script that decodes base64 """
import base64


encoded_string = "bXlwYXNzd29yZDk4OTgh"
decoded_bytes = base64.b64decode(encoded_string)
string = decoded_bytes.decode("utf-8")

with open("0-sniffing", mode="w", encoding="utf-8") as my_file:
    my_file.write(string)
