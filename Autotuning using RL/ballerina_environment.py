# %%
import re
import subprocess, requests
import random
import time

import numpy as np

concurrency = 100
usecase = 'passthrough'
message_size = '50B'


class BalEnv():
    def __init__(self, randomSeed=0 ):

        # Set the random seed
        random.seed(randomSeed)

        # subprocess.call(['ssh', 'jmeter', './home/wso2/killscript.sh'])
        # subprocess.call(['ssh', 'jmeter', './home/wso2/clear.sh'])
        # subprocess.call(['ssh', 'jmeter', 'nohup ./jmeter/run-performance-tests.sh -m 4G -u 100 -b 50 -s 0 -d 4200 -w 120 -i h1c_passthrough_new &'])
        subprocess.call(['./killscript'])
        subprocess.call(['sleep 5'])
        subprocess.call(['./startscript'])
        time.sleep(60)
        # Set the variables for the initial state
        self.latency_99per = collect_metrics()
        self.done_counter = 0

    #         self.concurrency = concurrency
    #         self.usecase = usecase
    #         self.message_size = message_size

    def reset(self, seed=0):
        # subprocess.call(['ssh', 'jmeter', './home/wso2/killscript.sh'])
        # subprocess.call(['ssh', 'jmeter', './home/wso2/clear.sh'])
        # subprocess.call(['ssh', 'jmeter', 'nohup ./jmeter/run-performance-tests.sh -m 4G -u 100 -b 50 -s 0 -d 4200 -w 120 -i h1c_passthrough_new &'])
        subprocess.call(['./killscript'])
        subprocess.call(['sleep 5'])
        subprocess.call(['./startscript'])
        # Initialize the environment with the given parameters
        self.__init__(randomSeed=seed)

        # Set the initial state to [initial latency]
        self.initial_state = np.array([self.latency_99per,1,1,1])

        return self.initial_state

    def step(self, action):

        done = False
        info = None

        # action is the thread pool size
        # subprocess.call(['java', '-jar', 'MBean.jar', 'set', str(int((action[0]+1)*98+4))])
        # print("Predicted ",(action[0]+1)*98+4)

        subprocess.call(['java', '-jar', 'MBean.jar', 'set', str(int((action[0]) * 196 + 4))])
        print("Predicted ", (action[0]) * 196 + 4)

        # Wait for the changes to take effect
        time.sleep(10)

        # Set the new state
        prev_latency = self.latency_99per
        new_latency = collect_metrics()

        self.latency_99per = new_latency
        state = self.latency_99per

        # Calculate reward
        reward = -(new_latency - prev_latency)

        if (1 <= reward <= -1):
            self.done_counter += 1

        elif (self.done_counter > 0):
            self.done_counter -= 1

        if (self.done_counter == 10):
            done = True

        return (np.array([state,1,1,1]), np.array([reward]), done, info)

    def observation_space_dimension(self):
        # Return the dimension of the state
        return 4

    def action_space_dimension(self):
        # Return the dimension of the action
        return 1


data = []

previous_time = time.time()
previous_requests = 0

filter = ""
splitter = ""

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
elif (bal_file == "ballerina-echo.bal"):
    filter = "response_time_seconds(?:_mean|_stdDev|{).*EchoService\$\$service\$0.*timeWindow=\"60000\".*(?:quantile=\"0.999\"|quantile=\"0.99\"|,}).*"
    throughput_filter = "http_requests_total_value.*EchoService\$\$service\$0.*"
    splitter = "{http_url=\"/service/EchoService\",protocol=\"http\",http_method=\"POST\",resource=\"helloResource\",service=\"EchoService$$service$0\","


def collect_metrics():
    res = query_metrics()
    print(res)
    data.append(res)
    print("99th per : " + str(res["99per"]), "\n")
    return float(res["99per"])


def query_metrics():
    metrics_array = {
        "requests": 0,
        "throughput": 0,
        "mean": 0,
        "std_dev": 0,
        "99per": 0,
    }
    try:
        global previous_time
        global previous_requests

        URL = "http://127.0.0.1:9797/metrics"

        current_time = time.time()

        # sending get request and saving the response as response object
        r = requests.get(url=URL)

        data = r.text
        data_list = data.split("\n")



        # print(data)
        for line in data_list:
            try:
                x = re.findall(
                    filter,
                    line)

                throughput = re.findall(throughput_filter, line)
                if (throughput):
                    current_requests = float((throughput[0].split(" "))[1])

                    metrics_array["requests"] = current_requests
                    throughput_calculated = (current_requests - previous_requests) / (
                            current_time - previous_time)

                    metrics_array["throughput"] = throughput_calculated

                    previous_requests = current_requests

                s = x

                if s:
                    y = s[0].split(" ")
                    z = y[0].split(
                        splitter)

                    meanOrStd = z[0].split("response_time_seconds")
                    timeWindowAndQuantile = z[1].split("\"")

                    if (meanOrStd[1] == ''):
                        if (timeWindowAndQuantile[3] == "0.99"):
                            metrics_array["99per"] = float(y[1]) * 1000

                    elif (meanOrStd[1] == "_mean"):
                        metrics_array["mean"] = float(y[1]) * 1000

                    elif (meanOrStd[1] == "_stdDev"):
                        metrics_array["std_dev"] = float(y[1]) * 1000

            except Exception as e:
                pass

        previous_time = current_time

    except Exception as e:
        pass
    return metrics_array
