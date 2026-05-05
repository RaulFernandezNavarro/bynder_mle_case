# How To Upload Assets Via Mass Uploader – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013870140

Summary[](https://support.bynder.com/hc/en-us/articles/360013870140#h_01JKX7CMYS74SB0MSHB9K3SAZJ)

--------------------------------------------------------------------------------------------------

If you have a large batch of assets you want to upload to your Asset Bank, you can use the Mass Uploader. Your files _must_ be accompanied by a CSV file listing your metaproperties and their values, which will then automatically populate the metaproperties and tags. Depending on your settings, new metaproperty options will also be created automatically.

If derivatives are enabled for your portal, the Mass Uploader will create them upon upload.

If you want to upload new versions to existing assets in batches, use the _Mass Version Updater_.

Who?[](https://support.bynder.com/hc/en-us/articles/360013870140#h_01JNDYCAAPS022K7ZMJF3YS5C3)

-----------------------------------------------------------------------------------------------

This feature/solution is enabled by a Bynder Admin.

Please note the user must have the _upload assets_ permission enabled. If your portal does not have this permission please contact your Bynder Admin.

Why?[](https://support.bynder.com/hc/en-us/articles/360013870140#h_01JNZT1AB5TENG11DANDJD11BX)

-----------------------------------------------------------------------------------------------

Bynder wants to save our customers time by allowing mass uploads to be batched. This allows properly provisioned assets to be added to the bank in large batches instead of one by one. 

How?[](https://support.bynder.com/hc/en-us/articles/360013870140#h_01JNZT1MY3CCH2DC2MDR057XE7)

-----------------------------------------------------------------------------------------------

### Properly Provision The Assets Before Uploading

Before uploading we require you to map the metaproperty and metaproperty options to the corresponding columns in your CSV file. Once the mapping is in place you can upload your CSV file.

Properly provisioning the CSV is integral to a successful upload. The Mass Uploader does not consider required fields or dependencies. If the CSV file contains only some of the required metaproperties and fields it will still be uploaded. Additionally, the Mass Uploader can extract EXIF/XMP/IPTC information. If the metaproperties in the CSV file contain values, they take precedence; however, if the values are missing, then the EXIF/XMP/IPTC information is retrieved.

### Creating A CSV File

1\. First, enter **Filename** in row one of **column B**. 

*   You must use the file extension in this section when filling out information. The extension is _case sensitive_ be careful to use .jpg versus .JPG or vice versa depending on the file itself. 

2\. Second, enter **Name** in row one of **column C.**

3\. Next, enter **Description** in row one of **column D.**

4\. Then, enter **Tags** in row one of **column E.**

*   Bynder will create a tag if the one listed does not exist. Be mindful of spelling, grammar, and separating tags by a comma (,).

5\. Lastly, use **columns F - XFD** for custom metaproperties. Row one of each column should have the name of the metaproperty, i.e. **Asset Type** in row one **column F**, **Region** in row one **column G,** and so on.

*   Just as with tags you can have multiple metaproperty options per asset, just separate them with a comma (,).

6\. Fill in the data for each asset you wish to mass upload. The assets information should match the structure we just created in the steps before. Assets without certain custom metaproperties can have that space left blank.

_Optional: Use **column A**_ as a place for the **ID** of the brand you want to tag the asset with. Make sure to build the structure as such, putting **ID** in row one of **column A.** To get your **Brand ID,** go to **Settings** > **Taxonomy** > **Brands** and click on the brand. Copy the ID from the URL in the address bar of your browser.

7\. Save your file as a semicolon-separated CSV file in **UTF-8** encoding, alternatively some portals can be configured to accept comma-separated CSV files. 

### Important Formatting Rules For Your CSV File

*   Do not use trailing spaces. Ensure all trailing whitespace is removed from your CSV file before submittal.
*   Use the metaproperty option labels in your CSV file and not the metaproperty option names.
*   Using some special characters (+, = , ' , \`) in filenames, or diacritics (ë, ç, û, etc.) in filenames could cause issues when being read by the mass uploader. Consider avoiding these special characters and follow a "normalized" naming convention for filenames.

### How to Use the Mass Uploader

Once your CSV file is prepared and metaproperty mapping is complete, you can start batch-uploading your files.

1.  Make sure your CSV file includes at least one asset's data.
2.  Click your name in the top right corner of the screen and click Mass Uploader.
3.  Drag and drop your CSV file to the left sidebar or click Add Files to upload your CSV file.
4.  If your CSV file is processed correctly, you will see the message "Your CSV file was successfully parsed." If not, read the error message, adjust your CSV file, and submit again.
5.  Drag and drop your files in the left sidebar or click Add Files. They will automatically start uploading and tagging with the metadata from the CSV file. You should not upload more than **500** assets per batch.
6.  Once a file is uploaded correctly, the status will change to Successful.

_Note: If a recently uploaded asset does not appear immediately simply refresh your asset overview page._

### Mass Uploader Limitations

*   Assets can not be marked as limited usage, archived, downloadable, or public.
*   You can not add a watermark to assets using the Mass Uploader.
*   The Mass Uploader doesn't generate automated tags.
*   The Mass Uploader won't index the content of digitized documents, such as PDF and Word documents. This means that when you enter their content in the search bar, these documents won't be returned as a search result.
*   The Mass Uploader is not meant to update metadata such as filenames.
*   It is not possible to add any Advanced Rights through the Mass Uploader (such as limited usage, archive, watermark, etc.)
*   It is not possible to Relate Assets via the Mass Uploader. This needs to be actioned manually once the assets are available in the DAM.

FAQs[](https://support.bynder.com/hc/en-us/articles/360013870140#h_01JH3TFWZ5R57MTS63NXGV18KK)

-----------------------------------------------------------------------------------------------

**Why is my CSV file not saving as a semicolon-separated CSV file?**  
Some software default saves your spreadsheets as comma-delimited files. 

**Do I always have to have semicolon-separated CSV files?**

No, Depending on your portal configuration you can use commas instead of semi-colons. 

**Why is the list I'm giving separating every item in my options list as separate metaproperty options?**

The mass uploader often uses commas as the delimiter, this means if you have an option with a list within it, and the list is comma delimited, each list item will be separated as its own option.

**How many files can I upload at once with the Mass Uploader?**

Please batch in increments of no more than 500.

**Why is the Mass Uploader not responding when uploading my CSV file?**  
Make sure your CSV file includes at least one asset's data.

**Will automated derivatives be generated for assets uploaded via the Mass Uploader?**  
Yes, automated derivatives (including those using regex terms) can be created via the Mass Uploader like they are with the standard front end uploader.

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013870140#01JKXD2A27M2DYQR7VF0JX16KP)

---------------------------------------------------------------------------------------------------------

[How To Use The Bynder Mass Version Updater](https://support.bynder.com/hc/en-us/articles/360013931879)

Share
