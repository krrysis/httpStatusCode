import csv
import requests

with open('urls.csv', 'r') as url_file, open('output.csv', 'w') as output_file:
    url_reader = csv.reader(url_file)
    output_writer = csv.writer(output_file)
    for row in url_reader:
        url = row[0]
        try:
            response = requests.get(url)
            output_writer.writerow([url, response.status_code])
        except requests.exceptions.RequestException as e:
            output_writer.writerow([url, e])