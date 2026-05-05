# Bynder Security and Compliance – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance

In the digital age, securing assets is paramount. At Bynder, we understand this necessity and have developed our Digital Asset Management (DAM) Software as a Service (SaaS) platform with a security-first approach. Our commitment to providing robust, out-of-the-box security measures ensures that our customers' digital assets are protected with the highest standards of security.

Bynder certification and compliance[](https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance#h_01HJ48XST2C9RCJ0QA4TVTHNKR)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Bynder currently holds the following certifications and complies with the following requirements:  
ISO 27001:2013  
ISO 27018:2019  
ISO 22301:2019  
PCI-DSS  
HIPAA  
GDPR  
CCPA

The Bynder products, processes, and systems are audited annually by an external third party against the different ISO standards. Next to this third-party verification, of which we can share summary reports and certifications under NDA, Bynder continuously monitors the effectiveness of its Security and Privacy controls and conducts internal audits.

Security management and policies[](https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance#h_01HJ48YAATKR83J4E46N146MJ3)

----------------------------------------------------------------------------------------------------------------------------------------------------------

Security policies are documented in our Information Security Management System (ISMS) control document, are approved by the management, and are enforced continuously through monitoring and internal audits. All policy changes are communicated, and training is provided to ensure everyone keeps abreast of the requirements.

Bynder's information security strategy is reviewed annually by the Chief Information Security Officer and is translated into Bynder's information security policy (ISP). Additionally, any contracts with third parties require conformity with Bynder security policies. Third parties must provide assurance (certification or an evidenced strong internal security program) of protecting their customers' data or results from recent penetration tests. Additionally, third parties must accept liability for any incidents and sign acceptance against our ISP.

We have clear incident response procedures, incident handling, and escalation procedures. For the top 10 identified risks, we have a clear response plan ready. Also, there's a fallback incident escalation plan for situations that do not fit the previously identified risks.

Data security[](https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance#h_01HJ48YTR5HS3H4HRAV0GP4C36)

---------------------------------------------------------------------------------------------------------------------------------------

**Encryption at rest:** All customer data stored in our database and S3 are encrypted at rest. Bynder uses AWS SSE-S3. SSE-S3 uses one of the strongest block ciphers available, 256-bit Advanced Encryption Standard (AES-256), to encrypt customer data

**Encryption in transit:** Customer data flowing over the public Internet is protected with TLSv1.2 or higher.

**Access control:** Bynder has formalized policies regarding access controls based on ISO 27001:2013. Bynder employs the fundamentals of least privilege, need to know, and segregation of duties regarding access management. Access rights are reviewed every quarter.

**Data hosting location:** Bynder partners with Amazon Web Services to host client data. Bynder currently uses the following data centers that are supplemented by Content Delivery Network (Cloudfront) for optimal local delivery:

*   ap-northeast-1 (S3 server in Asia Pacific, Tokyo)
*   eu-central-1 (S3 server in EU, Frankfurt)
*   us-east-1 (S3 server in US East - North Virginia)
*   us-west-1 (S3 server in US West - California)

As a definitive client decision, the Customer can choose from the following options to host its data:

**Option 1: EU-ONLY -** Customer selects to be hosted EU-only. The customer does not want any of its Customer data to be stored outside the European Economic Area. With this selection, the Customer's Bynder environment will be hosted in Frankfurt, Germany.

**Option 2: GLOBAL -** Customer selects to be hosted Globally. With our Global setup, customers can benefit from our multi-regional architecture. During the implementation, the Customer will have the option to choose the AWS Data Centre(s) on which it wishes to store its Customer Data: US West Coast (California), US East Coast (Virginia), Frankfurt (Germany), and Tokyo (Japan). Uploaded files will remain on the chosen Data Centre(s). All other information (e.g., usernames, configuration, settings) and all the metadata about uploaded assets will be replicated globally on Bynder's AWS clusters to provide individual Users with local speeds when accessing and working with the Product worldwide.

**Option 3: US-ONLY -** Customer selects to be hosted US-ONLY. The customer does not want any of its Customer data to be stored outside of the United States of America (USA). With this selection, Customer's Bynder environment will be hosted in Oregon and Ohio, USA.

Durability and backups[](https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance#h_01HJ490WWV2GJEVZWJ053G8JWP)

------------------------------------------------------------------------------------------------------------------------------------------------

### Durability

As a pure cloud vendor, Bynder was specifically designed and engineered for the SaaS infrastructure (AWS) on which it was born. All architecture and technology standards follow AWS best practices. The architecture follows a 3-tier and future-oriented design using microservices that are fully redundant, actively monitored, and auto-scaling.

### Backup

We back up data with continuous replication and use AES-256 to encrypt our backups. The recovery point objective (RPO) is 24 hours, and the recovery time objective (RTO) is a maximum of 1hr. The details of our backup policy have been laid out in the SLA.

### Physical security

Bynder implemented the following physical security measures in its different offices:

*   Doors are secured to prevent unauthorized access,
*   Only authorized personnel have access, either by access card or key, to their respective office,
*   Access is reviewed every quarter,
*   Personnel must always close the outer office doors,
*   Ground-level street-facing windows are secured with additional measures such as barred windows and security cameras.
*   All offices are secured with an alarm system.

Additionally, our hosting partner, Amazon Web Services data centers, is state of the art, utilizing innovative architectural and engineering approaches. Amazon has many years of experience designing, constructing, and operating large-scale data centers. This experience has been applied to the AWS platform and infrastructure. For more information about the security of AWS' data centers, please see here [https://aws.amazon.com/compliance/data-center/controls/](https://aws.amazon.com/compliance/data-center/controls/)
.

Network security[](https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance#h_01HJ492WQ70G0DE6WSVTRQKHQV)

------------------------------------------------------------------------------------------------------------------------------------------

Bynder Infrastructure Design defines the security levels and networks used internally. NAT is implemented in our environment to hide the internal network from the Internet, and all the external connections are approved during a formal procedure. Additionally, as required by our ISO27001:2013 implementation, we perform vulnerability assessments or penetration tests on your Internet-facing connections at least once a year and after any significant modifications.

The firewall rules are reviewed monthly, and firewall logs and IDS logs are used for qualification. Logs are retained indefinitely and are checked continuously and automatically for malicious behavior.  
Policies and procedures are established, supporting business processes and technical measures implemented to protect wireless network environments, including the following:

*   Perimeter firewalls implemented and configured to restrict unauthorized traffic.
*   Security settings enabled with strong encryption for authentication and transmission, replacing vendor default settings (e.g., encryption keys, passwords, and SNMP community strings).
*   User access to wireless network devices is restricted to authorized personnel.
*   Bynder has implemented a Network Access Control (NAC) solution to manage and regulate internal wireless network infrastructure access centrally. Bynder-owned devices have been provisioned with a digital certificate, which is required for a successful connection to the wireless network. As a security measure, Broadcasting Service Set Identifier (BSSID) is disabled for credential-based authentication. Authentication of users attempting to connect to the wireless network is achieved through Extensible Authentication Protocol-Transport Layer Security (EAP-TLS). EAP-TLS is a certification-based authentication method that utilizes digital certificates for authentication and encryption of network access communications.

Operational security[](https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance#h_01HJ494DZHYD7ATXH6RN4P57TZ)

----------------------------------------------------------------------------------------------------------------------------------------------

### Vulnerability management

#### Patching

System security patches are installed automatically when available in the OS Maintainer's repositories using "unattended-upgrades." The application is not patched due to our release mechanism, which completely builds the application servers from scratch with every new version. Changes to the application are tested thoroughly, and problems with external or internal systems are identified early in the process, making it possible to circumvent issues with broken external systems. With the separation of processes in our cluster, broken systems are easily quarantined and dealt with separately. By minimizing the OS or platform level software, the risk a system is impacted by patches is minimized.

#### Malware protection

All end-user devices (laptops, desktops) are protected through a plethora of security options, including a mobile device management (MDM) system, enforcing strict security settings on each device, as well as endpoint detection and response (EDR) and extended detection and response (XDR) solution able to perform a real-time malware scan, cross-layer detection and response and external devices blocking. Access to business applications is allowed on Bynder-managed devices only, and multi-factor authentication (MFA) for all critical apps and access to our infrastructure is enforced. Non-critical applications can be accessed, based on business needs, from devices enforcing security requirements (updated OS version, password/passcode enabled, disk encryption).

Bynder's infrastructure devices (servers) are also secured through technical measures, including access control lists, IP whitelisting, and a web application firewall (WAF). Additionally, Bynder's production servers are rebuilt and destroyed frequently using the server provisioning system provided by Amazon Web Services (CloudFormation). Servers are rebuilt for security patches from the OS, software upgrades of the Bynder product itself, or simply when additional capacity is required for delivering the Product. Rebuilding the servers has the added benefit of significantly limiting the possibility of infection by malware and viruses.

Security alerts and tests to ensure compliance[](https://support.bynder.com/hc/en-us/articles/360013873260-Bynder-Security-and-Compliance#h_01HJ495SVGQBZGGPTE2JN1WMDE)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We monitor our security procedures regularly and have the following alerts in place so that immediate action can be taken:

*   A file integrity monitoring system is in place to alert personnel of unauthorized modifications to critical systems.
*   All security alerts are monitored, analyzed, and distributed to appropriate personnel.  
    Intelligent threat detection on the cloud with Amazon GuardDuty, with which we enhance the security monitoring of our AWS accounts, instances, serverless and container workloads, users, databases, and storage for potential threats.
*   Third-party-managed or internal penetration tests, or "red team" exercises against networks, hosts, and applications, are in place and performed at least once a year as required by our ISO27001 implementation. The code is manually penetration tested by a qualified third party annually. Additionally, we have weekly automated vulnerability scanning (by Nessus).

Share
