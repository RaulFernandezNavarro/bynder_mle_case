# Adaptive Video Streaming – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/23906839206546

Adaptive Video Streaming enhances video delivery by converting uploaded files into multiple streamable formats, including **HLS** for live streaming, **iOS** devices, and **MPEG-DASH** for on-demand streaming and other platforms. It automatically adjusts video quality and resolution based on device and bandwidth while enabling seamless embedding into third-party platforms or CMSs via code or API.

[Multilingual subtitle](https://support.bynder.com/hc/en-us/articles/25061882331922)
 support ensures an inclusive and engaging experience, making content accessible to a global audience. [Predictable URLs](https://support.bynder.com/hc/en-us/articles/25059554242962)
 allow efficient retrieval of video assets based on predefined criteria, such as location, language, or target audience.

Maximize video performance with [CX Omnichannel (DAT)](https://support.bynder.com/hc/en-us/articles/18952775916562)
, which automates optimization to deliver high-quality, adaptive video content. Gain valuable insights with the [Delivery Metrics (Advanced Analytics) dashboard,](https://support.bynder.com/hc/en-us/articles/20094286365330)
 which tracks play rate data to identify popular videos, refine content strategies, and optimize underperforming content for better engagement.

### How to Enable this feature?

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Important Information About Existing Videos[](https://support.bynder.com/hc/en-us/articles/23906839206546#h_01JJMC2P16R11DEAG70J2CQ3HQ)

----------------------------------------------------------------------------------------------------------------------------------------

For Existing video content in your portal, we recommend that you either: 

*   **Option 1:** Delete the existing video asset and re-upload it. This ensures the asset is optimized for streaming.
*   **Option 2:** If deleting and re-uploading is not feasible, you can create a [Support ticket](https://support.bynder.com/hc/en-us/articles/19685047299730)
     to regenerate the specific video asset to enable streaming.

_Note: Regeneration should only be used for individual assets when no other option is viable._

How to Retrieve a Streamable Link[](https://support.bynder.com/hc/en-us/articles/23906839206546#h_01JHGR3X2VSSZN4TFY1EGFFXAZ)

------------------------------------------------------------------------------------------------------------------------------

1.  Ensure the video asset is [**marked as public**.](https://support.bynder.com/hc/en-us/articles/360013870200)
     
2.  Enable the **"Allow Embedding"** toggle. ![Screenshot 2025-02-27 at 2.37.23 PM.png](https://support.bynder.com/hc/article_attachments/24980636983954)
3.  Select the desired size dimensions for the video player or choose the responsiveness.
4.  Copy the **streamable link** (HLS or MPEG-DASH) or the **embeddable code**.

_Note: When using the streamable links to view the video, captions are disabled by default and users need to click the three dots button, then turn them on._

5.Paste the link or code into your CMS, third-party platform, or website.![](https://support.bynder.com/hc/article_attachments/23906839204626)![](https://support.bynder.com/hc/article_attachments/23906822819602)

Supported File Types[](https://support.bynder.com/hc/en-us/articles/23906839206546#h_01JHGR3X2V6M0SB9M9M71N3GZZ)

-----------------------------------------------------------------------------------------------------------------

*   Fragmented MP4 type

How To Customize Advanced Video Controls For The Portal[](https://support.bynder.com/hc/en-us/articles/23906839206546#h_01JZMPF537HYZ3S9YYBPYB8AJ0)

----------------------------------------------------------------------------------------------------------------------------------------------------

All Video player controls will be configured on a portal level to ensure users can always deliver consistent videos to their websites. This must be configured by your Bynder Admin.

1.  Open Portal Settings and scroll down to _**video player settings**_ under DAT presets.
2.  See the "**properties**" available to customize by turning toggles on and off for each features.
3.  **Test the feature** by turning the toggle on to see how the video example adjusts.
    *   Features available:
        1.  Autoplay
        2.  Looping
        3.  Subtitle visibility
        4.  Control visibility:
            *   Show controls
            *   Allow rewind and fast-forward
4.  **Enable** the toggles that match the portal needs.
5.  Click **save changes**.

These new settings will be applied to the embed code for every Adaptive streaming video using the Bynder Video player. See the changes applied in the asset detail view.

How To Customize Advanced Video Controls On An Asset Level[](https://support.bynder.com/hc/en-us/articles/23906839206546#01JZMPS98SK9J64S4JKRQNESAS)

-----------------------------------------------------------------------------------------------------------------------------------------------------

1.  From asset detail view **open** the _embed media_ section.
2.  Under the _Allow embedding_ toggle you will see the _Override portal settings_ toggle. Turn the **toggle on** and **click** on the _override settings_ button. A small modal will open.
3.  View the properties available to customize by turning the toggles on and off for each feature. Test the feature by turning the toggle on and see how embed code adjusts according to the changes being made.
    *   Features include:
        *   Autoplay
        *   Looping
        *   Subtitle visibility
        *   Control visibility:
            *   Show controls
                *   Allow rewind and fast-forward

_Note: On the bottom of the page the HTML code will adjust according to the toggles. When a toggle is on the parameter in the code will show **true**. EX: bvd-autoplay="true"._

_Note: Some video player settings can be over-ridden on an asset level, however this will be an "on the fly" delivery. The embed code will change depending on the settings that you have decided to over-ride and that embed code can be copy and pasted for single use. We will not save any overridden configurations for a single asset. To override the video player settings: copy & paste the embed code directly into your CMS or website._

FAQs[](https://support.bynder.com/hc/en-us/articles/23906839206546#h_01JX1YJNB52GRVXVE8XCNZ0A9X)

-------------------------------------------------------------------------------------------------

**What is the difference between "responsive" and "fixed" sizes for adaptive streaming in Bynder?**  
These settings refer to the dimensions of the video player, not the video content itself.  
**_Responsive Size:_** The video player will adjust its dimensions automatically based on the size of the user's browser window. If the browser size changes, the video player will resize accordingly to maintain its aspect ratio and fit the available space.  
_**Fixed Size:**_ The video player will maintain a specific, predefined width and height, regardless of changes to the browser window size. This is useful for ensuring the video player fits a particular layout, especially for vertical videos where you want to control the exact dimensions.  
**Can Bynder deliver videos in responsive sizes?**  
Yes, Bynder can deliver videos in responsive sizes, but it's the video player that is responsive, not the video content itself. The video asset needs to be uploaded to the DAM in the desired dimensions.  
**When should one use responsive vs. fixed size?**  
_**Responsive Size:**_ Use responsive sizing when you want the video player to adapt seamlessly to different screen sizes and devices, providing a flexible viewing experience. This is generally recommended for most web content.  
_**Fixed Size:**_ Use fixed sizing when you need precise control over the video player's dimensions, perhaps to fit a specific design layout, or when embedding vertical videos where a set width and height are critical to the presentation.  
**How can I demonstrate the responsiveness of the video player?**  
You can demonstrate responsiveness by embedding a responsive video player code on a webpage (e.g., using an online HTML editor like W3Schools) and then resizing your browser window. You will observe the video player adjusting its dimensions accordingly.  
**Do responsive and fixed size settings work with HLS and DASH links, or only with the Bynder embed code?**  
The responsive and fixed size settings for the video player only work with the Bynder embed code. They do not directly apply to raw HLS (HTTP Live Streaming) or DASH (Dynamic Adaptive Streaming over HTTP) links, as those links provide the video manifest, not the player itself.  
**What format does the Bynder embed code usually stream in?**  
The Bynder embed code, by default, provides the DASH manifest URL for streaming. However, it can often be modified within the embed code to specify other streaming formats if needed.  
**If a customer has adaptive streaming enabled, will video derivatives still work?**  
Yes, the only change will be the embed code. 

Share
