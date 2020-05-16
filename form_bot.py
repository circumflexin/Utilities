#! usr/bin/env python2
import csv, time, os
import fileinput, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

driver = webdriver.Firefox()


def find_by_xpath(locator):
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, locator))
	)

	return element

class FormPage(object):
	def fill_form(self, data):
		find_by_xpath('//input[@id = ""]').click()
		find_by_xpath('//input[@name = "name"]').send_keys(data['user[name]'])
		find_by_xpath('//input[@name = "email"]').send_keys(data['user[email]'])
		find_by_xpath('//input[@name = "postcode"]').send_keys(data['user[postcode]'])


		return self # makes it so you can call .submit() after calling this function

	def submit(self):
		find_by_xpath('//input[@name = "move:next"]').click()


with open ('users.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	c = 0
	for row in reader:
		driver.get("insert web form address")
		data = {}
		data ['user[name]'] = row[0] + " " + row[1]
		data ['user[email]'] = row[2]
		data ['user[postcode]'] = row[6]
		try:
			FormPage().fill_form(data).submit()
			find_by_xpath('//input[@name = "move:next"]').click()
			driver.quit() # closes the webbrowser
			c += 1
			f = open('bot_log.txt', 'a')
			f.write("\n")
			f.write(data['user[email]'])
			break
		except UnicodeDecodeError:
			with open ('skipped.txt', 'wb') as f:
				f.write("\n")
				f.write(data['user[email]'])
			break

display.stop()


with open('users.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	with open('tempfile.csv', 'wb') as csvfile:
		w = csv.writer(csvfile)
		for row in reader:
			w.writerow(row)
os.rename('tempfile.csv', 'petition.csv')
