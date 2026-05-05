# Protecting Your Bynder Portal with AWS Web Application Firewall (WAF) – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360016736380-Protecting-Your-Bynder-Portal-with-AWS-Web-Application-Firewall-WAF

To better protect your Bynder portal and ensure a safer user experience, we have integrated AWS Web Application Firewall (AWS WAF) into Bynder. Discover how this helps keep your portal secure.

### How to Enable AWS Web Application Firewall?

AWS WAF is automatically enabled for clients using our [CDN](https://support.bynder.com/hc/en-us/articles/360013875140)
. No additional configuration is required. If you are not yet on our CDN, please connect with your Customer Success Contact for more information. 

What is AWS Web Application Firewall?[](https://support.bynder.com/hc/en-us/articles/360016736380-Protecting-Your-Bynder-Portal-with-AWS-Web-Application-Firewall-WAF#h_01J596CSZS7BXCPXSX5KTWSEMY)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

AWS Web Application Firewall (AWS WAF) analyzes all incoming traffic on our servers in real time. It protects against common attacks, such as SQL injections, DDoS attacks, and Cross-Site Scripting (XSS), which could compromise security and impact the availability of our systems. Read more about AWS Web Application Firewall [here](https://aws.amazon.com/waf/)
.

Top 10 Security Risks Protected by AWS WAF[](https://support.bynder.com/hc/en-us/articles/360016736380-Protecting-Your-Bynder-Portal-with-AWS-Web-Application-Firewall-WAF#h_01J596D1KHBPGHX2MGAGEKMKD7)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

AWS WAF shields your portal from the top 10 security risks. This list is compiled by the Open Web Application Security Project (OWASP). Learn more about OWASP’s security risks [here](https://owasp.org/www-project-top-ten/)
.

*   Injections
*   Broken Authentication
*   Sensitive Data Exposure
*   XML External Entities (XXE)
*   Broken Access Control
*   Security Misconfiguration
*   Cross-Site Scripting (XSS)
*   Insecure Deserialization
*   Using Components with Known Vulnerabilities
*   Insufficient Logging & Monitoring
*   Additionally, AWS WAF blocks excessive resource usage by enforcing an API rate limit, ensuring seamless performance for all customers.

API Rate Limiting[](https://support.bynder.com/hc/en-us/articles/360016736380-Protecting-Your-Bynder-Portal-with-AWS-Web-Application-Firewall-WAF#h_01J596FFDZ2Z363XTV36MT0550)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bynder enforces a limit of 4,500 API requests per five-minute window per public IP address. This includes both original requests and retries.  
To stay safely within this limit, we recommend keeping your request rate around 10 requests per second. This allows room for occasional retries without exceeding the threshold.  
When updating asset metadata, include all changes for a single asset in one POST /v4/media/{assetId} request to reduce the total number of calls. For transient server errors (e.g., 5xx responses), implement exponential back-off with jitter. If you receive a 429 Too Many Requests response, pause all requests for five minutes before retrying.  
Following these guidelines will help ensure your integration runs reliably without interruptions or unintended impact on other systems.

Share
