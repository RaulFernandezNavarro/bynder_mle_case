# Automatically Save File Extension Upon Upload – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013931699-Automatically-Save-File-Extension-Upon-Upload

When uploading assets, you can automatically capture and save the file extension, making it easier to organize and filter them. The system extracts the file extension and tags the assets accordingly during the upload process. This lets you filter assets by their specific file extension, streamlining your asset management.

The system retrieves the file extension from the file’s metadata (e.g., EXIF, IPTC, XMP) and maps it to a metaproperty in your portal. This removes the need to manually enter the file extension each time you upload an asset.

We recommend using metadata mapping for automatic file extension saving upon upload. You can configure this or use our feature to automatically tag assets with the correct file extension during file conversion.

How to Automatically Save File Extension Upon Upload to Filter Assets by File Extension[](https://support.bynder.com/hc/en-us/articles/360013931699-Automatically-Save-File-Extension-Upon-Upload#h_01JJSSMV6JTHEEGJ5GD9XDAPSH)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Go to **Settings** > **Taxonomy** > **Metaproperties** **Management**.
2.  You can **create** **a** **new** **File Extension metaproperty** or use an **existing** **one** in your taxonomy, ensuring it is in a single-type format.
    *   When creating a new meta property, make sure you select the s**ingle**\-**select** **type**, enable **Autocomplete** search, and **Add** **new** **options**.
3.  Navigate to **Settings** > **Advanced** **Settings** > **Portal** **Settings** > **Embedded** **Metadata** **Configuration**.
4.  Two tabs will appear: one for asset upload and one for asset download.
    *   Make sure you're in the **On** **Asset** **Upload** section.![](https://support.bynder.com/hc/article_attachments/24318720341266)
5.  In the Custom Metadata Fields section, click **Add Custom Field.**![](https://support.bynder.com/hc/article_attachments/24318720342546)
6.  Enter **FileTypeExtension** for the left field and select the **File Extension metaproperty** created earlier.  ![](https://support.bynder.com/hc/article_attachments/24318729304978)
    *   **"FileTypeExtension"** is the recommended value, but **FileType** or similar metadata tags (such as those living in your files) may also work.
7.  Click **Save** **Changes**.

(Optional) Choose Metadata Preferences.[](https://support.bynder.com/hc/en-us/articles/360013931699-Automatically-Save-File-Extension-Upon-Upload#h_01JJSSQ8JNK2ER3EWQ4S3XNW4A)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  You can select whether you prefer upper or lower case for the file extension:
    *   Example: FileType: JPEG or FileTypeExtension: jpg
    *   However, we fully support only official XMP metadata tags now

Important Notes[](https://support.bynder.com/hc/en-us/articles/360013931699-Automatically-Save-File-Extension-Upon-Upload#h_01JJSSMV6JPR81HKFT4VE0BGWM)

--------------------------------------------------------------------------------------------------------------------------------------------------------

*   This feature applies only to **assets** **uploaded** **after it is enabled**. If you need to locate older assets by file extension, please contact your Customer Success Contact for portal re-identification.
    *   Re-identification is currently available for images and PDFs but not for video or audio files.
*   The **Save File Extension by Metadata Mapping** setting is required for this feature.

Share
