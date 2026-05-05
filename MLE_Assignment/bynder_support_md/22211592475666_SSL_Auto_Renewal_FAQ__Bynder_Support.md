# SSL Auto Renewal FAQ – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/22211592475666-SSL-Auto-Renewal-FAQ

We ensure seamless SSL/TLS certificate management through [automated SSL](https://support.bynder.com/hc/en-us/articles/360013875240-Create-a-Custom-URL-for-your-Portal#h_01HT2VX249JP3FVJ8AE228F3N8:~:text=for%20your%20portal.-,Automatic%20Procedure,-Navigate%20to%20your)
 renewal via Automated Certificate Management (ACM), reducing manual effort. Once a CNAME record is added to your DNS, no further intervention is required, eliminating the complexity typically involved in certificate management.

ACM safeguards against downtime by managing renewals efficiently and preventing issues related to expired, misconfigured, or revoked certificates. Additionally, private keys are securely stored using strong encryption and key management best practices, with no exchange of private keys needed. To further support smooth operations, ACM provides DNS record modification or deletion notifications 60 days before certificate expiration, ensuring timely action when necessary.

This information applies specifically to Bynder users who are transitioning from manual to automatic renewal.

### Not sure if you have manual vs automatic renewal?

Reach out to your Customer Success Contact or contact Customer Support.

FAQ[](https://support.bynder.com/hc/en-us/articles/22211592475666-SSL-Auto-Renewal-FAQ#h_01JB2044SHT3P64VJHYE8KTBGP)

---------------------------------------------------------------------------------------------------------------------

**Why SSL auto-renewal?**  
The maximum validity of SSL certificates has been limited in recent years from 5 to 3 to 2 years and is now down to 1 year from September 1, 2020. There is a chance that the validity period will be further limited. It is strongly encouraged because of the security benefits. SSL auto-renewal doesn’t require annual follow-ups. Once configured, the SSL certificate renews every year automatically.

**How does SSL auto-renewal work?**  
We provide CNAME records that need to be added to the domain system. Once that record is added, we can configure SSL auto-renewal so that further assistance isn't needed. The SSL certificate will be renewed every year automatically using the CNAME record. The Support Agent will be assisting with the implementation.

**What are the costs for adding SSL auto-renewal?**  
There is no cost involved in configuring the SSL auto-renewal.

**Can I provide my own SSL certificate?**  
No, this is not possible. We want to protect you from expiring certificates or potential downtime. That is why we'll request an SSL certificate for you and ensure it is renewed automatically using AWS Certificate Manager (ACM).

**What is a DNS Record?**  
The domain name system (DNS) is a naming database that locates and translates internet domains into internet protocol (IP) addresses. It maps the name people use to locate a website to the IP address a computer uses to locate a website/server. Read more about DNS here.

**How to Add the DNS Records?**  
You can add the DNS records to your domain provider's configuration panel. Check the help center of your domain provider for more information. Instructions on adding a CNAME are available for the most common domain registrars: GoDaddy, NameCheap, and Netfirms.  
What should I do when I can't add the provided CNAME records?  
Contact your domain provider's support department and ask for further technical assistance. Some providers don't support adding a CNAME starting with an underscore (\_) via their admin panel. You can ask their support agents to enter your record via their system's backend.

FAQ Amazon Certificate Manager (ACM)[](https://support.bynder.com/hc/en-us/articles/22211592475666-SSL-Auto-Renewal-FAQ#h_01JB205X7M8CXS7B75YH56A7J6)

------------------------------------------------------------------------------------------------------------------------------------------------------

For more information please see [here](https://aws.amazon.com/certificate-manager/faqs/)
.

**What is the validity period for ACM certificates?**  
Certificates issued through ACM are valid for 13 months (395 days). The SSL certificate on auto-renewal is renewed automatically 60 days before its expiration date.  
Will I be notified before my certificate is renewed and the new certificate is deployed?  
No. ACM may renew or rekey the certificate and replace the old one without prior notice.

**What algorithms do ACM-issued certificates use?**  
By default, certificates issued in ACM use RSA keys with a 2048-bit modulus and SHA-256. The ACM User Guide explains more about algorithms.

**Are browsers, operating systems, and mobile devices trust ACM public certificates?**  
Most modern browsers, operating systems, and mobile devices trust ACM public certificates. ACM-provided certificates are 99% ubiquity, including Windows XP SP3 and Java 6 and later.

**How can I confirm that my browser trusts ACM public certificates?**  
Some browsers that trust ACM certificates display a lock icon and do not issue certificate warnings when connected to sites that use ACM certificates over SSL/TLS, such as HTTPS.  
Public ACM certificates are verified by Amazon’s certificate authority (CA). Any browser, application, or OS that includes the Amazon Root CA 1, Amazon Root CA 2, Amazon Root CA 3, Amazon Root CA 4, Starfield Services Root Certificate Authority - G2 trusts ACM certificates. For more information about root CAs, visit the Amazon Trust Services Repository.

**Where does Amazon describe its policies and practices for issuing public certificates?**  
They are described in the Amazon Trust Services Certificate Policies and Amazon Trust Services Certification Practices Statement documents. For the latest versions, refer to the Amazon Trust Services repository.

**How can ACM help my organization meet my compliance requirements?**  
Using ACM helps you comply with regulatory requirements by making it easy to facilitate secure connections, a common requirement across many compliance programs such as PCI-DSS, FedRAMP, ISO, and HIPAA. For specific compliance information, please take a look [here.](http://aws.amazon.com/compliance.)
 

**How are the private keys of ACM-provided certificates managed?**  
A key pair is created for each certificate provided by ACM. ACM is designed to protect and manage the private keys used with SSL/TLS certificates. Strong encryption and key management best practices are used to protect and store private keys.  
No one has access to the private keys generated by the SSL auto-renewal.

**What is DNS validation?**  
With DNS validation, you can validate your domain ownership by adding a CNAME record to your DNS configuration. DNS Validation makes it easy to establish that you own a domain when requesting public SSL/TLS certificates from ACM.

**What are the benefits of DNS validation?**  
DNS validation makes it easy to validate that you own or control a domain to obtain an SSL/TLS certificate. With DNS validation, you simply write a CNAME record to your DNS configuration to establish control of your domain name. To simplify the DNS validation process, the ACM management console can configure DNS records for you if you manage your DNS records with Amazon Route 53. This makes establishing control of your domain name easy with a few mouse clicks. Once the CNAME record is configured, ACM automatically renews certificates that are in use (associated with other AWS resources) as long as the DNS validation record remains in place. Renewals are fully automatic and touchless.

**What records must I add to my DNS configuration to validate a domain?**  
You must add a CNAME record for the domain you want to validate. For example, to validate the name http://www.example.com, you add a CNAME record to the zone for http://example.com. The record you add contains a unique token that ACM generates specifically for your domain and your AWS account. You can obtain the two parts of the CNAME record (name and label) from ACM. For further instructions, refer to the ACM User Guide.

**Does DNS Validation require me to use a specific DNS provider?**  
No. You can use DNS validation with any DNS provider if the provider allows you to add a CNAME record to your DNS configuration.

**How many DNS records do I need if I want more than one certificate for the same domain?**  
One. You can obtain multiple certificates for the same domain name in the same AWS account using one CNAME record. For example, if you request two certificates from the same AWS account for the same domain name, you need only 1 DNS CNAME record.

**Can I validate multiple domain names with the same CNAME record?**  
No. Each domain name must have a unique CNAME record.

**How does ACM construct CNAME records?**  
DNS CNAME records have two components: a name and a label. The name component of an ACM-generated CNAME is constructed from an underscore character (\_) followed by a token, a unique string tied to your AWS account, and your domain name. ACM pre-pends the underscore and token to your domain name to construct the name component. ACM constructs the label from an underscore character prepended to a different token, which is also tied to your AWS account and your domain name. ACM pre-pends the underscore and token to a DNS domain name AWS uses for validations: acm-validations. Aws. The following examples show the formatting of CNAMEs for http://www.example.com, subdomain.example.com  
\_TOKEN1.www.example.com CNAME \_TOKEN2.acm-validations.aws  
\_TOKEN3.subdomain.example.com CNAME \_TOKEN4.acm-validations.aws

**How do I renew a certificate validated with DNS validation?**  
ACM automatically renews certificates that are in use (associated with other AWS resources) as long as the DNS validation record remains in place.

**What happens if I remove the CNAME record?**  
ACM cannot issue or renew certificates for your domain using DNS validation if you remove the CNAME record.

Share
