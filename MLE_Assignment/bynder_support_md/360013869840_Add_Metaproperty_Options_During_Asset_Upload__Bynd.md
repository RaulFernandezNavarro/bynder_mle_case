# Add Metaproperty Options During Asset Upload – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013869840-Add-Metaproperty-Options-During-Asset-Upload

When [uploading](https://support.bynder.com/hc/en-us/articles/360013931479)
 an asset, you can enhance its metadata by adding [new metaproperty options](https://support.bynder.com/hc/en-us/articles/6190351879186)
 that aren't already on the list. This applies specifically to **Select**\-**type** metaproperties and **Autocomplete**\-**type** metaproperties. Adding metaproperty options on the fly during asset upload can be a valuable feature for enhancing the classification and findability of your assets in Bynder.

*   **Enabled**: Users can create new metaproperty options when uploading or editing assets. This is helpful for dynamic environments and also allows non-admin users to add metaproperty options.
*   **Disabled**: Only options pre-added by the admin are available for selection, ensuring stricter control over metadata.

### Note

If the **Add** **new** **options** toggle is enabled, anyone with upload rights can add new metaproperty options. Be cautious, as this may lead to metadata inconsistencies, especially if non-admins are given upload permissions.

Important to Note[](https://support.bynder.com/hc/en-us/articles/360013869840-Add-Metaproperty-Options-During-Asset-Upload#h_01JBYY8RYGP96VEZT937QN0AE1)

---------------------------------------------------------------------------------------------------------------------------------------------------------

When creating a new metaproperty option:

*   The system uses the **Name** field, not the Label field, to check for existing options.
*   If a matching Name value isn't found, a new metaproperty option is created. The entered name will be used as both the option's **Name** and **Label**.

Example of Name and Label Handling[](https://support.bynder.com/hc/en-us/articles/360013869840-Add-Metaproperty-Options-During-Asset-Upload#h_01JBYY9QWS6GK8T8A13RXHDS67)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Be mindful of spaces and special characters, as these can cause duplicate entries:

*   If "New York" exists in your portal with the Name "NewYork" (no spaces), and a user adds "New York" (with a space) as a new option, the backend system converts the space to an underscore, creating "New\_York" as the Name.
*   This results in two metaproperty options with the same Label ("New York") but different Names ("NewYork" and "New\_York"), which can lead to confusion.

How to Add Metaproperty Options During Upload[](https://support.bynder.com/hc/en-us/articles/360013869840-Add-Metaproperty-Options-During-Asset-Upload#h_01JBYYAQKQW3K3XCXVYTNRG2D4)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  During the upload process, locate and expand the relevant metaproperty.
2.  Click **Add** **Option.**
3.  This will allow you to create a new metaproperty value.
4.  Input the **new** **option** **name**.
5.  **Description** (Optional): Add a description if needed.
6.  **Thumbnail** (Optional): Upload an image thumbnail for better visual representation.'
7.  Click **Add**
8.  The new metaproperty option will be created and automatically selected.
9.  The asset will be tagged with this new option upon upload.

Best Practices[](https://support.bynder.com/hc/en-us/articles/360013869840-Add-Metaproperty-Options-During-Asset-Upload#h_01JBYYCF980W63YRYGY9BXXMRW)

------------------------------------------------------------------------------------------------------------------------------------------------------

*   **Restrict User Permissions**: If consistent metadata is a priority, consider restricting who can add new metaproperty options to admins or trusted users.
*   **Regular [Audits](https://support.bynder.com/hc/en-us/articles/21213841926418)
    :** Review and manage metaproperty options periodically to prevent duplicates and maintain a clean metadata structure.
*   **User Training:** Educate users about the impact of spaces and special characters on metaproperty options to minimize inconsistencies.

Share
