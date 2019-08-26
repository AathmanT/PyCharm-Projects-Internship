import re

report = """# HELP ballerina_http:HttpClient_requests_total_value Total number of requests
# TYPE ballerina_http:HttpClient_requests_total_value counter
ballerina_http:HttpClient_requests_total_value{action="forward",} 5764550.0
# HELP ballerina_http:HttpCachingClient_1XX_requests_total_value Total number of requests that resulted in HTTP 1xx informational responses
# TYPE ballerina_http:HttpCachingClient_1XX_requests_total_value counter
ballerina_http:HttpCachingClient_1XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:HttpCaller_inprogress_requests_value Inprogress Requests
# TYPE ballerina_http:HttpCaller_inprogress_requests_value gauge
ballerina_http:HttpCaller_inprogress_requests_value{action="forward",} 95.0
# HELP http_requests_total_value Total number of requests
# TYPE http_requests_total_value counter
http_requests_total_value{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",} 9.0
# HELP http_1XX_requests_total_value Total number of requests that resulted in HTTP 1xx informational responses
# TYPE http_1XX_requests_total_value counter
http_1XX_requests_total_value{service="passthroughService$$service$0",resource="passthrough",} 0.0
# HELP ballerina_http:Caller_5XX_requests_total_value Total number of requests that resulted in HTTP 5xx server errors
# TYPE ballerina_http:Caller_5XX_requests_total_value counter
ballerina_http:Caller_5XX_requests_total_value{action="respond",} 0.0
# HELP http_requests_total_value Total number of requests
# TYPE http_requests_total_value counter
http_requests_total_value{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",} 1.0
# HELP ballerina_http:HttpClient_response_time_seconds_value Response Time
# TYPE ballerina_http:HttpClient_response_time_seconds_value gauge
ballerina_http:HttpClient_response_time_seconds_value{action="forward",} 0.008100922
# HELP ballerina_http:HttpClient_response_time_seconds A Summary of ballerina_http:HttpClient_response_time_seconds for window of 60000
# TYPE ballerina_http:HttpClient_response_time_seconds summary
ballerina_http:HttpClient_response_time_seconds_mean{action="forward",timeWindow="60000",} 0.010368890050522859
ballerina_http:HttpClient_response_time_seconds_max{action="forward",timeWindow="60000",} 0.1591777801513672
ballerina_http:HttpClient_response_time_seconds_min{action="forward",timeWindow="60000",} 4.61578369140625E-4
ballerina_http:HttpClient_response_time_seconds_stdDev{action="forward",timeWindow="60000",} 0.00877256431130438
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.33",} 0.0057659149169921875
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.5",} 0.007993698120117188
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.66",} 0.010801315307617188
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.99",} 0.04614067077636719
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.999",} 0.08154106140136719
# HELP ballerina_http:HttpClient_response_time_seconds A Summary of ballerina_http:HttpClient_response_time_seconds for window of 300000
# TYPE ballerina_http:HttpClient_response_time_seconds summary
ballerina_http:HttpClient_response_time_seconds_mean{action="forward",timeWindow="300000",} 0.010329935947204329
ballerina_http:HttpClient_response_time_seconds_max{action="forward",timeWindow="300000",} 0.2109355926513672
ballerina_http:HttpClient_response_time_seconds_min{action="forward",timeWindow="300000",} 3.85284423828125E-4
ballerina_http:HttpClient_response_time_seconds_stdDev{action="forward",timeWindow="300000",} 0.008767270776728862
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.33",} 0.0056743621826171875
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.5",} 0.007932662963867188
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.66",} 0.010801315307617188
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.99",} 0.04565238952636719
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.999",} 0.07958793640136719
# HELP ballerina_http:HttpClient_response_time_seconds A Summary of ballerina_http:HttpClient_response_time_seconds for window of 900000
# TYPE ballerina_http:HttpClient_response_time_seconds summary
ballerina_http:HttpClient_response_time_seconds_mean{action="forward",timeWindow="900000",} 0.010174264620895322
ballerina_http:HttpClient_response_time_seconds_max{action="forward",timeWindow="900000",} 0.4726543426513672
ballerina_http:HttpClient_response_time_seconds_min{action="forward",timeWindow="900000",} 3.5858154296875E-4
ballerina_http:HttpClient_response_time_seconds_stdDev{action="forward",timeWindow="900000",} 0.00940978173920284
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.33",} 0.0054607391357421875
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.5",} 0.0076885223388671875
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.66",} 0.010557174682617188
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.99",} 0.04565238952636719
ballerina_http:HttpClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.999",} 0.08740043640136719
# HELP ballerina_http:HttpClient_4XX_requests_total_value Total number of requests that resulted in HTTP 4xx client errors
# TYPE ballerina_http:HttpClient_4XX_requests_total_value counter
ballerina_http:HttpClient_4XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:HttpCachingClient_requests_total_value Total number of requests
# TYPE ballerina_http:HttpCachingClient_requests_total_value counter
ballerina_http:HttpCachingClient_requests_total_value{http_status_code="200",action="forward",} 18.0
# HELP ballerina_http:Client_4XX_requests_total_value Total number of requests that resulted in HTTP 4xx client errors
# TYPE ballerina_http:Client_4XX_requests_total_value counter
ballerina_http:Client_4XX_requests_total_value{action="forward",} 0.0
# TYPE ballerina_scheduler_ready_worker_count_value gauge
ballerina_scheduler_ready_worker_count_value 0.0
# HELP ballerina_http:Client_response_time_seconds_value Response Time
# TYPE ballerina_http:Client_response_time_seconds_value gauge
ballerina_http:Client_response_time_seconds_value{action="forward",} 0.008362699
# HELP ballerina_http:Client_response_time_seconds A Summary of ballerina_http:Client_response_time_seconds for window of 60000
# TYPE ballerina_http:Client_response_time_seconds summary
ballerina_http:Client_response_time_seconds_mean{action="forward",timeWindow="60000",} 0.01058268095598563
ballerina_http:Client_response_time_seconds_max{action="forward",timeWindow="60000",} 0.15917587280273438
ballerina_http:Client_response_time_seconds_min{action="forward",timeWindow="60000",} 4.92095947265625E-4
ballerina_http:Client_response_time_seconds_stdDev{action="forward",timeWindow="60000",} 0.009153626873586862
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="60000",quantile="0.33",} 0.005825042724609375
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="60000",quantile="0.5",} 0.008113861083984375
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="60000",quantile="0.66",} 0.010982513427734375
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="60000",quantile="0.99",} 0.048580169677734375
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="60000",quantile="0.999",} 0.08642196655273438
# HELP ballerina_http:Client_response_time_seconds A Summary of ballerina_http:Client_response_time_seconds for window of 300000
# TYPE ballerina_http:Client_response_time_seconds summary
ballerina_http:Client_response_time_seconds_mean{action="forward",timeWindow="300000",} 0.010579692730078612
ballerina_http:Client_response_time_seconds_max{action="forward",timeWindow="300000",} 0.2109355926513672
ballerina_http:Client_response_time_seconds_min{action="forward",timeWindow="300000",} 4.062652587890625E-4
ballerina_http:Client_response_time_seconds_stdDev{action="forward",timeWindow="300000",} 0.009294262820588978
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="300000",quantile="0.33",} 0.0057353973388671875
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="300000",quantile="0.5",} 0.008054733276367188
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="300000",quantile="0.66",} 0.010923385620117188
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="300000",quantile="0.99",} 0.04882621765136719
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="300000",quantile="0.999",} 0.08740043640136719
# HELP ballerina_http:Client_response_time_seconds A Summary of ballerina_http:Client_response_time_seconds for window of 900000
# TYPE ballerina_http:Client_response_time_seconds summary
ballerina_http:Client_response_time_seconds_mean{action="forward",timeWindow="900000",} 0.010428579756009365
ballerina_http:Client_response_time_seconds_max{action="forward",timeWindow="900000",} 0.4726543426513672
ballerina_http:Client_response_time_seconds_min{action="forward",timeWindow="900000",} 3.795623779296875E-4
ballerina_http:Client_response_time_seconds_stdDev{action="forward",timeWindow="900000",} 0.009928859445135572
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="900000",quantile="0.33",} 0.0055217742919921875
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="900000",quantile="0.5",} 0.0077800750732421875
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="900000",quantile="0.66",} 0.010679244995117188
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="900000",quantile="0.99",} 0.04907035827636719
ballerina_http:Client_response_time_seconds{action="forward",timeWindow="900000",quantile="0.999",} 0.09423637390136719
# HELP startup_time_milliseconds_value Startup time in milliseconds
# TYPE startup_time_milliseconds_value gauge
startup_time_milliseconds_value 1331.0
# HELP ballerina_http:Caller_4XX_requests_total_value Total number of requests that resulted in HTTP 4xx client errors
# TYPE ballerina_http:Caller_4XX_requests_total_value counter
ballerina_http:Caller_4XX_requests_total_value{action="respond",} 0.0
# HELP ballerina_http:HttpCachingClient_inprogress_requests_value Inprogress Requests
# TYPE ballerina_http:HttpCachingClient_inprogress_requests_value gauge
ballerina_http:HttpCachingClient_inprogress_requests_value{action="forward",} 105.0
# HELP ballerina_http:HttpClient_3XX_requests_total_value Total number of requests that resulted in HTTP 3xx redirections
# TYPE ballerina_http:HttpClient_3XX_requests_total_value counter
ballerina_http:HttpClient_3XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:HttpCaller_5XX_requests_total_value Total number of requests that resulted in HTTP 5xx server errors
# TYPE ballerina_http:HttpCaller_5XX_requests_total_value counter
ballerina_http:HttpCaller_5XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:HttpCachingClient_response_time_seconds_value Response Time
# TYPE ballerina_http:HttpCachingClient_response_time_seconds_value gauge
ballerina_http:HttpCachingClient_response_time_seconds_value{http_status_code="200",action="forward",} 0.042551618
# HELP ballerina_http:HttpCachingClient_response_time_seconds A Summary of ballerina_http:HttpCachingClient_response_time_seconds for window of 60000
# TYPE ballerina_http:HttpCachingClient_response_time_seconds summary
ballerina_http:HttpCachingClient_response_time_seconds_mean{http_status_code="200",action="forward",timeWindow="60000",} 0.015263875325520834
ballerina_http:HttpCachingClient_response_time_seconds_max{http_status_code="200",action="forward",timeWindow="60000",} 0.042720794677734375
ballerina_http:HttpCachingClient_response_time_seconds_min{http_status_code="200",action="forward",timeWindow="60000",} 7.5531005859375E-4
ballerina_http:HttpCachingClient_response_time_seconds_stdDev{http_status_code="200",action="forward",timeWindow="60000",} 0.019343495269982754
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.33",} 7.5531005859375E-4
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.5",} 0.002437591552734375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.66",} 0.002437591552734375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.99",} 0.042720794677734375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.999",} 0.042720794677734375
# HELP ballerina_http:HttpCachingClient_response_time_seconds A Summary of ballerina_http:HttpCachingClient_response_time_seconds for window of 300000
# TYPE ballerina_http:HttpCachingClient_response_time_seconds summary
ballerina_http:HttpCachingClient_response_time_seconds_mean{http_status_code="200",action="forward",timeWindow="300000",} 0.011810302734375
ballerina_http:HttpCachingClient_response_time_seconds_max{http_status_code="200",action="forward",timeWindow="300000",} 0.043209075927734375
ballerina_http:HttpCachingClient_response_time_seconds_min{http_status_code="200",action="forward",timeWindow="300000",} 7.5531005859375E-4
ballerina_http:HttpCachingClient_response_time_seconds_stdDev{http_status_code="200",action="forward",timeWindow="300000",} 0.015070966695904218
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.33",} 0.002117156982421875
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.5",} 0.006496429443359375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.66",} 0.009639739990234375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.99",} 0.043209075927734375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.999",} 0.043209075927734375
# HELP ballerina_http:HttpCachingClient_response_time_seconds A Summary of ballerina_http:HttpCachingClient_response_time_seconds for window of 900000
# TYPE ballerina_http:HttpCachingClient_response_time_seconds summary
ballerina_http:HttpCachingClient_response_time_seconds_mean{http_status_code="200",action="forward",timeWindow="900000",} 0.008762995402018229
ballerina_http:HttpCachingClient_response_time_seconds_max{http_status_code="200",action="forward",timeWindow="900000",} 0.043209075927734375
ballerina_http:HttpCachingClient_response_time_seconds_min{http_status_code="200",action="forward",timeWindow="900000",} 7.5531005859375E-4
ballerina_http:HttpCachingClient_response_time_seconds_stdDev{http_status_code="200",action="forward",timeWindow="900000",} 0.012452702883301628
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.33",} 0.002239227294921875
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.5",} 0.003414154052734375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.66",} 0.006496429443359375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.99",} 0.043209075927734375
ballerina_http:HttpCachingClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.999",} 0.043209075927734375
# HELP ballerina_http:Client_2XX_requests_total_value Total number of requests that resulted in HTTP 2xx successful responses
# TYPE ballerina_http:Client_2XX_requests_total_value counter
ballerina_http:Client_2XX_requests_total_value{action="forward",} 29.0
# HELP http_response_time_seconds_value Response Time
# TYPE http_response_time_seconds_value gauge
http_response_time_seconds_value{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",} 0.00131621
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 60000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",} 0.0
http_response_time_seconds_max{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",} 0.0
http_response_time_seconds_min{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",} 0.0
http_response_time_seconds_stdDev{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",} 0.0
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",quantile="0.33",} 0.0
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",quantile="0.5",} 0.0
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",quantile="0.66",} 0.0
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",quantile="0.99",} 0.0
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="60000",quantile="0.999",} 0.0
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 300000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",} 0.001312255859375
http_response_time_seconds_max{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",} 0.001312255859375
http_response_time_seconds_min{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",} 0.001312255859375
http_response_time_seconds_stdDev{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",} 0.0
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",quantile="0.33",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",quantile="0.5",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",quantile="0.66",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",quantile="0.99",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="300000",quantile="0.999",} 0.001312255859375
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 900000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",} 0.001312255859375
http_response_time_seconds_max{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",} 0.001312255859375
http_response_time_seconds_min{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",} 0.001312255859375
http_response_time_seconds_stdDev{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",} 0.0
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",quantile="0.33",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",quantile="0.5",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",quantile="0.66",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",quantile="0.99",} 0.001312255859375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",http_status_code="200",resource="passthrough",timeWindow="900000",quantile="0.999",} 0.001312255859375
# TYPE ballerina_scheduler_excepted_worker_count_value gauge
ballerina_scheduler_excepted_worker_count_value 0.0
# HELP ballerina_http:HttpCaller_4XX_requests_total_value Total number of requests that resulted in HTTP 4xx client errors
# TYPE ballerina_http:HttpCaller_4XX_requests_total_value counter
ballerina_http:HttpCaller_4XX_requests_total_value{action="forward",} 0.0
# HELP http_2XX_requests_total_value Total number of requests that resulted in HTTP 2xx successful responses
# TYPE http_2XX_requests_total_value counter
http_2XX_requests_total_value{service="passthroughService$$service$0",resource="passthrough",} 1.0
# HELP ballerina_http:HttpCachingClient_5XX_requests_total_value Total number of requests that resulted in HTTP 5xx server errors
# TYPE ballerina_http:HttpCachingClient_5XX_requests_total_value counter
ballerina_http:HttpCachingClient_5XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:Client_inprogress_requests_value Inprogress Requests
# TYPE ballerina_http:Client_inprogress_requests_value gauge
ballerina_http:Client_inprogress_requests_value{action="forward",} 117.0
# HELP ballerina_http:HttpClient_2XX_requests_total_value Total number of requests that resulted in HTTP 2xx successful responses
# TYPE ballerina_http:HttpClient_2XX_requests_total_value counter
ballerina_http:HttpClient_2XX_requests_total_value{action="forward",} 66.0
# HELP http_response_time_seconds_value Response Time
# TYPE http_response_time_seconds_value gauge
http_response_time_seconds_value{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",} 0.207663184
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 60000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.20703125
http_response_time_seconds_max{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.20703125
http_response_time_seconds_min{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.20703125
http_response_time_seconds_stdDev{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",} 0.0
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.33",} 0.20703125
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.5",} 0.20703125
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.66",} 0.20703125
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.99",} 0.20703125
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="60000",quantile="0.999",} 0.20703125
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 300000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.23274739583333334
http_response_time_seconds_max{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.3095703125
http_response_time_seconds_min{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.134765625
http_response_time_seconds_stdDev{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",} 0.06090198144666374
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.33",} 0.20703125
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.5",} 0.2119140625
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.66",} 0.2255859375
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.99",} 0.3095703125
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="300000",quantile="0.999",} 0.3095703125
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 900000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.3090277777777778
http_response_time_seconds_max{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.6513671875
http_response_time_seconds_min{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.134765625
http_response_time_seconds_stdDev{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",} 0.14160875454011004
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.33",} 0.2119140625
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.5",} 0.3076171875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.66",} 0.3095703125
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.99",} 0.6513671875
http_response_time_seconds{protocol="http",http_url="/metrics",resource="getMetrics",http_method="GET",service="PrometheusReporter$$service$0",timeWindow="900000",quantile="0.999",} 0.6513671875
# HELP ballerina_http:Client_3XX_requests_total_value Total number of requests that resulted in HTTP 3xx redirections
# TYPE ballerina_http:Client_3XX_requests_total_value counter
ballerina_http:Client_3XX_requests_total_value{action="forward",} 0.0
# HELP http_4XX_requests_total_value Total number of requests that resulted in HTTP 4xx client errors
# TYPE http_4XX_requests_total_value counter
http_4XX_requests_total_value{service="passthroughService$$service$0",resource="passthrough",} 0.0
# HELP ballerina_http:HttpCachingClient_4XX_requests_total_value Total number of requests that resulted in HTTP 4xx client errors
# TYPE ballerina_http:HttpCachingClient_4XX_requests_total_value counter
ballerina_http:HttpCachingClient_4XX_requests_total_value{action="forward",} 0.0
# HELP http_inprogress_requests_value Inprogress Requests
# TYPE http_inprogress_requests_value gauge
http_inprogress_requests_value{resource="getMetrics",service="PrometheusReporter$$service$0",} 1.0
# HELP ballerina_http:Caller_response_time_seconds_value Response Time
# TYPE ballerina_http:Caller_response_time_seconds_value gauge
ballerina_http:Caller_response_time_seconds_value{action="respond",http_status_code="200",} 3.34757E-4
# HELP ballerina_http:Caller_response_time_seconds A Summary of ballerina_http:Caller_response_time_seconds for window of 60000
# TYPE ballerina_http:Caller_response_time_seconds summary
ballerina_http:Caller_response_time_seconds_mean{action="respond",http_status_code="200",timeWindow="60000",} 0.006561554612308993
ballerina_http:Caller_response_time_seconds_max{action="respond",http_status_code="200",timeWindow="60000",} 0.1074213981628418
ballerina_http:Caller_response_time_seconds_min{action="respond",http_status_code="200",timeWindow="60000",} 6.103515625E-5
ballerina_http:Caller_response_time_seconds_stdDev{action="respond",http_status_code="200",timeWindow="60000",} 0.0064174471967723915
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.33",} 0.003341197967529297
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.5",} 0.005004405975341797
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.66",} 0.006957530975341797
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.99",} 0.030761241912841797
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="60000",quantile="0.999",} 0.0610346794128418
# HELP ballerina_http:Caller_response_time_seconds A Summary of ballerina_http:Caller_response_time_seconds for window of 300000
# TYPE ballerina_http:Caller_response_time_seconds summary
ballerina_http:Caller_response_time_seconds_mean{action="respond",http_status_code="200",timeWindow="300000",} 0.006533356433425611
ballerina_http:Caller_response_time_seconds_max{action="respond",http_status_code="200",timeWindow="300000",} 0.1689450740814209
ballerina_http:Caller_response_time_seconds_min{action="respond",http_status_code="200",timeWindow="300000",} 6.008148193359375E-5
ballerina_http:Caller_response_time_seconds_stdDev{action="respond",http_status_code="200",timeWindow="300000",} 0.006525186148467682
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.33",} 0.0032804012298583984
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.5",} 0.0049741268157958984
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.66",} 0.0068662166595458984
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.99",} 0.0319821834564209
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="300000",quantile="0.999",} 0.0620114803314209
# HELP ballerina_http:Caller_response_time_seconds A Summary of ballerina_http:Caller_response_time_seconds for window of 900000
# TYPE ballerina_http:Caller_response_time_seconds summary
ballerina_http:Caller_response_time_seconds_mean{action="respond",http_status_code="200",timeWindow="900000",} 0.00642275686287254
ballerina_http:Caller_response_time_seconds_max{action="respond",http_status_code="200",timeWindow="900000",} 0.3886716365814209
ballerina_http:Caller_response_time_seconds_min{action="respond",http_status_code="200",timeWindow="900000",} 5.91278076171875E-5
ballerina_http:Caller_response_time_seconds_stdDev{action="respond",http_status_code="200",timeWindow="900000",} 0.007084538759632644
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.33",} 0.0031125545501708984
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.5",} 0.0047910213470458984
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.66",} 0.0067136287689208984
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.99",} 0.0322263240814209
ballerina_http:Caller_response_time_seconds{action="respond",http_status_code="200",timeWindow="900000",quantile="0.999",} 0.0659177303314209
# HELP ballerina_http:HttpCaller_requests_total_value Total number of requests
# TYPE ballerina_http:HttpCaller_requests_total_value counter
ballerina_http:HttpCaller_requests_total_value{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",} 5760975.0
# HELP ballerina_http:HttpClient_requests_total_value Total number of requests
# TYPE ballerina_http:HttpClient_requests_total_value counter
ballerina_http:HttpClient_requests_total_value{http_status_code="200",action="forward",} 11.0
# HELP ballerina_http:Caller_2XX_requests_total_value Total number of requests that resulted in HTTP 2xx successful responses
# TYPE ballerina_http:Caller_2XX_requests_total_value counter
ballerina_http:Caller_2XX_requests_total_value{action="respond",} 5764541.0
# HELP http_requests_total_value Total number of requests
# TYPE http_requests_total_value counter
http_requests_total_value{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",} 5764529.0
# HELP ballerina_http:HttpCaller_3XX_requests_total_value Total number of requests that resulted in HTTP 3xx redirections
# TYPE ballerina_http:HttpCaller_3XX_requests_total_value counter
ballerina_http:HttpCaller_3XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:HttpClient_1XX_requests_total_value Total number of requests that resulted in HTTP 1xx informational responses
# TYPE ballerina_http:HttpClient_1XX_requests_total_value counter
ballerina_http:HttpClient_1XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:Caller_1XX_requests_total_value Total number of requests that resulted in HTTP 1xx informational responses
# TYPE ballerina_http:Caller_1XX_requests_total_value counter
ballerina_http:Caller_1XX_requests_total_value{action="respond",} 0.0
# HELP ballerina_http:Client_1XX_requests_total_value Total number of requests that resulted in HTTP 1xx informational responses
# TYPE ballerina_http:Client_1XX_requests_total_value counter
ballerina_http:Client_1XX_requests_total_value{action="forward",} 0.0
# HELP http_3XX_requests_total_value Total number of requests that resulted in HTTP 3xx redirections
# TYPE http_3XX_requests_total_value counter
http_3XX_requests_total_value{service="passthroughService$$service$0",resource="passthrough",} 0.0
# TYPE ballerina_scheduler_paused_worker_count_value gauge
ballerina_scheduler_paused_worker_count_value 0.0
# HELP ballerina_http:HttpCaller_requests_total_value Total number of requests
# TYPE ballerina_http:HttpCaller_requests_total_value counter
ballerina_http:HttpCaller_requests_total_value{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",} 3656.0
# HELP ballerina_http:HttpClient_response_time_seconds_value Response Time
# TYPE ballerina_http:HttpClient_response_time_seconds_value gauge
ballerina_http:HttpClient_response_time_seconds_value{http_status_code="200",action="forward",} 0.003217444
# HELP ballerina_http:HttpClient_response_time_seconds A Summary of ballerina_http:HttpClient_response_time_seconds for window of 60000
# TYPE ballerina_http:HttpClient_response_time_seconds summary
ballerina_http:HttpClient_response_time_seconds_mean{http_status_code="200",action="forward",timeWindow="60000",} 0.0
ballerina_http:HttpClient_response_time_seconds_max{http_status_code="200",action="forward",timeWindow="60000",} 0.0
ballerina_http:HttpClient_response_time_seconds_min{http_status_code="200",action="forward",timeWindow="60000",} 0.0
ballerina_http:HttpClient_response_time_seconds_stdDev{http_status_code="200",action="forward",timeWindow="60000",} 0.0
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.33",} 0.0
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.5",} 0.0
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.66",} 0.0
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.99",} 0.0
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="60000",quantile="0.999",} 0.0
# HELP ballerina_http:HttpClient_response_time_seconds A Summary of ballerina_http:HttpClient_response_time_seconds for window of 300000
# TYPE ballerina_http:HttpClient_response_time_seconds summary
ballerina_http:HttpClient_response_time_seconds_mean{http_status_code="200",action="forward",timeWindow="300000",} 0.0099945068359375
ballerina_http:HttpClient_response_time_seconds_max{http_status_code="200",action="forward",timeWindow="300000",} 0.0168304443359375
ballerina_http:HttpClient_response_time_seconds_min{http_status_code="200",action="forward",timeWindow="300000",} 0.003204345703125
ballerina_http:HttpClient_response_time_seconds_stdDev{http_status_code="200",action="forward",timeWindow="300000",} 0.0067901611328125
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.33",} 0.003204345703125
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.5",} 0.003204345703125
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.66",} 0.0168304443359375
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.99",} 0.0168304443359375
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="300000",quantile="0.999",} 0.0168304443359375
# HELP ballerina_http:HttpClient_response_time_seconds A Summary of ballerina_http:HttpClient_response_time_seconds for window of 900000
# TYPE ballerina_http:HttpClient_response_time_seconds summary
ballerina_http:HttpClient_response_time_seconds_mean{http_status_code="200",action="forward",timeWindow="900000",} 0.012544111772017046
ballerina_http:HttpClient_response_time_seconds_max{http_status_code="200",action="forward",timeWindow="900000",} 0.03661346435546875
ballerina_http:HttpClient_response_time_seconds_min{http_status_code="200",action="forward",timeWindow="900000",} 0.00115966796875
ballerina_http:HttpClient_response_time_seconds_stdDev{http_status_code="200",action="forward",timeWindow="900000",} 0.011970663384531876
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.33",} 0.00321197509765625
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.5",} 0.00884246826171875
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.66",} 0.01561737060546875
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.99",} 0.03661346435546875
ballerina_http:HttpClient_response_time_seconds{http_status_code="200",action="forward",timeWindow="900000",quantile="0.999",} 0.03661346435546875
# HELP ballerina_http:HttpCaller_response_time_seconds_value Response Time
# TYPE ballerina_http:HttpCaller_response_time_seconds_value gauge
ballerina_http:HttpCaller_response_time_seconds_value{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",} 0.002634058
# HELP ballerina_http:HttpCaller_response_time_seconds A Summary of ballerina_http:HttpCaller_response_time_seconds for window of 60000
# TYPE ballerina_http:HttpCaller_response_time_seconds summary
ballerina_http:HttpCaller_response_time_seconds_mean{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",} 0.010220282986402731
ballerina_http:HttpCaller_response_time_seconds_max{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",} 0.1562480926513672
ballerina_http:HttpCaller_response_time_seconds_min{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",} 4.425048828125E-4
ballerina_http:HttpCaller_response_time_seconds_stdDev{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",} 0.008369414437150403
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",quantile="0.33",} 0.0057353973388671875
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",quantile="0.5",} 0.007932662963867188
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",quantile="0.66",} 0.010740280151367188
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",quantile="0.99",} 0.04369926452636719
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="60000",quantile="0.999",} 0.07470512390136719
# HELP ballerina_http:HttpCaller_response_time_seconds A Summary of ballerina_http:HttpCaller_response_time_seconds for window of 300000
# TYPE ballerina_http:HttpCaller_response_time_seconds summary
ballerina_http:HttpCaller_response_time_seconds_mean{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",} 0.010202458181019777
ballerina_http:HttpCaller_response_time_seconds_max{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",} 0.1845684051513672
ballerina_http:HttpCaller_response_time_seconds_min{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",} 3.7384033203125E-4
ballerina_http:HttpCaller_response_time_seconds_stdDev{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",} 0.008474529283609943
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",quantile="0.33",} 0.0056438446044921875
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",quantile="0.5",} 0.007871627807617188
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",quantile="0.66",} 0.010679244995117188
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",quantile="0.99",} 0.04394340515136719
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="300000",quantile="0.999",} 0.07616996765136719
# HELP ballerina_http:HttpCaller_response_time_seconds A Summary of ballerina_http:HttpCaller_response_time_seconds for window of 900000
# TYPE ballerina_http:HttpCaller_response_time_seconds summary
ballerina_http:HttpCaller_response_time_seconds_mean{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",} 0.010053533571516834
ballerina_http:HttpCaller_response_time_seconds_max{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",} 0.4726543426513672
ballerina_http:HttpCaller_response_time_seconds_min{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",} 3.39508056640625E-4
ballerina_http:HttpCaller_response_time_seconds_stdDev{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",} 0.009163460404788323
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",quantile="0.33",} 0.0054607391357421875
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",quantile="0.5",} 0.0076580047607421875
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",quantile="0.66",} 0.010435104370117188
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",quantile="0.99",} 0.04418754577636719
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="200",timeWindow="900000",quantile="0.999",} 0.08300590515136719
# HELP ballerina_http:HttpCaller_response_time_seconds_value Response Time
# TYPE ballerina_http:HttpCaller_response_time_seconds_value gauge
ballerina_http:HttpCaller_response_time_seconds_value{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",} 0.003019659
# HELP ballerina_http:HttpCaller_response_time_seconds A Summary of ballerina_http:HttpCaller_response_time_seconds for window of 60000
# TYPE ballerina_http:HttpCaller_response_time_seconds summary
ballerina_http:HttpCaller_response_time_seconds_mean{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",} 0.010871457381987236
ballerina_http:HttpCaller_response_time_seconds_max{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",} 0.10058212280273438
ballerina_http:HttpCaller_response_time_seconds_min{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",} 5.5694580078125E-4
ballerina_http:HttpCaller_response_time_seconds_stdDev{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",} 0.01261488989595389
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",quantile="0.33",} 0.003887176513671875
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",quantile="0.5",} 0.006984710693359375
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",quantile="0.66",} 0.011226654052734375
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",quantile="0.99",} 0.061763763427734375
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="60000",quantile="0.999",} 0.10058212280273438
# HELP ballerina_http:HttpCaller_response_time_seconds A Summary of ballerina_http:HttpCaller_response_time_seconds for window of 300000
# TYPE ballerina_http:HttpCaller_response_time_seconds summary
ballerina_http:HttpCaller_response_time_seconds_mean{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",} 0.0098236275826017
ballerina_http:HttpCaller_response_time_seconds_max{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",} 0.10204696655273438
ballerina_http:HttpCaller_response_time_seconds_min{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",} 5.1116943359375E-4
ballerina_http:HttpCaller_response_time_seconds_stdDev{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",} 0.01094519538417629
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",quantile="0.33",} 0.003993988037109375
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",quantile="0.5",} 0.006496429443359375
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",quantile="0.66",} 0.009944915771484375
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",quantile="0.99",} 0.056148529052734375
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="300000",quantile="0.999",} 0.10058212280273438
# HELP ballerina_http:HttpCaller_response_time_seconds A Summary of ballerina_http:HttpCaller_response_time_seconds for window of 900000
# TYPE ballerina_http:HttpCaller_response_time_seconds summary
ballerina_http:HttpCaller_response_time_seconds_mean{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",} 0.009487377475596623
ballerina_http:HttpCaller_response_time_seconds_max{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",} 0.2753887176513672
ballerina_http:HttpCaller_response_time_seconds_min{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",} 4.367828369140625E-4
ballerina_http:HttpCaller_response_time_seconds_stdDev{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",} 0.014396293631075136
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",quantile="0.33",} 0.0029888153076171875
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",quantile="0.5",} 0.0051250457763671875
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",quantile="0.66",} 0.009031295776367188
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",quantile="0.99",} 0.05908012390136719
ballerina_http:HttpCaller_response_time_seconds{http_url="/service/EchoService",peer_address="netty:8688",http_method="POST",action="forward",http_status_code="0",timeWindow="900000",quantile="0.999",} 0.2177715301513672
# HELP http_inprogress_requests_value Inprogress Requests
# TYPE http_inprogress_requests_value gauge
http_inprogress_requests_value{service="passthroughService$$service$0",resource="passthrough",} 262.0
# HELP ballerina_http:HttpCachingClient_requests_total_value Total number of requests
# TYPE ballerina_http:HttpCachingClient_requests_total_value counter
ballerina_http:HttpCachingClient_requests_total_value{action="forward",} 5764604.0
# HELP ballerina_http:HttpCaller_2XX_requests_total_value Total number of requests that resulted in HTTP 2xx successful responses
# TYPE ballerina_http:HttpCaller_2XX_requests_total_value counter
ballerina_http:HttpCaller_2XX_requests_total_value{action="forward",} 5761245.0
# TYPE ballerina_scheduler_waiting_for_lock_worker_count_value gauge
ballerina_scheduler_waiting_for_lock_worker_count_value 0.0
# HELP ballerina_http:Caller_requests_total_value Total number of requests
# TYPE ballerina_http:Caller_requests_total_value counter
ballerina_http:Caller_requests_total_value{action="respond",http_status_code="200",} 5764541.0
# HELP ballerina_http:Caller_3XX_requests_total_value Total number of requests that resulted in HTTP 3xx redirections
# TYPE ballerina_http:Caller_3XX_requests_total_value counter
ballerina_http:Caller_3XX_requests_total_value{action="respond",} 0.0
# HELP ballerina_http:Caller_inprogress_requests_value Inprogress Requests
# TYPE ballerina_http:Caller_inprogress_requests_value gauge
ballerina_http:Caller_inprogress_requests_value{action="respond",} 90.0
# HELP ballerina_http:Client_5XX_requests_total_value Total number of requests that resulted in HTTP 5xx server errors
# TYPE ballerina_http:Client_5XX_requests_total_value counter
ballerina_http:Client_5XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:Client_requests_total_value Total number of requests
# TYPE ballerina_http:Client_requests_total_value counter
ballerina_http:Client_requests_total_value{action="forward",} 5764627.0
# TYPE ballerina_scheduler_running_worker_count_value gauge
ballerina_scheduler_running_worker_count_value 0.0
# HELP ballerina_http:HttpCachingClient_3XX_requests_total_value Total number of requests that resulted in HTTP 3xx redirections
# TYPE ballerina_http:HttpCachingClient_3XX_requests_total_value counter
ballerina_http:HttpCachingClient_3XX_requests_total_value{action="forward",} 0.0
# HELP ballerina_http:HttpCachingClient_response_time_seconds_value Response Time
# TYPE ballerina_http:HttpCachingClient_response_time_seconds_value gauge
ballerina_http:HttpCachingClient_response_time_seconds_value{action="forward",} 0.022393801
# HELP ballerina_http:HttpCachingClient_response_time_seconds A Summary of ballerina_http:HttpCachingClient_response_time_seconds for window of 60000
# TYPE ballerina_http:HttpCachingClient_response_time_seconds summary
ballerina_http:HttpCachingClient_response_time_seconds_mean{action="forward",timeWindow="60000",} 0.010505779011838513
ballerina_http:HttpCachingClient_response_time_seconds_max{action="forward",timeWindow="60000",} 0.1591777801513672
ballerina_http:HttpCachingClient_response_time_seconds_min{action="forward",timeWindow="60000",} 4.8065185546875E-4
ballerina_http:HttpCachingClient_response_time_seconds_stdDev{action="forward",timeWindow="60000",} 0.009027654886613607
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.33",} 0.0057964324951171875
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.5",} 0.008054733276367188
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.66",} 0.010923385620117188
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.99",} 0.04784965515136719
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="60000",quantile="0.999",} 0.08642387390136719
# HELP ballerina_http:HttpCachingClient_response_time_seconds A Summary of ballerina_http:HttpCachingClient_response_time_seconds for window of 300000
# TYPE ballerina_http:HttpCachingClient_response_time_seconds summary
ballerina_http:HttpCachingClient_response_time_seconds_mean{action="forward",timeWindow="300000",} 0.010467694320422128
ballerina_http:HttpCachingClient_response_time_seconds_max{action="forward",timeWindow="300000",} 0.2109355926513672
ballerina_http:HttpCachingClient_response_time_seconds_min{action="forward",timeWindow="300000",} 3.986358642578125E-4
ballerina_http:HttpCachingClient_response_time_seconds_stdDev{action="forward",timeWindow="300000",} 0.00904584296154887
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.33",} 0.0057048797607421875
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.5",} 0.007993698120117188
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.66",} 0.010862350463867188
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.99",} 0.04736137390136719
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="300000",quantile="0.999",} 0.08349418640136719
# HELP ballerina_http:HttpCachingClient_response_time_seconds A Summary of ballerina_http:HttpCachingClient_response_time_seconds for window of 900000
# TYPE ballerina_http:HttpCachingClient_response_time_seconds summary
ballerina_http:HttpCachingClient_response_time_seconds_mean{action="forward",timeWindow="900000",} 0.010312637459681159
ballerina_http:HttpCachingClient_response_time_seconds_max{action="forward",timeWindow="900000",} 0.4726543426513672
ballerina_http:HttpCachingClient_response_time_seconds_min{action="forward",timeWindow="900000",} 3.719329833984375E-4
ballerina_http:HttpCachingClient_response_time_seconds_stdDev{action="forward",timeWindow="900000",} 0.009665529359979292
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.33",} 0.0055217742919921875
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.5",} 0.0077495574951171875
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.66",} 0.010618209838867188
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.99",} 0.04760551452636719
ballerina_http:HttpCachingClient_response_time_seconds{action="forward",timeWindow="900000",quantile="0.999",} 0.09033012390136719
# HELP http_response_time_seconds_value Response Time
# TYPE http_response_time_seconds_value gauge
http_response_time_seconds_value{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",} 0.049396067
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 60000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",} 0.020460457285556927
http_response_time_seconds_max{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",} 0.17968368530273438
http_response_time_seconds_min{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",} 6.75201416015625E-4
http_response_time_seconds_stdDev{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",} 0.011918969070558179
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",quantile="0.33",} 0.015071868896484375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",quantile="0.5",} 0.018672943115234375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",quantile="0.66",} 0.022335052490234375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",quantile="0.99",} 0.06542587280273438
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="60000",quantile="0.999",} 0.10351181030273438
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 300000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",} 0.020416662550380504
http_response_time_seconds_max{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",} 0.22167587280273438
http_response_time_seconds_min{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",} 5.98907470703125E-4
http_response_time_seconds_stdDev{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",} 0.01213416077898626
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",quantile="0.33",} 0.014888763427734375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",quantile="0.5",} 0.018550872802734375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",quantile="0.66",} 0.022335052490234375
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",quantile="0.99",} 0.06640243530273438
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="300000",quantile="0.999",} 0.10595321655273438
# HELP http_response_time_seconds A Summary of http_response_time_seconds for window of 900000
# TYPE http_response_time_seconds summary
http_response_time_seconds_mean{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",} 0.020088733122802425
http_response_time_seconds_max{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",} 0.5273418426513672
http_response_time_seconds_min{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",} 4.863739013671875E-4
http_response_time_seconds_stdDev{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",} 0.013144420542635097
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",quantile="0.33",} 0.014341354370117188
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",quantile="0.5",} 0.018064498901367188
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",quantile="0.66",} 0.021970748901367188
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",quantile="0.99",} 0.06738090515136719
http_response_time_seconds{protocol="http",http_method="POST",service="passthroughService$$service$0",http_url="/passthrough",resource="passthrough",timeWindow="900000",quantile="0.999",} 0.12109184265136719
# TYPE ballerina_scheduler_waiting_for_response_worker_count_value gauge
ballerina_scheduler_waiting_for_response_worker_count_value 0.0
# HELP ballerina_http:HttpCaller_1XX_requests_total_value Total number of requests that resulted in HTTP 1xx informational responses
# TYPE ballerina_http:HttpCaller_1XX_requests_total_value counter
ballerina_http:HttpCaller_1XX_requests_total_value{action="forward",} 0.0
# HELP http_5XX_requests_total_value Total number of requests that resulted in HTTP 5xx server errors
# TYPE http_5XX_requests_total_value counter
http_5XX_requests_total_value{service="passthroughService$$service$0",resource="passthrough",} 0.0
# HELP ballerina_http:HttpClient_inprogress_requests_value Inprogress Requests
# TYPE ballerina_http:HttpClient_inprogress_requests_value gauge
ballerina_http:HttpClient_inprogress_requests_value{action="forward",} 126.0
# HELP ballerina_http:HttpCachingClient_2XX_requests_total_value Total number of requests that resulted in HTTP 2xx successful responses
# TYPE ballerina_http:HttpCachingClient_2XX_requests_total_value counter
ballerina_http:HttpCachingClient_2XX_requests_total_value{action="forward",} 56.0
# HELP ballerina_http:HttpClient_5XX_requests_total_value Total number of requests that resulted in HTTP 5xx server errors
# TYPE ballerina_http:HttpClient_5XX_requests_total_value counter
ballerina_http:HttpClient_5XX_requests_total_value{action="forward",} 0.0"""

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
    filter = "response_time_seconds(?:_mean|_stdDev|{).*transformationService\$\$service\$0.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*"
    throughput_filter = "http_requests_total_value.*transformationService\$\$service\$0.*"
    splitter = "{protocol=\"http\",http_method=\"POST\",resource=\"transform\",http_url=\"/transform\",service=\"transformationService$$service$0\","
