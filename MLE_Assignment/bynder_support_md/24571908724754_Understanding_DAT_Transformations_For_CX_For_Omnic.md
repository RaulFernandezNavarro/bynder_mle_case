# Understanding DAT Transformations For CX For Omnichannel – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/24571908724754

Summary[](https://support.bynder.com/hc/en-us/articles/24571908724754#h_01JKT3D7SYCH65X4NQMMHABY7Q)

----------------------------------------------------------------------------------------------------

This article aims to give you more information on what the DAT transformation options do. Use this guide to understand what the DAT change will entail. 

Transform[](https://support.bynder.com/hc/en-us/articles/24571908724754#h_01JKT5Y2YVSJ3V5Z6H7297GAVB)

------------------------------------------------------------------------------------------------------

#### **Background**

Change the background color of a transparent image.

*   Enter the HEX code of the color you want to fill the background within the **Color** field.
    

#### **Border**

Add a border around the image and specify the border width and border color.

*   Enter the HEX code for the border color in the **Color** field.
    
*   Set the border width by entering the number of pixels in the **Border** field.
    
    *   Example: Width = 30 - this means that all sides of the image will have a 30px border.
        
    *   To customize the border / padding width per side of the image update the URL by modifying the width parameter directly in order to customize a different border pixel per image side:
        
    *   Example: width = (30,20,30,20) - this indicates that 2 sides will have 20px border while the other two sides will have 30px border.
        
        *   1st number = Top side
            
            2nd number = right side
            
            3rd number = bottom side
            
            4th number = left side
            

#### **Crop**

Crop a part of the image.

*   Select the shape you want to apply to the crop by choosing one of the below options
    
    *   **Rectangle**
        
        The image will be cropped using a rectangle shape.
        
    *   **Ellipse**
        
        The image will be cropped using an ellipse shape.
        
    *   **Clipping Path**
        
        The image will be cropped according to the clipping path, which can be set up using image editing software. After the clipping path is applied, anything inside the path will be included, and the rest of the image will be removed. Clipping Path is supported **only** for PSD and TIFF files
        
          
        
        ![clipping_crop.gif](https://support.bynder.com/hc/article_attachments/24571908715922)
        
        Example of cropping with a clipping path.
        
    
*   Set the dimensions of your crop using the width and height fields in the **Dimensions** section.
    

_Note: The dimensions can only be set for **Rectangle** and **Ellipse** crops._

#### **Remove Background**

Remove the image background. The system will use the available clipping path information to mask the image and remove the background.

_Tip: Fill the removed background with a solid color using the **Background** transformation._

#### **Extend**

Extend the image to the specified dimensions.

*   In the Dimensions section, enter the new width and height to decide how much you want to extend the image canvas.
    
*   (Optional) If you want to fill the transparent area of the extended canvas with a solid background color, enter the HEX code of that color in the Background field.
    

#### **Fill**

Resize the image without distortion (losing the aspect ratio). As much of the image as possible will remain visible. The image may be cropped to create an image with the specified dimensions.

*   Resize the image by entering the desired dimensions in the width and height fields of the **Dimensions** section.
    
    *   _Note: We cannot upscale the image as this would lead to quality loss._
        
*   Open the **Focus** dropdown and decide which part of the image should be cropped by choosing one of the following options
    
    *   **Focus point**
        
        The image will be cropped from the predefined focus point, ensuring that only the most important visual information is available in the crop.
        
    *   **Gravity**
        
        With gravity, you can set which part of the image shouldn't be cropped. Depending on the entered dimensions, other sides may still be cropped.
        
        Use the gravity picker or the dropdowns in the **Graviy** section to set the gravity
        
        ![gravity_picker.jpg](https://support.bynder.com/hc/article_attachments/24571908717842)
        
    

#### **Fit**

Resize the image based on the specified dimensions. The aspect ratio won't change which means one size of the resized image may not have the exact specified dimension.

*   Resize your image by entering the desired image in the width and height fields in the **Dimensions** section.
    

_Note: We cannot upscale the image as this would lead to quality loss. Note that due to high density displays some content will appear fuzzier because it uses less pixels than your display._ 

#### **Flip**

Flip the image vertically.

#### **Rotate**

Rotate the image clockwise based on the specified degrees.

*   Enter the number of degrees you want to rotate the image in the Angle field.

#### **Scale**

Resizes the image to the specified dimensions without necessarily retaining the original aspect ratio.

#### **Trim**

Removes any transparent or white-colored areas at the edges of an image.

Filters[](https://support.bynder.com/hc/en-us/articles/24571908724754#h_01HCAK329WV6CHRDCRH8RTEEXP)

----------------------------------------------------------------------------------------------------

#### **Opacity**

Set the opacity level of the DAT derivate.

*   Use the **Opacity** slider to set the opacity level.
    

#### **Sepia**

Add a sepia tone filter to the DAT derivate.

#### **Contrast**

Adjust the contrast of the DAT derivate.

*   Use the **Contrast** slider to set the opacity level.
    

#### **Brightness**

Adjust the brightness of the DAT derivative.

*   Use the **Brightness** slider to set the brightness of the DAT derivative.
    

#### **Grayscale**

Add a grayscale tone filter to the DAT derivate.

#### **Blur**

Apply blur to the DAT derivative.

*   Use the **Blur** slider to set the blur level of the DAT derivative.
    

#### **Sharpness**

Set the sharpness level of the DAT derivate.

*   Use the **Sharpness** slider to set the brightness of the DAT derivative.
    

#### **Saturation**

Set the saturation level of the DAT derivate.

*   Use the **Saturation** slider to set the brightness of the DAT derivative.
    

#### **Text**

Apply a text layer to the image.

*   Enter the text for the overlay in the **Text** field.
    
*   Select the font for the text overlay in the **Font** dropdown.
    
*   Enter the HEX code of the desired font color in the **Text color** field.
    
*   Choose the position for the text overlay using the position picker or the dropdowns in the **Position** section.
    
*   (Optional) Set the padding for the text in the **Padding** field.
    
*   (Optional) Enter the number of degrees you want to rotate the text in the **Angle** field.
    

#### **Image**

Overlay an image over another.

_Note: Currently, only one image overlay transformation can be applied at once. DAT image overlays will not respect the size of the selected derivatives._ 

*   Select the asset you want to overlay by clicking on **Choose** **asset** in the image section
    
*   Search through your DAM assets and select the one you would like to use
    
*   Enter a percentage(1-100) to determine the opacity of the overlay image in the Opacity field
    
*   Select the position of the overlay image using the position picker or the dropdowns in the **Position** section
    
*   Enter a number (0-359) to determine the angle of the overlay image in the **Angle** section
    

#### **Color**

Apply a text layer to the image.

*   Enter the HEX code of the desired overlay color in the **color** field
    
*   Enter the percentage (1-100) to specify the transparency of the color overlay
    

Output[](https://support.bynder.com/hc/en-us/articles/24571908724754#h_01HCAK32A03VCX8CPTQ9XPQ4B6)

---------------------------------------------------------------------------------------------------

#### **Format**

This will convert the original file to a .JPG, .PNG, .WEBP or .AVIF file type. The default output format is .AVIF, if AVIF is not possible with the users browser the output will be .WEBP.

_Note: When converting .JPG or .PNG to .WEBP there can be a color conversion issue that may cause the asset to appear pixelated._ 

#### **Quality**

Set the quality of the output file. This only works for .WEBP and .JPG files.

#### **Automatic Download**

This ensures that the download of the DAT derivative will start automatically upon visiting the URL.

### SVG Limitations

DAT does not currently support SVG as an output format.

If you would like to use an SVG as an output, you should mark the file as **Public** in the **Advanced Rights** section of the asset, then use the **Original** **URL** that will appear in the **Public** **Links** section of the Asset Detail view.

SVG files loaded into Bynder will still generate Webp DAT derivatives that can be used with the DAT UI and Presets.

 [](https://support.bynder.com/hc/en-us/articles/24571908724754#h_01JKTNMBK6PH36RWJ8P05NQY9X)

----------------------------------------------------------------------------------------------

FAQs[](https://support.bynder.com/hc/en-us/articles/24571908724754#h_01JKTNQ2HF343KZG3BXR4YFK9H)

-------------------------------------------------------------------------------------------------

**What if I want a transformation that Bynder does not offer?**

Reach out to us! We love feedback and suggestions and take each one seriously.

Related Articles[](https://support.bynder.com/hc/en-us/articles/24571908724754#h_01JKTNMGK31XZVBMVMC26P6AHZ)

-------------------------------------------------------------------------------------------------------------

[Understanding Supported File Types For Conversion And Derivative Creation](https://support.bynder.com/hc/en-us/articles/360013875220)

[Understanding Transformations In DAT](https://support.bynder.com/hc/en-us/articles/24571908724754)

### _Level: Beginner_

Beginner-level articles are for everyone, these articles do not assume any prior Bynder knowledge. These articles are a great place to start your Bynder Journey.

Share
