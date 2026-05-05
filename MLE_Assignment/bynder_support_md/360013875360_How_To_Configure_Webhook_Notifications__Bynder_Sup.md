# How To Configure Webhook Notifications – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications

Summary [](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01JPQBRVE533SEC1GKRZZV3XK0)

------------------------------------------------------------------------------------------------------------------------------------------

Webhooks are a helpful tool to decrease extraneous API calls. Webhooks wait for an event before attempting to get the information from your API. Bynder utilizes Amazon Simple Notification Service (Amazon SNS) to send real-time alerts to your external systems. Because webhooks wait for an event to work they give real time responses to your server and allow for a faster processing time with less traffic. 

Who?[](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01JPQBRZ28Y078ASBW74JVS3P6)

--------------------------------------------------------------------------------------------------------------------------------------

This feature/solution is enabled by a Bynder Admin.

Why?[](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01JPQBS5CVCN8FZXZX41XZ4VD6)

--------------------------------------------------------------------------------------------------------------------------------------

Bynder allows users to have up to 10 webhooks by default, users can apply these webhooks to customize notifications for specific events. Consider using webhooks for a new asset upload, archival, or deletion. Each notification will include detailed information about the change in JSON, and can be used for verification through the API. Notification types vary by solutions enabled in Bynder. 

_Note: If you would like to request more than 10 webhook configurations please reach out to your Customer Success Contact._ 

How?[](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01JPQBS9F2QJQB32WK59VNN4BA)

--------------------------------------------------------------------------------------------------------------------------------------

Bynder supports standard SQS queues, SQS FIFO is not supported. We recommend adding a 2-5 second delay to the webhook before retrieving the asset data via the API.

### Navigating To Webhooks Settings

1.  Navigate to your **Portal** > **Advanced** **Settings** > **Portal Settings**.
2.  On the left-hand side, select **Webhooks**.
3.  Select **Configuring** **Webhooks** > **Configure** **New**.
4.  Add the **name** of the selected Webhook.
5.  Choose the desired protocol for receiving notifications, and follow those specific instructions below:

![](https://support.bynder.com/hc/article_attachments/20581921356690)[](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01J4J3XNAS7CE3M6D1MWJG8XQ1)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Configuring An Email Endpoint

1.  Name your **Connection.**
2.  Select **Email** or **Email**\-**JSON**  from the Protocol dropdown menu. **Email-JSON** will give you a JSON formatted response whereas **Email** will not.
3.  Input an email address to receive notifications. Make sure to check your spam folder for messages.
4.  Choose the events you want to track (e.g., created, updated, deleted). ![](https://support.bynder.com/hc/article_attachments/20581921359890)_Note: We are unable to create custom notification events._
5.  Click **Save**.
6.  Check your email for a confirmation notification from the endpoint.
7.  Confirm subscription in the body of the email.
8.  Once confirmed, refresh the page to ensure the setup is complete.

### Configuring An HTTP Or HTTPS Endpoint

1.  Name your **Connection.**
2.  Select **HTTP** or **HTTPS** from the Protocol dropdown menu.
3.  Put in your **HTTP** or **HTTPS** **endpoint**.
4.  Choose the events you want to track (e.g., creates, updates, and deletes).
5.  Select **Next** > **Configure**.
6.  Your endpoint should receive a **Subscription** **Verification** **message** containing a Subscription Verification URL link directly from AWS.
7.  Click the link/paste it into a browser window, this confirms the endpoint. 

_Note: You have 48 hours to confirm the endpoint before the URL expires. If that occurs, you will need to restart the setup._![](https://support.bynder.com/hc/article_attachments/20581917317266)

8\. If you don't get a Subscription Confirmation on your endpoint, please make sure it is set up correctly and that the correct HTTPS URL is present in the setup.

_Note: There is no way to re-send the Subscription Verification email, so you must delete the connection and set up a new one._

### Configuring An Amazon SQS Endpoint

1.  Name your **Connection.**
2.  Select **Amazon** **SQS** from the Protocol dropdown menu.
3.  Put in the **ARN** of your **SQS** queue and select Next.
4.  You will get a window with a Security Policy on the next screen. Add this security policy to your SQS queue to whitelist notifications from Bynder. When you add it to your SQS setup, the Resource section of the security policy should be replaced by your SQS queue name. Please do this step _**before**_ completing the setup in Bynder. The security policy must be in place on your SQS queue in order to receive the subscription confirmation message.
5.  Choose the events you want to track (e.g., creates, updates, and deletes).
6.  Select **Next** > **Configure**.
7.  Your SQS queue should receive a **Subscription** **Verification** message containing a Subscription Verification URL link. 

_Note: You have 48 hours to confirm the endpoint before the URL expires. If that occurs, you will need to restart the setup._

![](https://support.bynder.com/hc/article_attachments/20581917318546)

_Note: If you don't get a Subscription Confirmation on your endpoint, please ensure it is set up correctly and that the right SQS ARN is in the setup. There is no way to re-send the Subscription Verification email, so you must delete the connection and set up a new one after the 48 hour window passes._

### Editing, Deleting, or Disabling Your Webhook Connection

You cannot edit the HTTPS/HTTP, email, or SQS endpoints by clicking the Edit button; you need to create a new connection if you want to use a different endpoint.

1.  Navigate to your **Portal** > **Advanced** **Settings** > **Portal** **Settings**.
2.  On the left-hand side, select **Webhooks**.
3.  Select **Configuring** **Webhooks**.
4.  Navigate to the Webhook you want to edit, delete, or disable.
5.  Select **Edit**.  

### Notification Types

| SNS notification | Name |
| --- | --- |
| Media uploaded to Asset Bank.<br><br>This applies to each asset uploaded via the Mass Uploader | asset\_bank.media.create |
| New version uploaded to existing media or change of active version | asset\_bank.media.updated**\*** |
| Media set to archived | asset\_bank.media.archived**\*\*** |
| Media deleted | asset\_bank.media.deleted |
| Media metadata change (title, description, or any metaproperty change) | asset\_bank.media.meta\_updated**\*\*\*** |
| A New Asset Workflow job is created in the Portal or via the API | workflow. Job. create |
| SNS Notification - media set to be archived in X number of days | asset\_bank.media.pre\_archived |

\*asset\_bank.media.meta\_updated is sent when an asset is marked as archived.

\*\*asset\_bank.media.archived is sent when an asset is marked as archived.

\*\*\*asset\_bank.media.meta\_updated is sent when moving an archived asset from archive status to active.

**JSON Notification Example**

Below is an example of an 'asset\_bank.media.deleted' SNS notification in JSON.

{
        "media\_id": "29\*\*\*99D-BA27-\*\*\*B-94E0F070DA\*\*\*CAC",
        "media": {
                "userCreated": "Integrations Bynder",
                "limited": 0
                "watermarked": 0,
                "mediaItems": \[{\
                        "version": 1,\
                        "active": 1,\
                        "dateCreated": "2019-12-10T10:35:14Z",\
                        "fileName": null,\
                        "id": "141\*\*\*DD-E8C4-\*\*\*B-A4CC949B1E4E0F27",\
                        "size": 3824,\
                        "height": 19,\
                        "width": 24,\
                        "focusPoint": {\
                                "x": 12.0,\
                                "y": 9.5\
                        }\
                }, {\
                        "version": 1,\
                        "active": 1,\
                        "dateCreated": "2019-12-10T10:35:14Z",\
                        "fileName": null,\
                        "id": "D463\*\*\*C-EA27-4E9B-8B\*\*\*2309B62BE87",\
                        "size": 1670,\
                        "height": 19,\
                        "width": 24,\
                        "focusPoint": {\
                                "x": 12.0,\
                                "y": 9.5\
                        }\
                }\],
                "activeOriginalFocusPoint": {
                        "x": 12.0,
                        "y": 9.5
                },
                "archive": 0,
                "brandId": "8F7\*\*\*4F-\*\*\*8-4F32-902E2501A6433462",
                "copyright": "",
                "datePublished": "2019-12-10T10:35:13Z",
                "dateCreated": "2019-12-10T10:35:13Z",
                "description": "",
                "dateModified": "2020-02-07T16:30:16Z",
                "extension": \["png"\],
                "fileSize": 1670,
                "height": 19,
                "id": "29\*\*\*99D-BA27-\*\*\*B-94E0F070DA5DECAC",
                "idHash": "55261de977ff5163",
                "isPublic": 0,
                "name": "test",
                "orientation": "landscape",
                "tags": \[\],
                "type": "image",
                "width": 24,
                "property\_Country": \["France", "Germany", "Belgium"\]
        }
}

 [](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01K2PS6F0W6QG38RTABQY76R3R)

-----------------------------------------------------------------------------------------------------------------------------------

FAQs[](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01JPQAQERZBD7FSVBNZ5WS51J3)

--------------------------------------------------------------------------------------------------------------------------------------

**What if I want to create more than 10 webhooks?**

We can assist with this on a case by case basis.

**What system does Bynder use for webhooks?**

Amazon SNS is what Bynder uses for webhooks.

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013875360-How-To-Configure-Webhook-Notifications#h_01JPQAQMNPGX6QY26VBD2M4V5Y)

--------------------------------------------------------------------------------------------------------------------------------------------------

[Set Up Webhooks in Content Workflow for Notifications](https://support.bynder.com/hc/en-us/articles/19596398706322)

### _Level: Expert_

Expert-level articles are for users who have significant prior Bynder knowledge. These articles require you to know a lot of Bynder information and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