elif (bal_file == "h1_h1_passthrough.balx"):
    filter = "response_time_seconds(?:_mean|_stdDev|{).*passthroughService\$\$service\$0.*timeWindow=\"(?:300000|60000|900000)\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*"
    throughput_filter = "http_requests_total_value.*passthroughService\$\$service\$0.*"
    splitter = "{protocol=\"http\",http_method=\"POST\",service=\"passthroughService$$service$0\",http_url=\"/passthrough\",resource=\"passthrough\","

if not (os.path.exists("~/demofile2.txt")):
    print("Scenario name,timeWindow,type,value" + "\n")

print(bal_file + "\n")


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

        # print(data)
        for line in data_list:

            x = re.findall(
                filter,
                line)

            throughput = re.findall(throughput_filter, line)
            if (throughput):
                # f.write(throughput[0]+"\n")

                current_requests = float((throughput[0].split(" "))[1])
                print(str(current_requests) + " " + str(previous_requests))

                print(bal_file + ",timeWindow=60000,throughput," + str(
                    (current_requests - previous_requests) / (current_time - previous_time)) + "\n")
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
                splitter)
            # print(z[0],"\n",z[1],"\n",y[1],"\n\n")
            meanOrStd = z[0].split("response_time_seconds")
            timeWindowAndQuantile = z[1].split("\"")

            timeWindow = timeWindowAndQuantile[0] + timeWindowAndQuantile[1]

            print(bal_file + "," + timeWindow + ",")
            # print(timeWindow)
            if (meanOrStd[1] == ''):
                quantile = timeWindowAndQuantile[2][1:] + timeWindowAndQuantile[3]
                # print(quantile)
                print(quantile + ",")
            else:
                # print(meanOrStd[1])
                print(meanOrStd[1] + ",")

            # print(y[1], "\n\n")
            print(y[1] + "\n\n")


        previous_time = current_time
        previous_requests = current_requests
    except Exception as e:
        print(str(e))

query_metrics()


