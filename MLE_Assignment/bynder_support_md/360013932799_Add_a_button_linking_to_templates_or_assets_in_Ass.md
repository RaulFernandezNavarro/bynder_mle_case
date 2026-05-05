# Add a button linking to templates or assets in Asset Workflow – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013932799-Add-a-button-linking-to-templates-or-assets-in-Asset-Workflow

To help users quickly link to a guidelines page or, to select the right template for their campaign, Bynder can create a button in a workflow job linking to any page, image, or template. The button can be configured to only display if specific metaproperties have been filled in.

### Try it

1.  Go to **Settings > Taxonomy > Metaproperties management** and create a new metaproperty.
    
2.  Map this metaproperty onto a workflow metaproperty. Go to **Settings > Workflow > Metaproperties Management**.
    
3.  Click **\+ Add metaproperty**.
    
4.  In the **Type** dropdown, select **Asset Library metaproperty**. Next, select the button metaproperty you have created.
    
5.  Go to **Settings > Workflow > Preset Management > Job**.
    
6.  Create a new preset.
    
7.  In the **Stage** section, select **Form** in the **Type** dropdown.
    
8.  In the **Form** dropdown, select **Metaproperties**.
    
    ![form-option-preset.png](https://support.bynder.com/hc/article_attachments/10108140697490)
    
9.  Click in the **Editable metaproperties** section and select the metaproperty you created.
    
10.  In the **Attachment** section, add the created metaproperty to the **Metaproperties section**.
    

Now, when you create a job based on the preset you've created in step 8, the button appears in the form section of the workflow job.

If you want to make the button display only when a certain option is selected in the form, you need to make this metaproperty dependent on another metaproperty.

To create this dependency, create another metaproperty, for example:

![dependency-workflow.png](https://support.bynder.com/hc/article_attachments/10108140757906)

If your button should display based on, for example, user selecting the LinkedIn channel, then open the button metaproperty in **Settings > Workflow > Metaproperties Management** and select **Visible based on other metaproperty**, and select the option that should trigger the button. For example,

![workflow-dependency.png](https://support.bynder.com/hc/article_attachments/10108140807698)

### Learn more

*   [Manage metaproperties](https://support.bynder.com/hc/articles/360013872780#UUID-c8948609-a4fa-7eec-44fa-f6e9d98e5a47)
    
*   [Add Asset Library metaproperties to assets exported from workflow](https://support.bynder.com/hc/articles/360013932819#UUID-403827d4-f4cf-5888-f630-13861926cb8a "Add Asset Bank metaproperties to assets exported from workflow")
    

Share
