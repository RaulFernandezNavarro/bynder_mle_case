# Understanding And Using Metadata – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/17636258833042-Understanding-And-Using-Metadata

Summary[](https://support.bynder.com/hc/en-us/articles/17636258833042-Understanding-And-Using-Metadata#h_01JWJKQ01NC1CPNDKAK2FZ5G7E)

-------------------------------------------------------------------------------------------------------------------------------------

Metadata is data that describes other data. For example if you think of a book, the title, author, publisher, year published, and edition would all be metadata regarding the book. For assets the metadata is an effective system that makes the specific data of digital files simpler to work with. Metadata helps clarify information and makes it easier to find and manage digital files. 

Metadata is a critical component for search inside major marketing tech systems like CRM, DAM, and CMS, allowing for easier integration between marketing tools. 

Who?[](https://support.bynder.com/hc/en-us/articles/17636258833042-Understanding-And-Using-Metadata#h_01JWJM3XV4J6XRADEXN0HBN7Q7)

----------------------------------------------------------------------------------------------------------------------------------

This feature/solution is enable-able by any Bynder portal user.

Why?[](https://support.bynder.com/hc/en-us/articles/17636258833042-Understanding-And-Using-Metadata#h_01JWJM43SVE9MZH7K1P7YNSHP5)

----------------------------------------------------------------------------------------------------------------------------------

You can extract embedded metadata from your assets and map it to your existing metaproperties. This way, you can automate the enrichment of your assets with existing metadata. You can use any EXIF, XMP, or IPTC tag. However, the only fully custom metadata tags Bynder supports are those based on the XMP metadata standard. 

How?[](https://support.bynder.com/hc/en-us/articles/17636258833042-Understanding-And-Using-Metadata#h_01JWJM63CEQGC2C9WVACCKA1HF)

----------------------------------------------------------------------------------------------------------------------------------

### Consider:

Users can decide how they want to configure downloaded metadata, first there are some things to consider:

*   Do you want XMP metadata embedded with each download?
*   Should this be optional or required for each downloaded asset?
*   Do you want to remove the original metadata before downloading and ensure that only metadata configured in the DAM is embedded?  
*   If Bynder-specific metadata is included, could you decide which fields to map?
*   If including the default Bynder fields (e.g., title, description, tags), do you want them added to the standard tag or require them in another tag? Please note that Bynder default fields are not automatically mapped upon download. You must manually specify which fields you’d like the Bynder default fields to be mapped to.

### Creating Custom Metadata Fields

1.  Create a new Metaproperty, and select the **single-select** metaproperty type to map the metaproperty.
2.  Navigate to **Settings > Advanced Settings > Portal settings.**
3.  Click **Embedded metadata configuration** in the left sidebar and ensure you’re in the **On asset upload** tab.
4.  **Default metadata fields:** Click **View default fields** to review the default metadata continuously extracted and embedded in your assets once uploaded to Bynder, regardless of settings.
5.  Paste the exact name of the metadata tag in the **Custom metadata fields** box. Separate the values by commas in case you want to map multiple metadata tags.
6.  Click the **Metaproperties** dropdown to select the Bynder metaproperty to which the metadata should be mapped.
7.  Click the **Add Custom field** to add additional mappings.
8.  Click **Save Changes.**

_Note: In order to ensure that the correct value is extracted when mapping tags from EXIF, XMP and IPTC ensure that you use the correct namespace as well._ _For Example: WhiteBalance can be found under two namespaces XMP-exif and XMP-crs. If the namespace is not provided in the mapping and there is a value option for both tags then Bynder cannot know which will be extracted._  

![Screenshot 2024-12-05 at 3.48.55 PM.png](https://support.bynder.com/hc/article_attachments/27113157098898)

_Note: If you would like your changes to apply to **existing** assets in your portal, please contact Bynder support._

### Downloading Assets With Metadata

1.  Navigate to the asset(s) you want to download.
2.  Check the box next to **Include XMP metadata** in the Asset Details view. _This box can be checked by default if you want to make this required._
3.  Click one or more of the available files to start the download. Alternatively, you can click **Download all files** to download all the files at once.

_Note: Bynder default fields are not automatically mapped upon download. You will need to manually specify which fields you’d like the Bynder default fields to be mapped to._

### Exporting Metadata

You can export metaproperties and their values to specific metadata tags. We support exporting to XMP, IPTC, and EXIF.

If you don't want this metadata to be written to the default metadata tags, we can set it up so it is written to a specific tag.

For example, instead of writing the Bynder **Title** to the default **XMP:Title** tag, it can be written to **XMP-photoshop:Headline**. 

1.  Navigate to **Settings > Advanced Settings > Portal settings.**
2.  Click **Embedded metadata configuration** in the left sidebar and then the **On asset download** tab.
3.  **CSV download:** Enable this setting to allow users with the appropriate permission to download a CSV of the metadata for selected assets.
4.  **XMP download:** Enable this setting to embed the XMP metadata in the downloaded assets. If enabled, you can select which XMP metadata should be embedded.
5.  **Required download:** Enable the XMP metadata always to be embedded in the downloaded assets.
6.  **Update the existing XMP metadata:** Enable the mapping of the Bynder metadata to metadata fields upon download.  
    *   **Default Bynder metadata:** If you don’t want the default metadata to be written to the default metadata tags, add the metadata tag that you want the metadata written to, separated by a comma.
    *   **Metaproperties:** You can map Bynder metaproperties and their values to specific metadata tags. We support exporting to [XMP](https://exiftool.org/TagNames/XMP.html)
        , [IPTC](https://exiftool.org/TagNames/IPTC.html)
        , and [EXIF](https://exiftool.org/TagNames/EXIF.html)
        .  
        *   In the **Metaproperties** column, click the dropdown to select a Bynder metaproperty.
        *   In the **Metadata tags** column, paste the exact name of the metadata tag to which you’d like to write the metaproperty.
        *   Click **Add metaproperty** to add a mapping.
7.  Click **Save Changes**.

### Extracting XMP Metadata When Uploading Assets

Embedded metadata from cameras, photo editing tools, or other systems can be leveraged to automatically populate your metaproperties in Bynder. Supported metadata formats include EXIF, XMP, and IPTC tags. While any tag within these formats can be used, fully custom metadata tags must adhere to the XMP metadata standard to ensure compatibility.

_Note: Supported file types are the ones supported via the [Exiftool](https://exiftool.org/#supported)
 except:_ 

*   .zip
*   Office Documents
*   Audio files(aside from default fields, which _can_ be extracted).   

_Note: Metadata extraction for both default and custom metadata is supported for our uploaders aside from uploads via the API and templates._

### Default Metadata

Once uploaded to Bynder, the following default metadata is continuously extracted and embedded in your assets, regardless of settings. _This cannot be edited or disabled._

|     |     |
| --- | --- |
| **Bynder Field** | **Metadata Tags** |
| Author | Artist(XMP), By-Line(IPTC), Author(XMP), Creator(XMP) |
| Copyright | Copyright (IFD0, EXIF, XMP), CopyrightNotice (IPTC) |
| Description | Description(XMP), ImageDescription(EXIF), Caption-Abstract(IPTC) |
| DPI | XResolution(EXIF) |
| Make | Make (EXIF, XMP) |
| Model | Model (EXIF, XMP) |
| Publication date | CreateDate(EXIF, XMP), DateTime(XMP) |
| Tags | Keywords (IPTC), Subject (DC) |
| Title | Title(XMP-dc, XMP), Headline(IPTC), ObjectName(IPTC), ImageTitle(EXIF) |

![Screenshot 2025-09-11 at 10.29.55.png](https://support.bynder.com/hc/article_attachments/29486964965266)

The width and height that the user can see on the original files download button are being extracted by default from the following metadata based on the order provided below; in case the first in sequence does not exist:  
ImageHeight (PNG), ImageWidth (PNG)  
ImageHeight (DNG), ImageWidth (DNG)  
ImageHeight (File), ImageWidth (File)  
ImageHeight(ExifIFD), ImageWidth(ExifIFD)  
ImageHeight, ImageWidth

### UsingThe ExifTool

1.  Navigate to [ExifTool.](https://exiftool.org/)
    
2.  Select the appropriate package for your OS(Windows or MacOS).
3.  Open the **Terminal**.
4.  Type **ExifTool** and press space.
5.  Drag the file you would like to read into the **Terminal** and press **Enter**.
6.  Scroll through the metadata and **look for the name** of the metadata embedded in the asset. 
7.  This information can be used to write the metaproperty in your Bynder DAM.  

![uuid-da438980-c27a-a934-5a71-cdfbbbc4449c.png](https://support.bynder.com/hc/article_attachments/27113157100050)  
_Example of Exif data analysis using the ExifTool._

If the information you want to map to Bynder is not always available in the same Exif field and is saved to multiple Exif fields with (slightly) different names. In that case, you can map all Exif fields to the same metaproperty in Bynder.

FAQs[](https://support.bynder.com/hc/en-us/articles/17636258833042-Understanding-And-Using-Metadata#01JWR3WT4HM7HRV3364SYYW2KW)

--------------------------------------------------------------------------------------------------------------------------------

**When I make changes in Embedded Metadata Configuration, can I apply these changes to existing assets?**

No, if you change the Embedded Metadata settings, your changes will only apply to newly uploaded assets. If you want your changes to apply to all pre-existing assets, please contact Customer Support. 

**When I make changes in Embedded Metadata Configuration, can I apply these changes to existing assets?**

No, if you change the Embedded Metadata settings, your changes will only apply to uploaded assets after you make them. If you want your changes to apply to all pre-existing assets, please contact Customer Support. 

Related Articles[](https://support.bynder.com/hc/en-us/articles/17636258833042-Understanding-And-Using-Metadata#h_01JWR2YJACNM58JY4FWTTFGM8B)

----------------------------------------------------------------------------------------------------------------------------------------------

[How To Create Metaproperties](https://support.bynder.com/hc/en-us/articles/6190351879186)

[How To Download A CSV File With All Metadata](https://support.bynder.com/hc/en-us/articles/22486522910994)

[How To Upload Assets Via Mass Uploader](https://support.bynder.com/hc/en-us/articles/360013870140)

### _Level: Proficient_

Proficient-level articles are for users who have some prior Bynder knowledge. These articles require you to know the basics and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
