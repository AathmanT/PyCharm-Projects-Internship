import re

# report = """http_response_time_seconds_mean{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",} 0.01171875"""

# importing the requests library
import time, re, sys, os
import requests

# api-endpoint
filter = ""
splitter = ""

previous_time = time.time()
previous_requests = 0

bal_file = "h1_h1_passthrough.balx"

if (bal_file == "h1_transformation.balx"):
    filter = "response_time_seconds(?:_mean|_stdDev|{).*transformationService\$\$service\$0.*timeWindow=\"60000\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*"
    throughput_filter = "http_requests_total_value.*transformationService\$\$service\$0.*"
    splitter = "{protocol=\"http\",http_method=\"POST\",resource=\"transform\",http_url=\"/transform\",service=\"transformationService$$service$0\","
elif (bal_file == "h1_h1_passthrough.balx"):
    filter = "response_time_seconds(?:_mean|_stdDev|{).*passthroughService\$\$service\$0.*timeWindow=\"60000\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*"
    throughput_filter = "http_requests_total_value.*passthroughService\$\$service\$0.*"
    #     splitter = "{protocol=\"http\",http_method=\"POST\",service=\"passthroughService$$service$0\",http_url=\"/passthrough\",http_status_code=\"200\",resource=\"passthrough\","
    splitter = "{protocol=\"http\",http_method=\"POST\",service=\"passthroughService$$service$0\",http_url=\"/passthrough\",resource=\"passthrough\","


# if not (os.path.exists("~/demofile2.txt")):
#     print("Scenario name,timeWindow,type,value" + "\n")

# print(bal_file + "\n")


def query_metrics():
    try:
        global previous_time
        global previous_requests
        global report

        URL = "http://127.0.0.1:9797/metrics"

        current_time = time.time()

        # sending get request and saving the response as response object

        data = report
        data_list = data.split("\n")
        metrics_array = {
            "requests": 0,
            "throughput": 0,
            "mean": 0,
            "std_dev": 0,
            "99per": 0,
        }
        #         print(data)
        for line in data_list:
            try:
                x = re.findall(
                    filter,
                    line)
                #                 print(x)
                throughput = re.findall(throughput_filter, line)
                if (throughput):
                    # f.write(throughput[0]+"\n")

                    current_requests = float((throughput[0].split(" "))[1])
                    #                     print(current_requests , " " , previous_requests)
                    #                     print(current_requests)
                    metrics_array["requests"] = current_requests
                    metrics_array["throughput"] = (current_requests - previous_requests) / (
                                current_time - previous_time)

                    previous_requests = current_requests
                # x=re.findall("response_time_seconds(?:_mean|_stdDev|{).*guide:0.0.0.orderMgt.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"(?:0.999|0.99|)\"|).*", line)
                # x=re.findall("(?:http_response_time_mean{|http_response_time_stdDev|http_response_time_seconds{).*guide:0.0.0.orderMgt.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"(?:0.999|0.99|)\"|).*", line)
                # x=re.findall("^http_response_time_seconds_mean.*|^http_response_time_seconds_max.*", line)
                # x=x[0].split(",} ")
                # y=re.sub("{protocol=\"http\",http_url=\"/ordermgt/order/100500\",service=\"guide:0.0.0.orderMgt$$service$0\",resource=\"findOrder\",http_method=\"GET\",\"","",x[0])
                s = x

                if (s):
                    #                     print(s)
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

                    #                     print(bal_file + "," + timeWindow + ",")
                    # print(timeWindow)
                    if (meanOrStd[1] == ''):
                        quantile = timeWindowAndQuantile[2][1:] + timeWindowAndQuantile[3]
                        # print(quantile)

                        #                         print(quantile + ",")
                        if (timeWindowAndQuantile[3] == "0.99"):
                            metrics_array["99per"] = y[1]

                    elif (meanOrStd[1] == "_mean"):
                        # print(meanOrStd[1])
                        #                         print(meanOrStd[1] + ",")
                        metrics_array["mean"] = y[1]
                    elif (meanOrStd[1] == "_stdDev"):
                        metrics_array["std_dev"] = y[1]
            #                         print(meanOrStd[1] + ",")
            # print(y[1], "\n\n")
            #                     print(y[1] + "\n\n")
            except Exception as e:
                print(e)

        previous_time = current_time

    except Exception as e:
        print(str(e))
    return metrics_array


query_metrics()

