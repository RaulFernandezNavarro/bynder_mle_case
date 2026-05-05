# How To Configure SAML, OpenID, And Google Single Sign-on (SSO) – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013936419

Summary[](https://support.bynder.com/hc/en-us/articles/360013936419#h_01JNDD5TXX2EAQHRF8EFCGC71J)

--------------------------------------------------------------------------------------------------

Enabling Single Sign-on (SSO) saves Bynder Admins time once provisioned. This guide will explain SSO and how to enable it within your Bynder portal. 

Who?[](https://support.bynder.com/hc/en-us/articles/360013936419#h_01JNDDHRWV4HAF0WJQPCNM5KR6)

-----------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once enabled users with the _Portal Settings_ or _Manage Login Configuration_ permissions can create and manage SSO profiles and flows. 

Why?[](https://support.bynder.com/hc/en-us/articles/360013936419#h_01JNDDV1ZXAQS9GDCRNGFPZARS)

-----------------------------------------------------------------------------------------------

Implementing SSO can save a lot of time for users and administrators. SSO's primary role in online security is that it enables you to access multiple web applications using one set of login credentials.

With SSO, anyone in your network can simply click the SSO button on the portal's login page to quickly login. 

SSO also allows for automatic creation of new user accounts through Just-in-Time provisioning (JIT). This eliminates the need for manual account creation by Bynder Admins. After setting up a profile or group mapping, a user account with the appropriate permission profile is automatically created when a user logs in for the first time using SSO.

How?[](https://support.bynder.com/hc/en-us/articles/360013936419#h_01JNDEA65BQST0ZD4JZXX2WR37)

-----------------------------------------------------------------------------------------------

### Create A New SSO Flow

1.  Navigate to **Settings > Advanced Settings > Portal Settings.**
    
2.  Click **Login Configuration** on the left sidebar.
    
3.  Click **New login method**, then select **SAML, Google, or OpenID** **SSO.**
    
4.  Enter a **name** for the SSO flow to allow you to identify it quickly, and then click **Save**.
    
5.  **Settings**: These are the minimum settings needed to integrate with the identity provider.
    
6.  **View** **setup** **instructions**: Click to see all the instructions and details needed to set up Bynder on your identity provider.
    
    *   Click **Permalink** **XML** to access this information as an XML file.
        
    *   _optional_ **Add** **XML** **file**: Click to upload or paste the XML file from your identity provider. If you add an XML file, the settings below will be prefilled automatically; otherwise, you must enter the details from your identity provider, such as Okta, Azure, Google, Salesforce etc.
        
    
7.  Identity provider identifier: Enter the **primary** **identifier** of your identity provider, also known as entity ID or issuer.
    
8.  Identity provider login URL: Enter the **endpoint** from your identity provider where Bynder should send the login requests.
    
9.  **(Google Only)**Allowed Domains: Enter the email domains that can log into the Bynder DAM (i.e. if yourcompany.com is added, then users with yourcompany.com email addresses will be able to log in). Multiple domains can be set if needed.
    

Identity provider certificate: Click **Add Certificate** to add the certificate from your identity provider. You can add multiple certificates.

*   Enter the **certificate** **name**, then either upload the certificate or paste the details in the Certificate box. Click the to edit or ![trash.png](https://support.bynder.com/hc/article_attachments/10640558071570) to delete.
    
*   You will see real-time validation for the certificate, including Inactive, Active, or Expired. If the certificate is Active, you will also see the expiration date. PEMx509 is the only supported format for the certificate.
    

### OpenID Specific Settings:

 These are the settings needed to integrate with OpenID. You can find them in the application configuration of your identity provider. For additional information contact your Identity provider customer support.

*   **Client ID:** Enter the Client ID from your SSO provider.
    
*   **Client secret:** Enter the secret from your SSO provider.
    
*   **Scope**: Enter the scopes (identifiers for resources) that you want the SSO provider to have access.
    
*   **Authorization** **URL**: Enter the URL where users need to be sent in order to start the authentication process.
    
*   **Token** **URL**: Enter the URL to exchange the authorization code for the access token.
    
*   **JWKS** **URL**: Enter the URL that contains the JSON Web Key Set to verify the identity token.
    
*   **Use user info endpoint:** Enable if the user's claims (information) will be fetched from the user endpoint. Enter the **user** **info** **endpoint** URL here.
    
    *   If disabled, the claims will be read from the token only.
        
    

### Provision Users

User provisioning allows you to choose how you would like Bynder to handle your SSO users.

*   **Just-in-time(JIT) user provisioning**: Click the ![toggle_app.png](https://support.bynder.com/hc/article_attachments/10640558097042) to **enable** or **disable** JIT. **Enable** JIT if you want Bynder to automatically create users in the portal when they log in with SSO for the first time. If **disabled**, an admin will need to manually create a user in Bynder before they can log in for the first time using SSO. 
    
    *   You must select the **default** **user** **permission** **profile** from the dropdown list if enabled. Unless you have added user **profile mapping**, users will automatically be added to this permission profile upon login. 
        
    *   If **disabled**, an admin must manually create a user in Bynder before logging in for the first time using SSO.
        
    *   Bynder supports automated user de-provisioning via SCIM with Okta and Azure.
        
    *   Enabling this feature requires all user attribute fields that are required to have a corresponding attribute ID, which typically requires _First name_ and _Last name._
        

### Updating User Profiles

**Update user attributes:** Enable if you'd like to update user attributes according to the mappings defined below.

**Update user profiles:** Enable if you'd like to update user profiles according to the mappings defined below.

**Update user groups:** Enable if you'd like to update user groups according to the mappings defined below.

**Update users upon login:** Click to **enable** or **disable** this feature and choose which attributes you would like to **update upon every user login.**

_Note: Do not enable **Update** **users** **upon** **login** when you do not have relevant mappings in your Identity provider. When this feature is enabled, and if a user does not match any of the Permission Profiles set or no profile mappings are set up, the user will be assigned the **default permission profile.**_

### Mapping User Attributes

You can map the attributes such as: Username, Email, First name, Last name, and more in Bynder to the corresponding attributes in your identity provider. By default, Bynder will use NameID to map the username and email when updating or creating users. To map these attributes from your identity provider, **uncheck** the relevant checkbox and input the relevant user attribute IDs.

![CUSTOM_ATTRIBUTE_MAPPING_FOR_SAML_SSO.png](https://support.bynder.com/hc/article_attachments/10640572528658)

### User Profiles Mapping 

Optionally, you can map permission profiles in Bynder with the profiles in your identity provider. This will automatically add users with specific identity provider profiles to a permission profile within Bynder, reducing repetitive work for the Bynder administrator.

1.  Click **Add** **Profile.**
    
2.  You can enter the **name of the User profile attribute**, the name used in your identity provider for the user group attribute.
    
    _Note: An exact match is required for the mapping to work._
    
3.  Select the Bynder permission profile from the dropdown, then add the **identity** **provider** **profiles** that should be mapped to it. If the user profile name on the Identity provider side does not match any of the Profile mappings set, the user will be assigned the **default permission profile.**
    
4.  Click +**Add** **Profile** to add additional Profiles to the mappings.
    

_Note:_ We recommend sorting permission profiles from highest to lowest to make sure users aren't accidentally assigned a lower permission level than intended.

![user_profile_mapping.png](https://support.bynder.com/hc/article_attachments/10640572564114)

### User Group Mapping

1.  Click **Add** **Groups** to map user groups in Bynder with groups in your identity provider. This will automatically add users that belong to a specific identity provider group to the appropriate user group within Bynder.
    
2.  Enter the **User** **group** **attribute** **name**, the name used in your identity provider for the user group attribute. _An exact match is required for the mapping to work._
    
3.  Select the **Bynder** **user** **group** from the dropdown, then add the **identity** **provider** **groups** that should be mapped to it.
    
4.  Click **Add** **Group** to add additional mappings.
    

![user_group_mapping.png](https://support.bynder.com/hc/article_attachments/10640558203154)

### Updating The Identity Provider Certificate

For your users to continue logging in via SSO, you must update the identity provider certificate(s) before the expiration date. These can be added anytime; Bynder only uses the currently active certificates when logging in.

1.  Navigate to **Settings** > **Advanced** **Settings** > **Portal** **Settings**.
    
2.  Click **Login** **Configuration** on the left sidebar.
    
3.  Click the login method for which you need to update the certificate, then select **settings**.
    
4.  In the **Identity** **Provider** **Certificates** section, click **Add** **Certificate** or click the pencil icon next to the certificate that is about to expire.
    
5.  Enter the **certificate name,** then either upload the certificate or paste the details in the Certificate box. Click the ![configure-users_pencil.png](https://support.bynder.com/hc/article_attachments/10640558056466) to edit or the ![trash.png](https://support.bynder.com/hc/article_attachments/10640558071570) to delete.
    
6.  You will see real-time validation for the certificate, including Inactive, Active, or Expired. If the certificate is active, you will also see the expiration date.
    

FAQs[](https://support.bynder.com/hc/en-us/articles/360013936419#h_01HJ6G7QF1Q5MTNQSCRGY4M5ZH)

-----------------------------------------------------------------------------------------------

**Can I map the email and username separately for users?**

Bynder supports the functionality of mapping the email and username separately. This will allow for accurate mappings if your users have usernames that are different from their emails.

**What happens if I have reached my license limit?**

The user will not be created if you've reached the licensed user seat limit outlined in your agreement. They will see an error message when attempting to log in, and an error will be logged in to Single Sign-on logs.

**Can SSO users still use their Bynder credentials to log in?**

No, users with SSO set-up may only use SSO to log in. 

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013936419#h_01JN69T4KTE5MNQKBCKHE0566J)

-----------------------------------------------------------------------------------------------------------

[How To Redirect Single Sign-On (SSO) Logins](https://support.bynder.com/hc/en-us/articles/18241496809874-Redirect-Single-Sign-On-SSO-Logins)

[How To Use Single Sign-On (SSO) Troubleshooting Logs](https://support.bynder.com/hc/en-us/articles/7780356129426)

[How To Enable And Use Azure SCIM With Bynder](https://support.bynder.com/hc/en-us/articles/29068712565010)

[How To Enable And Use Okta SCIM With Bynder](https://support.bynder.com/hc/en-us/articles/27929897102866)

### _Level: Expert_

Expert-level articles are for users who have significant prior Bynder knowledge. These articles require you to know a lot of Bynder information and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
