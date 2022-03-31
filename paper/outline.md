（this part almost done）
# What are the security issues facing Big Data
The data stored in Big Data is very huge and often stored in a distributed manner, and it is because of this storage method, the storage path view is relatively clear, and the data volume is too large, resulting in data protection, relatively simple, hackers more easily use the relevant vulnerabilities to implement illegal operations, causing security problems. Although big data security still inherits the three characteristics of traditional data security confidentiality, integrity and availability, but also has its own special characteristics.

（this part still working on it）
# Technical issues and challenges facing big data security
Big data security threats permeate all aspects of the big data industry chain, including data production/collection, processing and sharing, and the causes of risk are complex and intertwined; there are both external attacks and internal leaks; there are both technical vulnerabilities and management flaws; there are both new risks triggered by new technologies and new models, and there are also traditional security issues that continue to trigger. This report will focus on the security threats faced by big data itself, analyze from three aspects of big data platform security, data security and personal information security, and identify the security needs of big data.






(A) platform security issues and challenges
1, big data platform in Hadoop open source model lack of overall security planning, their own security mechanisms have limitations

2, big data platform services for many users, a variety of scenarios, the performance of traditional security mechanisms can hardly meet the demand

3、The large-scale distributed storage and computing mode of the big data platform leads to exponential growth in the difficulty of security configuration

4, for the big data platform network attack means present new features, traditional security monitoring technology exposure is insufficient

(II) data security issues and challenges

1, the number of data leakage incidents continues to grow, causing increasingly serious harm Big data has become a significant target of network attacks because of its huge value and centralized storage management model

2, data collection link has become a new risk point affecting decision analysis

3、The confidentiality protection problem in the data processing process is gradually emerging

4、The complexity of the data flow path makes it extremely difficult to trace the source

(C) personal privacy security challenges
1、Traditional privacy protection technology faces the possibility of failure due to the superb analytical capability of big data

2, traditional privacy protection technology is difficult to adapt to the non-relational database of big data












# **I. Big data security risks**

(A) Big data suffers from unusual flow attacks

　　The data stored in big data is very huge, often using distributed storage, and it is because of this storage method, the storage path view is relatively clear, and the amount of data is too large, resulting in data protection, relatively simple, hackers more easily use the relevant vulnerabilities, the implementation of illegal operations, causing security problems. Due to the very large number of end users in the big data environment and the large number of audience types, the authentication link for customer identity requires a lot of processing power. As the APT attack has a strong target, and the attack time is long, once the attack is successful, the final data output from the big data analysis platform will be obtained, which is easy to cause the greater information security risks.

　　**(B) Big data information leakage risk**

　　The risk of information leakage of big data platform in the data collection and information mining of big data, we should pay attention to the security of user privacy data, and carry out data mining without leaking user privacy data. What needs to be considered is to ensure that the user privacy data within each storage point is not illegally leaked and used during the information transmission and data exchange of distributed computing is the main issue of information security in the current big data context. At the same time, the current volume of big data data is not fixed, but dynamically increased in the application process, but most of the traditional data privacy protection technologies are for static data, so how to effectively deal with the dynamic data attributes and expressions of big data data privacy protection is also a security issue to focus on. Finally, the data of big data is far more complex than traditional data, and whether the privacy protection of existing sensitive data can meet the complex data information of big data is also a security issue that should be considered.

　　**(C) Security risks in the process of big data transmission**

　　Data life cycle security issues. Along with the rapid development of big data transmission technology and applications, more and more security risks are gradually exposed in all stages and links of the big data transmission life cycle. For example, the big data transmission link, in addition to the risk of leakage and tampering, may also be used by data stream attackers, and the data may be gradually distorted in the dissemination, etc. Another example is that, in addition to the risk of unauthorized use and destruction of data in the big data transmission processing link, due to the heterogeneous, multi-source and correlation characteristics of big data transmission, even if multiple data sets are desensitized and processed individually, there is still the risk of personal information leakage due to correlation analysis of data sets.

　　Infrastructure security issues. As the main carrier and infrastructure for big data transmission and convergence, cloud computing provides storage place, access channel, and virtualized data processing space for big data transmission. Therefore, the security of stored data in the cloud platform has also become a major factor hindering the development of big data transmission.

