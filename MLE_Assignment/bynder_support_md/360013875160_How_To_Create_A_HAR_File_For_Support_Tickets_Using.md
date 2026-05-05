# How To Create A HAR File For Support Tickets Using Google Chrome – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/360013875160

Summary[](https://support.bynder.com/hc/en-us/articles/360013875160#h_01JJV7H31QAY696K4V22DQSM57)

--------------------------------------------------------------------------------------------------

If you encounter an issue and need assistance from Bynder Support, you may be asked to provide a HAR file and the log file from your browser's console for investigation. This guide will explain how to accomplish this task.

Who?[](https://support.bynder.com/hc/en-us/articles/360013875160#h_01JJV7KYYA45WKCJ3EF8RFYDYZ)

-----------------------------------------------------------------------------------------------

This is not a Bynder feature, but a feature of your browser, therefore anyone can create a HAR file and log. 

Why?[](https://support.bynder.com/hc/en-us/articles/360013875160#h_01JJV7M76KFDGARQFXW5AXD2C7)

-----------------------------------------------------------------------------------------------

A HAR file, which stands for "HTTP Archive" file, is a format used to store detailed information about all network interactions between a web browser and a website. HAR files allow Bynder Support to analyze and troubleshoot performance issues. 

How?[](https://support.bynder.com/hc/en-us/articles/360013875160#h_01HVVNAGJC6MPH9FX4P4FHYB3F)

-----------------------------------------------------------------------------------------------

Start by opening Chrome, and navigate to the Bynder page where you encountered the issue.

Click the ![vertical_menu.png](https://support.bynder.com/hc/article_attachments/10640501763346) button to open the Chrome menu and go to **More Tools > Developer Tools**.

![Screenshot 2025-01-30 at 10.18.42.png](https://support.bynder.com/hc/article_attachments/24305323571858)

Alternatively, you can right-click anywhere on the page and click the **Inspect** option.

![Screenshot 2025-01-30 at 10.39.33.png](https://support.bynder.com/hc/article_attachments/24305276804626)

The Developer Tools will open as a side panel or at the bottom of the page. Click the **Network** tab.

Make sure the ![record_button_console.png](https://support.bynder.com/hc/article_attachments/10640501785106) record button in the top left corner of the Developer Tools is red, which means it is recording. If the button is grey, click it to start recording.

Select and enable **Preserve log** to prevent the log from being cleared when you refresh the page.

Click the ![no entry icon.png](https://support.bynder.com/hc/article_attachments/25778939107730) icon to clean the page before refreshing the page.

Refresh the page and reproduce the issue you encountered before (make sure that the **Network** tab is still open).

After you have captured the issue, save the network calls of the activity that you have recorded on your machine by clicking the "Export HAR" button.   
![Screenshot 2024-10-25 at 14.59.06.png](https://support.bynder.com/hc/article_attachments/22312843513106)

Open the **Console** tab to save the console's output; right-click within the tab and click **Save as** to save the log file on your machine.

Send the HAR and Log file to the Support team via your open ticket.

_Tip: We recommend you permanently delete the file when you no longer need it to protect your personal data._

**Record and Share HAR Files With Caution**

*   When you retrieve a HAR file, all the internet traffic from that browser tab is captured. This also includes cookies and sensitive data, such as personal data, payment information, and/or passwords.
*   Anyone with access to you HAR file can view this data and use it to impersonate your account(s).
*   Record and share a HAR file with caution and avoid capturing sensitive data.

 [](https://support.bynder.com/hc/en-us/articles/360013875160#h_01JQX98HPA68G1XCGDY1P9Q8G7)

--------------------------------------------------------------------------------------------

FAQs[](https://support.bynder.com/hc/en-us/articles/360013875160#h_01JJV96ABYNB04T9ERZCN200MK)

-----------------------------------------------------------------------------------------------

**If this has personal data is it the best option?**

Yes, Bynder support will only use the necessary information from the log and HAR file to assist in fixing the issue you are facing. 

 [](https://support.bynder.com/hc/en-us/articles/360013875160#h_01JQX98HPAFTS0HFTQKFFRN151)

--------------------------------------------------------------------------------------------

Related Articles[](https://support.bynder.com/hc/en-us/articles/360013875160#h_01JJV8ZD4TQTHSM5YVC7PCR66Y)

-----------------------------------------------------------------------------------------------------------

[How To Submit A Bynder Support Ticket](https://support.bynder.com/hc/en-us/articles/19685047299730-How-To-Submit-A-Bynder-Support-Ticket)

### _Level: Beginner_

Beginner-level articles are for everyone, these articles do not assume any prior Bynder knowledge. These articles are a great place to start your Bynder Journey.

Share
