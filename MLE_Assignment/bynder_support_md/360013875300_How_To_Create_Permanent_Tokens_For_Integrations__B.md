# How To Create Permanent Tokens For Integrations – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013875300-How-To-Create-Permanent-Tokens-For-Integrations

Summary[](https://support.bynder.com/hc/en-us/articles/360013875300-How-To-Create-Permanent-Tokens-For-Integrations#h_01JY3YRZM15R0KV2XZQSCYC6WX)

--------------------------------------------------------------------------------------------------------------------------------------------------

If you are building an integration that _does not_ require user interaction and only uses machine-to-machine communication you can authenticate the integration via permanent tokens. The tokens will not expire. If you are building a new integration we recommend using OAuth2 Apps.

Who?[](https://support.bynder.com/hc/en-us/articles/360013875300-How-To-Create-Permanent-Tokens-For-Integrations#h_01JY3YV3NXWHM2Z6CXN5TFPHTJ)

-----------------------------------------------------------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once permanent tokens have been enabled the feature can be used with your portal. Users will need the _Manage Bynder permanent tokens_ permission to create and delete permanent tokens.

Why?[](https://support.bynder.com/hc/en-us/articles/360013875300-How-To-Create-Permanent-Tokens-For-Integrations#h_01HQQV6AGG5JSANJ4X5CJS13X0)

-----------------------------------------------------------------------------------------------------------------------------------------------

A permanent API token can be created to keep a system in sync with Bynder or to upload data, such as assets. Permanent tokens help with non-human interactions between machines. For example, a product company wants to sync its Product Information Management (PIM) metadata with Bynder asset metaproperties. Another helpful use of permanent tokens would be if a marketing team is looking for generic assets that their DAM does not include and  purchases assets on stock repositories. These assets need to be uploaded to the Bynder DAM using the API.

How?[](https://support.bynder.com/hc/en-us/articles/360013875300-How-To-Create-Permanent-Tokens-For-Integrations#h_01HQQV6AGGEJBJRCX3VGF47VXF)

-----------------------------------------------------------------------------------------------------------------------------------------------

1.  **Navigate** to your Bynder portal.
    
2.  Go to **Settings > Advanced Settings > Portal Settings** and click **Permanent Tokens**.
    
3.  Click **Add new token**.
    
4.  Enter a description for the token in the **Description** field.
    
    ![perm_token_.png](https://support.bynder.com/hc/article_attachments/10640504526738)
    
5.  Select **Integration** from the dropdown menu.
    
    *   If your integration does not appear in the dropdown choose **Other** and type in the integration name.
        
        ![OTHER_INTEGRATION.png](https://support.bynder.com/hc/article_attachments/10640504549138)
        
    
6.  Click **Assigned user** dropdown to assign the permissions of a user to the token. Enter the name of the user and click one of the returned search results.
    
7.  In **Scopes section** select the Bynder resources you want to access with this permanent token.
    
8.  Click **Create token** to create the token. The new permanent token will be displayed.
    
9.  Copy the token information; make sure not to lose it, since it will only be displayed once and cannot be regenerated. You can now find the token in your permanent tokens overview screen. This is a permanent token and does not need to be refreshed. 
    

_Note: The token cannot be edited after creation. If changes need to be made, you will need to create a new permanent token with the new changes, and delete the old token._

### Deleting Permanent Tokens

1.  **Navigate** to your Bynder portal.
    
2.  Go to **Settings > Advanced Settings > Portal settings** and click **Permanent Tokens**.
    
3.  **Click** the settings wheel next to the token you want to delete.
    
4.  Click **Delete token**. A popup will open.
    
5.  Read the warning message and click the **Delete** button if you wish to permanently delete the token. 
    
6.  The token is now deleted and can no longer be used. **This action _cannot_ be undone.**
    

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013875300-How-To-Create-Permanent-Tokens-For-Integrations#h_01JY3YSPCY6JJB9QTT4AT2F9HB)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[How To Create And Manage OAuth2 Apps](https://support.bynder.com/hc/en-us/articles/360013875180)

Share
