# importing the requests library
import time,re
import requests,schedule

# api-endpoint
previous_time=0

def query_metrics():
	try:
		global previous_time
		f = open("demofile2.txt", "a")

		URL = "http://127.0.0.1:9797/metrics"

		current_time = time.time()

		# sending get request and saving the response as response object
		r = requests.get(url = URL)

		data=r.text
		data_list=data.split("\n")



		f.write("throughput="+str(float((data_list[2].split(" "))[1])/(current_time-previous_time))+" ")


		#print(data)
		for line in data_list:

			x = re.findall(
				"response_time_seconds(?:_mean|_stdDev|{).*guide:0.0.0.orderMgt.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*",
				line)
			# x=re.findall("response_time_seconds(?:_mean|_stdDev|{).*guide:0.0.0.orderMgt.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"(?:0.999|0.99|)\"|).*", line)
			# x=re.findall("(?:http_response_time_mean{|http_response_time_stdDev|http_response_time_seconds{).*guide:0.0.0.orderMgt.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"(?:0.999|0.99|)\"|).*", line)
			# x=re.findall("^http_response_time_seconds_mean.*|^http_response_time_seconds_max.*", line)
			# x=x[0].split(",} ")
			# y=re.sub("{protocol=\"http\",http_url=\"/ordermgt/order/100500\",service=\"guide:0.0.0.orderMgt$$service$0\",resource=\"findOrder\",http_method=\"GET\",\"","",x[0])
			s = x

			if (s):
				# print(y)
				# print(s[0])
				# print(((s[0].split(" "))[0]),"\n",(s[0].split(" "))[1],"\n\n")
				# print(((s[0].split(" "))[0]).split("{")[0],"\n",(s[0].split(" "))[1],"\n\n")
				y = s[0].split(" ")
				z = y[0].split(
					"{protocol=\"http\",http_url=\"/ordermgt/order/100500\",service=\"guide:0.0.0.orderMgt$$service$0\",resource=\"findOrder\",http_method=\"GET\",")
				# print(z[0],"\n",z[1],"\n",y[1],"\n\n")
				meanOrStd = z[0].split("response_time_seconds")
				timeWindowAndQuantile = z[1].split("\"")

				timeWindow = timeWindowAndQuantile[0] + timeWindowAndQuantile[1]

				f.write(timeWindow+" ")
				print(timeWindow)
				if (meanOrStd[1] == ''):
					quantile = timeWindowAndQuantile[2][1:] + timeWindowAndQuantile[3]
					print(quantile)
					f.write(quantile+" ")
				else:
					print(meanOrStd[1])
					f.write(meanOrStd[1]+" ")

				print(y[1], "\n\n")
				f.write(y[1]+ "\n\n")

		f.close()
		previous_time=current_time
	except Exception as e :
		print(e)



schedule.every(1).minute.do(query_metrics)

while True:
	schedule.run_pending()
	#print("waiting")
	time.sleep(1)


