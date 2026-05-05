# How To Use Bynder's AI-Powered Facial Recognition Feature – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/20530684581266

Summary[](https://support.bynder.com/hc/en-us/articles/20530684581266#h_01JW8D7JH6H8C2QX8FV0XM7QZ9)

----------------------------------------------------------------------------------------------------

Bynder's AI Facial Recognition feature automatically tags image assets by identifying faces, eliminating the need for extensive manual tagging. This allows for quick asset searches featuring pre-defined individuals. The faces are detected and indexed immediately after upload, and any previously uploaded assets are detected and indexed after the feature is enabled in your account.

Who?[](https://support.bynder.com/hc/en-us/articles/20530684581266#h_01JW8D7RVAWNFRJT8MHVQ0C2ZS)

-------------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once the feature is enabled users need the _edit assets_ permission to edit or delete the identified faces name.

Why?[](https://support.bynder.com/hc/en-us/articles/20530684581266#h_01JW8DDZXRVZDME3BNFMC9FWAG)

-------------------------------------------------------------------------------------------------

Upon upload users can tag an individual in an image, after this the individual the feature automatically tags them in new and existing assets, ensuring consistent and expedient tagging across your library.

Bynder's AI Facial Recognition feature simplifies managing employee headshots, models, and identifying event attendees.

How?[](https://support.bynder.com/hc/en-us/articles/20530684581266#h_01J5DR7Q43X3J25WA8MP19EGKX)

-------------------------------------------------------------------------------------------------

### Searching For A Person Using Face Recognition 

1.  Navigate to your **Assets**.
2.  Navigate to the search bar to **enter the name of the person** you're looking for. 
    *   Type the full name or part of it, or search for an "unnamed person" if they haven't been tagged with a specific name. Alternatively, if a smart filter has been configured, you can use it to refine your search.
        
        ![Screenshot 2024-08-16 at 10.51.26 AM.png](https://support.bynder.com/hc/article_attachments/26984912019986)
        
3.  Once you find an asset that contains the person’s face, select it.

(Optional) Navigate to the **AI** **Recognized** **Tags** section within the asset.

*   Select the **View** **All** **Assets** icon ![Screenshot 2024-08-16 at 10.52.24 AM.png](https://support.bynder.com/hc/article_attachments/26984910244882) next to the person's name.
    
    ![Screenshot 2024-08-16 at 10.53.05 AM.png](https://support.bynder.com/hc/article_attachments/26984912022034)
    
*   You'll be directed to a filtered view showing all the assets where this person's face appears.

_Note: Any permission restrictions set on an image asset will be honored and will affect if an image asset is retrievable using this feature._![Screenshot 2024-08-16 at 10.53.26 AM.png](https://support.bynder.com/hc/article_attachments/26984910247954)

_Note: The DAT derivate, a manual derivative, and default derivatives don’t suffice as an AI Search derivative. Get in touch with your Customer Success Contact as a new derivative may need to be generated to ensure that all assets are included for Bynder's AI tools._

4\. Alternatively users can see the person who is tagged in an asset by scrolling over the asset.

![Ideas _ Notepad - Frame 6.jpg](https://support.bynder.com/hc/article_attachments/28943868219922)

### Adding A Name

1\. Navigate to the asset you wish to add the name to. 

2\. Open the **AI-modal.**

3.Hover over the face you wish to tag, and click it to add the name. Alternatively, click the + icon from the list to add the name.

![Ideas _ Notepad - Frame 7.jpg](https://support.bynder.com/hc/article_attachments/28943812682002)

### Editing A Name

1.  Navigate to the asset you want to edit.
2.  Select the ![](https://support.bynder.com/hc/article_attachments/20794698436882) button next to the **AI-recognized.**![](https://support.bynder.com/hc/article_attachments/20794677917842)
3.  Select the ![](https://support.bynder.com/hc/article_attachments/20794677919634) button next to the name.![](https://support.bynder.com/hc/article_attachments/20794677921810)
4.  Select the ![](https://support.bynder.com/hc/article_attachments/20794698440722) button and start typing the correct name. 
5.  Press **Enter.**![](https://support.bynder.com/hc/article_attachments/20794677925522)

### Removing A Name

1.  Navigate to the asset you want to edit.
2.  Select the ![](https://support.bynder.com/hc/article_attachments/20794698436882) button next to **AI-recognized.**![](https://support.bynder.com/hc/article_attachments/20794677917842)
3.  Select the name and click the ![](https://support.bynder.com/hc/article_attachments/20794698444050) button.

_Note: When you remove the name, it will replace the name with the **unnamed person** tag, this cannot be removed._

Best Practices[](https://support.bynder.com/hc/en-us/articles/20530684581266#h_01J82T27M6NB1T7FAVDARCYHSD)

-----------------------------------------------------------------------------------------------------------

### Supported File Types

The feature works with original files in JPG or PNG format that are smaller than 15 MB in size. For other formats or files exceeding 15MB, at least one derivative less than 15MB must be available on the asset. 

### Create A Smart Filter 

We _highly_ recommend creating a new smart filter to make searching for the recognized person(s) easier for users. When the smartfilter is set we recommend using the _fa-group_ icon to allow the smartfilter to appear with a person-based icon. Enable the _multi filter_ setting so users can search multiple people. 

_Note: We suggest using our translation services to ensure that the_ **_people_** _smartfilter is in the correct language of the user._ ![](https://support.bynder.com/hc/article_attachments/20794698431250)

### Important Metaproperty Configuration Information

*   Once the feature is enabled in your portal, a new metaproperty with the name “**Recognized\_Face**” will be automatically created. 
*   This metaproperty is a **read-only** and **Multi-select** type. 
*   You _**should not**_ change this metaproperty to a **single** **select**, as it will disrupt the functionality.
*   It will not appear in the Upload or Edit screen (except for users with the Edit hidden metaproperties on assets _**and**_ edit assets permission enabled).
*   You can edit the **displayed** name of the metaproperty, which _does not_ affect the feature.
*   You _can_ customize the thumbnail of the metaproperty options. This allows you to show a thumbnail of the faces next to the names inside of the Smartfilter.
*   _**Do not delete**_ a name option from the metaproperty as this may cause issues with the feature. If you delete the name as a **metaproperty** **option,** it will remove the name from the smart filter but it will _**not**_ remove the face tag.

FAQs[](https://support.bynder.com/hc/en-us/articles/20530684581266#h_01J5DR7Q43RERD9N7GQV0D0R4K)

-------------------------------------------------------------------------------------------------

**Is there a character limit for names?**

Yes, there is a character limit of up to 150 characters (including white spaces). 

**Are celebrities automatically recognized and named?**

No, celebrities must be defined in the same way other faces are.

**Can I reuse any tagging I’ve done manually before this feature?**

There is no option to import such data in bulk. 

**How many faces can be identified in an image?** 

A maximum of 100 faces can be found in a single image.

**Can you have two names on one face?** 

No, you cannot.

Related Articles[](https://support.bynder.com/hc/en-us/articles/20530684581266#h_01JW8GMNK4S9DK39HNRG1WBGK6)

-------------------------------------------------------------------------------------------------------------

[Create Metaproperty Options](https://support.bynder.com/hc/en-us/articles/10341416276370)

[Use Filters to Search for Assets](https://support.bynder.com/hc/en-us/articles/360013870120)

[Create a New Smart Filter](https://support.bynder.com/hc/en-us/articles/360013931419)

[Understanding Supported File Types For Conversion And Derivative Creation](https://support.bynder.com/hc/en-us/articles/360013875220)

### _Level: Beginner_

Beginner-level articles are for everyone, these articles do not assume any prior Bynder knowledge. These articles are a great place to start your Bynder Journey.

Share
