# Predictable URL Support for Adaptive Video Streaming – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/25059554242962

Predictable URLs for Adaptive Video Streaming allow you to efficiently retrieve video assets based on predefined criteria, such as location, language, or target audience.  By structuring URLs consistently, this feature allows you to automate content retrieval and deliver the most relevant assets to end-users or downstream systems. It improves content management, enhances user experience, boosts SEO, and ensures brand consistency.

These URLs are generated using asset characteristics, known as Metaproperties, which define key details like country, city, or other specific identifiers. This structure simplifies content retrieval and ensures the correct video is delivered based on user needs or system requirements.

With Predictable URLs, you can easily link video assets to product information and efficiently deliver them to external sites. For example, product demonstration videos can be customized based on location, ensuring customers see content relevant to their region.

How to Enable this feature?[](https://support.bynder.com/hc/en-us/articles/25059554242962#h_01JNEA5H2971KPT7BEMGMSJ58C)

------------------------------------------------------------------------------------------------------------------------

This feature is available for those who have CX Omni Channel/ Dynamic Asset Transformation (DAT) enabled in your portal. 

Key Features[](https://support.bynder.com/hc/en-us/articles/25059554242962#h_01JNE9TJB025T1Z29K1VCJ2J1X)

---------------------------------------------------------------------------------------------------------

*   Targeted Content Delivery: Serve content matching the user’s context (e.g., destination, audience type) using Metaproperties for precise targeting.
*   Improved SEO: Structured, predictable URLs improve content discoverability on search engines.
*   Seamless Integration: Maintain consistent content delivery across different systems, ensuring smooth integration with e-commerce sites, PIM systems, and marketing tools.

How to Use Predictable URL Support[](https://support.bynder.com/hc/en-us/articles/25059554242962#h_01JNE9TJB0S3VWBPA8VRMX16G5)

-------------------------------------------------------------------------------------------------------------------------------

Once this feature has been enabled in your portal,

1.  Upload a new video asset or select an existing one. 
    
2.  In the **Embed** **Media** section, toggle the **"Allow Embedding"** setting to on. This setting ensures that video content can be embedded into external platforms or systems.
3.  If you have not done so already, tag the asset with relevant Metaproperties (e.g., country, language) and their corresponding options (e.g., "Maldives" for country).
4.   These tags enable the content to be dynamically retrieved based on user needs.
5.  Build Your Predictable URL
6.  The Predictable URL structure consists of key components. These URLs allow seamless and automated retrieval of adaptive video content based on the defined Metaproperty and option.

### Example URLs:

HLS URL: https://baseurl/match/vod-stream/country/maldives/play-hls2.m3u8

DASH URL: [https://baseurl/match/vod-stream/country/maldives/play-dash.mpd](https://baseurl/match/vod-stream/country/maldives/play-dash.mpd) 

*   **Base URL:** Your portal’s root URL (e.g., https://baseurl).
*   **/match**: Directs the system to match the asset based on specific metadata.
*   **/vod-stream:** Specifies that the content is a video-on-demand stream.
*   **/Metaproperty\_name:** The name of the Metaproperty (e.g., “country”).
*   **/Metaproperty\_option:** The value associated with the Metaproperty (e.g., “Maldives”).
*   **/play-hls2.m3u8 or /play-dash.mpd:** The specific video streaming format (HLS or DASH).
*   **/poster:** Use this for thumbnail retrieval. 

Best Practices & Key Watchouts[](https://support.bynder.com/hc/en-us/articles/25059554242962#h_01JNE9TJB06S0YEFDSN7CRAWVM)

---------------------------------------------------------------------------------------------------------------------------

### Case Sensitivity

Case-Sensitivity. Metaproperty and Metaproperty options are case-sensitive and need to be written in the URL exactly as they are tagged: 

*   i.e., the country and Maldives should start with uppercase **C** and **M.**
    

### Ensure Correct Streaming Format

The final URL parameter should reflect the type of streaming format being used—either HLS or DASH:

*   HLS: play-hls2.m3u8
*   DASH: play-dash.mpd

Both formats require specific video players that support the respective protocols. Ensure the player used is compatible with the selected format.

### Manifest URL Modification

When embedding video content on external sites, modify the manifest URL in the embed code to include the Predictable URL parameters.

For example:

*   HLS:  
    <video bvd-manifest-url="https://baseurl/match/vod-stream/country/maldives/play-hls2.m3u8">
*   DASH:  
    <video bvd-manifest-url="https://baseurl/match/vod-stream/country/maldives/play-dash.mpd">

### Tagging Accuracy

Ensure that assets are tagged with accurate and relevant Metaproperties and options. Incorrect or missing tags may prevent content from being retrieved correctly.

### Player Compatibility

Verify that the video player used supports both HLS and DASH streaming formats. If a particular format is chosen, ensure the player can deliver the appropriate stream.

Share
