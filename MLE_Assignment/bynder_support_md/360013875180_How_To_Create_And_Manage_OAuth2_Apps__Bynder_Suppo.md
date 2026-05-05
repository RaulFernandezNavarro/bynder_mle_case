# How To Create And Manage OAuth2 Apps – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013875180

Summary[](https://support.bynder.com/hc/en-us/articles/360013875180#h_01JP7435087445TMSK5TCSRMMY)

--------------------------------------------------------------------------------------------------

Create more integrations for your Bynder brand portal using the OAuth 2.0 setup to quickly provide authorized access to the Bynder API. This empowers users to create account-specific integrations to leverage Bynder throughout their brand ecosystem.

Who?[](https://support.bynder.com/hc/en-us/articles/360013875180#h_01JP74329VECE9FVBD51EZ3P1W)

-----------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once enabled users with the _Manage OAuth apps_ permission can access and manage OAuth Apps.

Why?[](https://support.bynder.com/hc/en-us/articles/360013875180#h_01JP742Y6HTJCNAC65EQX2SHCY)

-----------------------------------------------------------------------------------------------

OAuth2 or _Open Authorization_ enables the user to give the third-party application access to their data without having to share their credentials. This is the industry standard for online authorization. Bynder believes in simple, efficient, and secure when it comes to our product and integrations, which is why we offer OAuth2 Apps for our users.

How?[](https://support.bynder.com/hc/en-us/articles/360013875180#h_01JP742TCTXM3GMEWW23Z025SM)

-----------------------------------------------------------------------------------------------

### Creating A New OAuth App

1\. Navigate to **Settings > Advanced Settings > Portal settings** and click **OAuth Apps**.

![OAUTH_APP.png](https://support.bynder.com/hc/article_attachments/10640487663506)

2\. Click **Register new application** to create your first OAuth App.

![register_a_new_application.png](https://support.bynder.com/hc/article_attachments/10640501947410)

3\. Configure your **OAuth** **App**.

![details_new_oauth_application_.png](https://support.bynder.com/hc/article_attachments/10640501964562)

_Note: The Client Secret will only be visible once and needs to be regenerated in case it is lost. If you regenerate it, your existing operations with the last client secret will no longer work._

Users who manage OAuth Apps can revoke all refresh tokens for an OAuth App and, if needed, delete the application once and for all, which will permanently delete the application's associated refresh tokens.

![oauth_app.jpg](https://support.bynder.com/hc/article_attachments/10640487763090)

### Editing An Existing OAuth App

All OAuth App specifications can be changed **except** the OAuth scopes. When you want to modify the OAuth scopes, we recommend creating a new application.

1.  Go to **Settings > Advanced Settings > Portal settings** and click **OAuth Apps**.
    
2.  Click **OAuth Apps**.
    
3.  Click  next to the application you want to modify.
    
4.  Modify your OAuth App information.
    
5.  Click **Update application** to save your changes.
    

### Revoking Refresh Tokens

1.  Go to **Settings > Advanced Settings > Portal settings** and click **OAuth Apps**.
    
2.  Click **OAuth Apps**.
    
3.  Click  next to the application you want to revoke the refresh tokens for.
    
4.  Click **Revoke refresh tokens**. A popup will open.
    
5.  Read the warning message and click **Revoke all refresh tokens** if you want to revoke the refresh tokens. This action **cannot be undone**.
    

### Deleting An Application

1.  Go to **Settings > Advanced Settings > Portal settings** and click **OAuth Apps**.
    
2.  Click **OAuth Apps**
    
3.  Click  next to the application you want to delete.
    
4.  Click **Delete application**. A popup will open.
    
5.  Read the warning message and click **Delete** to delete the application. This will permanently delete the application and revoke all associated refresh tokens. This action **cannot be undone**.
    

### Understanding Grant Types

Part of the OAuth 2.0 specification is grant types, which are different methods for acquiring an access token to authorize API calls.

We offer the following grant types: 

*   **Authorization Code + Refresh Token**
    
    The authorization code grant will allow you to access Bynder on a user's behalf. The application redirects the user to the authorization page, where the user must log in and approve the authorization request. If approved, Bynder will redirect the user to the application with an authorization code. The application can then exchange this code for an access token.
    
    A refresh token can be obtained by specifying the **offline** scope in the authorization request. This token will not expire and allows the application to request new access tokens without user interaction.
    
*   **Client Credentials**
    
    The client credentials grant allows applications to obtain access tokens solely using the client ID and client secret without user interaction. In the case of Bynder, the issued access tokens will still be linked to the configured assigned user.
    
    This grant is the most comparable to the OAuth 1.0a API tokens. This is helpful for machine-to-machine interaction. 
    

FAQs[](https://support.bynder.com/hc/en-us/articles/360013875180#h_01HQQV2W8SNW7YNYXF5BAX5HWX)

-----------------------------------------------------------------------------------------------

**What does this mean for my existing integrations or scripts calling the Bynder API?**

OAuth 2.0 works in parallel with OAuth1a. They can coexist, but we want to promote OAuth 2.0 (OAuth Apps) as much as possible since it is the newest implementation to provide authorized access to the Bynder API and will continuously improve.

**What are the main benefits of OAuth 2.0?**

Bynder's OAuth 2.0 scope implementation for OAuth Apps provides complete transparency to the user regarding what the application can request on the user's behalf. In addition, access tokens can now be refreshed, which means users no longer need to re-authenticate every 30 days. Still, they can be refreshed in the background using the refresh token generated by the OAuth 2.0 service.

**How to migrate my migrations from OAuth1 to OAuth 2.0?**

Customers can easily upgrade to OAuth 2.0 by using our Bynder SDKs. The new endpoints and refresh mechanisms have been fully implemented in all our SDKs, allowing a fast upgrade for your integrations.

**How can I update my OAuth App over time?**

All OAuth App specs can be changed except for OAuth scopes. At this point, we did not implement the update of the OAuth scopes for an existing application. Therefore, we recommend you create a new application.

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013875180#h_01JNG92RYKBSYWA0ZCH7YHBWV1)

-----------------------------------------------------------------------------------------------------------

[How To Enable And Use SCIM With Bynder](https://support.bynder.com/hc/en-us/articles/27929897102866)

[Integrations Hub](https://support.bynder.com/hc/en-us/articles/11400106439698)

### _Level: Expert_

Expert-level articles are for users who have significant prior Bynder knowledge. These articles require you to know a lot of Bynder information and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
