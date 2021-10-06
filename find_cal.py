# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:14:12 2021
@author: Alec Burslem
"""

import xml.etree.ElementTree as ET
from pathlib import Path

check_id = "DX330C"

cal_dir = "C:\\Users\\Alec Burslem\\OneDrive - University of St Andrews\\Utilities\\test"
cal_list = Path(cal_dir).glob('**/*.xml')

for cal in cal_list:
	tree = ET.parse(cal)
	root = tree.getroot()
	ID = root.find('ID').text
	name = root.find('NAME').text
	if check_id == ID:
		print(name)
	elif check_id == name:
		print(ID)
