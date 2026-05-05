# How To Enable And Use Okta SCIM With Bynder – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/27929897102866

Summary[](https://support.bynder.com/hc/en-us/articles/27929897102866#h_01JZMQEP7W3VXA3WR3RS9RMKWB)

----------------------------------------------------------------------------------------------------

Bynder supports SCIM functionality, including creating, updating and deactivating user accounts with Okta. SCIM, or System for Cross-domain Identity Management, is an open standard designed to automate the process of user identity management and provisioning across different cloud-based services and applications. 

Who?[](https://support.bynder.com/hc/en-us/articles/27929897102866#h_01JZMQHE01BXVJYGHEYG14AJE2)

-------------------------------------------------------------------------------------------------

This feature/solution is enabled by a Bynder Admin.

Users with the _Manage Users,_ _Manage Portal Settings_ and _Manage OAuth apps_ permissions can manage SCIM.

Why?[](https://support.bynder.com/hc/en-us/articles/27929897102866#h_01JZMQNQR3WT7S8Z80446ZPZXC)

-------------------------------------------------------------------------------------------------

Bynder takes security seriously. We also understand that staying secure and up-to-date can be an immense workload.  SCIM handles automatic updates to user information stored in the Bynder portal whenever changes occur in the central identity provider (IdP), without the need of user logging in. SCIM capabilities within Bynder save time and increase portal management efficiency. 

How?[](https://support.bynder.com/hc/en-us/articles/27929897102866#h_01JZMQYFVACSY57BZR6502Y436)

-------------------------------------------------------------------------------------------------

### Enabling SCIM In Bynder

1.  Create a dedicated user account specifically for SCIM related operations. Ensure the permission profile of this user is set to Administrator, or at least a profile that has the _Manage Portal Settings_, _Manage users_ and _Manage OAuth apps_ permissions.
    *   This ensures that changes made via SCIM are kept separate from modifications performed through Bynder's _User Management_. By enabling SCIM, you acknowledge and accept that all tracked changes will be associated with the user account linked to the generated token.
2.  Log in as the SCIM user.
3.  Navigate to **Advanced Settings -> Portal Settings -> OAuth Apps**.
4.  Click on _**add new app.**_
5.  **Provide** an application name (required) and a description (optional).
6.  **Select** SCIM: Okta as the integration.
7.  Select the grant type supported by your IdP.
8.  **Add** the redirect URI and **press +**.
    
    _For Okta use the URIs provided in the Okta documentation:_
    
        https://system-admin.okta.com/admin/app/cpc/{appName}/oauth/callback
        https://system-admin.okta-emea.com/admin/app/cpc/{appName}/oauth/callback
        https://system-admin.oktapreview.com/admin/app/cpc/{appName}/oauth/callback
        https://system-admin.trexcloud.com/admin/app/cpc/{appName}/oauth/callback
        https://system-admin.okta1.com:1802/admin/app/cpc/{appName}/oauth/callback 
    

10\. The scopes are preselected for you to support SCIM integration. **Click** _Register application_.

11\. **Copy the Client ID** and Client Secret and store it safely. You will never see your Client Secret in Bynder’s UI again.

### Okta Setup

1.  Ensure you have an **App Integration for Bynder in Okta** with the provisioning type set to SCIM.
2.  **Create a SCIM token** in the Bynder Portal (see section above).
3.  **Configure** the SCIM provisioning integration settings in Okta:

*   _**Base URL:**_ Specify the SCIM service URL for your targeted Bynder portal https://yourportaldomain.com/api/2/scim
*   _**Unique Identifier Field for Users:**_ userName
*   _**Supported Provisioning Actions:**_
    *   _**Import New Users and Profile Updates:**_ Import data from Bynder to Okta.
    *   _**Push New Users:**_ Create users.
    *   _**Push Profile Updates:**_ Update user information.
*   _**Authentication Mode:**_ OAuth2
*   _**Access Token Endpoint URI:**_ https://yourportaldomain.com/v7/authentication/oauth2/token
*   _**Authorization Endpoint URI:**_  
    https://yourportaldomain.com/v7/authentication/oauth2/auth?scope=admin.user:read admin.user:write offline
*   _**Client ID and Client Secret:**_ Input the credentials generated during the Bynder OAuth2 app creation.

4.  **Authenticate** the connection.
5.  **Configure** allowed actions in the _Provisioning tab_ of your Okta application:

*   Create Users
*   Update User Attributes
*   Deactivate Users

### Okta Username Limitations:

*   Having multiple users in Okta with the same username that only differs by letter casing might cause conflicts and access issues for those users and thus should be avoided.
*   When a username is changed in Okta, this will trigger the creation of a new user in Bynder portal.
*   If a username is changed in Okta to the same value but with different letter casing, it will trigger deactivation of that user in the Bynder portal. Attempting reactivation will not succeed. _If this happens please reach out to Bynder support._

### Tracking Changes Done Through SCIM

1.  Open the user profile of the SCIM dedicated user account and copy the ID from the browser URL, alternatively, use the email of the SCIM user.
2.  Navigate to _**Reporting -> Change history**_.
3.  **Filter** by the _Responsible user email_ or _Responsible user ID_. The visible results are changes performed by your SCIM-dedicated account.

FAQs[](https://support.bynder.com/hc/en-us/articles/27929897102866#h_01JZMSBWW4BQ8JBN2H13DM8PZD)

-------------------------------------------------------------------------------------------------

**Will users which are deactivated or deleted in the IdP be automatically deactivated in Bynder’s portal?**

We do not support permanent deletion via SCIM. To permanently delete a user, please do it through Bynder User Management UI.

**Can Admins create users with SCIM that will not use SSO for logging in?**

No, Bynder supports user creation via SCIM only for users who will be logging in through SSO. However, modifying users via SCIM can be done for both SSO users and those logging in with login credentials.

**How are new users profiles set up when created?**

New users created through SCIM will have a default profile. As long as you use SSO with J_ust in time provisioning_ and have profile or group mapping set up, these values will be updated upon the next login.

**What attributes can be updated in Bynder via SCIM and vice versa?**

Bynder supports updating username, email, first name, last name, and active status (Active/Inactive) via SCIM. Any other user attributes cannot be updated via SCIM. This will **not** work in reverse, and updating the userName attribute in Bynder will break the SCIM integration.

**Can I reactivate a user?**

Users who have been deactivated for less than 180 days will not be eligible for reactivation through SCIM, even if they are reactivated in the IdP.

**Can SCIM deactivate users from the existing user base in Bynder portal or only future users that were created through SCIM after it has been enabled?**

All existing users will be supported, as long as they are SSO users.

Related Articles[](https://support.bynder.com/hc/en-us/articles/27929897102866#h_01JZMST5MBZ4T3E91GN09NVFFA)

-------------------------------------------------------------------------------------------------------------

[How To Redirect Single Sign-On (SSO) Logins](https://support.bynder.com/hc/en-us/articles/18241496809874)

[How To Configure SAML, OpenID, And Google Single Sign-on (SSO)](https://support.bynder.com/hc/en-us/articles/6614562131474)

[How To Enable And Use Azure SCIM With Bynder](https://support.bynder.com/hc/en-us/articles/29068712565010)

### _Level: Proficient_

Proficient-level articles are for users who have some prior Bynder knowledge. These articles require you to know the basics and may also require higher-level portal rights to accomplish the task outlined within the article.   
 

Share
