# Import Figma Files into Studio – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/23928665594002

With Studio's [Figma](https://www.figma.com/)
 import feature, designers can bypass the time-consuming task of manually recreating designs, allowing them to focus on crafting impactful content. Whether it’s for quick template creation or flexible import options, this feature boosts design reusability, optimizes workflows and ensures high design fidelity with minimal post-import adjustments. 

#### How to enable this feature?

If you are interested in enabling it in your Studio account, please contact your Customer Success Contact. 

**Who can import design files in Studio?**

Users with the following rights can import design files into Studio:

*   [**Admin**](https://support.bynder.com/hc/en-us/articles/360016135860-Permissions-in-Studio#:~:text=permission%20profiles%20here-,Admin%20User%20Permissions,-Can%20manage%20configurations)
    
*   [**Content Designer**](https://support.bynder.com/hc/en-us/articles/360016135860-Permissions-in-Studio#:~:text=Contributor%20(not%20Owner).-,Regular%20User%20Permissions%20(Content%20Designer%20%2B%20Content%20Creator),-Content%20Designer)
    

Before you Import[](https://support.bynder.com/hc/en-us/articles/23928665594002#h_01JHJSJSG3GV197Y1ASQA124WW)

--------------------------------------------------------------------------------------------------------------

*   Ensure all the fonts used in your Figma design have been uploaded to Studio. Using fonts available in Studio will produce the best results, as this avoids issues like mismatched text size or positioning during the import process.
    *   If the required fonts haven't been uploaded, follow the steps to upload your custom fonts to Studio.
*   Treat your Figma project as a [template](https://support.bynder.com/hc/en-us/sections/18509461347730-Templates)
    . Identify elements that should remain static and those that Studio users must be able to edit. 
*   Ensure text boxes are set up flexibly to avoid restrictions for content creators.
*   Plan editable components strategically to enhance usability.

How to Import Figma Designs into Studio[](https://support.bynder.com/hc/en-us/articles/23928665594002#h_01JHJSJSG3BMSJ04AXDRJHY4S9)

------------------------------------------------------------------------------------------------------------------------------------

1.  [Create a New Design.](https://support.bynder.com/hc/en-us/articles/14490030392082)
    
2.  Click on the **New Design** button in Studio.
3.  Navigate to the **Figma Import** tab in the left menu.
4.  Establish a connection to your Figma account by following the on-screen steps.
5.  Paste the Figma share link or choose from your previously connected design files.
6.  Use the dropdown menu to navigate between the pages in your Figma file.
7.  **Choose Frames to Import**
    *   Ensure each design is within a top-level frame to be available for selection.
8.  Select whether to import frames as **individual** **pages** or **designs**.
9.  Click **Create Design** and allow Studio to process the frames into editable Studio.
10.  Review the import in Studio and adjust elements if required. 

Limitations[](https://support.bynder.com/hc/en-us/articles/23928665594002#h_01JHJSJSG3GJ43Q1XJZ8G80TZM)

--------------------------------------------------------------------------------------------------------

#### **General Setup**

*   Only elements within **top-level frames** are imported.
*   The **order of top-level frames** determines the **thumbnail sequence** in Studio.
*   **Layer and group hierarchies** within frames are maintained during import.

#### **Fills**

*   **Solid color fills**: Only the first fill is imported.
*   **Image fills**: Automatically converted to Studio image elements.
*   **Not supported**: Gradients, video fills, drop shadows and container opacity values.

#### **Images**

*   **Transparency and blend modes**: Supported at the layer level but not for fills.
*   **Unsupported features**: Drop shadows on containers and rounded corners for images (supported for shapes).

#### **Shapes and Vectors**

*   Shapes and vectors convert to **Studio custom shape elements**.
*   **Blend modes and opacity**: May not render as expected.
*   To avoid clipping issues, convert shapes to **SVGs**.
*   Shapes using "Exclude" or "Vector" operations may behave unpredictably.

#### **Rotations and Dimensions**

*   **Rotation values**: Adjusted during import (**calculated as Figma\_Value - 360**).
*   **Group sizes**: Include all elements extending beyond the frame in Figma.

Share
