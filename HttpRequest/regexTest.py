import re

str = """# HELP http_requests_total_value Total number of requests
# TYPE http_requests_total_value counter
http_requests_total_value{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",} 1.0
# TYPE ballerina_scheduler_waiting_for_lock_worker_count_value gauge
ballerina_scheduler_waiting_for_lock_worker_count_value 0.0
# HELP http_response_time_seconds_value Response Time
# TYPE http_response_time_seconds_value gauge
http_response_time_seconds_value{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",} 0.016575984
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 60000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",} 0.0164794921875
http_response_time_seconds_max{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",} 0.0164794921875
http_response_time_seconds_min{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",} 0.0164794921875
http_response_time_seconds_stdDev{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",} 0.0
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",quantile="0.33",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",quantile="0.5",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",quantile="0.66",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",quantile="0.99",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="60000",quantile="0.999",} 0.0164794921875
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 300000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",} 0.0164794921875
http_response_time_seconds_max{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",} 0.0164794921875
http_response_time_seconds_min{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",} 0.0164794921875
http_response_time_seconds_stdDev{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",} 0.0
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",quantile="0.33",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",quantile="0.5",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",quantile="0.66",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",quantile="0.99",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="300000",quantile="0.999",} 0.0164794921875
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 900000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",} 0.0164794921875
http_response_time_seconds_max{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",} 0.0164794921875
http_response_time_seconds_min{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",} 0.0164794921875
http_response_time_seconds_stdDev{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",} 0.0
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",quantile="0.33",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",quantile="0.5",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",quantile="0.66",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",quantile="0.99",} 0.0164794921875
http_response_time_seconds{protocol="http",http_url="/ordermgt/order/100500",service="guide:0.0.0.orderMgt$$service$0",resource="findOrder",http_method="GET",timeWindow="900000",quantile="0.999",} 0.0164794921875
# HELP ballerina_http:Caller_requests_total_value Total number of requests
# TYPE ballerina_http:Caller_requests_total_value counter
ballerina_http:Caller_requests_total_value{action="respond",http_status_code="200",} 2.0
# HELP http_inprogress_requests_value Inprogress Requests
# TYPE http_inprogress_requests_value gauge
http_inprogress_requests_value{resource="getMetrics",service="PrometheusReporter$$service$0",} 1.0
# HELP ballerina_http:Caller_response_time_seconds_value Response Time
# TYPE ballerina_http:Caller_response_time_seconds_value gauge
ballerina_http:Caller_response_time_seconds_value{action="respond",http_status_code="200",} 0.011706883
# HELP ballerina_http:Caller_response_time_seconds A Summary of ballerina_http:Caller_response_time_seconds for window of 60000
# TYPE ballerina_http:Caller_response_time_seconds summary
ballerina_http:Caller_response_time_seconds_mean{action="respond",http_status_code="200",timeWindow="60000",} 0.031768798828125
ballerina_http:Caller_response_time_seconds_max{action="respond",http_status_code="200",timeWindow="60000",} 0.05194091796875
ballerina_http:Caller_response_time_seconds_min{action="respond",http_status_code="200",timeWindow="60000",} 0.01165771484375
ballerina_http:Caller_response_time_seconds_stdDev{action="respond",http_status_code="200",timeWindow="60000",} 0.020111083984375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.33",} 0.01165771484375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.5",} 0.01165771484375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.66",} 0.05194091796875
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.99",} 0.05194091796875
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.999",} 0.05194091796875
# HELP ballerina_http:Caller_response_time_seconds A Summary of ballerina_http:Caller_response_time_seconds for window of 300000
# TYPE ballerina_http:Caller_response_time_seconds summary
ballerina_http:Caller_response_time_seconds_mean{action="respond",http_status_code="200",timeWindow="300000",} 0.031768798828125
ballerina_http:Caller_response_time_seconds_max{action="respond",http_status_code="200",timeWindow="300000",} 0.05194091796875
ballerina_http:Caller_response_time_seconds_min{action="respond",http_status_code="200",timeWindow="300000",} 0.01165771484375
ballerina_http:Caller_response_time_seconds_stdDev{action="respond",http_status_code="200",timeWindow="300000",} 0.020111083984375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.33",} 0.01165771484375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.5",} 0.01165771484375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.66",} 0.05194091796875
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.99",} 0.05194091796875
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.999",} 0.05194091796875
# HELP ballerina_http:Caller_response_time_seconds A Summary of ballerina_http:Caller_response_time_seconds for window of 900000
# TYPE ballerina_http:Caller_response_time_seconds summary
ballerina_http:Caller_response_time_seconds_mean{action="respond",http_status_code="200",timeWindow="900000",} 0.031768798828125
ballerina_http:Caller_response_time_seconds_max{action="respond",http_status_code="200",timeWindow="900000",} 0.05194091796875
ballerina_http:Caller_response_time_seconds_min{action="respond",http_status_code="200",timeWindow="900000",} 0.01165771484375
ballerina_http:Caller_response_time_seconds_stdDev{action="respond",http_status_code="200",timeWindow="900000",} 0.020111083984375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.33",} 0.01165771484375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.5",} 0.01165771484375
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.66",} 0.05194091796875
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.99",} 0.05194091796875
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.999",} 0.05194091796875
# HELP ballerina_http:Caller_3XX_requests_total_value Total number of requests that resulted in HTTP 3xx redirections
# TYPE ballerina_http:Caller_3XX_requests_total_value counter
ballerina_http:Caller_3XX_requests_total_value{action="respond",} 0.0
# HELP ballerina_http:Caller_inprogress_requests_value Inprogress Requests
# TYPE ballerina_http:Caller_inprogress_requests_value gauge
ballerina_http:Caller_inprogress_requests_value{action="respond",} 0.0
# HELP ballerina_http:Caller_2XX_requests_total_value Total number of requests that resulted in HTTP 2xx successful responses
# TYPE ballerina_http:Caller_2XX_requests_total_value counter
ballerina_http:Caller_2XX_requests_total_value{action="respond",} 2.0
# HELP http_requests_total_value Total number of requests
# TYPE http_requests_total_value counter
http_requests_total_value{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",} 1.0
# TYPE ballerina_scheduler_running_worker_count_value gauge
ballerina_scheduler_running_worker_count_value 0.0
# HELP http_inprogress_requests_value Inprogress Requests
# TYPE http_inprogress_requests_value gauge
http_inprogress_requests_value{resource="findOrder",service="guide:0.0.0.orderMgt$$service$0",} 0.0
# HELP ballerina_http:Caller_5XX_requests_total_value Total number of requests that resulted in HTTP 5xx server errors
# TYPE ballerina_http:Caller_5XX_requests_total_value counter
ballerina_http:Caller_5XX_requests_total_value{action="respond",} 0.0
# HELP ballerina_http:Caller_1XX_requests_total_value Total number of requests that resulted in HTTP 1xx informational responses
# TYPE ballerina_http:Caller_1XX_requests_total_value counter
ballerina_http:Caller_1XX_requests_total_value{action="respond",} 0.0
# TYPE ballerina_scheduler_excepted_worker_count_value gauge
ballerina_scheduler_excepted_worker_count_value 0.0
# TYPE ballerina_scheduler_ready_worker_count_value gauge
ballerina_scheduler_ready_worker_count_value 0.0
# TYPE ballerina_scheduler_waiting_for_response_worker_count_value gauge
ballerina_scheduler_waiting_for_response_worker_count_value 0.0
# HELP startup_time_milliseconds_value Startup time in milliseconds
# TYPE startup_time_milliseconds_value gauge
startup_time_milliseconds_value 4416.0
# HELP http_response_time_seconds_value Response Time
# TYPE http_response_time_seconds_value gauge
http_response_time_seconds_value{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",} 0.097215366
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 60000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.09716796875
http_response_time_seconds_max{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.09716796875
http_response_time_seconds_min{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.09716796875
http_response_time_seconds_stdDev{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.0
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.33",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.5",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.66",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.99",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.999",} 0.09716796875
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 300000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.09716796875
http_response_time_seconds_max{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.09716796875
http_response_time_seconds_min{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.09716796875
http_response_time_seconds_stdDev{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.0
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.33",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.5",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.66",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.99",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.999",} 0.09716796875
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 900000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.09716796875
http_response_time_seconds_max{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.09716796875
http_response_time_seconds_min{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.09716796875
http_response_time_seconds_stdDev{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.0
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.33",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.5",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.66",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.99",} 0.09716796875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.999",} 0.09716796875
# TYPE ballerina_scheduler_paused_worker_count_value gauge
ballerina_scheduler_paused_worker_count_value 0.0
# HELP ballerina_http:Caller_4XX_requests_total_value Total number of requests that resulted in HTTP 4xx client errors
# TYPE ballerina_http:Caller_4XX_requests_total_value counter
ballerina_http:Caller_4XX_requests_total_value{action="respond",} 0.0
"""


class TimeWindow:
    timeWindow = 0
    mean = 0
    stdDev = 0
    percentile = 0
    value = 0


min_1 = TimeWindow()
min_5 = TimeWindow()
min_15 = TimeWindow()

for line in str.split("\n"):

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


        print(timeWindow)
        if (meanOrStd[1] == ''):
            quantile = timeWindowAndQuantile[2][1:] + timeWindowAndQuantile[3]
            print(quantile)
        else:
            print(meanOrStd[1])

        print(y[1], "\n\n")
        # print(z[1].split("\""))
        # if((z[0].split("response_time_seconds"))[1]=="_mean"):