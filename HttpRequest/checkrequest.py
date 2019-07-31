# importing the requests library
import time,re,sys
import requests,schedule



def query_metrics():
	try:

		f = open(str(time.time()), "a")

		URL = "http://127.0.0.1:9797/metrics"



		# sending get request and saving the response as response object
		r = requests.get(url = URL)

		data=r.text

		f.write(data)
		f.close()

	except Exception as e:
		print(e)



schedule.every(1).minute.do(query_metrics)

while True:
	schedule.run_pending()
	#print("waiting")
	time.sleep(1)


