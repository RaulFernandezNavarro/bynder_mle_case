# How To Use The Bynder Asset Tracker – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013933619-How-To-Use-The-Bynder-Asset-Tracker

Summary[](https://support.bynder.com/hc/en-us/articles/360013933619-How-To-Use-The-Bynder-Asset-Tracker#h_01JY3YBHZ2CWXHZ6ABGMEGTQBP)

--------------------------------------------------------------------------------------------------------------------------------------

Users can see where an asset is used in an integration using the Asset Tracker. If your Bynder Portal is integrated with Drupal 8, Episerver, or the Wordpress integration, you can implement the Asset tracker yourself by using our asset usage API calls. In addition, users can use Bynder SDKs, which already have the Asset Tracker usage calls implemented by default. 

Who?[](https://support.bynder.com/hc/en-us/articles/360013933619-How-To-Use-The-Bynder-Asset-Tracker#h_01JY3YEYME7GT1DGG94EDJ5HBQ)

-----------------------------------------------------------------------------------------------------------------------------------

Users with the _View Portal Insights_ permission can view the Asset Trackers data.

How?[](https://support.bynder.com/hc/en-us/articles/360013933619-How-To-Use-The-Bynder-Asset-Tracker#h_01HDKV9R2BABVJVQYT42EYV1V7)

-----------------------------------------------------------------------------------------------------------------------------------

### Manually Integrating The Asset Tracker

If you are building an integration on your own, you can implement the Asset Tracker by using the asset usage API calls. These API requests are implemented in our SDKs so they can be used to do the API requests to create the asset usages on an asset.

We have a list of existing Integration IDs which are needed in the API requests to create a usage.

*   *   *   **Create**: Use this call to create a record for the Asset Tracker that the asset is used externally. 
        *   **Retrieve:** Use this call to retrieve information on where your assets are used externally.
        *   **Delete:** When you no longer use the asset on your external CMS, the record also needs to be removed from the Asset Tracker.

### Existing Integration ID's

|     |     |
| --- | --- |
| **Integration** | **ID** |
| Adobe Experience Manager | 0191a303-9d99-433e-ada4-d244f37e1d7d |
| Bloomreach | b8e1252f-0216-49f5-8360-3df87f537dab |
| ConnectingTheDots | 0b47825e-60fe-11ee-ae05-325096b39f47 |
| Contentful | ac534173-7ee1-493b-98b7-a6d88ce7a450 |
| Contentstack | c778dee0-637a-11ee-81e7-325096b39f47 |
| Crownpeak | ba5d21ae-bebc-438e-ad88-9b064439914f |
| Drupal 7 | 67e4cef1-320a-4ec8-b307-0a6614325259 |
| Drupal 8 | a7129512-c6e3-47a3-be40-9a66503e82ed |
| Episerver | 33a51dc8-d40e-4f4a-81c2-5d5ffe5885e7 |
| Hootsuite | a27a424b-fceb-48fe-9d5e-6ab29cf05c91 |
| InRiver | 41a92562-bfd9-4847-a34d-4320bcef5e4a |
| Kentico | 8fb1cf11-0a43-4c45-9d64-d7661f8380fc |
| Magento | 47c638ea-2bb6-4713-9dd7-9a217dbb0472 |
| Salesforce Commerce Cloud | 1f8bfa30-ac8c-4188-9327-cd467dc1700b |
| Salesforce Social Studio | 6e89f68c-5ff7-4ec2-bbb6-00a64f713e8c |
| Sanity | 1030c042-1862-4ffe-b6a7-669670e75ebc |
| SDL | d0e21010-d207-4d18-a0db-93436124d779 |
| Sitecore | e5552bdb-ecbf-4a95-85c2-21d31482cdeb |
| Strapi | a4b8ed74-ce54-4ac3-921b-b6fee2dfaa27 |
| Trello | 6aab56e9-df3e-428e-b8f3-ecdc9956d0aa |
| Tune | 34c5fef7-430a-47a1-8fbf-76d7654daa19 |
| TYPO3 | 8517905e-6c2f-47c3-96ca-0312027bbc95 |
| Umbraco | e05dbbe0-2e31-4605-b45b-6b96eaa7800a |
| Veriflies | d3d2ef22-f068-4ee4-a494-9ad874488ce6 |
| Visual Art | 1ead9055-0866-4844-936b-6cbd33e29851 |
| WordPress | b242c16d-70f4-4101-8df5-87b35bbe56f0 |
| Workfront | 7e7c0335-fde5-4ac0-bb68-471336a4a1c1 |
| Wrike | 145fee4f-914f-4f02-acd7-46af6b4ae1c9 |

### Viewing The Asset Tracker

1.  Navigate to or search for an asset and click to be directed to the **Asset** **detail** **page**.
2.  Click the **Statistics** tab.![Screenshot 2023-10-25 at 1.07.04 PM.png](https://support.bynder.com/hc/article_attachments/14664072663570)
3.  Click **View** **Asset** **report** at the bottom of the tab.
    *   Here, you can see the CMS system(s) the asset is used on, which page, and when it was added.
    *   Click on the **URL** to go to the page where the asset is used.

FAQs[](https://support.bynder.com/hc/en-us/articles/360013933619-How-To-Use-The-Bynder-Asset-Tracker#h_01JY3Y7C7X316JPTMCSNG99EVP)

-----------------------------------------------------------------------------------------------------------------------------------

**Why do I not see any information on the asset I have selected?**

If you do not see any information in your selected asset, your asset is most likely not used on an external CMS solution. When adding an asset to one of the supported CMS solutions, the data in the Asset tracker gets automatically updated. Double-check to make sure that your CMS is supported natively, or check whether your custom Asset Tracker integration is working correctly.[](https://support.bynder.com/hc/en-us/articles/360013933619-How-To-Use-The-Bynder-Asset-Tracker#h_01JY3Y57F9JTQEFAH2JRAG8J3Q)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013933619-How-To-Use-The-Bynder-Asset-Tracker#h_01JY3Y323H9DREZ6AC7018WPAE)

-----------------------------------------------------------------------------------------------------------------------------------------------

[Bynder SDKs](https://developers.bynder.com/sdks)

[Bynder API calls (via Apiary)](https://bynder.docs.apiary.io/#reference/asset-usage)

Share
