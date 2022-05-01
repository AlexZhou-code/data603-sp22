# **The big data security problems we encounter and how security platforms work**

## **I. Current situation**
Nowadays, network threats have evolved from traditional viruses to malicious attacks like worms and denial of service, etc. Today's network threats are becoming more and more sophisticated and are no longer limited to traditional viruses, Trojans, botnets, spyware, rogue software, network fraud, spam, worms, phishing, etc. are a serious threat to network security. Network attacks are often a blend of viruses, worms, Trojan horses, spying, scanning technology in one hybrid attack. Hackers use worms to create botnets and integrate more attack sources to focus on the target to launch a violent denial of service attack. Such a single anti-virus software or firewall and other security devices are difficult to block the hackers' attacks, so a more advanced linkage system is needed to prevent a variety of attacks, which gives birth to OSSIM, a security information management platform.

## **II. Introduction of OSSIM**
OSSIM provides a base platform that enables security monitoring functions by integrating open-source products. It aims to provide a centralized, organized, framework-based system capable of better monitoring and display. OSSIM is clearly positioned as an integrated solution, and its goal is not to develop a new feature, but to take advantage of the rich and powerful variety of programs (including Mrtg, Snort, Nmap, Openvas, and Ntop and other open-source system security software). Integrating them in an open architecture system environment that preserves their original functions and roles, OSSIM supports up to 2395 plug-ins so far (http://www.alienvault.com/community/plugins). The core work of the OSSIM project is responsible for integrating and correlating the information provided by the various products, as well as integrating related functions. Due to the advantages of open-source projects, these tools are already tried and tested, and have been tested in all aspects and are reliable.

![ OSSIM Architecture]( https://johnvidler.co.uk/linux-journal/LJ/242/11676f1.large.jpg)
*<p align="center"> Cited from https://johnvidler.co.uk/linux-journal/LJ/242/11676.html</p>*

# Module composition of OSSIM

OSSIM information security integrated management system is designed to be composed of five parts: security plug-in, agent process (Agent), association engine (Server), data warehouse (Database), and Web framework (Framework).

1). Security plug-ins (Plug-ins) that is, all kinds of security products and facilities. Such as firewalls, IDS and so on. Here we introduce the following open source security tools under Linux: Arpwatch, P0f, Snort, Nesus, Spade, Tcptrack, Ntop, Nagios, Osiris these plugins are aimed at a certain aspect of network security

2). Agent process
Agent process (Agent) will run on multiple or single host, responsible for collecting relevant information (such as alarm logs, etc.) from each security device, security tools, and will collect all kinds of information in a unified format, and then pass these data to the server.
3). Sensor
Sensor is usually understood as a program, but it is not a definite program, but a logical unit concept, in OSSIM, the Agent and the plug-in composition of a combination of network behavior monitoring function is called a sensor (Sensor), Sensor's functional range are mainly.
Intrusion detection (snort)
Vulnerability scanning (nessus)
Anomaly detection (Spade, p0f, pads, arpwatch, RRD ab behaviour)
Network traffic monitoring and profiling (ntop)
Capture local router, firewall, IDS and other hardware device logs as firewall used in specific deployments, the above functions can usually be deployed on a single server, or can be deployed in multiple servers.

4). Association Engine
Association engine (Server) is the core part of OSSIM security integrated management system, supporting distributed operation, responsible for correlating events transmitted by agents and risk assessment of network assets.

5). Data Warehouse
Data warehouse (Database) by the Server to write the correlation results to the Database, in addition, the system users (such as security administrators) can also read and write to the Database through Framework (web console). The data warehouse is the source of information for event analysis and policy adjustment of the whole system, which is divided into Event Database (EDB), Knowledge Database (KDB) and User Database (UDB) in general. This is also the biggest flaw of OSSIM architecture.

6).Web Framework
Web framework (Framework) console, providing users (security administrators) Web page to control the operation of the system (such as setting policies), is the front end of the entire system, used to achieve the user and the system B / S mode of interaction (in fact, a hybrid model of C / S + B / S). Frameworkd is a daemon that binds the knowledge base and event base of OSSIM and listens to port 40003. It is responsible for correlating user commands received by Fromend with other components of the system and drawing Web charts for front-end display.


![Log Collection and Normalization](https://johnvidler.co.uk/linux-journal/LJ/242/11676f2.large.jpg)

# Deployment of OSSIM
For shared networks, the function of collecting network traffic data can be achieved by simply setting the network interface connected to the traffic collection point in the shared network to hybrid operation mode. Compared with the switched network, the reliability of the hub network is low when the network is congested, and SNMP interrogation commands and response packets may be delayed or lost, when NTOP also detects the data inaccurately, and for the case of switched network, the support of switching equipment (such as a switch with SPAN ports) is required.

Ossim traffic collection host is generally connected to a port of the switch device where the server Vlan is located, through the switch's SPAN to (Switched PortAnalyzer) port to analyze all traffic mirrored to this collection point. SPAN is very flexible in use, can monitor a single port of the switch, but also can monitor multiple source ports, but the destination port There can be only one destination port.

![How to Calculate the Risk Associated with an Event](https://johnvidler.co.uk/linux-journal/LJ/242/11676f3.large.jpg)


# OSSIM process analysis

In the following we briefly analyze the system workflow of OSSIM.

1). The detectors (Sensor), which are the safety plug-ins of the whole system, perform their respective tasks and give alarms when problems are found.

2). The alarm information of each detector will be collected and centralized.

3). Each alarm record will be parsed and stored in the event database (EDB).

4). Each event is given a priority according to the set policy.

5). Risk assessment of events and calculation of a risk factor for each alarm.

6). Send each event with priority to the correlation engine, which will correlate the events.

Note: The correlation engine means that on the basis of the alarm events reported by each intrusion detection sensor (intrusion detection system, firewall, etc.), it forms the intrusion behavior determination after correlation analysis, and reports the correlation analysis results to the console.

7). After correlation analysis of one or more events, the correlation engine generates new alarm records, assigns them also to priority, and performs risk assessment and stores them in the database.

8). The user monitoring monitor will generate a real-time risk map based on each event.

9). The most recent correlation alarm record is given in the control panel and the full event record is provided in the bottom console.

![Example of Analysis and Correlation of Events](https://johnvidler.co.uk/linux-journal/LJ/242/11676f4.large.jpg)

## Conclusion:
The number of security events generated by security devices and network applications is huge, and usually 99% of security events are false alarms, while a small number of security events with real threats are submerged in false alarm information and difficult to identify. The relationship between the horizontal and vertical aspects (e.g., different spatial sources, time series, etc.) that exist between security events cannot be analyzed in an integrated manner, and therefore the underreporting is serious and cannot be predicted in real time. An attack activity is often followed by another attack activity, with the former providing the basic conditions for the latter; an attack activity generates security events on multiple security devices; security events from multiple different sources are actually a collaborative attack, all of which lack effective integrated analysis. Security managers lack global real-time awareness of the overall network security posture. Leverage the detection capabilities of multiple security devices, the fatal weakness of centralized processing is the huge amount of data to be analyzed and processed, those huge redundancies, independently scattered, security events obviously can not be used directly as a basis for response


## Reference:
https://johnvidler.co.uk/linux-journal/LJ/242/11676.html
https://www.verizon.com/business/resources/reports/dbir/2021/masters-guide/ https://www.ibm.com/downloads/cas/BK0BB0V1
https://cve.mitre.org/cve/data_feeds.html
https://cybersecurity.att.com/products/ossim
https://github.com/ossimlabs/ossim