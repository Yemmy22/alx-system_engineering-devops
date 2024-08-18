INCIDENT SUMMARY:
Between the hours of 14:30 and 16:02 UTC on the 17th of August, 2024, 20 Million users were denied access to a subset of services on our application. 
The event was triggered following deployment of application upgrades at 14:30 UTC. 
The update contained code for creation of new server blocks intended to host files for new services being rolled out by the company.
A bug in this code caused essential configuration filenames to rename with incorrect extension thereby, invalidating the overall configuration setup leading to server downtime. 
The event was detected by our datadog monitoring system and on-call persons were alerted via PagerDuty and Slack app.  The incident response team swiftly commenced troubleshooting the possible causes including DDOS attack, network bugs, request overload and code bugs on recently deployed applications.
This is a major (level 2) incident which affected 20% of our web application users.
There was further impact as noted by mentions on social media especially Twitter and LinkedIn of the event, as well as multiple calls to the customer service department, raised in relation to this incident. 
 
 


TIMELINE: 


14:30 UTC - On the 17th of August, 2024, our integrated datadog/PagerDuty monitoring system was triggered and the Head of Engineering was paged. A surge in user complaints to our customer hotlines further confirmed the emergency.
14:48 UTC - Next, an on-call network engineer was paged, because the Head of Engineering didn't own the service, delaying the response by 17 minutes.
15:05 UTC - After receiving a page, a network engineer came online on the Slack app.
15:20 UTC – The network engineer confirmed the absence of networking impediments because ICMP tests from remote origins returned response signals from the affected node and the existing firewall rules supported bidirectional interaction.  This led to the assumption that there might be a need to review cluster configuration on affected nodes.
 
15:23 UTC - Because the engineer did not have a background on the assumed cause affecting the EC2 nodes, a second alert was sent to a full stack engineer who came into the room at 15:33 UTC.
 
15:33 UTC – The backend engineer focused on system configuration and resource retrieval  tests, and discovered a failure to generate response once the web application URI requests at a certain level of file path.
16:02 UTC – The issue was resolved and the affected server was back to serving resources which it was previously unable to serve.
 ROOT CAUSE AND RESOLUTION:
The application had an outage because the server could not respond to requests received.
The request could not be responded because relevant files at root of the node were inaccessible
The files were inaccessible because there was a mismatch in name of files requested and files available to be served.
Because a change was pushed resulting in mismatch occasioned by erroneous file extension name.


RESOLUTION:
We used a three-pronged approach to the recovery of the system by rolling back the most recent upgrades and reverted configuration builds to the older version being part of the last known system wide modifications. This was aimed to swiftly achieve uptime on the affected node.
By increasing the size of unaffected EC2 Auto Scaling Group to increase the number of nodes available to support the workload which affected EC2s couldn’t serve, and reduce the likelihood of scheduling on oversubscribed nodes.
Disabled the Escalator autoscaler to prevent the clusters from aggressively scaling-down
Reverted the Build Engineering on the affected nodes to the previous version and redeployed a reviewed configuration build which fulfills the intent of the previous deployment without error.
    
 CORRECTIVE ACTIONS:
What can be improved/fixed:
Generally, we must review our operations strategy in respect of deployment and ensure updates are well tested to avoid conflicts that break existing systems and ground operations. We can improve the accuracy of our alert systems and designated on-call persons to provide swifter resolution to emergent challenges in the future.
Addressing the issue:
In order to avoid a recurrence we must ensure that unit test verify that work has been properly maintained before builds are pushed
Bulk operation workloads which are atypical of normal operation should be reviewed.
Bulk ops should start slowly and monitored, increasing when service metrics appear nominal.
Introduction of a secondary mechanism to collect information across clusters.

