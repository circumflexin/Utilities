#!usr/bin/python

def HTML_to_CSV(page, table_class, tags):
	payload = {
	'log' : 'Test',
    'pwd' : ''
	} # authentication info
	with requests.Session() as s:
		p = s.post('insert web adress ', data=payload) # authenicate if necessary
    	r = s.get(page)
    	result = r.text
	# parse html tree and find table, translate HTML table to csv file
	soup = BeautifulSoup(result, "lxml")

	table = soup.find(attrs={"class" : table_class})

	headers = [header.text for header in table.find_all('th')]

	rows = []

	for row in table.find_all('tr'):
		rows.append([val.text.encode('utf8') for val in row.find_all('td')])


	with open('output_file.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(headers)
		writer.writerows(row for row in rows if row)

	with open('output_file.csv','rb') as csvinput:
		with open('appended.csv', 'wb') as csvoutput:
			writer = csv.writer(csvoutput, lineterminator='\n')
			reader = csv.reader(csvinput)

			all = []
			row = next(reader)
			row.append('tag_list')
			all.append(row)

			for row in reader:
				row.append(tags)
				all.append(row)

			writer.writerows(all)

	with open('appended.csv', 'rb') as f:
		encoded = base64.urlsafe_b64encode(f.read())
		return(encoded)