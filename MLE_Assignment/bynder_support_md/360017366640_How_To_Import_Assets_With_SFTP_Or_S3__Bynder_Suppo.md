# How To Import Assets With SFTP Or S3 – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360017366640-How-To-Import-Assets-With-SFTP-Or-S3

Summary[](https://support.bynder.com/hc/en-us/articles/360017366640-How-To-Import-Assets-With-SFTP-Or-S3#h_01JNXCHF15376YHZ9XRMJ00CEE)

---------------------------------------------------------------------------------------------------------------------------------------

SFTP provides a secure way to transfer files without using external hard drives. Bynder offers SFTP, powered by AWS Transfer Family, as a secure method for transferring files directly to an AWS bucket. This allows quicker mass uploads for Bynder portals.

Who?[](https://support.bynder.com/hc/en-us/articles/360017366640-How-To-Import-Assets-With-SFTP-Or-S3#h_01JNXCGVEWZNC6KJD8NSSJ86FN)

------------------------------------------------------------------------------------------------------------------------------------

This feature/solution can only be enabled by your Customer Success Contact. 

Why?

Bynder wants to save you time and be as efficient as possible. This option allows for the transfer of large files without limitations on data or file size. Bynder will provide an AWS bucket username and set up the SFTP server. To proceed, you'll need an SFTP client that supports secure connections using a private and public RSA-2048 SSH key. This setup ensures a secure connection and limits access to the isolated SFTP server. Once files are transferred to the AWS bucket, we will import them into your portal. If you already have assets in an S3 bucket, we can assist with transferring files from there as long as the appropriate permissions are in place. Once the import process is complete, all transferred files will be deleted from the AWS bucket and the SFTP server.

How?[](https://support.bynder.com/hc/en-us/articles/360017366640-How-To-Import-Assets-With-SFTP-Or-S3#h_01HMHW5YWREB0G2PMGSJD26EM1)

------------------------------------------------------------------------------------------------------------------------------------

### Setting Up The Import Sheet

1.  Carefully check the import sheet's spelling, capitalization, and spacing of words and phrases. The media import will fail if a value is too similar to an existing value in your DAM. Even small inconsistencies can cause the asset import to fail and delay the media import process.
2.  Each import sheet should have no more than 50,000 assets, split your imports into multiple sheets if you have more assets to import.
3.  You must create a media import sheet based on your Bynder portal taxonomy. Request this from your Onboarding Manager or Customer Success Contact. 
4.  In addition to your files, your Onboarding or Customer Success Contact will need a completed Excel file or Google Sheet that includes the information, metaproperty options, and other data you want to apply to your files. There should not be any demo data included.
5.  The first ten columns of the spreadsheet are static and must exist in a specific order. They cannot be removed or rearranged.

**Necessary Order:** 

1.  1.  **Bynder\_title (Required):** Even if the filename will be the Bynder title, this field must be filled in with the filename.
    2.  **Description:** Asset description in asset detail view.
    3.  **Bynder\_brand (Required):** Leave the column blank; the Bynder team will complete this.
    4.  **ISO Publication Date:** (YYYY-MM-DD)
    5.  **Bynder\_copyright.**
    6.  **Tags:** (comma-separated, no trailing/white spaces)
    7.  **Path to Assets (Required).**
    8.  **ArchiveDate:**  0 or blank if not needed, 1 to archive on import, or **YYYY-MM-DD** for a future archive date. 
    9.  **WatermarkDate:** 0 or blank if not needed, 1 to watermark on import, or YYYY-MM-DD for a future watermark date.
    10.  **New Filename:** The New Filename can be used to overwrite the filename in the SFTP and show it as the "original filename" in Bynder. **Leave it empty if not needed.****![CSVexample copy.png](https://support.bynder.com/hc/article_attachments/25153021303314)![CSVexample.png](https://support.bynder.com/hc/article_attachments/25153021303698)**

### Import Sheet Dos And Don'ts 

*   The **file** **paths** must include the **full filename** and **extensions** (for example, Volumes/Drive/file\_name.ext).
*   If the SFTP has all files in one directory, this can just be the filename with the extension **(example\_name.png).** However, ff the SFTP contains folders, the full path to the asset **(folder/subfolder/example\_name2.png)** must be used.
*   **File Type/Extension:** The media import script does not automatically pull in EXIF data; let the Bynder team know if you’d like the File Type/Extension mapped through our scripting to the custom File Type/Extension metaproperty and leave this column blank.
*   **Metaproperty and metaproperty option** **automations** are not respected. Data validation can be used for single-select metaproperties if desired. _All custom metaproperties on the import sheet must exist in the portal taxonomy._
*   Any options that do not match existing option labels in the portal taxonomy will be created. Watch out for improper variations that would otherwise have to be cleaned up after the import. This cannot be disabled as it can be with Mass Upload.
*   Each line/row in the import sheet represents an asset to be imported. Therefore, assets should be in a 1:1 relation to the sheet. If the same path to an asset occurs in multiple rows, only one row/asset will be imported for that path.
*   Each line/row must include values for the required columns specified above.
*   Multiple metaproperty options (multi-select) and the descriptive keyword tags **(column F)** should be comma-separated in the same cell with no "trailing spaces." For example, **Option 1,Option 2,Option 3** NOT Option 1, Option 2, Option 3.
*   Avoid special characters (such as accented characters or other UTF-8 characters outside the main character set found on a standard keyboard) in the file path to the asset. Special characters are supported for all other fields (custom metaproperties, etc.) but should be provided in UTF-8 format to ensure correct transfer during import.
*   Double quotes, single quotes, and apostrophes are often formatted in Microsoft Office as "smart quotes" or "curly quotes" can cause issues. It's best to find and replace all these with standard text "straight quotes."
*   ® ™ © $ £ - Symbols and é ñ î - Accented letters such as letters with grave, acute, circumflex, tilde, and umlaut can be supported. The provided sheet must be formatted in UTF-8 format, or an Excel file should be provided. This way, the PS team can honor the special characters.
*   White space characters such as tabs, new lines, and embedded returns should be replaced.
*   Avoid special characters (even if formatted using UTF-8) where possible in the path field. Single spaces are acceptable in the path, but double spaces are not.

### Importing Files Using SFTP Or AWS S3

**SFTP**

1.  Generate a public SSH Key.
2.  Our Platform Services team uses this key from the Onboarding or Customer Success Contact, and they will create your SFTP location.
3.  Upload your files to the AWS Bucket and fill out the Import sheet.

**AWS S3**

1.  If you requested an S3 to S3 transfer, you'll be asked to provide the current S3 address of the assets along with the Access Key ID and Secret Access Key for a user with permission to access the bucket and retrieve the files.
2.  Our Platform Services team receives these details from your Onboarding or Customer Success Contact, and they will transfer the files to Bynder.

### Generating An SSH Key And Log In To The SFTP Location

Start by creating an RSA-2048 SSH key pair, including a private and public key. Follow the instructions below depending on your operating system:

*   *   [Windows](https://learn.microsoft.com/en-us/viva/glint/setup/sftp-ssh-key-gen#create-an-ssh-key-pair-on-microsoft-windows)
        
    *   [MacOS](https://help.dreamhost.com/hc/en-us/articles/115001736671-Creating-a-new-Key-pair-in-Mac-OS-X-or-Linux)
        

_Note: When you create your keys, we strongly suggest setting up a passphrase for the private key. Keep the private key and passphrase private from everyone. Bynder will never ask you for this information._

1.  Send the public key to your Onboarding Manager or Customer Success Contact, who will provide you with a username and other necessary details to connect to the SFTP server.      _Note: Never send Bynder the **private** key and its passphrase._ 
2.  Create a new SFTP connection using the following details in your preferred SFTP client. We recommend using Cyberduck or FileZilla.
    *   The name of the fields below may vary depending on the SFTP client you're using.
        *   **Server**: Fill in the server endpoint that Bynder provided you with.
        *   **Port**: The port number will be set automatically and should always be 22.
        *   **Username**: The username Bynder provided you with.
            
        *   **SSH** **Private** **Keys**: Select the private key you generated in step 1. When prompted, enter the passphrase for this key![](https://support.bynder.com/hc/article_attachments/16543633992210)
            
            Above is an example of SFTP configuration in Cyberduck.
            

3\. Connect to the SFTP server. You may see a Host Key Fingerprint the first time you connect. Check if this fingerprint matches the Host Key Fingerprint Bynder provided you with. This way, you can ensure you're connecting to the correct server. The Host Key Fingerprint may not be shown depending on your SFTP client.

4\. Start transferring your files once you're successfully connected to the SFTP server.

 5. Notify your onboarding manager or customer success contact once all the files have been transferred successfully, and you've filled out your import sheet.

6\. Bynder will import your files into your Bynder portal. We will inform you once this is complete.

FAQs[](https://support.bynder.com/hc/en-us/articles/360017366640-How-To-Import-Assets-With-SFTP-Or-S3#h_01J7Y13HVREJGTR6ZVN7DVA6ZT)

------------------------------------------------------------------------------------------------------------------------------------

**Can I export my files from Bynder to my SFTP server or AWS S3 bucket?**

Yes, you can export your files. 

**How long does it take to complete the import?**

SFTP: It takes approximately one week per TB to load via SFTP.

S3: It takes approximately 3-5 days per TB to load from S3 to S3.

Related Articles[](https://support.bynder.com/hc/en-us/articles/360017366640-How-To-Import-Assets-With-SFTP-Or-S3#h_01JNXE1ZWJSFVP6YJAV69S7AKJ)

------------------------------------------------------------------------------------------------------------------------------------------------

[Export Bynder Assets with SFTP or S3](https://support.bynder.com/hc/en-us/articles/21403219582866)

### _Level: Proficient_

Proficient-level articles are for users who have some prior Bynder knowledge. These articles require you to know the basics and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
