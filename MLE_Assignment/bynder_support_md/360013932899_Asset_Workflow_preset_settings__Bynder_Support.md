# Asset Workflow preset settings – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013932899-Asset-Workflow-preset-settings

If a user wants to start a new workflow in Asset Workflow, they can select a preset. A preset helps to create jobs more quickly. Presets generally have predefined approvers and stages and can indicate if templates should be used for creating assets.

Learn more about Asset Workflow [here](https://support.bynder.com/hc/articles/360013932859#UUID-bd14377e-5d28-120c-acd1-4340abbcce5d "Creative Workflow")
.

Who can manage presets?[](https://support.bynder.com/hc/en-us/articles/360013932899-Asset-Workflow-preset-settings#h_01HKXHTGNKV3TMZN1P9ZNY6WSF)

-------------------------------------------------------------------------------------------------------------------------------------------------

How to create or edit a preset[](https://support.bynder.com/hc/en-us/articles/360013932899-Asset-Workflow-preset-settings#h_01HKXHTGNKN5ZGB1BT74V5Z9Y1)

--------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Navigate to **Settings** > **Workflow** > **Preset** Management
    
2.  Here, you will find a list of all the presets in the account.
    
3.  To edit an existing preset, click **Preset** **Name**. To add a new preset, click **Add Preset.**
    

**Preset Name**

The **Name** of the preset

**Campaign**

The **Campaign** associated with the preset. You can consider campaigns as buckets for your Workflow Jobs - a way to organize jobs into different buckets (similar to folders).

**Accountable**

The **Accountable** user is the user who was kicked off the job and is accountable for the job as a whole.

**When a job is completed, submit assets to:**

Submit assets to either the Asset Bank or the [Waiting Room.](https://support.bynder.com/hc/articles/360013870280#UUID-2a8284e9-a547-2f1a-533c-a26060b81762)

**Use own templates**

They are used when you use the Print Templates solution and want users to be able to edit Templates and send them for approval.

**Export assets automatically**

Assets are automatically exported to the Asset Bank once the job is finished when they have the _In Review_ or _Approved_ status. Assets with the _rejected_ status will not automatically export to the Asset Bank.

**The job description is required.**

Adding a **Description** will be required each time a job is kicked off.

**Hide accountable**

Users will not see the user or group accountable when creating jobs based on this preset.

**Hide attachments**

Disables the ability to add attachments.

**Hide deadline**

Hide the deadline date from users.

**Hide description**

Hide the description field from users.

**Hide sidebar**

Hides the sidebar with attachments and project information.

**Hide stages**

Hides the navigation bar with stages within the job.

**Enable reorder**

This time-saving feature allows users to reuse the Workflow job they created. When reordering, the job will start in the stage marked as the start stage for reordering. Any filled-in information or created Print  Templates will be copied to the new job. Users can make the necessary modifications without having to start from scratch.

**Enable start date**

Allows users to set a future start date for the job.

**Disable annotations on assets**

Disable the ability for users to [annotate](https://support.bynder.com/hc/articles/360013871560#UUID-e8a42c90-2f7b-a633-9e7c-399f81214e3e "Workflow annotations")
 assets.

**Disable asset editing**

Disable the ability for users to edit assets in created Print templates.

**Disable comments**

Disable the ability for users to comment on assets.

**Disable reopening**

Disable the ability for users to reopen a job after it is finished.

**Only allow removing assets when they have no comments or annotations**

When this setting is enabled, assets can only be removed when they have no comments or annotations

**Disable asset download for profiles**

Allows you to determine which permission profiles cannot download assets from within a non-download stage. When checked, you can set up the profiles in the **Disable asset download for profiles** section in the top right corner of the Edit preset section. Any users added to **Disable** **asset** **download** **for** **profiles** will still be able to download assets in any stage marked as a download stage.

**Use Brandstore approval flow.**

Discontinued setting

**Preselect approved assets when exporting.**

When submitting assets to the Asset Bank, the assets that have been approved are preselected. Non-approved or rejected assets are not selected.

**Public job**

Discontinued setting

**When a job is completed, submit the assets**

Allows assets to be automatically sent to the waiting room or Asset Bank when a job is finished.

**Use in calendar**

Discontinued setting

**Enable commenting by replying to system emails**

Allows users to comment on a job by replying to the [Asset Workflow email](https://support.bynder.com/hc/articles/360013933059#UUID-d5c21132-ea2d-87ee-a1aa-da17475b066c "Workflow emails")
 they received. Learn more about Workflow emails and [Reply to emails to add a comment to workflow.](https://support.bynder.com/hc/articles/360013871500#UUID-0f9d8b0c-64ac-0660-2d54-7bfcda236e2d "Reply to email to add a comment in workflow")

**Always add a list of job assets and download links to job emails**

All notification emails will include a download link to the job asset(s).

**In job-related emails, always add a list of download links to attachments**

All notification emails will include a download link to the job attachment(s).

**Remove links to job from workflow emails**

Removes the link to the job from workflow emails.

**Use Bynder metaproperties**

Discontinued setting

**Pre-fill selected group or user to view private messages**

Allows you to set up which preselected user groups can see private messages. When users write a private message, the configured group(s) will be preselected in the **Only** **visible** for the box.

**Add job to exported assets using "Workflow link" metaproperty**

Includes the job [link from which the asset](https://support.bynder.com/hc/en-us/articles/360013871440-Link-assets-to-workflow-jobs)
 was exported in a metaproperty on the asset in the DAM.

**Use the filename as a title when exporting assets**

Use the filename as the title after exporting assets.

#### Stage Type

Select one of the following stage types:

**Default**

When creating a preset, the stage type is automatically set to **default**. You can use this stage type when you want to use the stage for asset uploading and tasks.

**Template**

Allows users to create their print Template from the preselected templates.

**Form**

[Workflow metaproperties](https://support.bynder.com/hc/en-us/articles/360013871580-Workflow-metaproperties)
 can be selected in this stage and populated as form fields.

**Approval**

Generates and shows an approval code when the approval stage is submitted to the next stage.

### Note

Do not use multiple approval stages in a workflow preset.

**Download**

Use this stage type for centralizing downloads. A download button will be shown below each thumbnail, allowing users to download the asset with one click.

When selecting this stage type, any user who was added to the **Disable** **asset** **download** **for** **profiles** setting will be able to download in this stage.

### Note

In the download stage, only approved assets can be downloaded.

**Collection**

Discontinued feature 

**Default assets filter**

By default, users will see all assets in the stage. This option allows you to set the open, awaiting, approved, or rejected view as the default filter.

**Editable by**

Allows you to set up who can edit this stage. Select **All** if all users with the edit stage permission should be able to edit. Select the **stage responsible** if only the users responsible for it can modify it. Choose **stage** **responsibility** & **job** **accountability. If** the job is accountable, you should also be allowed to edit this stage. Learn more about a[ssigning edit rights to stages.](https://support.bynder.com/hc/en-us/articles/360013871420-Assign-edit-rights-to-stages)

**Responsible**

Set which user or Workflow user group is responsible for the stage.

**Let the user choose responsibly.**

The user responsible for this stage can choose the user responsible for the next stage.

### Note

Don't allow users to set themselves as responsible. The user cannot choose themselves as responsible for the next stage.

**Restrict choice to a selected group.**

Only users in the selected Workflow group can be set as **stage** **responsible**.

**Allow inviting new users.**

When submitting the job to the next stage, users can set an external person as the **stage** **responsible**. This person will receive an invite by email with instructions to register for an account. When enabling this option, use the **Profile** **for** **Invited Users** dropdown to set which permission profile the invited users should be added to.

**Let the user choose a deadline.**

The user can choose the deadline for the next stage.

**Description**

You can add a description to explain to the user what they are expected to do at this stage. By default, a text preview of 232 characters is visible on the stage, and the rest is truncated. Users can click **Show** **More** to see the full text. Check the stage setting. **Show** a **full** **description** if you want the full text displayed by default.

**Start the job at this stage when reordering.**

When users reorder, a new Asset Workflow job will be created, and they will start at this stage. Any previous stage(s) are automatically skipped.

**Enable approval**

Allows users to approve or reject assets on an asset level within a stage. Users need permission **to approve** **assets** to approve or reject Asset Workflow assets.

### Note

Selecting this will not automatically generate an approval code; you need to mark the stage type as approval.

**Enable time booking**

Discontinued feature

**Enable asset upload**

Allow the upload of the asset(s) during a stage.

### Note

This must also be selected if you wish to upload a template.

**Upload assets automatically**

This allows assets to be uploaded automatically. By default, assets are not uploaded automatically after selecting them, and users have to click the **Upload** **all** **Assets** button to initiate the upload.

**Make asset upload required.**

This will require the stage responsible(s) to upload an asset before the job can be submitted to the next stage. If no asset is uploaded, users will receive a pop-up warning message asking them to upload one or more assets before submitting the job to the next stage.

**Choose responsible when creating the job.**

Allows the user to choose who is responsible for this stage when creating a job.

**Choose a deadline when creating the job**

Allows the user to choose the deadline for this stage when creating a job.

**Allow downloading the original version of watermarked assets**

Allows users to download watermarked assets in this stage. The watermarked assets are sent to an Asset Workflow job when using an Approval Workflow. With this option, users can download the watermarked material at this stage without waiting for the job to finish. Learn more about [download approval workflows](https://support.bynder.com/hc/en-us/articles/360017349119-Download-approval-workflows#UUID-50014b87-5942-d103-758b-b47667ea19eb_section-idm4480052158577631552266400823)

**Show full description**

Displays the complete description instead of the short preview of 232 characters.

**Enable tasks**

Enable tasks for this stage. Tasks can be set up in the Tasks section at the bottom of the stage settings.

**Disable notifications**

Allows you to disable specific email notifications from being sent out for this stage. When checked, you can select the notifications you want to disable in the **Disabled** **notifications** dropdown. Learn more about [Workflow notifications](https://support.bynder.com/hc/en-us/articles/360015293600-Notifications)
.

**Use custom search string for Asset bank import dialog**

You can use the custom search string to narrow down the assets the users can choose from when they add assets from the Asset Bank to the stage. When checked, you can enter your search string in the Search string field that appears.

**Use custom action labels.**

It allows you to custom-translate the Send labels **to the previous stage** and **Submit to the following stage** buttons.

**Use custom actions**

Allows you to set up custom action buttons for moving forward and backward to/from stages.

**Tasks**

It allows you to add tasks within a stage that you can assign on the fly or templatize a user or group to be responsible. You can choose a deadline for the Task, **Mark the task as necessary**, and Mark the task as required. Learn more about [Asset Workflow tasks.](https://support.bynder.com/hc/en-us/articles/360015349980-Creative-Workflow-tasks)

General Preset Settings[](https://support.bynder.com/hc/en-us/articles/360013932899-Asset-Workflow-preset-settings#h_01HKXHTGNM20VP1D792NYCX7R2)

-------------------------------------------------------------------------------------------------------------------------------------------------

**Attachments**

You can drag and drop files here that you want to add as an attachment to each job by default.

**Metaproperties**

Here, you can add Asset Workflow metaproperties. When creating a new job, these metaproperties will be displayed in the **Additional** **Information** section of the submission form for reference throughout the job.

**Enable for profiles**

Allows you to configure which permission profiles can kick off a job from this preset. Only users with permission profiles listed here can create a job based on this preset.

*   Only regular users and those above can utilize the workflow solution.
    

**Enable for groups**

Allows you to configure which user groups can kick off a job from this preset.

Only users with permission profiles listed here can create a job based on this preset.

**Custom form labels**

It allows you to set up custom form labels to display another label for the job name and description field.

Saving Options[](https://support.bynder.com/hc/en-us/articles/360013932899-Asset-Workflow-preset-settings#h_01HKXHTGNMPNPHW8PSV7Z6H41R)

----------------------------------------------------------------------------------------------------------------------------------------

There are different ways of saving a preset:

*   **Save** - simply saves the job while staying in the preset editor
    
*   **Save & Close** - saves the job and exits back to Preset Management
    
*   **Save as new** - saves as a new copy
    
    ### Note
    
    When updating and saving a preset, the changes will apply only to future jobs created with the preset, not to existing jobs already using it.
    

Share
