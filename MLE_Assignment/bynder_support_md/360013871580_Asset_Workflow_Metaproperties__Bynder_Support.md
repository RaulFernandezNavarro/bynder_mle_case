# Asset Workflow Metaproperties – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013871580-Asset-Workflow-Metaproperties

There are two types of Asset Workflow Metaproperties.

Campaign metaproperties[](https://support.bynder.com/hc/en-us/articles/360013871580-Asset-Workflow-Metaproperties#h_01HKYDRWN8PQD2G03BF2M3C026)

------------------------------------------------------------------------------------------------------------------------------------------------

You can use campaign metaproperties to create recurring fields, which you can add to specific campaign presets. This could be useful if you often need to retrieve the same information in your Workflow Campaigns. For example, country and city information or the market your campaign is targeting.

You can also use these metaproperties to set up filters for your Asset Workflow overview screen.

### How to create a campaign metaproperty?

1.  Go to **Settings > Workflow > Metaproperty Management** and click **Campaign**.
    
2.  Click **Add metaproperty** to create a new campaign metaproperty.
    
3.  Select the type of field you want to use in the **Type** dropdown and enter a label for the field in the **Label** section. In the **Description** field, you can enter additional information. For certain field types, you may want to enter a question you would like your users to answer using the available options.
    

**Checkbox**

Select this type if you want users to tick one or more options. They can check or uncheck the available options.

![checkboxes.png](https://support.bynder.com/hc/article_attachments/10108180749842)

**Date**

This will display a date picker that users can use to select a date.

![date.png](https://support.bynder.com/hc/article_attachments/10108180803346)

**Input field**

If you choose this field any metaproperty options that do not exist will be created and mapped to the newly created option.

![Workflow_input_.png](https://support.bynder.com/hc/article_attachments/10108180858386)

**Multiselect**

This will display a searchable dropdown list allowing your users to select one or more options. In the **Options** section you can enter the values you want your users to choose from.

![multiselect.png](https://support.bynder.com/hc/article_attachments/10108177713298)

**Radio button**

This will display radio buttons. Radio buttons only allow one option to be selected. Since one of the available values always has to be selected, we advise using this type for required fields only. If the field is not required to fill in, make sure you add an N/A option, so users can leave the field unanswered.

![radio_button.png](https://support.bynder.com/hc/article_attachments/10108177766162)

**Selectbox**

This will display a searchable dropdown list allowing your users to select one of the available options. Unlike the multiselect dropdown, this type only allows you to select one option. In the **Options** section you can enter the values you want your users to choose from.

![selectbox.png](https://support.bynder.com/hc/article_attachments/10108181024530)

**Smart**

The smart type will generate a unique identifier for the campaign. You can use this identifier to make a reference to the campaign in one of your external systems. The unique identifier can be created by inputting data from your users and general information such as the creation date of the campaign. Follow the steps below to set up a smart option.

### Note

The unique identifier is generated based on the order of the smart elements. Make sure you add the elements in the right sequence.

1.  Make sure that the **Type** dropdown is set to **Smart**.
    
2.  Go to the **Smart options** section and click **Add part**.
    
3.  Click the **Type** dropdown and select **Selectbox** or **Smart**.
    
    **Selectbox**
    
    This will allow users to choose from certain options. The value assigned to the selected option will be used in the unique identifier. You could for example use a selectbox to let your users select a market for your product. If a user selects the market label "Europe", the value "EU" could be used as part of your unique identifier.
    
    **Smart**
    
    With smart data you can use portal data as components for your unique identifier.
    
    **Date: Day**
    
    This will look at the creation date of the campaign. The day of the month the campaign was created will be used as a numeric value in the unique identifier.
    
    **Date: Month**
    
    This will look at the creation date of the campaign. The month number will be used as a numeric value in the unique identifier.
    
    **Date: Year**
    
    This will look at the creation date of the campaign. The year will be used as a numeric value in the unique identifier.
    
    **Job: Numeric ID**
    
    Not supported for campaigns
    

**Text**

You can use this type to show text to your users. Enter the text you want to display in the **Description** field.

_Note: The character limit on a text box is 255 characters._

**Text area**

This will display a text field allowing your users to enter text.

_Note: Text area metaproperties cannot be searched in the overview page and do not appear in the job overview tab.The character limit on a text box is 255 characters._

**Asset Bank metaproperty**

With this type you can show an Asset Bank metaproperty. Click the dropdown and select the metaproperty that you would like to use.

4.  (Optional) Tick the **Always show this metaproperty when creating a Campaign** box if you want this metaproperty field to always populate when you create a new campaign that does not have a preset.
    
5.  (Optional) Tick the **Export to Bynder** checkbox if you want the input data of the metaproperty to be exported to an existing metaproperty. Enter the exact name of the existing Asset Bank metaproperty.
    
6.  (Optional) If you want to make this field required, tick the **This metaproperty is required** checkbox.
    
7.  (Optional) Tick the **Set character limits** box if you want to set up a minimum or maximum number of characters for your **Input field**, **Text,** or **Textarea** field. Users will get to see a warning message when their input does not match the criteria.
    
8.  (Optional) Tick the **Set selection limits** option if you want to regulate the minimum and maximum number of selections users can make in the **Multiselect** field. Users will get to see a warning message when their selection does not match the criteria.
    
9.  (Optional) if you want to make the field dependent on another campaign metaproperty, tick the **Visible based on other metaproperty** checkbox. Select the metaproperty you want to make it dependent on in the dropdown that appears.
    
10.  Click the **Save** button at the top of the metaproperty to save the new metaproperty.
    

### How to add campaign metaproperties to a campaign preset?

After you create your campaign metaproperties you can add them to a campaign preset. The metaproperties will be visible as fields in the popup that you get to see when creating a new campaign that is based on that preset. Adding campaign metaproperties can be useful if you often create new campaigns, where users need to fill in the same kind of information.

1.  Go to **Settings > Workflow > Preset Management** and click **Campaign**.
    
2.  Click **Add preset** or open one of the existing presets.
    
3.  Click the **Metaproperties** dropdown and select the campaign metaproperties you would like to add.
    
4.  Click **Save & close** to save the campaign preset.
    

### How to add a campaign metaproperty as a campaign filter?

Campaign filters are available on the campaign overview page and allow users to filter and find the campaigns they're looking for. For example, if your Workflow campaigns are tagged with countries, users can use the filter to search for the country they are looking for.

Campaign metaproperties of which the type is set to **Asset Bank metaproperty** can be used as campaign filters. After you've added this campaign metaproperty to a campaign preset, you can start creating campaign filters on the Smartfilter Management page of your portal. Follow the steps below.

### Note

Only campaign metaproperties of which the type is set to **Asset Bank metaproperty** can be used as campaign filters.

1.  Go to **Settings > Taxonomy > Smartfilter Management**.
    
2.  Add a new smart filter with the type **workflowcampaign** and use the input fields for the available portal languages to set up labels for the filter. [See this article for more instructions](https://support.bynder.com/hc/articles/360013931419#UUID-e1143b65-b79d-119b-c82b-84425854c7c1)
    .
    
3.  Click **Save** and you will be redirected to the Smartfilter Management overview page.
    
4.  Click the ![settings_menu.png](https://support.bynder.com/hc/article_attachments/10108181060882) icon of the smart filter you just created to further configure it.
    
5.  In the **Metaproperty** column, select the Asset Bank metaproperty that you want to use for the filter.
    

### Note

This should be the same Asset Bank metaproperty as you linked to the campaign metaproperty.

6.  Tick the **Show label** box, click the **+** icon to add the option, and click the **Save** button to save the new filter.
    

The campaign filter will now be available on the Asset Workflow campaign overview page. Users can use these filters to filter for the campaign they're looking for.

### How to remove campaign metaproperties from a campaign?

1.  Go to **Settings > Workflow > Preset Management** and click **Campaign**.
    
2.  Open the preset for which you want to remove campaign metaproperties.
    
3.  Go to the **Metaproperties** section, hover over the metaproperty you want to remove, and click the **X** icon to delete it.
    
4.  (Optional) Repeat the steps above to remove other metaproperties.
    

### How to delete campaign metaproperties?

1.  Go to **Settings > Workflow > Preset Management** and click **Campaign**.
    
2.  Look for the campaign metaproperty you want to delete and click the **Remove** button.
    
3.  Read the warning message in the popup and click the **Yes, remove** button if you wish to permanently remove the campaign metaproperty.
    
    ### Note
    
    This action is permanent and cannot be undone.
    
4.  (Optional) Repeat these steps if you want to remove more campaign metaproperties
    

Job metaproperties[](https://support.bynder.com/hc/en-us/articles/360013871580-Asset-Workflow-Metaproperties#h_01HKYDRWN9TCEB4PAPQCQFFNM4)

-------------------------------------------------------------------------------------------------------------------------------------------

Job metaproperties allow you to create fields. You can use these forms to create fields for your Asset Workflow presets.

### How to create a job metaproperty?

1.  Go to **Settings > Workflow > Metaproperty Management** and click **Job**.
    
2.  Click **Add metaproperty** to create a new campaign metaproperty.
    
3.  Select the type of field you want to use in the **Type** dropdown and enter a label for the field in the **Label** section. In the **Description** field, you can enter additional information. For certain field types, you may want to enter a question you would like your users to answer using the available options.
    

**Checkbox**

Select this type if you want users to tick one or more options. They can check or uncheck the available options.

![checkboxes.png](https://support.bynder.com/hc/article_attachments/10108180749842)

**Date**

This will display a date picker that users can use to select a date.

![date.png](https://support.bynder.com/hc/article_attachments/10108180803346)

**Input field**

![input_field.png](https://support.bynder.com/hc/article_attachments/10108181146130)

**Multiselect**

This will display a searchable dropdown list allowing your users to select one or more options. In the **Options** section you can enter the values you want your users to choose from.

![multiselect.png](https://support.bynder.com/hc/article_attachments/10108177713298)

**Radio button**

This will display radio buttons. Radio buttons only allow one option to be selected. Since one of the available values always has to be selected, we advise using this type for required fields only. If the field is not required to fill in, make sure you add an N/A option, so users can leave the field unanswered.

![radio_button.png](https://support.bynder.com/hc/article_attachments/10108177766162)

**Selectbox**

This will display a searchable dropdown list allowing your users to select one of the available options. Unlike the multiselect dropdown, this type only allows you to select one option. In the **Options** section you can enter the values you want your users to choose from.

![selectbox.png](https://support.bynder.com/hc/article_attachments/10108181024530)

**Smart**

The smart type will generate a unique identifier for the campaign. You can use this identifier to make a reference to the campaign in one of your external systems. The unique identifier can be created by inputting data from your users and general information such as the creation date of the campaign. Follow the steps below to set up a smart option.

### Note

The unique identifier is generated based on the order of the smart elements. Make sure you add the elements in the right sequence.

1.  Make sure that the **Type** dropdown is set to **Smart**.
    
2.  Go to the **Smart options** section and click **Add part**.
    
3.  Click the **Type** dropdown and select **Selectbox** or **Smart**.
    
    **Selectbox**
    
    This will allow users to choose from certain options. The value assigned to the selected option will be used in the unique identifier. You could for example use a selectbox to let your users select a market for your product. If a user selects the market label "Europe", the value "EU" could be used as part of your unique identifier.
    
    **Smart**
    
    With smart data you can use portal data as components for your unique identifier.
    
    **Date: Day**
    
    This will look at the creation date of the campaign. The day of the month the campaign was created will be used as a numeric value in the unique identifier.
    
    **Date: Month**
    
    This will look at the creation date of the campaign. The month number will be used as a numeric value in the unique identifier.
    
    **Date: Year**
    
    This will look at the creation date of the campaign. The year will be used as a numeric value in the unique identifier.
    
    **Job: Numeric ID**
    
    This will use the numbers of the job ID and use them as a component for the unique identifier.
    

**Text**

You can use this type to show text to your users. Enter the text you want to display in the **Description** field.

**Textarea**

This will display a text field allowing your users to enter text.

**Asset Bank metaproperty**

With this type you can show an Asset Bank metaproperty. Click the dropdown and select the metaproperty that you would like to use.

4.  (Optional) Tick the **Always show this metaproperty when creating a Campaign** box if you want this metaproperty field to always populate when you create a new campaign that does not have a preset.
    
5.  (Optional) Tick the **Export to Bynder** checkbox if you want the input data of the metaproperty to be exported to an existing metaproperty. Enter the exact name of the existing Asset Bank metaproperty.
    
6.  (Optional) If you want to make this field required, tick the **This metaproperty is required** checkbox.
    
7.  (Optional) Tick the **Set character limits** box if you want to set up a minimum or maximum number of characters for your **Input field**, **Text,** or **Textarea** field. Users will get to see a warning message when their input does not match the criteria.
    
8.  (Optional) Tick the **Set selection limits** option if you want to regulate the minimum and maximum number of selections users can make in the **Multiselect** field. Users will get to see a warning message when their selection does not match the criteria.
    
9.  (Optional) if you want to make the field dependent on another campaign metaproperty, tick the **Visible based on other metaproperty** checkbox. Select the metaproperty you want to make it dependent on in the dropdown that appears.
    
10.  Click the **Save** button at the top of the metaproperty to save the new metaproperty.
    

### How to add job metaproperties to a job preset?

1.  Go to **Settings > Workflow > Preset Management** and click **Job**.
    
2.  Click **Add preset** or open one of the existing presets.
    
3.  There are two ways you can add job metaproperties to a job preset. You can add them to the popup users get to see when they start a new job or you can add them on a stage level.
    

**Popup**

1.  Scroll down to the **Metaproperties** section at the bottom of the preset page and click the dropdown.
    
2.  Enter the name of the metaproperty you want to add and click the item to add it.
    
3.  (Optional) Repeat the step above to add other metaproperties.
    
    **Stage level**
    
    By combining and adding job metaproperties to a specific stage you can create forms, which help you to get the information you need from your users. Follow the steps below.
    
    **Read-only metaproperties**
    
    These read-only fields will show information that was filled in by a user at a previous stage. You can, for example, add a read-only metaproperty in the second and third stages to display the information that was filled in by a user in the first stage. This way, other users can still see and use the information filled in during previous stages. Read-only metaproperties cannot be changed
    
    **Editable metaproperties**
    
    This will add editable fields that users can use to fill in the required information. You can add these metaproperties to stages where you want your users to fill in the information. Use read-only metaproperties in other stages to show the information that was entered during previous stages.
    
4.  Click **Save & close** or **Save** to save the changes.
    

### How to remove job metaproperties from a job preset?

1.  Go to **Settings > Workflow > Preset Management** and click **Job**.
    
2.  Open the preset for which you want to remove job metaproperties.
    
    **Pop up**
    
    Scroll down to the **Metaproperties** section at the bottom of the page, hover over the metaproperty you want to remove, and click the **X** icon to delete it.
    
    **Stage level**
    
    Scroll to the **Form** stage where you want to remove metaproperties.
    
    In the **Read-only metaproperties** or **Editable metaproperties** field, hover over the metaproperty you want to remove and click the **X** icon to delete it
    
3.  (Optional) Repeat the second step if you want to delete more job metaproperties.
    
4.  Click **Save & close** or **Save** to save the changes.
    

### How to delete job metaproperties?

1.  Go to **Settings > Workflow > Preset Management** and click **Job**.
    
2.  Look for the job metaproperty you want to delete and click the **Remove** button.
    
3.  Read the warning message in the popup and click the **Yes, remove** button if you wish to permanently remove the job metaproperty.
    
    ### Note
    
    This action is permanent and cannot be undone.
    
4.  (Optional) Repeat these steps if you want to remove more job metaproperties.
    

Share
