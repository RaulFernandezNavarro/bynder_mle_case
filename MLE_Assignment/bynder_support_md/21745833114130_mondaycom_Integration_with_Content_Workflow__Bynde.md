# monday.com Integration with Content Workflow – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/21745833114130

[monday.com](https://monday.com/)
 (monday) is a cloud-based platform that allows users to create their own applications and project management software. 

This integration seamlessly connects a monday board to a Content Workflow project. This integration allows users to trigger the creation of a task in Content Workflow directly from an item in monday.com. Once the connection is established, the item in monday.com and the task in Content Workflow are linked bidirectionally. This means updates made in monday.com will be synced in real-time to Content Workflow and vice versa. Users can configure which fields are connected (within certain limitations), making the integration highly flexible for different workflows.

### Note

This integration is available to Bynder + Content Workflow customers with access to the [Bynder Integration Hub](https://support.bynder.com/hc/en-us/articles/11400106439698)
. If you're a Content Workflow customer but **do not** have access to the Bynder Integration Hub, this integration is currently _unavailable_. However, we recommend checking our [product roadmap](https://support.bynder.com/hc/en-us/articles/4406445265938)
 for updates on when this integration will become accessible to all Content Workflow customers.  
The number of automations you can set up depends on your monday.com account type. For more information, click [here](https://monday.com/)
.

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

**Who can set up this integration?**

Users with the following rights can set up this integration

*   [Create Projects](https://support.bynder.com/hc/en-us/articles/14809314432274-Roles-and-Permissions-in-Content-Workflow)
    
*   [Manage Webhooks](https://support.bynder.com/hc/en-us/articles/14809314432274-Permissions-and-Roles-in-Content-Workflow#:~:text=tool%2C%20where%20enabled.-,Manage%20Webhooks,-Permission%20is%20required)
    
*   [Access All Items](https://support.bynder.com/hc/en-us/articles/14809314432274-Permissions-and-Roles-in-Content-Workflow#:~:text=Workflow%20product%20updates.-,Access%20all%20items,-Ability%20to%20view)
    
*   [Create Items](https://support.bynder.com/hc/en-us/articles/14809314432274-Permissions-and-Roles-in-Content-Workflow#:~:text=have%20access%20to.-,Create%20items,-Ability%20to%20add)
    
*   [Set Due Dates](https://support.bynder.com/hc/en-us/articles/14809314432274-Permissions-and-Roles-in-Content-Workflow#:~:text=assignees%20from%20items.-,Set%20due%20dates,-Ability%20to%20add)
    
*   [Update Workflow Status](https://support.bynder.com/hc/en-us/articles/14809314432274-Permissions-and-Roles-in-Content-Workflow#:~:text=Update%20workflow%20status)
    

### Caution  

Admins should ensure that automations set up through this integration are not deleted or disabled in monday.com. Doing so will halt event processing, and system updates will no longer sync. The automations will still be visible in the monday.com automation center.

How to Set up the Integration[](https://support.bynder.com/hc/en-us/articles/21745833114130#h_01J9KYDPDJK05MSJKEG06G0KPN)

--------------------------------------------------------------------------------------------------------------------------

 If you want to add more than one monday board, you’ll need to create multiple configurations. 

1.  Navigate to **Settings** > **Advanced** **settings** > **Portal** **settings**.
2.  Click **Browse** **Integrations** in the left sidebar.
3.  Select **monday**/**Content** **Workflow** **Integration**.
4.  Select **Add** **new** **account** and add your monday.com credentials.
5.  Within your monday.com account, navigate to your admin console and copy your **Personal API Token,** which can be found [here](https://support.monday.com/hc/en-us/articles/360005144659-Does-monday-com-have-an-API)
    .![](https://support.bynder.com/hc/article_attachments/21836682363794)
6.  Select the **monday board** you want to sync.![](https://support.bynder.com/hc/article_attachments/21836682365586)
7.  Select a **column** **type** from the dropdown menu to sync an item from monday to Content Workflow. The following column types are available to trigger a sync: 
    *   Text
    *   Long Text
    *   Status
    *   Checkbox
    *   Dropdown
    *   Email
    *   Tags
8.  After selecting the column, choose a **specific** **value** from that column to trigger the sync with Content Workflow. 
    *   If the column type has predefined values (e.g., Status), they will appear for selection. 
    *   If the column doesn’t have predefined values (e.g., Text), you can manually enter the value for sync.![](https://support.bynder.com/hc/article_attachments/21836653350930)
9.  Select the column in monday.com to track the item's status in Content Workflow.
    *   This can either be a **status** or **text** **field**.
    *   Any status changes in Content Workflow will automatically update the corresponding field in monday.com and vice versa. This _bidirectional_ sync keeps both platforms in real time.![](https://support.bynder.com/hc/article_attachments/21836682370834)
10.  Select the monday.com column to use to name your Content Workflow item. 
    *   This field can use either a **name** or **text** column type.![](https://support.bynder.com/hc/article_attachments/21836682371474)
11.  (Optional) Select the option to **add a link on monday.** You can directly add a link to the Content Workflow item on your monday board. 
    *   A dropdown will appear with available columns. 
        *   This field is only compatible with the **link** column type.![](https://support.bynder.com/hc/article_attachments/21836653355538)
12.  (Optional) Select the **Sync Due Dates** option to sync the **monday** **status** **column** with the **Content** **Workflow** **status** due date.
    *   A dropdown with available **date** **column** types will appear. 
    *   Date fields will sync bi-directionally between each platform.![](https://support.bynder.com/hc/article_attachments/21836682372370)
13.  Enter your **Content** **Workflow** **Credentials** (content workflow account email and API key for Content Workflow.
    *   You can generate an API key by clicking [here](https://support.bynder.com/hc/en-us/articles/14984593670034)
        .
14.  Select the **Content** **Workflow** **project** where synced items will be created. 
    *   When a sync is triggered from monday.com, this project will automatically create a new item.![](https://support.bynder.com/hc/article_attachments/21836653356434)
15.  Select which **Content** **Workflow** **template** to use when creating a new item from your sync.![](https://support.bynder.com/hc/article_attachments/21836653356946)
16.  Once all settings have been configured, click **Save**.

### Note

To sync multiple boards/projects, you must create a [new connection](https://support.bynder.com/hc/en-us/articles/21745833114130#h_01J9KYDPDJK05MSJKEG06G0KPN)
 for each board.  

How to Use the Integration[](https://support.bynder.com/hc/en-us/articles/21745833114130#h_01J9KYH2C6CEBQMKGDHFDQ5EM7)

-----------------------------------------------------------------------------------------------------------------------

After configuration, you can update your monday trigger in the selected board to start syncing Content Workflow projects. Once triggered, any updates made to the configured column will sync in real time between Monday.com and Content Workflow, ensuring both platforms stay up to date.

Edit Integration[](https://support.bynder.com/hc/en-us/articles/21745833114130#h_01J9KYHBPR642DRBGP63FSQFWT)

-------------------------------------------------------------------------------------------------------------

You can edit the configuration to update your board, column, or trigger, update the settings, or edit your monday settings.

1.  Navigate to **Settings** > **Advanced** **settings** > **Portal** **settings**.
2.  Click **Active** **Integrations** on the left sidebar, then **edit** in the connection section you want to update.
3.  Make your changes, then click **Save**.

FAQ[](https://support.bynder.com/hc/en-us/articles/21745833114130#h_01JKTKM5QTYJ6XH8MR411BN7Q3)

------------------------------------------------------------------------------------------------

**Can I turn off automations in monday.com?**  
No, disabling or deleting automations in monday.com will stop the integration from working. Ensure that automations remain active to allow updates to process between the platforms.

**Can I sync custom fields between monday.com and Content Workflow?**  
Only specific column data types can be synced (Text, Long Text, Status, Checkbox, Dropdown, Email, Tags, Date, and Links). All other custom fields are not supported. 

**Are there any limitations to the number of tasks I can sync?**  
There are no specific limitations on the number of tasks, but syncing large volumes of data could result in slower performance.

**Can I assign different templates to different tasks in CW?**  
Users can select any available template when creating a new item in Content Workflow.

**What happens if I delete the monday item or Content Workflow item?**

If you delete an item in monday or Content Workflow, you must re-establish the connection to continue synchronization. In that case, you'll need to create a new item in monday, automatically generating a new task in Content Workflow or visa versa. These newly created items will then be linked together.

Share
