# How To Enable And Use Azure SCIM With Bynder – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/29068712565010-How-To-Enable-And-Use-Azure-SCIM-With-Bynder

Summary[](https://support.bynder.com/hc/en-us/articles/29068712565010-How-To-Enable-And-Use-Azure-SCIM-With-Bynder#h_01JZMQEP7W3VXA3WR3RS9RMKWB)

-------------------------------------------------------------------------------------------------------------------------------------------------

Bynder supports SCIM functionality, including creating, updating and deactivating user accounts with Azure. SCIM, or System for Cross-domain Identity Management, is an open standard designed to automate the process of user identity management and provisioning across different cloud-based services and applications. 

Who?[](https://support.bynder.com/hc/en-us/articles/29068712565010-How-To-Enable-And-Use-Azure-SCIM-With-Bynder#h_01K3R0EJN72JS4DAK8GY2SD69H)

----------------------------------------------------------------------------------------------------------------------------------------------

This feature/solution is enabled by a Bynder Admin.

Users with the _Manage Users,_ _Manage Portal Settings_ and _Manage Bynder permanent API tokens_ permissions can manage Azure SCIM .

How?[](https://support.bynder.com/hc/en-us/articles/29068712565010-How-To-Enable-And-Use-Azure-SCIM-With-Bynder#h_01JZMQYFVACSY57BZR6502Y436)

----------------------------------------------------------------------------------------------------------------------------------------------

### Enabling Azure SCIM In Bynder

1.  Create a dedicated user account specifically for SCIM related operations. Ensure the permission profile of this user is set to Administrator, or at least a profile that has the _Manage Portal Settings_, _Manage users_ and _Manage Bynder permanent API tokens_ permissions.
    *   This ensures that changes made via SCIM are kept separate from modifications performed through Bynder's _User Management_. By enabling SCIM, you acknowledge and accept that all tracked changes will be associated with the user account linked to the generated token.
2.  Log in as the SCIM user.
3.  While logged in as the dedicated SCIM user, go to:  
    **Advanced Settings → Portal Settings → Permanent tokens**. Click Add new token.
4.  Fill in the token details:
    *   **Description** – Enter a clear name, e.g. SCIM Token.
    *   **Integration** – Select **SCIM** -> Entra ID (Azure AD) from the dropdown.
        *   Make sure to select the correct Azure option. _Do not select **Backup** -> Azure option._
    *   **Assigned user** – Select the dedicated SCIM user account created earlier.
    *   The scopes are preselected for you to support SCIM integration.
    *   Click **Create token**. The token will be displayed only once, _copy it and store it securely_. You will need this token later when configuring Azure SCIM provisioning.

### Azure Setup

If you have previously configured your SSO with Entra ID by selecting Bynder App Gallery, you will _need_ to configure it again on a new custom application to enable SCIM provisioning. This will also require changes in your SSO configuration within Bynder Portal.

It is possible to use the existing Bynder application in Entra ID for SSO and create a new application for SCIM provisioning only, but this could become more complicated for long term maintenance and consistency, Bynder does not recommend this option.

1.  Create a Custom Enterprise Application. (_**Skip steps 1 - 8**_ if you already have a Bynder SSO Custom Application.)
2.  Sign in to the Azure Portal with an account that has **Application Administrator** or higher permissions.
    
3.  Navigate to: **Azure Active Directory → Enterprise applications**.
    
4.  Click **\+ New application**.
    
5.  In the **Browse Azure** **AD** **Gallery** screen, click **Create your own application**.
    
6.  Enter an application name such as **Bynder SCIM.**
    
7.  Under _**What are you looking to do with your application?**_, select:  
    **Integrate any other application you don't find in the gallery (Non-gallery)**.
    
    _Note: Do not use the Bynder gallery application that is recommended by Azure. This app does not support SCIM provisioning._ 
    
8.  Click **Create**.
    

### Configuring Provisioning

1.  In the left navigation pane of the application, click **Provisioning**.
    
2.  For **Provisioning Mode**, select **Automatic**.
    
3.  **For Authentication Method,** Choose **Bearer Token** and paste.
    
    *   In **Tenant Url** type `https://<your-bynder-domain>.bynder.com/api/2/scim`
        
    *   In the **Token** paste the Permanent Token you generated in Bynder.
        
4.  Click **Test Connection**. If the test succeeds, click **Save**.
    
    _Note:_ If the test fails, verify the token, permissions, and URL.
    

### Azure Mapping

1.  In the left navigation pane of the application, click **Provisioning**.
    
2.  Choose **Mappings** → **Provision Microsoft Entra ID Users** (Enabled should be set to Yes). ![Screenshot 2025-08-12 at 16.09.55-20250812-140957.png](https://support.bynder.com/hc/article_attachments/29071335846674)
    
3.  Set the attributes as described below:
    *   userName → userPrincipalName
    *   name.givenName → givenName
    *   name.familyName → surname
    *   emails\[type eq "work"\].value → mail (or emails\[type eq "work"\].value → userPrincipalName)

_Note:_ mail, givenName, and surname are required fields for Bynder SCIM provisioning. Ensure that every user you assign has these attributes populated in Azure.

_Note:_ For the mail mapping section, you can use _userPrincipalName_ if it is in email format (e.g., user@company.com).

![Screenshot 2025-08-12 at 16.13.46-20250812-141347.png](https://support.bynder.com/hc/article_attachments/29076822902034)

_Note:_ Azure Entra provisioning compares many string attributes in a case-insensitive way. As a result, changing only the letter case of an attribute value (e.g., `John` → `john`, `USER@EXAMPLE.COM` → `user@example.com`) **does not trigger** an outbound SCIM update. We recommend users normalize identifiers to a consistent casing in the mappings (for example, map `userName`/email to lowercase) to avoid “invisible” changes not being sent.

*   To normalize in **Attribute Mappings**, use an expression like:
    
    *   `ToLower([mail])` → `emails[type eq "work"].value`
        
    *   `ToLower([userPrincipalName])` → `userName`  
        This ensures stable, predictable values and avoids case-only diffs being ignored.
        
*   **Required attributes for Bynder.** The following attributes are mandatory for each provisioned user in Bynder:
    
    *   `mail` (email address)
        
    *   `givenName` (first name)
        
    *   `surname` (last name)  
        Users missing any of these attributes will fail to provision via SCIM.
        
    
    Use the user's login name as `mail` if it is in a valid email format.
    

### Assign Users Or Groups

1.  In the left menu, go to **Users and groups**.
    
2.  Click **\+ Add user/group**, select who should be provisioned, and click **Assign**. ![Screenshot 2025-08-12 at 16.16.34-20250812-141651.png](https://support.bynder.com/hc/article_attachments/29093984922130)
    

### Test With Provision On Demand

1.  In the left-hand menu of the application, go to **Provision on demand**.
    
2.  Search for a user that is assigned to the application.
    
3.  Select the user and click **Provision**. ![Screenshot 2025-08-12 at 16.18.19-20250812-141821.png](https://support.bynder.com/hc/article_attachments/29093991794450)
    
4.  Wait for the process to complete and review the results:
    
    *   **Success** – the user should now appear in Bynder. ![Screenshot 2025-08-12 at 16.19.33-20250812-141935.png](https://support.bynder.com/hc/article_attachments/29093991795218)
        
    *   **Error** – check the error details. Common issues include:
        
        *   Missing required attributes (`mail`, `givenName`, `surname`).
            
        *   Invalid SCIM endpoint or token.
            
        *   Insufficient permissions for the SCIM account in Bynder.
            

_Tip_**:** Always test with at least one real user before enabling full automatic provisioning. This helps avoid bulk errors and ensures mappings are correct.

### Enable Provisioning

1.  Return to **Provisioning**.
    
2.  Set **Provisioning Status** to **On**.
    
3.  Click **Save**. Azure will start syncing users to Bynder. Initial sync may take several minutes.
    

### Troubleshooting

**Important:** In some cases, SCIM provisioning may complete with errors due to missing attributes, permission issues, or endpoint connectivity problems.  
To ensure you are notified promptly, it is strongly recommended to enable the **“Send an email notification when a failure occurs”** option under **Provisioning → Settings** in your Azure Enterprise Application.

![Screenshot 2025-08-13 at 13.31.31-20250813-113134.png](https://support.bynder.com/hc/article_attachments/29094427533458)

**Check the provisioning logs:** Go to **Monitor → Provisioning logs**, you can see detailed records of each provisioning attempt, including:

*   The user or group being provisioned.
    
*   The action performed (create, update, delete).
    
*   The result (success, failure) and any error messages.
    

Use the log details to identify common issues such as missing required attributes, invalid SCIM endpoints, or permission problems with the SCIM user account.

![Screenshot 2025-08-13 at 13.30.46-20250813-113049.png](https://support.bynder.com/hc/article_attachments/29094401173650)

Azure runs SCIM provisioning cycles at fixed intervals — by default, **every 40 minutes**. Changes made in Azure may take up to one full cycle to appear in Bynder.

Related Articles [](https://support.bynder.com/hc/en-us/articles/29068712565010-How-To-Enable-And-Use-Azure-SCIM-With-Bynder#h_01K3TMQ0VPXVBR0GYSAXT9FP7D)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[How To Enable And Use Okta SCIM With Bynder](https://support.bynder.com/hc/en-us/articles/27929897102866)

### _Level: Expert_

Expert-level articles are for users who have significant prior Bynder knowledge. These articles require you to know a lot of Bynder information and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