　　Personal privacy security issues. Under the condition that the existing privacy protection regulations are not sound and privacy protection technology is not perfect, personal privacy leaks on the Internet lose control, and social software such as WeChat, Weibo and QQ hold the social relationship of users, monitoring systems record people's chat, Internet and travel records, and online payment and shopping websites record people's consumption behavior. However, in the era of big data transmission, the threat people face is not only limited to the leakage of personal privacy, but also the prediction of people's status and behavior based on big data transmission. In recent years, the leakage of personal information of social security system in many domestic provinces and the leakage of 12306 account information and other big data transmission security incidents show that big data transmission not properly handled can cause great infringement on user privacy. Therefore, in the big data transmission environment, how to manage the data well and protect personal privacy while ensuring the benefits of data usage is one of the great challenges faced in the era of big data transmission.

　　**(iv) Storage management risk of big data**

　　The data type and data structure of big data are incomparable to traditional data. On the storage platform of big data, the data volume is non-linear or even exponential speed growth, and the data storage of various types and various structures will inevitably trigger the concurrent and frequent disorderly operation of multiple application processes, which will easily cause data storage misalignment and data management chaos, and bring about big data storage and later processing for Security risks. Whether the current data storage management system can meet the data storage requirements of massive data in the context of big data remains to be tested. However, if the data management system is not upgraded with corresponding security mechanisms, it will be too late when problems arise.

## **Second, big data security challenges**

　　Although big data security still inherits the three characteristics of traditional data security confidentiality, integrity and availability, it also has its special characteristics, mainly in the following two aspects.

　　(a) personal privacy protection

　　Previously, data was an enterprise's asset, which was used within the enterprise and in a local environment, and the mobility was not strong, so the personal privacy of data was not outstanding. However, in the Internet+ era, data are everywhere, and various data are accumulated to form multiple data associations, which can be used by lawless elements and people with ulterior motives to cause personal privacy information leakage through multiple data association analysis. How to effectively protect personal privacy is the first important issue facing big data security.

　　(II) Cross-border data flow

　　In the present era, the flow of data is important. Global shopping promotions are participated by several countries, and the cross-border flow of data is a special attribute of big data. It is important to protect the security of cross-border data in terms of legal system, data service outsourcing, and combating cybercrime.

　　Therefore, when establishing the framework of big data security standards system, we should analyze the applicability of security standards in all aspects of the life cycle of traditional data collection, organization, storage, and processing, and then adopt the suitable ones, revise the unsuitable ones, and add the missing ones.

　　External unauthorized personnel to the information system for malicious intrusion, illegal access to private data; data has easy replicability, after the occurrence of data security events, can not be effective traceability and audit; big data has the flow, sharing needs, a large number of data convergence transmission increased the risk of data leakage.

　　(C) Traditional security measures are difficult to adapt

　　The characteristics of big data massive, multi-source, heterogeneous and dynamic lead to complex storage structure of big data system, openness, distributed computing and efficient and accurate services, these special needs cannot be solved by traditional security measures.

　　(D) platform security mechanism needs to be improved

　　We used to use ORACLE database, and in the era of big data, everyone based on hadoop architecture. In the hadoop architecture, the user's identity identification and authorized access and other security capabilities are weak. At the same time some components of open source hadoop are not tested when used, there may be vulnerabilities and malicious code inside, and there are backdoors opened by people.

　　(E) Application access control is becoming more and more complex

　　In the database era application access control through the database access mechanism to solve. Each user has to register, and only after registration can access to the database. But in the era of big data, there are a large number of unknown users and a large number of unknown data, there are many users who do not know his identity, although he registered also do not know who he is, so pre-set roles and pre-set permissions for the role can not be done.

　　What are the security problems faced by big data. Zhongchen Magic Big Data Platform says Big Data has made a huge impact and brought profound influence on our social and economic activities. It will definitely be a trend to make full use of big data technology to tap the great value of information so as to realize and form a strong competitive advantage.

https://www.verizon.com/business/resources/reports/dbir/2021/masters-guide/
https://www.ibm.com/downloads/cas/BK0BB0V1
https://cve.mitre.org/cve/data_feeds.html
