# Create a DAT Derivative Using URL Parameters – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/18953104053266

You can create [Dynamic Asset Transformations](https://support.bynder.com/hc/en-us/articles/18952775916562)
 by adding parameters to the DAT derivative URL or by adding them in your Asset Detail View. Once you've set up all the necessary transformations, you can configure the [output](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK32A03VCX8CPTQ9XPQ4B6)
 options. Once generated, the DAT derivative will have the selected file extension. When you need to apply Dynamic Asset Transformation (DAT) on a website or another platform, automating the process is crucial. For instance, in the case of a web store where product photos require consistent cropping to 800 by 800 pixels with a 5-pixel border, manually creating these transformations in Bynder repeatedly is inefficient. Utilizing our [API](https://support.bynder.com/hc/en-us/articles/360017186900)
, you can integrate DAT on your external platform by utilizing the DAT base URL along with specific parameters to achieve the desired transformations efficiently.  

Watch the DAT training video [here](https://support.bynder.com/hc/en-us/articles/20373097654674)
 to get started!

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Available Transformations

|     |     |     |     |
| --- | --- | --- | --- |
| [Transform](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK329XDPDK31PE81ZHN8C2) | [Filters](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK329YAMJMXJZCZ6A7PXSP) | [Overlay](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK329ZKE3F9Z7PGHS3G5K5) | [Output](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK32A03VCX8CPTQ9XPQ4B6) |
| Background | Brightness | Color Fill/Box | File Type |
| Border | Grayscale | Text | Quality |
| Crop | Blur | Image | Automatic Download |
| Scale | Sharpness |     |     |
| Crop | Saturation |     |     |
| Rotate | Temperature |     |     |
| Flip |     |     |     |
| Mirror |     |     |     |
| Border |     |     |     |
| Background |     |     |     |

Create DAT Derivatives Using URL Parameters[](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HXYTYGJVTEZXRN1SZBRSCFXJ)

----------------------------------------------------------------------------------------------------------------------------------------

1.  Navigate to Asset Bank.
    
2.  Select the asset that you want to create a Dynamic Asset Transformation.
    
3.  Copy the DAT derivative URL in the **Link to Public Files** section. This URL functions as the base URL to which you'll add your transformations.
    
4.  Create your customized DAT derivative by adding one of the transformations indicated in the table below directly behind the derivative URL.
    
5.  Click the corresponding dropdown for more detailed information on the available transformations.
    

Transform[](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK329XDPDK31PE81ZHN8C2)

------------------------------------------------------------------------------------------------------

### Fill

*   Ensure that as much of the image as possible remains visible. With gravity, you can set which part of the image shouldn't be cropped. Depending on the entered dimensions, other sides may still be cropped. The aspect ratio is maintained. See the example below.
    
    ?io=transform:fill,width:100,height:200,gravity:center
    

| **Properties** | **Name** | **Type** | **Default Value** | **Range** |
| --- | --- | --- | --- | --- |
| Transformed image width in pixels | width | int | ﹥0 and less than max width (max-width = width of the base DAT derivative) |     |
| Transformed image height in pixels | height | int | ﹥0 and less than max height (max height = width of the base DAT derivative) |     |
| Indicates which area to keep for the transformation. The other areas may be cropped. | gravity | sting | center | Center, top, top left, topright, left, right, bottom, bottom left, bottom right |

### Fit

Resize the image based on the specified parameters. The aspect ratio will not change. See the example below.

?io=transform:fit,width:200,height:200

| **Properties** | **Name** | **Type** | **Default Value** | **Required** |
| --- | --- | --- | --- | --- |
| Transformed image width in pixels | width | int | ﹥0 and less than max width (max width = width of the base DAT derivative) | Yes |
| Transformed image height in pixels | height | int | ﹥0 and less than max height (max height = width of the base DAT derivative) | Yes |

### Extend

Extend the image to the specified dimensions. See the example below.

?io=transform:extend,width:110,height:100

| **Name** | **Type** | **Default Value** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- | --- |
| width | int | ﹥0 and less than max width (max width = width of the base DAT derivative) | Fit the image (resize) to a box based on the specified width and height. |     | Yes |
| height | int | ﹥0 and less than max height (max height = width of the base DAT derivative) |     |     |     |
| background | string | white |     | HTML color names (red, white, black, yellow) or HEX codes. Use **auto** to set the most dominant color inside the image as border color. |     |

### Scale

Scale the image to the specified width and height. The aspect ratio may change. See the example below.

?io=transform:scale,width:200,height:200

| **Name** | **Type** | **Default value** |
| --- | --- | --- |
| width | int | ﹥0 and less than max width (max width = width of the base DAT derivative) |
| height | int | ﹥0 and less than max height (max height = width of the base DAT derivative) |

### Crop

Crop a part of the image. See the example below.

?io=transform:crop,width:200,height:200

| **Name** | **Type** | **Default Value** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- | --- |
| width | int | ﹥0 and less than max width (max width = width of the base DAT derivative) |     |     | Yes |
| height | int | ﹥0 and less than max width (max width = width of the base DAT derivative) |     |     | Yes |
| gravity | string | center | The crop will start from the specified area. This part of the image will remain and other areas may be cropped. | Center, top, topleft, topright, left, right, bottom, bottomleft, bottomright | No  |
| path | string | circle | This will change the crop to a round shape. Make sure width and height are set to the same dimensions in order to use a circle. Use different dimensions to use an oval. |     | No  |
| background | string | white | Add a background color | HTML color names (red, white, black, yellow) or HEX codes. Use **auto** to set the most dominant color inside the image as border color. | No  |
| blur | int | 0   | Blur the edge of the crop | 0 to 100 | No  |

### Rotate

Rotate the image clockwise based on the specified degrees. See the example below.

?io=transform:rotate,angle:270

| **Name** | **Type** | **Default Value** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- | --- |
| angle | int | 0   | Rotate the image by a certain angle in degrees, clockwise | 0 < 360 | Yes |

### Flip

Flip the image vertically. See the example below.

?io=transform:flip

### Mirror

Flip the image horizontally. See the example below.

?io=transform:mirror

### Border

Add a border around the image and specify the border width and border color. See the example below.

?io=transform:border,width:2,color:black

| **Name** | **Type** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- |
| width | int | The border width specified in pixels. | ﹥0 and less than the maximum width of the DAT derivative | Yes |
| color | string | The color of the border | Specify the border color using HTML color names (red, white, black, yellow) or HEX codes. Use **auto** to set the most dominant color inside the image as border color. | No  |

### Background

Change the background color of a transparent image. See the example below.

?io=transform:background,color:grey

| **Name** | **Type** | **Default Value** | **Range** | **Required** |
| --- | --- | --- | --- | --- |
| color | string | white | Specify the background color using HTML color names (red, white, black, yellow) or HEX codes. Use **auto** to set the most dominant color inside the image as border color. | Yes |

Filters[](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK329YAMJMXJZCZ6A7PXSP)

----------------------------------------------------------------------------------------------------

#### Opacity

Adjust the transparency of the whole image.

?io=filter:opacity,amount:60

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| amount | int | 0—100 (% based value) | No  |

#### Sepia

Apply a sepia filter to the image.

?io=filter:sepia

#### Contrast

Adjust the contrast level of the image.

?io=filter:contrast,amount:80

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| amount | int | \-100—100 (% based value) | No  |

#### Brightness

Adjust the brightness level of the image.

?io=filter:brightness,amount:80

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| amount | int | \-100—100 (% based value) | No  |

#### Grayscale

Convert the colors an image to black and white.

?io=filter:grayscale

#### Blur

Apply a blur effect to the image.

?io=filter:blur,radius:20

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| radius | int | ﹥0 (blur radius in pixels) | No  |

#### Sharpness

Adjust the sharpness of the image.

?io=filter:sharpness,amount:80

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| amount | int | \-100—100 (% based value) | No  |

#### Saturation

Adjust the saturation level of the image.

?io=filter:saturation,amount:80

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| amount | int | \-100—100 (% based value) | No  |

#### Vignette

Add a vignette effect to the image.

?io=filter:vignette,amount:100,color:black,softness:50

    
| **Name** | **Type** | Description | **Range** | **Required** |
| --- | --- | --- | --- | --- |
| amount | int | Controls the opacity of the gradient | 0-10 | No  |
| color | string | HTML color names (red, white, black, yellow) or HEX codes. Use **auto** to set the most dominant color inside the image as border color. |     | No  |
| softness | int | % based value | \-100—100 | No  |

#### Temperature

Adjust the color temperature of the image.

?io=filter:temperature,amount:5000

| **Name** | **Type** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- |
| amount | int | Controls the color temperature in kelvin | 800-12000 | yes |

Overlay[](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK329ZKE3F9Z7PGHS3G5K5)

----------------------------------------------------------------------------------------------------

#### Color Overlay

Apply an overlay with a solid color and specified transparency to the image.

?io=overlay:box,color:red,opacity:20

     
| **Nam**e | **Type** | **Default Value** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- | --- |
| color | string |     | Specify the color using HTML color names (red, white, black, yellow) or HEX codes. Use **auto** to set the most dominant color inside the image as border color. |     | yes |
| opacity | int | 25% | % based value | 0-100 | no  |

#### Text Overlay

Apply a text layer to the image.

?io=overlay:text,content:some%20text,font:Arial,size:11,color:black,angle:45

     
| **Name** | **Type** | **Default Value** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- | --- |
| content | string |     | URL encoded string |     | yes |
| font | string | arial | supported fonts and uploaded custom fonts |     | no  |
| size | int | 16  | font size | ﹥1  | no  |
| color | string | #fff | Specify the color using HTML color names (red, white, black, yellow) or HEX codes. Use **auto** to set the most dominant color inside the image as border color. |     | no  |
| angle | int |     | angle units |     | no  |

#### Image Overlay

Apply an image layer to the image.

io=overlay:image,asset:{asset\_id},width:200,opacity:45,angle:45,gravity:center,padding:30

     
| **Name** | **Type** | **Default Value** | **Description** | **Range** | **Required** |
| --- | --- | --- | --- | --- | --- |
| asset | uuid |     | The existing asset ID of a Bynder image asset (used for the overlay) |     | yes |
| width | int |     | overlay width | ﹥0  | no  |
| height | int |     | overlay height | ﹥0  | no  |
| rotate | int |     | rotation amount in degrees | 0-359 | no  |
| opacity | int | 100% | adjust overlay transparency | 0-100 | no  |
| gravity | string | center |     | *   center<br>    <br>*   right<br>    <br>*   left<br>    <br>*   topleft<br>    <br>*   top<br>    <br>*   topright<br>    <br>*   bottomleft<br>    <br>*   bottom<br>    <br>*   bottomright | no  |
| padding | int |     | applies padding to the overlay image | ﹥0  | no  |

Output[](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK32A03VCX8CPTQ9XPQ4B6)

---------------------------------------------------------------------------------------------------

### Convert Output File to JPG, PNG, WEBP and AVIF

Convert the original file to a JPG, PNG, WEBP or AVIF file.

?format=jpg

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| format | string | jpg, png, webp, avif | yes |

### Output Quality

?quality=80

Set the quality of the output file. This only works for webP and jpg files.

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| quality | int | 1-100 | yes |

### Automatic Download

&download=true

Ensure that the download of the DAT derivative will start automatically upon visiting the URL.

| **Name** | **Type** | **Range** | **Required** |
| --- | --- | --- | --- |
| download | int | true | yes |

Limitations[](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01HCAK32A0PVPESVR6NWN71CCB)

--------------------------------------------------------------------------------------------------------

DAT does not currently support SVG as an output format.

If you would like to use an SVG as an output, you should mark the file as **Public** in the **Advanced Rights** section of the asset, then use the **Original** **URL** that will appear in the **Public** **Links** section of the Asset Detail view.

SVG files loaded into Bynder will still generate Webp DAT derivatives that can be used with the DAT UI and Presets.

Related Articles[](https://support.bynder.com/hc/en-us/articles/18953104053266#h_01K38TSXVJ3Z7E4YA1086X3P7H)

-------------------------------------------------------------------------------------------------------------

[How To Create A DAT Derivative In Asset Detail View](https://support.bynder.com/hc/en-us/articles/360018559260-How-To-Create-A-DAT-Derivative-In-Asset-Detail-View)

Share
