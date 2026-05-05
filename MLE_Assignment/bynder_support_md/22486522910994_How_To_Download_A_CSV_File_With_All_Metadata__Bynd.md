# How To Download A CSV File With All Metadata – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/22486522910994-How-To-Download-A-CSV-File-With-All-Metadata

Summary[](https://support.bynder.com/hc/en-us/articles/22486522910994-How-To-Download-A-CSV-File-With-All-Metadata#h_01JR2W5GPZN9KBY0M96REY5XDR)

-------------------------------------------------------------------------------------------------------------------------------------------------

You can download metadata for selected assets as a CSV file. The CSV will include certain default metadata and custom ones with extra information about the current state of the asset that are available in the portal.

Who?[](https://support.bynder.com/hc/en-us/articles/22486522910994-How-To-Download-A-CSV-File-With-All-Metadata#h_01JR2W6751W4QZG51QMBMF73AR)

----------------------------------------------------------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once enabled users need the _Export metadata CSV file on download_ permission to use this feature.

Why?[](https://support.bynder.com/hc/en-us/articles/22486522910994-How-To-Download-A-CSV-File-With-All-Metadata#h_01JR2W6MH86G6WF7HZ0G9W0C12)

----------------------------------------------------------------------------------------------------------------------------------------------

If users want to download metadata for assets for auditing purposes, downloading the metadata allows them to ensure data quality and compliance within their DAM. Furthermore, if a user wants to download metadata for assets to integrate and leverage this data in an external system, or for supporting additional operational workflows.

How?[](https://support.bynder.com/hc/en-us/articles/22486522910994-How-To-Download-A-CSV-File-With-All-Metadata#h_01JR2XMC29K61TEPW3CNVEGKA1)

----------------------------------------------------------------------------------------------------------------------------------------------

1.  Navigate to your Asset Bank. You can search or filter assets to find the ones you want.
2.  In the **Asset** **Overview** screen, click the left button on your mouse and drag the mouse over the assets you want to select. The items in the blue selection will be selected when you release the mouse button, or you can click **Command-A** to select all the assets. 

*   We recommend that you download in batches. When triggering the download, the system has to zip the file first. The bigger the CSV file, the more likely it is to fail, as you might have a time-out or lose internet connection for a minute.  

4.  Click ![download.png](https://support.bynder.com/hc/article_attachments/25974640397330)in the top filter bar. 
5.  The **Download selection** pop-up window will open select **Export to CSV,** which will download metadata in a CSV without downloading the assets. 
6.  Click **Start Download.**
7.  Once the download is complete, it will be **saved to your device**. 

### What Information Is Being Exported?

The order of the metadata is presented below. Custom metaproperties that appear after the _Description_ are going to follow the Z-index order that has been configured in the portal.

_Note: Derivatives inherit the values of the original asset aside from Watermark_ and _Public._ _Date/Time fields are represented in the UTC timezone._

|     |     |
| --- | --- | 
| **Metadata Name** | **Description** |
| Asset ID | Example:<br><br>0D7D5817-C6AE-47B5-AECCD417F3D441D1 |
| Title | Title of the asset as presented in the Asset Bank. |
| Filename | Original filename of the asset in the Asset Bank. |
| Description | Description of the asset in the Asset Bank. |
| Custom Metaproperties | _This data will be custom based on the settings configured._ |
| Tags | Comma separated list of tags. |
| Watermark | **For original Asset:** True or False.<br><br>_If there is a future date then the value will be false._<br><br>**For derivatives:** True or False based on the value set in the configuration of the derivative preset. |
| Watermark Date | Watermark effective date if there is a future date for the asset to be watermarked. |
| Public | True or False |
| Archive | True or False<br><br>_If there is a future date set the value will be false._ |
| Archive Date | Effective date when the asset becomes archived. |
| Downloadable | True or False |
| Limited Usage | True or False<br><br>If _Now_ is selected then it should be True<br><br>If _until_ is selected then the value will be true. |
| Limited Usage Date | Limited usage end date when _until_ is shown. |
| Created By | User name |
| Creation Date | Date created |
| Published Date | Date published extracted from original file during upload. |
| Modified By | User name |
| Modified Date | Date modified |
| Copyright | Copyright information extracted from original file during upload. |
| File Size | File size represented in kilobytes. |

FAQs[](https://support.bynder.com/hc/en-us/articles/22486522910994-How-To-Download-A-CSV-File-With-All-Metadata#h_01JR2YJJRCJG2FH09KWBHFY7F8)

----------------------------------------------------------------------------------------------------------------------------------------------

**When will a zip file be created?**

A .zip file will be created if you select more than one asset regardless of size.

**Why can't I download a CSV file when I have the correct permission enabled?**

This may happen if the feature is not enabled. Please reach out to your Customer Success Contact to have it enabled. 

Related Articles[](https://support.bynder.com/hc/en-us/articles/22486522910994-How-To-Download-A-CSV-File-With-All-Metadata#h_01JR2YJSA8ZX0YH9CTW061HVQ0)

----------------------------------------------------------------------------------------------------------------------------------------------------------

[How To Download And Export Assets With Metadata](https://support.bynder.com/hc/en-us/articles/11907726078866)

[How To Create Custom Metadata Fields](https://support.bynder.com/hc/en-us/articles/360013931199)

[Metadata Embedding Options for Downloaded Assets](https://support.bynder.com/hc/en-us/articles/22486558223762)

### _Level: Proficient_

Proficient-level articles are for users who have some prior Bynder knowledge. These articles require you to know the basics and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
