# Create Predictable URLs in DAT – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/12427637384338-Create-Predictable-URLs-in-DAT

[Dynamic Asset Transformation (DAT)](https://support.bynder.com/hc/en-us/articles/18952775916562)
 enables you to create optimized assets as needed for external systems. By using consistent URLs, you can easily access assets based on their characteristics, allowing automated and efficient retrieval of the right content. This feature supports various asset types like videos, documents, and other public assets in your asset bank, providing flexibility in using predictable URLs for different asset types.

By utilizing asset characteristics with metaproperties, users can programmatically access the most relevant content and deliver it smoothly to end users and downstream systems. This functionality boosts efficiency, facilitates targeted content delivery, enhances SEO efforts, and maintains brand consistency across connected systems.

[Predictable URLs for Adaptive Video Streaming](https://support.bynder.com/hc/en-us/articles/25059554242962)
 allow you to efficiently retrieve video assets based on predefined criteria, such as location, language, or target audience, etc.

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Structure of Predictable URLs[](https://support.bynder.com/hc/en-us/articles/12427637384338-Create-Predictable-URLs-in-DAT#01H8PRT17K1QZQJPCCSDWNZ1NH)

-------------------------------------------------------------------------------------------------------------------------------------------------------

Your URLs will be based on metaproperty options. Below is the structure for building the URLs. 

https://baseurl/match/metaproperty\_name/metaproperty\_option/name

Example:  
[https://byndair.bynder.com/match/Country/France/](https://byndair.bynder.com/match/Country/France/)
EiffelTower

*   **Base URL:** The URL of your Bynder DAM.  
    *   [https://byndair.bynder.com/](https://byndair.bynder.com/match/Country/France/)
        [match/Country/France/Eiffel\_Tower](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
         
*   **Match:** A fixed prefix indicating the use of a predictable URL.
    *   [https://byndair.bynder.com/](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
        [match/](https://byndair.bynder.com/match/Country/France/)
        [Country/France/Eiffel\_Tower](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
         
*   **Metaproperty\_name:** The database name of the metaproperty  
    *   [https://byndair.bynder.com/match/](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
        [Country/](https://byndair.bynder.com/match/Country/France/)
        [France/Eiffel\_Tower](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
         
*   **Metaproperty\_option:** The specific metaproperty option for the metaproperty you’ve selected.  
    *   [https://byndair.bynder.com/match/Country/](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
        [France/](https://byndair.bynder.com/match/Country/France/)
        [Eiffel\_Tower](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
         
*   **Name** (optional): see more [here](https://support.bynder.com/hc/en-us/articles/12427637384338-Create-Predictable-URLs-in-DAT#01H8PRT17KRRW8EW3HF2FA6DNK)
    . 

Supported Name Types[](https://support.bynder.com/hc/en-us/articles/12427637384338-Create-Predictable-URLs-in-DAT#01H8PRT17KRRW8EW3HF2FA6DNK)

----------------------------------------------------------------------------------------------------------------------------------------------

An optional part of the URL allows you to assign a name to the asset, which can be beneficial for SEO purposes. The following characters are allowed in the name of a predictable URL. These conditions also apply to **metaproperty\_name** and **metaproperty\_option.**

*   Lowercase letters (a-z)
*   Uppercase letters (A-Z)
*   Numbers (0-9)
*   Underscore (\_)

Predictable URLs for other asset types[](https://support.bynder.com/hc/en-us/articles/12427637384338-Create-Predictable-URLs-in-DAT#h_01J837BF7QXWRQWQNMY50Q4C5X)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Predictable URLs support retrieving the original file, allowing it to work with other asset types. They can be used for your asset bank's videos, documents, and other public assets. This will give the flexibility to use predictable URLs for any asset.

To get the original asset using predictable URLs, you need to start the URL path with /match/original/

The rest of the URL will be the same as described in this article above

#### Link structure to get the original asset

https://baseurl/match**/original/**metaproperty\_name/metaproperty\_option/name

#### Example

[https://byndair.bynder.com/match**/original/**Country/France/](https://byndair.bynder.com/match/Country/France/)
EiffelTower  
**Note**

Because this link will return the original asset, transformations cannot be added to it. The original asset will always be returned without alterations.

Supported Metaproperty Types[](https://support.bynder.com/hc/en-us/articles/12427637384338-Create-Predictable-URLs-in-DAT#h_01HQ41SBNH5SZ4EGVKKN3G3VXK)

--------------------------------------------------------------------------------------------------------------------------------------------------------

The following metaproperty types are supported

*   **Single**
*   **Multi**\-**select**
*   **Text**
*   **Long Text**

_Note:_ The _date type_ is not supported. 

Important information:[](https://support.bynder.com/hc/en-us/articles/12427637384338-Create-Predictable-URLs-in-DAT#h_01JKZY2NJPE9BHRP6N676VA0ZP)

--------------------------------------------------------------------------------------------------------------------------------------------------

*   **Public Assets:** To utilize predictable URLs, assets must be public within the DAM. Learn more about marking assets as public assets [here](https://support.bynder.com/hc/en-us/articles/360013870200)
    .
*   **Additional Metaproperties:** Following the same format, add additional metaproperties and options.
    *   [https://byndair.bynder.com/match/Country/France/](https://byndair.bynder.com/match/Country/France/)
        City/Paris/Season/Summer/EiffelTower
*   **Multiple Results:** If a metaproperty combination has multiple asset results, the URL will retrieve the most recently uploaded asset that matches the given criteria by default. However, you can set the default based on the date uploaded, date created, date updated, or the asset name in descending or ascending order. If you’d like to update this, please contact your Customer Success Contact.
*   **Database name:** You must use the name for the metaproperty and option rather than the label.
*   **Case Sensitivity:** The URL is case-sensitive for both metaproperty names and options. Ensure that the capitalization matches the metaproperty configuration to retrieve the desired asset.
*   **Trailing Slash:** A trailing slash must be included when the URL ends with a metaproperty option. Example: [https://byndair.bynder.com/match/Country/France/](https://byndair.bynder.com/match/Country/France/)
    *   However, when a Name is added to the URL, the trailing slash must be omitted. Example: [https://byndair.bynder.com/match/Country/France/Eiffel\_Tower](https://byndair.bynder.com/match/Country/France/Eiffel_Tower)
         
*   **Cache Invalidation:** If an asset is changed, the cache will be invalidated to display the most up-to-date asset.  
     
    
    ### Note
    
    We don’t currently invalidate when a metaproperty or option is edited or deleted, but only when an asset is changed, such as when a new version is added, the focus point is updated, or the asset is deleted.
    
*   **Transformations:** Transformations can be applied to your predictable URL assets by adding the parameters offered in DAT after your last metaproperty option or name.
    *   [https://byndair.bynder.com/match/Country/France/**?io=transform:border,width:20&io=filter:sepia**](https://byndair.bynder.com/match/Country/France/?io=transform:border,width:20&io=filter:sepia)
         

Share
