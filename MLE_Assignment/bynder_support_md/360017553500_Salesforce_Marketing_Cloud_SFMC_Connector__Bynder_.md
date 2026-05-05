# Salesforce Marketing Cloud (SFMC) Connector – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360017553500

[Salesforce Marketing Cloud (SFMC)](https://www.google.com/search?q=Salesforce+Marketing+Cloud+(SFMC)&rlz=1C5GCCM_en&oq=Salesforce+Marketing+Cloud+(SFMC)&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg8MgYIAhBFGD3SAQcxMTJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8)
 is a comprehensive digital marketing platform that provides powerful tools for automating marketing efforts across multiple channels. By integrating Bynder with SFMC, marketers can streamline their workflows, accelerate campaign execution, and enhance brand consistency.

This integration is designed to eliminate process bottlenecks and ensure that personalized content can be delivered swiftly across various channels, enabling marketers to keep pace with the growing demand for engaging content.

Click [here](https://www.bynder.com/en/videos/bynder-integrates-with-salesforce-marketing-cloud/)
 for a video walkthrough of how the integration works.  

*   Authenticate and log in to Bynder right from Marketing Cloud
*   Search and filter to easily find assets based on permissions
*   Add Bynder assets to any content that uses content blocks in SFMC
*   Select derivatives made for specific channels (DAT included)
*   [A/B Testing with Advanced Content](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JB2QJN53QRC4VPH53TD0MEJR)
    
*   Scale to fit, crop, and resize on the fly

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

**Who can set up and manage integrations?**

Users with the following rights can set up integrations: 

*   [**Portal Settings**](https://support.bynder.com/hc/en-us/articles/18433246503442-Permissions-in-Asset-Bank#:~:text=Manage%20portal%20settings%20%2D%20Allows%20users%20to%20access%20portal%20settings.)
    

Before Setting Up Integration[](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JB9YWM1HFP35MJTAZTR3YMNM)

------------------------------------------------------------------------------------------------------------------------

Make sure you have a Sales Force Marketing Cloud account and Email Studio enabled in SF Content Builder. Ensure that your Bynder assets are configured to allow SFMC users access based on their roles and needs.

How to Install and Set Up the Salesforce Marketing Cloud Connector[](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JB2PBG4YJGGZ85ZPTP3THNBA)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Log into your Salesforce Marketing Cloud account.
    
2.  Use the installation URL to install the package.
    
    *   You will receive the installation package URL from your Customer Success Contact.
        
3.  You will be redirected to the SFMC setup to confirm the installation.

How to Add Bynder Assets Using Content Builder

### Note

If you have [DAT](https://support.bynder.com/hc/en-us/articles/18952775916562)
 enabled, transformation options are available within the Bynder Custom Content Block (UCV). Learn more here.

1.  Once you’ve successfully downloaded the Connector, navigate to your SFMC.
    
2.  Navigate to the ![content_builder_salesforce.png](https://support.bynder.com/hc/article_attachments/10641470598418) Content block and select **Content Builder i**n the dropdown.
    
3.  Find the content item, such as an email template, to which you want to add a Bynder asset. Click its name to open it.
    
    *   Alternatively, click the **Create** button in the top right corner and click **Email message** to create a new email.
        
4.  Click **Edit > Edit Content** in the top right corner if you opened an existing content item.
    
    *   Ensure you're in the **Blocks** tab of the left sidebar and scroll to the **Custom** section.
        
5.  Drag and drop the **Bynder** block to where you want to add an asset to your content.
    
    *   The [Compact View](https://support.bynder.com/hc/articles/360014369640#UUID-3ab280b1-6742-4e2a-e596-60a5fb175166)
         will display in the **Content** tab of the left sidebar.
        
6.  Click **Connect** if your company's Bynder portal URL is already filled in in the pop-up. If not, enter the URL in the below format. A pop-up will open, allowing you to log in to your Bynder environment. Log in to the portal the usual way.![](https://support.bynder.com/hc/article_attachments/22260414255634)
    

How to Add Bynder Assets to a Custom Content Block[](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JB2PBG4ZP36ZXA3JQ8NSJ2BE)

---------------------------------------------------------------------------------------------------------------------------------------------

Use Content Blocks to create reusable, modular content for messages in the Marketing Cloud. If a general Bynder Content Block is set up in your environment, you can create custom blocks enriched with Bynder assets. This streamlines content creation by eliminating the need to manually add assets—such as your brand logo—every time you send an email.

You ensure consistency and efficiency by storing assets in your Bynder portal and embedding them in a Content Block. Each time the asset is updated in Bynder, the block automatically reflects the change, saving time and guaranteeing you always use the latest version.

When you crop or resize a Bynder asset in Salesforce Marketing Cloud (SFMC), it's saved in the SFMC library. As a result, any version updates made in Bynder won’t automatically appear in your Content Block—you'll need to update the asset manually in Marketing Cloud.

1.  Log in to your Marketing Cloud environment.
2.  Select ![content_builder_salesforce.png](https://support.bynder.com/hc/article_attachments/10641470598418) the **Content Builder** button and click **Content Builder** in the next dropdown.
3.  Click the **Create > Content Blocks > Bynder** to create a new block with a Bynder asset.
    *   Depending on your setup, the name of the **Bynder** block may vary.
4.  The [Compact View](https://support.bynder.com/hc/articles/360014369640#UUID-3ab280b1-6742-4e2a-e596-60a5fb175166)
     will display in the **Content** tab of the left sidebar.
5.  Click **Connect** when your company's Bynder portal URL is already filled in in the pop-up, and you still need to log in. If not, enter the URL in the format below. A pop-up will open, allowing you to log in to your Bynder environment. Log in to the portal the usual way.
6.  Check [here](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JB2PBG4ZP36ZXA3JQ8NSJ2BE)
     for information about adding an asset to your Content Block using the Compact View.
7.  You can configure your content block further using the Block Setting and HTML Editor tabs. Read more about creating Content Blocks [here](https://help.salesforce.com/articleView?id=mc_ceb_create_content_blocks.htm&amp;type=5)
    .
8.  Click the **Save** button in the top right corner. A pop-up will open.
9.  Enter a name for your Custom Block in the **Name** field.
10.  (Optional) Fill in the additional non-required fields.
11.  Click **Save** to create your new Content Block

How to Edit, Replace, or Delete a Bynder Image in Cloud Connector[](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JB2PBG4ZD127AXDVT6YGCKT9)

------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Go to the content item where you want to edit, replace, or delete your Bynder asset.
    
2.  Click the **Edit** button at the top right corner. Your Bynder asset will appear in the **Content** tab.
    
3.  Perform one of the following actions:
    

### Edit Image

1.  Modify your Bynder image using the available cropping, resizing, formatting, and other tools in Content Builder.

### Replace Image

1.  Click the **Replace Image** button to replace the image. Use the Compact View to select another image or to change the derivative used.

### Delete Image

1.  Click the **Delete Image** below the image to delete the image. The Compact View will show again. Ignore this and go to the next step.
2.  Click the **Save** button in the top right corner to save your modifications.

Important Information[](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JBA01NCNH51GATB17VZ5W2ED)

----------------------------------------------------------------------------------------------------------------

*   Changing the data source may render the rule invalid if the fields used in the rule are not present in the newly selected data source. The rule relies on attributes specific to the original data source, so switching to a different one will cause the rule to break.
*   A pop-up message will appear to notify the user when the data source is changed, indicating that the rule is no longer valid.

 [](https://support.bynder.com/hc/en-us/articles/360017553500#h_01JB2QJHRY79EMANT7G9B0PHNR)

--------------------------------------------------------------------------------------------

Share
