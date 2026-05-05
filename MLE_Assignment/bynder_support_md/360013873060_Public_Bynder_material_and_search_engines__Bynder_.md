# Public Bynder material and search engines – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013873060-Public-Bynder-material-and-search-engines

If you are worried about search engines indexing your public assets or collections, there are measures you can take to prevent this. If a link to your public material is not mentioned on any external page, blog, or website, it is highly unlikely that search engine bots will be able to index it.

To further ensure that your public assets and collections are not indexed, we can create a robots.txt file for your portal. This file will include instructions to disallow search engine bots from crawling and indexing your public Bynder materials. If you would like this set up for your portal, please contact your Customer Success Contact.

However, if a search engine discovers an external link to your public material, it may be indexed. In this case, people may be able to find and access your public assets and collections by using relevant keywords in the search engine.

Note: Once the robots.txt file has been set up, search engine bots won't be able to access your Bynder portal and can't index any type of content. It's not possible to set up exceptions for specific content types.

Note: Please be advised that this will not de-index a file that was previously publicly available via the public url before the feature was enabled. In this case, you would need to set a header X-Robots-Tag: **noindex** on the public url on your end. One way to do this would be to use a rewriting proxy script in front of the original file, which adds headers like **noindex**. We currently don't offer a solution for de-indexing on the Bynder side. 

Note: robots.txt is not customizable to allow or disallow specific search engines. It is either on or off.

Share
