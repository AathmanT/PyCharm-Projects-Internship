# importing the requests library
import time,re,sys,os
import requests

# api-endpoint
filter=""
splitter=""

previous_time=time.time()
previous_requests=0

# bal_file=sys.argv[1]
bal_file="h1c_h1c_transformation.bal"

if(bal_file=="h1_transformation.balx" or bal_file=="h1c_h1c_transformation.bal"):
	filter="response_time_seconds(?:_mean|_stdDev|{).*transformationService\$\$service\$0.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*"
	throughput_filter="http_requests_total_value.*transformationService\$\$service\$0.*"
	splitter="{protocol=\"http\",http_method=\"POST\",resource=\"transform\",http_url=\"/transform\",service=\"transformationService$$service$0\","
elif(bal_file=="h1_h1_passthrough.balx" or bal_file=="h1_h1_passthrough_new.balx" or bal_file=="h1c_h1c_passthrough_prime.balx"):
	filter = "response_time_seconds(?:_mean|_stdDev|{).*passthroughService\$\$service\$0.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*"
	throughput_filter = "http_requests_total_value.*passthroughService\$\$service\$0.*"
	splitter = "{protocol=\"http\",http_method=\"POST\",service=\"passthroughService$$service$0\",http_url=\"/passthrough\",resource=\"passthrough\","



if not( os.path.exists("~/PycharmProjects/QueryPerfBayesian/demofile2.txt")):
	f = open("demofile2.txt", "a")
	f.write("Scenario name,timeWindow,type,value" + "\n")
	f.close()

f = open("demofile2.txt", "a")
f.write(bal_file+"\n")
f.close()

def query_metrics():

		global previous_time
		global previous_requests
		f = open("demofile2.txt", "a")

		URL = "http://127.0.0.1:9797/metrics"

		current_time = time.time()

		# sending get request and saving the response as response object
		r = requests.get(url = URL)

		data=r.text
		data_list=data.split("\n")
		f.write(data)
		# print(data)
		for line in data_list:
			try:
				x = re.findall(
					filter,
					line)

				throughput = re.findall(throughput_filter, line)
				if(throughput):
					#f.write(throughput[0]+"\n")
					current_requests=float((throughput[0].split(" "))[1])
					f.write(str(current_requests)+" "+str(previous_requests))


					f.write(bal_file+",timeWindow=60000,throughput," + str((current_requests-previous_requests) / (current_time - previous_time)) + "\n")
					previous_requests=current_requests

				s = x

				if (s):
					# print(y)
					# print(s[0])
					# print(((s[0].split(" "))[0]),"\n",(s[0].split(" "))[1],"\n\n")
					# print(((s[0].split(" "))[0]).split("{")[0],"\n",(s[0].split(" "))[1],"\n\n")
					y = s[0].split(" ")
					z = y[0].split(
						splitter)
					# print(z[0],"\n",z[1],"\n",y[1],"\n\n")
					meanOrStd = z[0].split("response_time_seconds")
					timeWindowAndQuantile = z[1].split("\"")

					timeWindow = timeWindowAndQuantile[0] + timeWindowAndQuantile[1]

					f.write(bal_file+","+timeWindow+",")
					#print(timeWindow)
					if (meanOrStd[1] == ''):
						quantile = timeWindowAndQuantile[2][1:] + timeWindowAndQuantile[3]
						#print(quantile)
						f.write(quantile+",")
					else:
						#print(meanOrStd[1])
						f.write(meanOrStd[1]+",")

					#print(y[1], "\n\n")
					f.write(y[1]+ "\n\n")
			except Exception as e:
				print(e)
				f.write(str(e))
				f.write("\n"+line+"\n\n")

		f.close()
		previous_time=current_time


query_metrics()




