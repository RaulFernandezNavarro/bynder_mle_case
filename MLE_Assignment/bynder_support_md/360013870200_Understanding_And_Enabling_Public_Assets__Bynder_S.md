# Understanding And Enabling Public Assets – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013870200

Summary[](https://support.bynder.com/hc/en-us/articles/360013870200#h_01JNX5FZQQG46Z3FY32QJR6PYW)

--------------------------------------------------------------------------------------------------

Bynder empowers users to make assets public by generating a URL for the asset, which can be shared with non-Bynder users or linked on your website. This highly customizable built-in feature offers complete control over how you share your public assets. 

_Note: We're upgrading our image link system to a faster and more reliable /asset/ format. Your old /m/ links will still work because we're automatically redirecting them. Eventually, all links will be in the /asset/ format, but your existing links will always be supported.  
_

Who?[](https://support.bynder.com/hc/en-us/articles/360013870200#h_01JNX5G649A71A7E9BQ7XFCFPN)

-----------------------------------------------------------------------------------------------

This feature/solution is enable-able by any Bynder portal user.

Users must have the _Mark assets as public_ permission. If you do not have this permission enabled please contact your Bynder Admin.

Why?[](https://support.bynder.com/hc/en-us/articles/360013870200#h_01JNX5M0SD8AHAGCD5D7QRQ222)

-----------------------------------------------------------------------------------------------

Users can choose to make certain assets visible, downloadable, or downloadable with a watermark. Users can even configure their portal so that once an asset is archived, the public URL becomes inaccessible, or users can create a _Public Collection_ to share multiple assets with non-Bynder users.

How?[](https://support.bynder.com/hc/en-us/articles/360013870200#h_01HHN0NE5J03PGE17PFT7ZKMRN)

-----------------------------------------------------------------------------------------------

### Marking Assets As Public

1.  You can edit one or more images in the asset overview by clicking on them to batch select, or you can click an asset and click the **Edit** tab on the Asset detail page.
    
2.  Expand the **Advanced Rights** tab.
    
3.  Select **Mark as public**. When an asset is marked public, a publicly accessible URL is created for it. Any user who has the URL can then view and download the asset. This does not make the derivatives public. This does allow the original asset to be visible via the URL and API.
    

_Note: Contact your customer success contact to enable public derivatives to be accessible from the asset detail page, by default derivatives are only visible via the API. Once enabled users will need the_ Download original assets _and the_ Download public asset _derivatives permissions to view public links within the Asset Detail view._

Sharing An Asset Via Public Link

1.  Navigate to your Portal. 
2.  Select an asset and click the thumbnail.
3.  Navigate to your Asset Detail view. 
4.  Scroll down to find **link to public files.![Screenshot 2024-11-04 at 4.51.20 PM.png](https://support.bynder.com/hc/article_attachments/25194395425298)**
5.  You will see the options for public files depending on how they were configured. 

_Note:_ When downloading an asset from a public link the asset will only download the asset name, and not any custom naming that has been configured. 

### Deleting Public Assets

When you delete a public asset, the public URLs will no longer be accessible. If the public URLs have been cached, they will remain working until the cache has expired. The default expiry time of our CDN offered by Amazon Web Services (AWS) is 24 hours. If you use a custom CDN, the public URLs will no longer work when your custom expiry time has expired.

### Making Public URLs Inaccessible by Archiving or Limiting Assets

By default, an asset's public URLs will be accessible when it is archived or limited. If you don't want this to be the case, we can set up your portal so that public URLs no longer work when an asset is archived or limited, simply _contact your customer success contact to enable this feature_.

Public URLs of an asset that has been visited recently are most likely cached. **Archiving or limiting an asset doesn't invalidate the public URLs.** This means that even when you archive or limit a public asset the cached public URL(s) will remain accessible until the cache has expired. 

### Understanding /m/ Structure Public Links

**Original file**

https://YourPortalURL.com/m/\[idhash\]/original/\[asset-name\].\[file-extension\]

**Derivative**

https://YourPortalURL.com/m/\[idhash\]/\[derivative-prefix\]-\[asset-name\].\[file-extension\]

**/m/**

The /m/ element indicates that it is a public link.

**idhash**

The idhash is a randomly generated hash based on the mediaID. It's a 16-character hexadecimal string.

**original**

This indicates that the URL links to the original file.

**derivative-prefix**

This is a mandatory reference to determine which derivative of the asset to use

**asset-name**

This value represents the name of the asset.

**file-extension**

The file extension of the original file or derivative.

**ensure download**

Type **?download** behind the public URL, ensuring the asset will be downloaded immediately instead of only viewed.

###  Understanding /asset/ Structure Public Links

**Original file**

https://YourPortalURL.com/asset/\[asset-id\]/\[asset-name\]

**Standard Derivative**

https://YourPortalURL.com/asset/\[asset-id\]/thumbnail/\[thumbnail-name\]-\[asset-name\]

**Custom Derivative**

https://YourPortalURL.com/asset/\[asset-id\]/\[derivative-prefix\]/\[asset-name\]

**/asset/**  
The /asset/ element indicates that it is a public link.

**asset-id**  
The ID of the asset in UUID format

**Thumbnail**

This is a reference to determine a request for a standard derivative

**thumbnail-name**

This is a reference to a standard derivative, this can be ‘mini’, ‘thul’ or ‘webimage’

**derivative-prefix**  
This is a mandatory reference to determine which derivative of the asset to use  
**asset-name**  
This value represents the name of the asset.

_Note: Currently, public links are built with these two structures, in the near future, all assets will be the **/asset/** links structure. Any **/m/** link currently in use will be backwards compatible and continue working._

### Understanding Customized Public URLs

You can customize your public URLs for SEO optimization or to meet your brand's naming conventions. You can replace any text behind the /original/ or derivative-prefix element with your own text. Based on the random IDhash, the system can still redirect users to the correct public original file or public derivative.

**Example**

The two public URLs below link to the original file and to the 'socialmedia' derivative. This is the default non-customized version of both URLs

https://YourPortalURL.com/m/2dca1fb32bd065d1/**original**/Bynder-Logo-Blue.png

https://YourPortalURL.com/m/2dca1fb32bd065d1/**socialmedia-**Bynder-Logo-Blue.jpg

Optionally, the text, or "slug", behind the **original** and **social media-** elements can be fully removed or customized. You can make the changes in your preferred text editor. You cannot make customizations in the portal itself.

_Note: Renaming an asset will not alter the ID hash._

Example of a customized public URL:

https://YourPortalURL.com/m/2dca1fb32bd065d1/**original**/Bynder-Logo.png

https://YourPortalURL.com/m/2dca1fb32bd065d1/**socialmedia-**Logo.jpg

 FAQs[](https://support.bynder.com/hc/en-us/articles/360013870200#h_01JNX7ZZKGXH88P1GREQMD5XP7)

------------------------------------------------------------------------------------------------

**Can I uncheck making an asset public?**

If you decide to make an asset public, you will not be able to clear the checkbox and make it private again. You can only delete or archive it.

**When the CloudFront CDN is used how long does a link take to update?**

If your public assets are served through our CloudFront CDN, their link can refresh in real-time. 

**Are thumbnails automatically public?**

Thumbnails are public by default.

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013870200#h_01JNX874RV0NARZXJEGPYZFM5A)

-----------------------------------------------------------------------------------------------------------

[How To Create And Manage Custom Links](https://support.bynder.com/hc/en-us/articles/21861490210450)
 

[How To Create A Public Collection](https://support.bynder.com/hc/en-us/articles/15954306339474)

[How To Make Landing Pages and Guides Public](https://support.bynder.com/hc/en-us/articles/22047232015378)
 

### _Level: Beginner_

Beginner-level articles are for everyone, these articles do not assume any prior Bynder knowledge. These articles are a great place to start your Bynder Journey.

Share
