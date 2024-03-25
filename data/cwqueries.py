cw_data = [
    {
        "text": "Show all logs where the values forloggingType are ERROR",
        "query": """fields @message
| parse @message "[*] *" as loggingType, loggingMessage
| filter loggingType = "ERROR"
| display loggingMessage"""
    },
    {
        "text": "show the latest 20 log events",
        "query": """fields @timestamp, @message
| sort @timestamp desc
| limit 20"""
    },
    {
        "text": "show latest 20 logs with range greater than 3000",
        "query": """fields @timestamp, @message
| filter (range>3000)
| sort @timestamp desc
| limit 20"""
    },
    {
        "text": "show latest 20 logs with range greater than 3000 in account with id 123456789012",
        "query": """fields @timestamp, @message
| filter (range>3000 and accountId=123456789012)
| sort @timestamp desc
| limit 20"""
    },
    {
        "text": "show all logs where the field logGroup is example_group",
        "query": """fields @timestamp, @message
| filter logGroup in ["example_group"]"""
    },
    {
        "text": "show logs where f1 contain the word Exception",
        "query": """fields f1, f2, f3 
| filter f1 like "Exception" """
    },
    {
        "text": "show logs where f1 contain the word Exception",
        "query": """fields f1, f2, f3 
| filter f1 =~ /Exception/"""
    },
    {
        "text": "show logs where f1 contain the word Exception",
        "query": """fields f1, f2, f3 
| filter f1 like /Exception/"""
    },
    {
        "text": "show logs where f1 begins with string ServiceLog",
        "query": """fields f1, f2, f3
| filter f1 like /ServiceLog./"""
    },
    {
        "text": "show logs where f1 includes the string ServiceLog",
        "query": """fields f1, f2, f3
| filter f1 like /ServiceLog.*/"""
    },
    {
        "text": "show logs where f1 doesn't contain the word Exception",
        "query": """fields f1, f2, f3 
| filter f1 not like "Exception" """
    },
    {
        "text": "show logs where f1 doesn't contain the word Exception or exception",
        "query": """fields f1, f2, f3 
| filter f1 like /(?i)Exception/"""
    },
    {
        "text": "identify all patterns in logs with containing ERROR",
        "query": """filter @message like /ERROR/
| pattern @message"""
    },
    {
        "text": "identify all patterns and count of logs that start with 'Failed to do: *'" ,
        "query": """filter @message like /ERROR/
| parse @message 'Failed to do: *' as cause
| pattern cause
| sort @sampleCount asc"""
    },
    {
        "text": "Use a glob expression to extract the fields @user, @method, and @latency from the log field @message and return the average latency for each unique combination of @method and @user.",
        "query": """parse @message "user=*, method:*, latency := *" as @user,
    @method, @latency | stats avg(@latency) by @method,
    @user"""
    },
    {
        "text": "Use a regular expression to extract the fields @user2, @method2, and @latency2 from the log field @message and return the average latency for each unique combination of @method2 and @user2.",
        "query": """parse @message /user=(?<user2>.*?), method:(?<method2>.*?),
    latency := (?<latency2>.*?)/ | stats avg(latency2) by @method2, 
    @user2"""
    },
    {
        "text": "Extracts the fields loggingTime, loggingType and loggingMessage, filters down to log events that contain ERROR or INFO strings, and then displays only the loggingMessage and loggingType fields for events that contain an ERROR string.",
        "query": """fields @message
    | parse @message "* [*] *" as loggingTime, loggingType, loggingMessage
    | filter loggingType IN ["ERROR", "INFO"]
    | display loggingMessage, loggingType = "ERROR" as isError"""
    },
    {
        "text": "find the top 15 packet transfers across hosts from Amazon VPC flow logs",
        "query": """stats sum(packets) as packetsTransferred by srcAddr, dstAddr
    | sort packetsTransferred  desc
    | limit 15"""
    },
    {
        "text": "first find the total traffic volume in 5-minute bins, then calculates the highest, lowest, and average traffic volume among those 5-minute bins.",
        "query": """FIELDS strlen(@message) AS message_length
| STATS sum(message_length)/1024/1024 as logs_mb BY bin(5m)
| STATS max(logs_mb) AS peak_ingest_mb, 
        min(logs_mb) AS min_ingest_mb, 
        avg(logs_mb) AS avg_ingest_mb"""
    },
    {
        "text": "find the number of distinct IP addresses in sessions and find the number of sessions by client platform, filter those IP addresses, and then finally find the average of session requests per client platform.",
        "query": """STATS count_distinct(client_ip) AS session_ips, 
      count(*) AS requests BY session_id, client_platform
| FILTER session_ips > 1
| STATS count(*) AS multiple_ip_sessions, 
        sum(requests) / count(*) AS avg_session_requests BY client_platform"""
    },
    {
        "text": "first combine messages into 5-minute blocks, then aggregate those 5-minute blocks into 10-minute blocks and calculate the highest, lowest, and average traffic volumes within each 10-minute block.",
        "query": """FIELDS strlen(@message) AS message_length
| STATS sum(message_length) / 1024 / 1024 AS logs_mb BY BIN(5m) as @t
| STATS max(logs_mb) AS peak_ingest_mb, 
        min(logs_mb) AS min_ingest_mb,
        avg(logs_mb) AS avg_ingest_mb BY dateceil(@t, 10m)"""
    },
    {
        "text": "show recent logs with unique value of server field",
        "query": """fields @timestamp, server, severity, message 
| sort @timestamp asc 
| dedup server"""
    },
    {
        "text": "Find the 25 most recently added log events.",
        "query": """fields @timestamp, @message | sort @timestamp desc | limit 25"""
    },
    {
        "text": "Get a list of the number of exceptions per hour.",
        "query": """filter @message like /Exception/ 
| stats count(*) as exceptionCount by bin(1h)
| sort exceptionCount desc"""
    },
    {
        "text": "Get a list of log events that aren't exceptions.",
        "query": """fields @message | filter @message not like /Exception/"""
    },
    {
        "text": "Get the most recent log event for each unique value of the server field.",
        "query": """fields @timestamp, server, severity, message 
| sort @timestamp asc 
| dedup server"""
    },
    {
        "text": "Get the most recent log event for each unique value of the server field for each severity type.",
        "query": """fields @timestamp, server, severity, message 
| sort @timestamp desc 
| dedup server, severity"""
    },
    {
        "text": "Determine the amount of overprovisioned memory.",
        "query": """filter @type = "REPORT"
| stats max(@memorySize / 1000 / 1000) as provisonedMemoryMB,
    min(@maxMemoryUsed / 1000 / 1000) as smallestMemoryRequestMB,
    avg(@maxMemoryUsed / 1000 / 1000) as avgMemoryUsedMB,
    max(@maxMemoryUsed / 1000 / 1000) as maxMemoryUsedMB,
    provisonedMemoryMB - maxMemoryUsedMB as overProvisionedMB"""
    },
    {
        "text": "Create a latency report.",
        "query": """filter @type = "REPORT" |
stats avg(@duration), max(@duration), min(@duration) by bin(5m)"""
    },
    {
        "text": "Search for slow function invocations, and eliminate duplicate requests that can arise from retries or client-side code. In this query, @duration is in milliseconds.",
        "query": """fields @timestamp, @requestId, @message, @logStream 
| filter @type = "REPORT" and @duration > 1000
| sort @timestamp desc
| dedup @requestId 
| limit 20"""
    },
    {
        "text": "Find the top 15 packet transfers across hosts:",
        "query": """stats sum(packets) as packetsTransferred by srcAddr, dstAddr
| sort packetsTransferred  desc
| limit 15"""
    },
    {
        "text": "Find the top 15 byte transfers for hosts on a given subnet.",
        "query": """filter isIpv4InSubnet(srcAddr, "192.0.2.0/24")
| stats sum(bytes) as bytesTransferred by dstAddr
| sort bytesTransferred desc
| limit 15"""
    },
    {
        "text": "Find the IP addresses that use UDP as a data transfer protocol.",
        "query": """filter protocol=17 | stats count(*) by srcAddr"""
    },
    {
        "text": "Find the IP addresses where flow records were skipped during the capture window",
        "query": """filter logStatus="SKIPDATA"
| stats count(*) by bin(1h) as t
| sort t"""
    },
    {
        "text": "Find a single record for each connection, to help troubleshoot network connectivity issues.",
        "query": """fields @timestamp, srcAddr, dstAddr, srcPort, dstPort, protocol, bytes 
| filter logStream = 'vpc-flow-logs' and interfaceId = 'eni-0123456789abcdef0' 
| sort @timestamp desc 
| dedup srcAddr, dstAddr, srcPort, dstPort, protocol 
| limit 20"""
    },
    {
        "text": "Find the distribution of records per hour by query type.",
        "query": """stats count(*) by queryType, bin(1h)"""
    },
    {
        "text": "Find the 10 DNS resolvers with the highest number of requests.",
        "query": """stats count(*) as numRequests by resolverIp
| sort numRequests desc
| limit 10"""
    },
    {
        "text": "Find the number of records by domain and subdomain where the server failed to complete the DNS request.",
        "query": """filter responseCode="SERVFAIL" | stats count(*) by queryName"""
    },
    {
        "text": "Find the number of log entries for each service, event type, and AWS Region.",
        "query": """stats count(*) by eventSource, eventName, awsRegion"""
    },
    {
        "text": "Find the Amazon EC2 hosts that were started or stopped in a given AWS Region.",
        "query": """filter (eventName="StartInstances" or eventName="StopInstances") and awsRegion="us-east-2" """
    },
    {
        "text": "Find the AWS Regions, user names, and ARNs of newly created IAM users.",
        "query": """filter eventName="CreateUser"
| fields awsRegion, requestParameters.userName, responseElements.user.arn"""
    },
    {
        "text": "Find the number of records where an exception occurred while invoking the API UpdateTrail.",
        "query": """filter eventName="UpdateTrail" and ispresent(errorCode)
| stats count(*) by errorCode, errorMessage"""
    },
    {
        "text": "Find log entries where TLS 1.0 or 1.1 was used",
        "query": """filter tlsDetails.tlsVersion in [ "TLSv1", "TLSv1.1" ]
| stats count(*) as numOutdatedTlsCalls by userIdentity.accountId, recipientAccountId, eventSource, eventName, awsRegion, tlsDetails.tlsVersion, tlsDetails.cipherSuite, userAgent
| sort eventSource, eventName, awsRegion, tlsDetails.tlsVersion"""
    },
    {
        "text": "Find the number of calls per service that used TLS versions 1.0 or 1.1",
        "query": """filter tlsDetails.tlsVersion in [ "TLSv1", "TLSv1.1" ]
| stats count(*) as numOutdatedTlsCalls by eventSource
| sort numOutdatedTlsCalls desc"""
    },
    {
        "text": "Find the last 10 4XX errors",
        "query": """fields @timestamp, status, ip, path, httpMethod
| filter status>=400 and status<=499
| sort @timestamp desc
| limit 10"""
    },
    {
        "text": "Identify the 10 longest-running Amazon API Gateway requests in your Amazon API Gateway access log group",
        "query": """fields @timestamp, status, ip, path, httpMethod, responseLatency
| sort responseLatency desc
| limit 10"""
    },
    {
        "text": "Return the list of the most popular API paths in your Amazon API Gateway access log group",
        "query": """stats count(*) as requestCount by path
| sort requestCount desc
| limit 10"""
    },
    {
        "text": "Create an integration latency report for your Amazon API Gateway access log group",
        "query": """filter status=200
| stats avg(integrationLatency), max(integrationLatency), 
min(integrationLatency) by bin(1m)"""
    },
    {
        "text": "Find the instances that are sending the most traffic through your NAT gateway.",
        "query": """filter (dstAddr like 'x.x.x.x' and srcAddr like 'y.y.') 
| stats sum(bytes) as bytesTransferred by srcAddr, dstAddr
| sort bytesTransferred desc
| limit 10"""
    },
    {
        "text": "Determine the traffic that's going to and from the instances in your NAT gateways.",
        "query": """filter (dstAddr like 'x.x.x.x' and srcAddr like 'y.y.') or (srcAddr like 'xxx.xx.xx.xx' and dstAddr like 'y.y.')
| stats sum(bytes) as bytesTransferred by srcAddr, dstAddr
| sort bytesTransferred desc
| limit 10 """
    },
    {
        "text": "For uploads determine the internet destinations that the instances in your VPC communicate with most often for uploads and downloads.",
        "query": """filter (srcAddr like 'x.x.x.x' and dstAddr not like 'y.y.') 
| stats sum(bytes) as bytesTransferred by srcAddr, dstAddr
| sort bytesTransferred desc
| limit 10"""
    },
    {
        "text": "For downloads determine the internet destinations that the instances in your VPC communicate with most often for uploads and downloads.",
        "query": """filter (dstAddr like 'x.x.x.x' and srcAddr not like 'y.y.') 
| stats sum(bytes) as bytesTransferred by srcAddr, dstAddr
| sort bytesTransferred desc
| limit 10"""
    },
    {
        "text": "Find the most relevant fields, so you can review your access logs and check for traffic in the /admin path of your application.",
        "query": """fields @timestamp, remoteIP, request, status, filename| sort @timestamp desc
| filter filename="/var/www/html/admin"
| limit 20"""
    },
    {
        "text": "Find the number unique GET requests that accessed your main page with status code '200' (success).",
        "query": """fields @timestamp, remoteIP, method, status
| filter status="200" and referrer= http://34.250.27.141/ and method= "GET"
| stats count_distinct(remoteIP) as UniqueVisits
| limit 10"""
    },
    {
        "text": "Find the number of times your Apache service restarted.",
        "query": """fields @timestamp, function, process, message
| filter message like "resuming normal operations"
| sort @timestamp desc
| limit 20"""
    },
    {
        "text": "Get the number of EventBridge events grouped by event detail type",
        "query": """fields @timestamp, @message
| stats count(*) as numberOfEvents by `detail-type`
| sort numberOfEvents desc"""
    },
    {
        "text": "Find the 10 slowest requests",
        "query": """fields @timestamp, @message, @duration 
| sort @duration desc 
| limit 10"""
    },
    {
        "text": "Show top 20 slowest requests instead and display requestId as a column",
        "query": """fields @timestamp, @message, @requestId, @duration 
| sort @duration desc 
| limit 20"""
    }
]