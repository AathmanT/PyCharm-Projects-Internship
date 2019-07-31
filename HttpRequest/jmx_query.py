import jmxquery

jmxConnection = jmxquery.JMXConnection("service:jmx:rmi:///jndi/rmi://localhost:1234/jmxrmi")
jmxQuery = [jmxquery.JMXQuery("com.ballerina.autotuning:type=basic,name=dynamicTuning")]
#jmxQuery = [jmxquery.JMXQuery("com.baeldung.tutorial:name=game,type=basic")]
#jmxQuery = [jmxquery.JMXQuery("*:*")]

metrics = jmxConnection.query(jmxQuery)
for metric in metrics:
    print(f"{metric.to_query_string()} ({metric.value_type}) = {metric.value}")
