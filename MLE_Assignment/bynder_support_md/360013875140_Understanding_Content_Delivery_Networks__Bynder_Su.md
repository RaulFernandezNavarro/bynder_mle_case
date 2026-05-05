# Understanding Content Delivery Networks – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013875140-Understanding-Content-Delivery-Networks

Summary[](https://support.bynder.com/hc/en-us/articles/360013875140-Understanding-Content-Delivery-Networks#h_01JNX92E7YJCM2N8KAGF1P9C39)

------------------------------------------------------------------------------------------------------------------------------------------

A Content Delivery Network, or CDN is a system that helps make your media and assets load faster by spreading them out across multiple servers worldwide. When people access your content, they are directed to the closest server to them, allowing faster load times. Bynder uses Amazon CloudFront as our default CDN provider. If desired, you can use your own CDN. 

Bynder uses Amazon Web Services'(AWS) CloudFront, a CDN network that ensures high availability with servers worldwide. CloudFront caches images across multiple endpoints, allowing for fast delivery. Bynder also utilizes flexible hosting and autoscaling from AWS, enabling easy and automatic scaling of server capacity. Amazon CloudFront has a 24-hour expiry time for cached content. However, Bynder has implemented _Automatic Invalidation_, which automatically invalidates CloudFront CDN URLs when a new version of an asset is uploaded. This means that external integrations using CloudFront will always display the latest version of assets, without having to wait for the cache to expire.

### Downloading And Sharing Files Through Bynder’s CDN

When you download assets from the asset library, you are using the CDN (Content Delivery Network). The first download through CDN is usually slower, but increases over time. Bynder can customize your portal to allow users to enable CDN with Bynder Express. This means that when you share files with Bynder Express, the recipients can download the files using CDN when they click on the download link in the notification they receive. If users have permission to download the original file, they can do so through CDN. The link to the image is only available for a limited time for security reasons. If the asset is marked as public, you can retrieve a permanent link via the API. When assets are marked as public, all the thumbnails and web versions are also public in Bynder and can be distributed through CDN. If needed, we can customize your portal so that thumbnails become private. When using CDN, the maximum file size you can download is 20GB.

_Note: Depending on the amount of traffic being used you may be charged for CDN usage._ 

### Configuring Other CDN Providers

Bynder is compatible with other CDN providers, such as Akamai. If you decide to use a provider other than Amazon CloudFront, you will need to set up and configure the CDN on your side. When it's up and running, please contact your Customer Success Contact to enable your CDN provider for your Bynder portal. Configuring a custom CDN **will** **not** replace our Amazon CloudFront setup but work alongside it. Amazon CloudFront will be used for all portal activity, like downloading assets and displaying thumbnails. Your custom CDN will host your assets for web/API use.

### Other CDN Provider Limitations

*   **Cache invalidations:** If you decide to delete an asset that should not be public, Bynder would need to manually invalidate the public link, as it would not occur automatically. If this occurs frequently we recommend building an integration to make this process automatic.
    
*   **Assets** **versioning invalidated**: When a new version of an asset is uploaded, it will not be automatically updated in your portal.
    
*   **Usage tracking:** Real-time metrics are a feature that allows you to keep up-to-date with what is happening in your portal, i.e., what assets are being viewed or downloaded by users**.** When using a custom CDN this feature will not work for DAT or public links.
    

### Configuring AWS And Other CDN Providers

The below configuration is from AWS. The wording may vary slightly on your side when setting this up for a different CDN provider.

![CDN.png](https://support.bynder.com/hc/article_attachments/10640501674514)

*   Path pattern - This is the default URL path that we use for public assets. Fill in: /m/\* For DAT use transform/\*
*   Origin or origin group - Select the URL of your Bynder portal. For example eulocal.getbynder.com
*   Viewer Protocol Policy- We only support the HTTPS protocol, so make sure to redirect HTTP to HTTPS.
*   Allowed HTTP Methods - Select GET and HEAD. Other HTTP methods are not necessary.
*   Whitelist Headers - Add Host and Origin. Optionally other headers can be added as well.
*   Minimum and Maximum TTL—You can configure the TTL values to determine when you want the cached asset to expire. Once it has expired, the asset must be requested from the server again.
*   Caching Content For Custom CDN Users
*   If you are using your own Content Delivery Network (CDN) and want to control over when your Bynder assets are cached, you can utilize cache-control. By setting cache-control, you can determine how long your Bynder assets are cached. When your CDN is not set up by Bynder, but you still want to control when the Bynder assets cached on your CDN expire, you can make use of cache-control.
*   Cache-control can only be set up for the original file and cannot be configured for (OTF) derivatives.
*   The configured expiry date will apply to all Bynder assets. It is not possible to set up an expiry time for assets individually. 

FAQs[](https://support.bynder.com/hc/en-us/articles/360013875140-Understanding-Content-Delivery-Networks#h_01JXQ78GHX33NAZESP48WZ96WD)

---------------------------------------------------------------------------------------------------------------------------------------

**How long does cache take to clear?**

With Bynder's CDN it is 24-hours, with other provider options it is based on your cache-control set-up.

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013875140-Understanding-Content-Delivery-Networks#h_01JXQ79QFFHZKYVEF41DA7DWZ6)

---------------------------------------------------------------------------------------------------------------------------------------------------

[Understanding And Enabling Public Assets](https://support.bynder.com/hc/en-us/articles/360013870200)

### _Level: Proficient_

Proficient-level articles are for users who have some prior Bynder knowledge. These articles require you to know the basics and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
