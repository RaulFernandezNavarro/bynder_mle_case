# How To Enable And Use The Brightcove Integration – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/23981678927890

Summary[](https://support.bynder.com/hc/en-us/articles/23981678927890#h_01JY405QKBBV51A0JR6W60ZF5A)

----------------------------------------------------------------------------------------------------

**Brightcove** is a leading global video platform that provides businesses with tools for managing, delivering, and monetizing video content. Known for its robust features, Brightcove simplifies video hosting, streaming, and analytics while enhancing audience engagement and ensuring seamless playback across all devices. The integration between Brightcove and Bynder streamlines video content management and distribution. By leveraging Bynder’s DAM capabilities and Brightcove’s video tools, organizations can enhance efficiency, minimize risks, and maintain a consistent video publishing process. This integration enables a one-way upload from Bynder to Brightcove.

Who?[](https://support.bynder.com/hc/en-us/articles/23981678927890#h_01JY40444KZTC2SZ8197C5ZE7J)

-------------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once this integration is enabled users with the _Portal Settings_ permission can manage this integration.

Why?[](https://support.bynder.com/hc/en-us/articles/23981678927890#h_01JHR55MXTYVFCMFPZ3XF363JE)

-------------------------------------------------------------------------------------------------

Once the Brightcove integration is set up, Bynder can send videos to Brightcove based on specific triggers. A metaproperty called **Send to Brightcove** acts as the trigger for syncing videos. Any video asset marked with this metaproperty, either during upload or afterward, will automatically be synced to Brightcove. If a new version of a synced video is uploaded to Bynder, the existing video in Brightcove will automatically be updated with the latest version. This integration ensures the content remains up-to-date without manual intervention.

_Note: While the video file is synced, metadata associated with the asset in Bynder is not transferred to Brightcove. If required, you’ll need to manage metadata updates separately in Brightcove._

How?[](https://support.bynder.com/hc/en-us/articles/23981678927890#h_01JHR55MXTSWNB0B5592Z7GPWQ)

-------------------------------------------------------------------------------------------------

### Configuring The Brightcove Integration

1.  Navigate to **Settings > Advanced Settings > Portal Settings** in Bynder.
2.  Configure the integration under **Brightcove** in the integrations section.
3.  Set up authentication by entering your Brightcove credentials and Bynder domain URL.
4.  **Define** the metadata properties to trigger the sync, including:
    *   **Send to Brightcove:** Yes/No
    *   **Brightcove Status:** Displays sync status.
    *   **Brightcove URL:** Writes a link to the video in Brightcove to Bynder Asset’s Metadata
5.  **Save** the configuration.

### Using The Brightcove Integration

1.  Navigate to the **Asset Bank.**
2.  Select a **video** **asset** to sync.
3.  Update the **Send to Brightcove** metaproperty and choose which **Ingestion** **Profile** you’d like to use. 
4.  **Save the changes** to trigger the sync. The video will sync to Brightcove.

### Editing The Brightcove Integration

1.  Go to **Settings > Advanced Settings > Portal Settings**.
2.  Navigate to **Active Integrations** and edit the Brightcove configuration.
3.  **Save** the changes after making updates.

### Creating An API Application For Bynder X Brightcove

1.  **Navigate** to the admin settings panel, go to **API Authentication** and click on **\+ Add Application**.
2.  Add a **name,** **description** (optional), and **select** the user who will be associated with this connection. Actions performed by the integration in Brightcove will be attributed to the user selected here.![](https://support.bynder.com/hc/article_attachments/23981688546194)

![](https://support.bynder.com/hc/article_attachments/23981688547218)

3\. Select the following APIs to expose for the integration:

*   *   CMS Video Read
    *   CMS Video Read/Write
    *   Dynamic Ingest Create
    *   Dynamic Ingest Push Files
    *   Ingestion Profiles Configuration Read
    *   Ingestion Profiles Configuration Read/Write
    *   Ingestion Profiles Read**![](https://support.bynder.com/hc/article_attachments/23981688549906)**

4\. Copy the **Client ID** and **Client Secret** and keep them secure.  

*   *   *   You must enter this into the configuration wizard for your Brightcove authentication.![](https://support.bynder.com/hc/article_attachments/23981688550674)

5.  Get your **account ID** when setting up the configuration.  
    *   Find this under account information in the admin panel.  
          
        ![](https://support.bynder.com/hc/article_attachments/23981678925586)

FAQs[](https://support.bynder.com/hc/en-us/articles/23981678927890#h_01JHR5PSJY9B52F61Z51DS551J)

-------------------------------------------------------------------------------------------------

**What happens if I delete a video in Bynder or Brightcove?**

Deleting a video in Bynder will not remove it from Brightcove, and vice versa.

**What file types can be synced?**

Only supported video file types will sync from Bynder to Brightcove.

**Are there size limitations?**

Assets have no size limitations.

**How frequently does the sync occur?**

Bynder to Brightcove syncs are event-based and occur in real-time after configuring the metaproperty.

Related Articles[](https://support.bynder.com/hc/en-us/articles/23981678927890#h_01JY4020F62MEQSJDBD6SW4QNJ)

-------------------------------------------------------------------------------------------------------------

[Brightcove Website](https://www.brightcove.com/)

Share
