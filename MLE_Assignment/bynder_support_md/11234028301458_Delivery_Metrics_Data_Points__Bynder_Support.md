# Delivery Metrics Data Points – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/11234028301458-Delivery-Metrics-Data-Points

Delivery Metrics provides detailed analytics and insights on the usage of your assets outside of the DAM. This lets you better understand how your assets perform and are used across different channels. The Delivery Metrics report includes information about how often the asset has been viewed, the websites where it's been viewed, and the top transformations if you're using [Dynamic Asset Transformation](https://support.bynder.com/hc/en-us/articles/360018559260)
 (DAT). 

Learn more about the asset level report that's available [here](https://support.bynder.com/hc/en-us/articles/10257152407058)
. 

Views[](https://support.bynder.com/hc/en-us/articles/11234028301458-Delivery-Metrics-Data-Points#h_01HKT1Z4E8J3WR3JXEP2181TCX)

-------------------------------------------------------------------------------------------------------------------------------

Asset views refer to the number of times a DAT or public link asset is requested externally. The term 'view' is consistent with other analytics tools, such as Google Analytics page views. Most websites follow lazy loading best practices, meaning the content is only requested and shown when the user navigates that page section, not just when the page is first loaded.

A link is counted as a view whenever requested through the Bynder CDN. This includes when assets are viewed while embedded on a webpage, in a mobile app, in a separate tab, or when a user right-clicks to download the asset.

### Note

It can take up to 2 days before an asset view is registered and displayed within the report. 

Websites [](https://support.bynder.com/hc/en-us/articles/11234028301458-Delivery-Metrics-Data-Points#h_01HKT1Z4E8DQQQXKHG0K9P45RV)

-----------------------------------------------------------------------------------------------------------------------------------

The top websites where the asset is viewed will be displayed. We identify the websites where an asset is used with the [referer header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)
. This header is sent along with the request for an asset. For example, if an asset is used on https://support.bynder.com/, the asset request to https://assets.bynder.com/ would have https://support.bynder.com/ as the content of the referer header.

### Note

If a request does not include the referer header, the website will be counted under a hyphen "-" in the Top Websites section.

Requests that don't have a referer header might occur when users right-click and save the image or right-click to view the image in a separate tab in their browser. In those cases, the asset is not embedded on a web page, and the referer header won't be sent.

Referrer data will also not be collected if your website has a Referrer-Policy header set to no-referrer or same-origin. More information regarding the Referrer-Policy header can be found [here.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy)

### Note

Some proxies remove the referer header for images. We cannot show website information if you use a proxy or CDN in front of Bynder that doesn't forward the referer header. Please ensure the referer header is passed along with the asset request to see website views. 

Transformations[](https://support.bynder.com/hc/en-us/articles/11234028301458-Delivery-Metrics-Data-Points#h_01HKT1Z4E8QGTA3NA8DB0CSF4P)

-----------------------------------------------------------------------------------------------------------------------------------------

If you use [Dynamic Asset Transformation](https://support.bynder.com/hc/en-us/articles/360018559260)
, the top transformations for the assets will display. If multiple transformations are applied simultaneously, each transformation is counted separately. 

Example:

Whenever a DAT link is used, it is usually accompanied by query parameters that define the transformations that need to be applied. An example DAT link is: 

[https://datdemo.getbynder.com/transform/a8ad6713-8687-4356-b22f-d09334bdf7b2/Musician?io=transform:fill,width:1200,height:1200&io=filter:grayscale](https://datdemo.getbynder.com/transform/a8ad6713-8687-4356-b22f-d09334bdf7b2/Musician?io=transform:fill,width:1200,height:1200&io=filter:grayscale)

In the example above, io=transform: fill,width:1200,height:1200&io=filter: grayscale defines the transformation. In this case, the transformations are a 'fill' and a 'grayscale' transformation. In the delivery metrics report, this will be counted as both a fill and grayscale transformation. 

Limitations[](https://support.bynder.com/hc/en-us/articles/11234028301458-Delivery-Metrics-Data-Points#h_01HKT1Z4E8GFJTRAMRNJWK71K5)

-------------------------------------------------------------------------------------------------------------------------------------

*   Delivery metrics will not work well with a caching proxy or a custom.  
    CDN. Requests served by a cache that is not the Bynder CDN will not be counted, as no request reaches the Bynder platform. If a custom CDN or caching proxy is set up, only the requests forwarded to the Bynder platform will be displayed in the delivery metrics report.
*   If you use DAT presets, the transformations used in that preset are not displayed in the transformation metrics. Only DAT requests that use query parameters are displayed in the report. 
*   Currently, Delivery Metrics cannot track [predictable URLs.](https://support.bynder.com/hc/en-us/articles/12427637384338)
    

Share
