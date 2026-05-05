# Create and Apply DAT Presets – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/5071969529874

A DAT preset consists of predefined transformations you can apply to as many assets as you want. You can create and apply a DAT preset to save time and help avoid manually applying the same [transformation](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN485H8BEGGPCNPS0AHCCVN)
 to your assets. 

Learn how to [group your DAT Preset](https://support.bynder.com/hc/en-us/articles/16251526622226)
s to better organize them.

**Who can create DAT Presets?**

Create DAT Presets[](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN3EYFK303EV0S6YRD6VZWB)

--------------------------------------------------------------------------------------------------------------

1.  Navigate to your Bynder Portal.
2.  Select **Advanced Settings**\> **Portal** **Settings** > **DAT** **Presets in the top right corner.**
3.  Click the **➕ New preset** button.
4.  Enter a name for the new preset in the **Preset name** field.
5.  You can check off if you would like to add this preset to an existing [Preset group](https://support.bynder.com/hc/en-us/articles/16251526622226)
    . 
6.  Click the **➕ New transformation** button.
7.  Open the **Transformation** dropdown and select one of the [available transformations](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN485H8BEGGPCNPS0AHCCVN)
    .
    *   Read more about the transformations [here](https://support.bynder.com/hc/en-us/articles/5071969529874#UUID-f33c8c66-f7b3-d2ce-2abb-470d8c5251fa_section-idm4519428882246432986391816176 "Transforms")
        .
8.  Use the fields, sliders, and options that appear to configure the transformation.
9.  (Optional) Click the **➕ Add transformation** button to add another transformation to the DAT preset.
10.  Click the **Format** dropdown and select the file extension you want the output file to have.
11.  Click the **Quality** dropdown and select one of the available options to set the quality of the output file.
12.  Click **Save Changes** to save the new DAT preset.

Available Transformation[](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN485H8BEGGPCNPS0AHCCVN)

--------------------------------------------------------------------------------------------------------------------

### Transforms

#### Background: Change the background color of a transparent image.

*   Enter the HEX code of the color you want to fill the background within the Color field.

#### Border: Add a border around the image and specify the border width and border color.

*   In the Color field, enter the HEX code for the border color. In the Border field, set the border width by entering the number of pixels.

#### Crop: You can crop a part of an image. Select the shape you want to apply to the crop by choosing one of the options below.

*   **Rectangle:** The image will be cropped using a rectangle shape.
*   **Ellipse:** The image will be cropped using an ellipse shape.
*   **Clipping Path(Only for PSD and TIFF files): The image will be cropped, respecting the clipping path. Clipping paths can be set up using image editing software. After applying the clipping path, anything inside the path will be included**, and the rest of the image will be removed. Only **one clipping path can** work with this function.
*   **Set the dimensions** of your crop using the width and height fields located in the **dimensions** section. (can only be applied to **rectangle** and **ellipse** crops)  ![clipping_crop.gif](https://support.bynder.com/hc/article_attachments/10641690028818)

#### Remove Background: Remove the image background. The system will use the available clipping path information to mask the image and remove the background.

*   Fill the removed background with a solid color using the **Background** transformation.

#### Extend: Extend the image to the specified dimensions.

*   Enter the new width and height in the **Dimensions** section.
*   For a transparent background, you can set the opacity to 0%
*    
    *   (Optional) If you want to fill the transparent area of the extended canvas with a solid background color, enter the HEX code of the color in the Background field.

#### Fill: Resize the image without distortion (losing the aspect ratio). As much of the image as possible will remain visible. The image may be cropped to create an image with the specified dimensions.

*   Resize the image by entering the desired dimensions in the width and height fields of the **Dimensions** section. 
*   You cannot upscale the image as it will lead to quality loss.

1.  Open the **Focus** dropdown and determine which part of the image should be copped by selecting the following options:
    *   **Focus point:** The image will be cropped from the predefined focus point, ensuring that the most important visual information will be available in your crop.
    *   **Gravity: S**et which part of the image shouldn't be cropped. Depending on the entered dimensions, other sides may still be cropped. Use the **gravity** **picker** or the dropdowns in the **Gravity** section to set the gravity. ![gravity_picker.jpg](https://support.bynder.com/hc/article_attachments/10641651992850)

Fit: Resize the image based on specific dimensions. The aspect **will not** change, meaning one size of the resized image may not have the exact specific dimensions. 

*   You cannot upscale the image as it will lead to quality loss.

Flip: Flip the image vertically. 

Mirror: Flip the image horizontally.

Rotate: Rotate the image clockwise based on specific degrees.

*   Enter the number of degrees you want to rotate the image in the **Angle** field. 

Scale: Scale the image to the specific width and height. The aspect ratio may change

*   Resize your image by entering the desired image in the width and height fields in the **Dimensions** section.

### Filters

#### Opacity: Set the opacity level of the derivative.

*   Use the Opacity slider to set the level.

#### Sepia: Add a sepia tone filter to the derivative

#### Contrast: Adjust the contract of the derivate.

*   Use the **Contrast** slider to set the level.

#### Brightness: Adjust the brightness of the derivate.

*   Use the **Brightness** slider to set the level.

#### Grayscale: Add a grayscale tone to the derivative.

#### Blur: Apply a blur to the derivative.

*   Use the **Blur slide to** set the level.

#### Sharpness: Set the sharpness level to the derivative.

*   Use the **Sharpness slide to** set the level.

#### Saturation: Set the saturation level to the derivative.

*   Use the **Saturation slide to** set the level.

Overlay[](https://support.bynder.com/hc/en-us/articles/5071969529874#01HKN5DSR7FDXNRPAQ46AQ5G80)

-------------------------------------------------------------------------------------------------

### Text Overlay: Apply a text layer to an image.

1.  Enter the text for the overlay in the **Text** field.
2.  Select the font from the **Font** dropdown.
3.  In the Text color field, enter the HEX code of the desired font.
4.  Choose the position for the text overlay using the position picker or from the dropdown options in the **Position** section.
5.  (Optional) Set the padding for the text in the **Padding** field.
6.  (Optional) Enter the number of degrees to rotate the text in the **Angle** field.

### Image Overlay: Overlay an image over another.

1.  Select the asset you want to overlay by selecting an asset in the **image** section.
2.  Search through your **DAM** assets and select an image.
3.  Enter a **percentage**(1-100) to determine the **opacity** of the overlay image in the [Opacity field](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN53FAQKQGAR6B6MPARZ7PE)
    
4.  Select the position of the overlay image using the position picker or the dropdowns in the **Position** section
5.  In the Angle section, enter a number (0-359) to determine the angle of the overlay image.

### Color Overlay: Apply a text layer to the image.

1.  Enter the **HEX** **code** of the desired overlay color in the color field
2.  Enter the **percentage** (1-100) to specify the transparency of the color overlay

### Note

The DPI output for DAT is 72 DPI and cannot be changed at this time.

**Who can view and apply DAT Presets?**

Users with the following permissions can view and apply DAT:

*   **Show DAT URL**
*   **View and Download Presets**
*   **Download public asset derivatives**

Apply a DAT Preset[](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN56VWVRH0QS78MDG44TJJ2)

--------------------------------------------------------------------------------------------------------------

1.  Navigate to your Portal.
2.  Select **Advanced** **Settings**\> **Portal** **Settings** > **DAT** **Presets in the top right corner**.
3.  Select the asset for which you want to apply the DAT Preset.
4.  Click **Transformations** in the right sidebar. A screen to configure the DAT transformations will open.
5.  Click the preset you want to apply in the right sidebar. A preview of the DAT derivative will be generated.
6.  Click the ![link_brand_guidelines.png](https://support.bynder.com/hc/article_attachments/10641652018194) button to copy the URL of the DAT derivative and click ![hamburger_menu.png](https://support.bynder.com/hc/article_attachments/10641690098706) and **Download** to download the DAT derivative.

### Note

If you currently use [public derivatives](https://support.bynder.com/hc/en-us/articles/360013870200)
 and want to redirect to DAT, please reach out to your customer success contact who can enable it for you.

Edit a DAT Preset[](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN5776MZQSEG3C5RVTPPERY)

-------------------------------------------------------------------------------------------------------------

1.  Navigate to your Portal.
2.  Select **Advanced** **Settings**\> **Portal** **Settings** > **DAT** **Presets in the top right corner**.
3.  Click ![hamburger_menu.png](https://support.bynder.com/hc/article_attachments/10641690098706) next to the preset you want to edit and click **Edit**.
4.  Modify or delete existing transformations or add new ones by clicking the **➕ Add transformation** button. Click the **Output options** dropdown to change the output options.
5.  Click **Save Changes** to save the modifications.

Delete a DAT Preset[](https://support.bynder.com/hc/en-us/articles/5071969529874#h_01HKN3EYFM37Z9RWWSZGRWFYSF)

---------------------------------------------------------------------------------------------------------------

1.  Navigate to your Portal.
2.  Select **Advanced Settings**\> **Portal** **Settings** > **DAT** **Presets in the top right corner**.
3.  Click ![hamburger_menu.png](https://support.bynder.com/hc/article_attachments/10641690098706) next to the preset you want to delete and click **Remove**.
4.  Your preset will be deleted.
    
    ### Note
    
    This action is permanent and can't be undone.
    

Share
