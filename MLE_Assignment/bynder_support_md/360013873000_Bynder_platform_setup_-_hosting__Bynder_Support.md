# Bynder platform setup - hosting – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013873000-Bynder-platform-setup-hosting

Your application, user database, Javascript code, and content are hosted on a dedicated platform. How all the data is hosted depends on the platform setup and setup options you select.

Hosting[](https://support.bynder.com/hc/en-us/articles/360013873000-Bynder-platform-setup-hosting#h_01HW67QNX07BHVY9FBQFPT7ZWC)

--------------------------------------------------------------------------------------------------------------------------------

The following options are available:

*   **US-only hosting**—Clients with this option can use only the US-only clusters. The data is not replicated outside the US. We use us-east-2 (Ohio) as the primary region and us-west-2 (Oregon) as a failover for this cluster. This is a great option for clients concerned about their data privacy.
    
*   **EU-only (local) hosting**—the server is located in Frankfurt, Germany. The data hosted in Frankfurt will not exit the European Economic Area (EEA) unless written permission has been obtained from the client. The transfer is permitted if the non-EEA country to which the data is being transferred has equivalent data protection legislation or Bynder is compelled by law to do so. It might happen that the upload and download times will be slightly slower if the customer uses Bynder outside Europe.
    
    It's recommended that clients with this setup use CDN because then all user data is stored locally in the EU, and only the web versions (derivatives) of the content are hosted globally.
    
    This hosting setup tends to be selected by European companies that want to be careful with their user data and with parts of their content so that other governments or companies cannot access and retrieve their data. The risk for this is higher when data is stored outside of the EU.
    
*   **Global hosting—the data can exit the European Economic Area (EEA) but will still be treated with the same high standard of protection. CDN is an easy way to fully use** this service. Global hosting makes scaling easier, increases the reliability of uptime, and reduces the risk of latency. The data is then hosted in four regions. See [Data hosting regions supported by AWS and Bynder](https://support.bynder.com/hc/articles/360013934099#UUID-7787de93-78d4-69a9-afa4-cc67ed73baa0 "Data hosting regions supported by AWS and Bynder")
    .
    

### Note

Assets are stored in the region where they are uploaded. Metadata is replicated to all regions for fast access.

 [](https://support.bynder.com/hc/en-us/articles/360013873000-Bynder-platform-setup-hosting#h_01HW67QNX0D22K66C7MFZJJM7G)

--------------------------------------------------------------------------------------------------------------------------

Share
