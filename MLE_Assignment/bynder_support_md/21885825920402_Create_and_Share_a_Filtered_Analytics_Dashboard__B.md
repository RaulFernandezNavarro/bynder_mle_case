# Create and Share a Filtered Analytics Dashboard – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/21885825920402-Create-and-Share-a-Filtered-Analytics-Dashboard

[Bynder Analytics](https://support.bynder.com/hc/en-us/articles/360013932579)
 offers a convenient feature that allows [filters](https://support.bynder.com/hc/en-us/articles/20047789830290)
 to be embedded directly into the URL of a dashboard, streamlining the process of sharing specific data views. With this functionality, when a user opens the shared URL, the relevant filters are automatically applied, displaying the dashboard data according to the specified parameters. This eliminates the need to manually reapply the same filters every time you revisit or share a dashboard, saving time and effort.

Whether you're working with complex datasets or need to focus on specific metrics, you can bookmark your favorite filter URLs and share them with your team to ensure consistency in reporting. By leveraging the filter values in the Analytics interface, you can easily create custom URLs that fit your reporting needs.

How to Share Filtered Analytics Dashboard[](https://support.bynder.com/hc/en-us/articles/21885825920402-Create-and-Share-a-Filtered-Analytics-Dashboard#h_01J9SBYPHM3C9GEPYZCKFA7NX8)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Important

The applied filter **will** **not** automatically reflect the URL. You must copy and paste the filter and apply it to the URL.

1.  Navigate to **Reporting > Analytics**.
2.  Determine which filters you want to apply.
3.  All URLs follow a similar pattern: first, the base URL, and then the filters. You can use all the filters visible in the dashboard and the full advanced filter functionality (include, exclude, contain, etc.).   
    Follow this key to begin to apply filters to the URL. 
    *   You can bulk filter multiple assets, users, or other values by constructing a string with those values (e.g., in Excel) and then pasting the string into the URL as a filter. This method allows you to quickly apply a filter to many items simultaneously, saving time compared to manually selecting each option.
4.  Copy and paste the URL and share or bookmark it to avoid applying the same filters on every visit.
    *   Tip: Copy filters from one dashboard to another (if the same filters are available.

Example [](https://support.bynder.com/hc/en-us/articles/21885825920402-Create-and-Share-a-Filtered-Analytics-Dashboard#h_01J9SCH8R2ANM46FA55GQE2AQQ)

-----------------------------------------------------------------------------------------------------------------------------------------------------

Here is an example if you want to filter the [**Uploads**](https://support.bynder.com/hc/en-us/articles/20095005964946-Asset-Bank-Dashboard-in-Advanced-Analytics#:~:text=one%20unique%20download.-,Uploads,-Upload%20Dashboard%20focuses)
 **dashboard** on the **last 30 days for only image**s and **exclude** **admins**:

1.  Navigate to **Reporting > Analytics > Dashboard (Uploads Dashboard)**.
    *   https://portalname/b-analytics/asset-bank/**uploads**
2.  Add **?**
    *   https://portalname/b-analytics/asset-bank/uploads**?**
3.  Add **Time+Frame=30+days**
    *   https://portalname/b-analytics/asset-bank/uploads?**Time+Frame=30+days**
4.  Add **&**
    *   https://portalname/b-analytics/asset-bank/uploads?Time+Frame=30+days**&**
5.  Add **Asset+Type=Image**
    *   https://portalname/b-analytics/asset-bank/uploads?Time+Frame=30+days**Asset+Type=Image**
6.  Add **&**
    *   https://portalname/b-analytics/asset-bank/uploads?Time+Frame=30+daysAsset+Type=Image**&**
7.  Add **Profile+Name=-Admin**
    *   https://portalname/b-analytics/asset-bank/uploads?Time+Frame=30+daysAsset+Type=Image& **Profile+Name=-Admin**
8.  his gives the following full URL: **https://portalname/b-analytics/asset-bank/uploads?Time+Frame=30+days&Asset+Type=Image&Profile+Name=-Admin**
9.  You can now bookmark the URL with the applied filters or share it with others with **advanced** **reporting** permission.

Key to Apply URL Logic for Filters[](https://support.bynder.com/hc/en-us/articles/21885825920402-Create-and-Share-a-Filtered-Analytics-Dashboard#h_01J9SD7VXRR9H590GA5B338871)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

*   Spaces are replaced with a ‘+’ 
*   To exclude an item, prefix the name with an ‘-’  
     

|     |     |
| --- | --- | 
| **Date Filter Type** | **Example** |
| Is in the Last | Time+Frame=180+days |
| Is on the day | Time+Frame=2024-09-29 |
| Is in range | Time+Frame=2024-09-01+to+2024-09-15 |
| Is before | Time+Frame=before+1+month+ago |
| Is on or after | Time+Frame=after+1+month+ago |
| Is in the year | Time+Frame=2024 |
| Is in the month | Time+Frame=2024-09 |
| Is this | Time+Frame=this+month |
| Is next | Time+Frame=next+month |
| Is previous | Time+Frame=last+month |
| Is  | Time+Frame=4+month+ago+for+2+month |
| Is any time | Time+Frame= |

|     |     |
| --- | --- | 
| **Filter Type** | **Example** |
| Is  | Asset+Type=Image,Document |
| Contains | Profile+Name=%25Admin%25,%25Removed+Users%25 |
| Starts with | Profile+Name=Admin%25,Removed+Users%25 |
| Ends with | Profile+Name=Admin%25,Removed+Users%25 |
| Is blank | Search+Terms=EMPTY |
| Is null | Search+Terms=NULL |
| Is not | Profile+Name=-Admin,-Removed+Users |
| Doesn't contain | Profile+Name=-%25Admin%25,-%25Removed+Users%25 |
| Doesn't start with | Profile+Name=-Admin%25,-Removed+Users%25 |
| Doesn't end with | Profile+Name=-Admin%25,-Removed+Users%25 |
| Is not blank | Search+Terms=-EMPTY |
| Is not null | Search+Terms=-NULL |

|     |     |
| --- | --- | 
| **Date Granularity** | **Example** |
| Daily | Date+Granularity=day |
| Weekly | Date+Granularity=week |
| Monthly | Date+Granularity=month |
| Quarterly | Date+Granularity=quarter |
| Yearly | Date+Granularity=year |

FAQ [](https://support.bynder.com/hc/en-us/articles/21885825920402-Create-and-Share-a-Filtered-Analytics-Dashboard#h_01J9SDAZ2DVJM1EWBFTNP70867)

-------------------------------------------------------------------------------------------------------------------------------------------------

**Do I need a specific permission type to view a shared URL?** 

Yes, only those with advanced reporting permission can view the shared URL. 

**Does the URL update when filters are adjusted?** 

No, while filters are applied when accessing a dashboard via a URL, the URL itself will not change if users manually adjust filters within the dashboard. 

**Is there a limit to adding values to a filter?** Yes, there’s a general limit to the length of a URL (2048 characters). 

Share
