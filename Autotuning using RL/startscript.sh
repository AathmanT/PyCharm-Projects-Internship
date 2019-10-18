#!/usr/bin/env bash
nohup java -jar ~/LocalBuildBallerinaPerformanceTest/performanceCommon/performance-common/components/netty-http-echo-service/target/netty-http-echo-service-0.3.1-SNAPSHOT.jar &

nohup /home/aathmsn/Downloads/Compressed/Test/ballerina-0.990.2-SNAPSHOT/bin/ballerina run -e b7a.runtime.scheduler.corepoolsize=100 -e b7a.runtime.scheduler.maxpoolsize=100 -e b7a.runtime.scheduler.queuetype=default-linked -e b7a.runtime.scheduler.keepalivetime=60 --observe ~/LocalBuildBallerinaPerformanceTest/extracted\ from\ the\ zip/ballerina/bal/h1c_h1c_passthrough.bal &

sleep 10

nohup ~/Downloads/apache-jmeter-5.1.1/bin/jmeter -n -t ~/Downloads/apache-jmeter-5.1.1/bin/SequentialTest.jmx &