# Download Approval Asset Workflows – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360017349119-Download-Approval-Asset-Workflows

Download approval workflows allow you to approve download requests by multiple users in addition to providing more insight into why users make use of downloading watermarked materials.

Tell me more about download approval workflows[](https://support.bynder.com/hc/en-us/articles/360017349119-Download-Approval-Asset-Workflows#h_01HKXHGX27CMVFBZN9A12CZDCH)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A download approval workflow is a Asset Workflow preset that helps you to gather more information on why users want to download a watermarked asset. This type of workflow can also facilitate an approval process with multiple steps where assets need to be approved by multiple approvers.

### Note

Once the job is sent to the final download stage all users who have access to the job will be able to download the original assets without watermark in the download stage, regardless of whether they were added to **Disable** **asset** **download** **for** **profiles**.

If your approval process requires  more than two individuals to approve, you can add one or more stages in between and assign them to specific approvers.

### Note

Make sure that the **Finish** **job** button in the last stage of the approval workflow is clicked in order for the user to receive an email notification that the approval process has been completed.

How to create an approval workflow[](https://support.bynder.com/hc/en-us/articles/360017349119-Download-Approval-Asset-Workflows#h_01HKXHGX286JMDH4G2XSR0W8X7)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Go to ![settings_menu.png](https://support.bynder.com/hc/article_attachments/10341506262162)**Settings > Workflow > Preset management** and click **Add preset**.
    
2.  Click the **Campaign** dropdown and assign the preset to an existing Asset Workflow campaign.
    
3.  Set up the first stage to retrieve information on why the user wants to download the watermarked asset. Read more about Asset Workflow presets [here](https://support.bynder.com/hc/articles/360013932899#UUID-dfa7a3cc-8229-b794-0faf-f3dade5215a7)
    .
    
    *   Set the stage **Type** to **Form**.
        
    *   In the **Form** section set up the right [job metaproperties](https://support.bynder.com/hc/articles/360013871580#UUID-fc57c313-1b60-5739-c04f-1bc1fba930de)
        , so that you can gather the necessary information for your approver(s) to process the download request.
        
    *   Disable the download of the original file by making sure the option **Allow downloading the original version of watermarked assets** is not selected for this stage.
        
    
4.  Click **Add another stage** and set up the approver stage the following way:
    
    *   Set the stage **Type** to **Default**.
        
    *   Click the **Assign responsibility** field and assign the stage to the right approver or group of approvers.
        
    
5.  Click **Add another stage** and set up the download stage the following way:
    
    *   Set the stage **Type** to **Download**.
        
    *   (Optional) Set up a responsible user for this stage by selecting the appropriate user or user group in the **Assign responsibility** field.
        
    *   Select the option **Allow downloading the original version of watermarked assets** in order to let the user download the original file without watermark.
        
    *   (Optional) Select the option to **Enable** **downloads**.
        
        *   If you select **Enable** **downloads** you can additionally select **Allow only approved assets to be downloaded.**
            
        
    
6.  (Optional) In case you want multiple users or user groups to approve the asset you can add extra approval stages in between the first and the last stage. Follow the instructions in **step 4** to set up more approval stages.
    
7.  Click **Save** to save your preset
    

You can now start [assigning your approval flow](https://support.bynder.com/hc/en-us/articles/360017349119-Download-Approval-Asset-Workflows#UUID-50014b87-5942-d103-758b-b47667ea19eb_section-idm4480052158577631552266400823 "How to assign an approval flow to an asset")
 to individual watermarked assets or create different approval flows.

How to assign an approval flow to an asset[](https://support.bynder.com/hc/en-us/articles/360017349119-Download-Approval-Asset-Workflows#h_01HKXHGX28D722X1KPYXVS69NN)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Follow the steps below to assign an approval flow to a watermarked asset.

1.  Open the asset for which you want to set up an approval flow.
    
2.  Open the **Edit** tab.
    
3.  Go to the **Advanced Rights** section and make sure the options **Show watermark** and **Downloadable** are ticked.
    
4.  Tick the **Start workflow** option and in the dropdown that appears select the desired approval flow.
    
5.  Click **Save** to save the changes.
    

Users who want to download the watermarked asset can click the Start download request button in the asset detail view to request the download.

![start_download_request_creative_workflow.png](https://support.bynder.com/hc/article_attachments/10341537375122)

Share
