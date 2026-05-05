# Notification Types in Your Portal – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360015293600-Notification-Types-in-Your-Portal

You can manage your notifications in the [Notifications Center.](https://support.bynder.com/hc/en-us/articles/360013875280)
 [Below](https://support.bynder.com/hc/en-us/articles/360015293600-Notification-Types-in-Your-Portal#h_01HNGAKE21BYV2QY9GQ1NQSK21)
 is a breakdown of the types of notifications you can set up for your users and the requirements to enable them: [In-app](https://support.bynder.com/hc/en-us/articles/360013875280)
, [Email](https://support.bynder.com/hc/en-us/articles/16741097994258)
, and [SNS](https://support.bynder.com/hc/en-us/articles/360013875360)
 notifications.

### Note

The information below applies to the latest version of our [Notification Center](https://support.bynder.com/hc/articles/360013875280#UUID-7e182c15-f518-c468-3327-12c323ef0345 "Notification Center")
. Contact your Customer Success Contact if your version of the notification center looks different to discuss updating your portal to the latest version.

Notification Types & Requirements[](https://support.bynder.com/hc/en-us/articles/360015293600-Notification-Types-in-Your-Portal#h_01HNGAKE21BYV2QY9GQ1NQSK21)

--------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Asset Bank** | **In-app notification** | **Email notification** | **SNS notification** | **Recipients** | **Requirements** |
| New asset upload |     |     | ✅**\*** |     | \* Requires [new asset notification](https://support.bynder.com/hc/articles/360013875280#UUID-7e182c15-f518-c468-3327-12c323ef0345_section-idm2318477753031 "Notifications for new asset uploads, updated asset metadata and deleted assets")<br> and [SNS notifications](https://support.bynder.com/hc/articles/360013875360#UUID-0f95d85c-0a6d-a85e-458b-108a6fec26d5 "SNS Notifications") |
| The new version was uploaded to an existing asset | ✅**\*** |     | ✅**\*\*** | Users who downloaded the asset before | \* Requires [new version update notification](https://support.bynder.com/hc/articles/360013875280#UUID-7e182c15-f518-c468-3327-12c323ef0345_section-idm231847728500785 "Notifications for new version uploads")<br>.<br><br>\*\* Requires [SNS notifications](https://support.bynder.com/hc/articles/360013875360#UUID-0f95d85c-0a6d-a85e-458b-108a6fec26d5 "SNS Notifications") |
| Upload request | ✅   | ✅**\*** |     | *   Users who have the **Audit uploaded media for this option** right set on the metaproperty option level<br>    <br>*   Users who have the **Audit media in the waiting room** enabled for their permission profile. | \* Only users configured as auditors on the metaproperty option can receive an email notification. Additional configuration is required. Read more about it [here](https://support.bynder.com/hc/articles/360013870280#UUID-2a8284e9-a547-2f1a-533c-a26060b81762)<br>.<br><br>Users with general audit rights will not receive an email notification |
| Download request | ✅   | ✅**\*** |     | *   Users who have the **Audit download requests for this option** right set on the metaproperty option level<br>    <br>*   Users who have the **Audit media in the waiting room** enabled for their permission profile. | \* Only users configured as auditors on the metaproperty option can receive an email notification. Additional configuration is required. Read more about it [here](https://support.bynder.com/hc/articles/360013870280#UUID-2a8284e9-a547-2f1a-533c-a26060b81762)<br>.<br><br>Users with general audit rights will not receive an email notification |
| The asset has been archived | ✅**\*** |     | ✅**\*\*** | Users who have downloaded the asset before | \* Requires [archive asset notification](https://support.bynder.com/hc/articles/360013875280#UUID-7e182c15-f518-c468-3327-12c323ef0345_section-idm231847755538131 "Notifications for archived assets")<br><br>\*\* Requires [SNS notifications](https://support.bynder.com/hc/articles/360013875360#UUID-0f95d85c-0a6d-a85e-458b-108a6fec26d5 "SNS Notifications") |
| The asset will be archived in the future | ✅**\*** |     |     | Users who have downloaded the asset before | \* Requires [archive asset notification](https://support.bynder.com/hc/articles/360013875280#UUID-7e182c15-f518-c468-3327-12c323ef0345_section-idm231847755538131 "Notifications for archived assets") |
| Asset removal |     |     | ✅**\*** | Users who have downloaded or shared the asset before | \* Requires [removal of asset notification](https://support.bynder.com/hc/articles/360013875280#UUID-7e182c15-f518-c468-3327-12c323ef0345_section-idm231847755538131 "Notifications for archived assets")<br> and [SNS notifications](https://support.bynder.com/hc/articles/360013875360#UUID-0f95d85c-0a6d-a85e-458b-108a6fec26d5 "SNS Notifications") |
| Asset share |     | ✅   |     | The user(s) the assets are shared with |     |
| Saved filter share |     | ✅   |     | The user(s) the saved filter is shared with |     |
| **Waiting Room** | **In-app notification** | **Email notification** | **SNS notification** | **Recipients** | **Requirements** |
| Asset waiting for approval/ rejection |     | ✅   |     |     |     |
| **Bynder Express** | **In-app notification** | **Email notification** | **SNS notification** | **Recipients** | **Requirements** |
| Bynder Express email share |     | ✅   |     | *   The user who shared the share will receive a confirmation email<br>    <br>*   The recipient(s) of the share will receive an email to download the share |     |
| **Change History** | **In-app notification** | **Email notification** | **SNS notification** | **Recipients** | **Requirements** |
| Change History CSV file is ready. | ✅   |     |     | The user who requested the CSV file |     |
| **Asset Workflow** | **In-app notification** | **Email notification** | **SNS notification** | **Recipients** | **Requirements** |
| New job creation |     | ✅   | ✅   | The user(s) responsible for the first stage |     |
| Job submitted to next stage |     | ✅   |     | *   The accountable(s) of the job<br>    <br>*   The responsible user(s) of the current stage<br>    <br>*   The responsible user(s) of the stage the job is submitted to |     |
| Job submitted to the previous stage |     | ✅   |     | *   The accountable(s) of the job<br>    <br>*   The responsible user(s) of the current stage<br>    <br>*   The responsible user(s) of the previous stage of the job is submitted to |     |
| Workflow completion |     | ✅   |     | *   The accountable(s) of the job<br>    <br>*   The responsible user(s) of the final stage |     |
| New comment |     | ✅   |     | *   The accountable(s) of the job<br>    <br>*   The responsible user(s) of the active stage |     |
| New comment with the user tag |     | ✅   |     | *   The accountable(s) of the job<br>    <br>*   The responsible user(s) of the active stage<br>    <br>*   The user who is tagged in the comment |     |
| Reply to message |     | ✅   |     | The user(s) participating in the message thread |     |
| New private message |     | ✅   |     | The user(s) the private message is intended for |     |
| Reply to private message. |     | ✅   |     | The user(s) participating in the private message thread. |     |
| External server removal |     | ✅   | ✅**\*** |     | An external mailing server needs to be configured<br><br>\* Requires [SNS notifications](https://support.bynder.com/hc/articles/360013875360#UUID-0f95d85c-0a6d-a85e-458b-108a6fec26d5 "SNS Notifications") |
| **External Uploader** | **In-app notification** | **Email notification** | **SNS notification** | **Recipients** | **Requirements** |
| New upload | ✅   | ✅   |     | *   All users with the right to audit media in the Waiting Room will receive an in-app notification.<br>    <br>*   Email confirmation of a successful upload will be sent to the person who uploaded the files. |     |
| **User management** | **In-app notification** | **Email notification** | **SNS notification** | **Recipients** | **Requirements** |
| A new user account was created. |     | ✅**\*** |     | The user the account is created for | \* The **Send email notification** option needs to be enabled in the **Add New User** screen |
| User account removal |     | ✅   |     | The user whose account has been removed |     |
| CSV export |     | ✅   |     | The user who requested the CSV export |     |

Share
