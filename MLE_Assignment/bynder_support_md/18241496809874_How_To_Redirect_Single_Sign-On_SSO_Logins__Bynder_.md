# How To Redirect Single Sign-On (SSO) Logins – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/18241496809874

Summary[](https://support.bynder.com/hc/en-us/articles/18241496809874#h_01JNDT8RDKAGS2M6D9369QJYEC)

----------------------------------------------------------------------------------------------------

By default, all users logging into Bynder do so via the Bynder login page. However, after setting up your Single Sign-On (SSO) provider(s) you can set up a redirect to override the portal login page and automatically direct a user to the configured SSO provider based on the predefined conditions such as a Visitor IP address (single IP, multiple IPs, or subnets), or if a OAuth2 flow is in use.

Who?[](https://support.bynder.com/hc/en-us/articles/18241496809874#h_01JNDTAXB69947YT3PB34MA82E)

-------------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once enabled users with the _Portal Settings_ or _Manage Login Configuration_ permissions can create and manage SSO profiles and flows. 

Why?[](https://support.bynder.com/hc/en-us/articles/18241496809874#h_01JNDTCAYF7RXC4FQS7WPW0P8T)

-------------------------------------------------------------------------------------------------

Bynder understands that some users may want to direct their users away from a visible login page for brand or flow consistency. This feature allows Bynder admins to provision their user profiles this way. 

How?[](https://support.bynder.com/hc/en-us/articles/18241496809874#h_01HV57XATDQYKWYEZQR5QJVHD6)

-------------------------------------------------------------------------------------------------

1.  Navigate to **Settings** > **Advanced** **Settings** > **Portal** **Settings**.
2.  Click **Login** **Configuration** on the left sidebar.
3.  Select **Add Override.![Screenshot 2024-04-10 at 8.17.46 PM.png](https://support.bynder.com/hc/article_attachments/18241764225810)**
4.  Select the configured login method from the dropdown menu.
    *   Both active and inactive login methods will appear.
    *   Any override created for an inactive login method will not be used—the system will disregard this.
5.  Check the checkbox if you would like to redirect to the selected login method by default.
    *   By checking this box, the override will be used for all users instead of the Bynder login page appearing.
    *   If you check this box, you cannot create any conditions. 
6.  Select **Add** **condition** for the selected override.
    *   **Visitor IP address**
        *   Only IP (IPv4, IPv6) and subnet format are allowed.
        *   You can enter as many addresses as you like. Make sure to add a comma to separate addresses.
        *   IP addresses cannot be duplicated. If duplicates are added, they will be automatically removed.
    *   **Is Using OAuth2 flow (Yes/No)**
7.  Select **Save**.
8.  Select the ![Screenshot 2024-04-10 at 8.16.21 PM.png](https://support.bynder.com/hc/article_attachments/18241808992402) button to rearrange the override options.
    *   Overrides are prioritized based on their position in the list.
    *   For example, suppose the override at the top redirects visitors from IP address 123.45.67.89 to Login Method 1, and the override below is a default override for Login Method 2. In that case, all visitors with IP 123.45.67.89 will use Login Method 1, and everyone else will use Login Method 2.

_Note: When a user matches the conditions of multiple overrides, the login method positioned the highest will be used for redirection._

![Screenshot 2024-04-10 at 8.30.26 PM.png](https://support.bynder.com/hc/article_attachments/18241803147410)

### How to Edit or Delete an Override

1.  Navigate to **Settings** > **Advanced** **Settings** > **Portal** **Settings**.
2.  Select **Login** **Configuration** on the left sidebar.
3.  To edit, select **Edit.** 
4.  To delete, select **Delete.** 
5.  To deactivate, select **Deactivate.**

_Note: If you have multiple overrides with overlapping conditions and delete/deactivate the one at the top, the system will automatically select the following available override._

FAQs[](https://support.bynder.com/hc/en-us/articles/18241496809874#h_01HV58QV5BB9GWFBFG116867Y5)

-------------------------------------------------------------------------------------------------

**Is there a limit to the number of overrides I can add?**

There is no limit to the number of overrides you can create.

**What happens if I create an override and then deactivate the login method?**  
If you have multiple overrides with overlapping conditions and delete/deactivate the login method, the system will automatically select the following override available. The system will disregard an override made with an inactive login method.

**If I create a login override, will my users ever see the Bynder login page?**  
Yes, the Bynder login page is shown when the visitor does not match any of the conditions defined in other active overrides.

**Can I test the overrides before making them live?**

Once you create an override, it will be live for your users. However, if you would like to test an override, we recommend you create an override for the login method of your choice and then set it to your IP address. Then, this override will be active only for you (and anyone else sharing the same IP address), allowing you to test the override before it goes live. Please remember to remove the IP address once you are ready for users to have access to this override.

Related Articles[](https://support.bynder.com/hc/en-us/articles/18241496809874#h_01JNDV6JA35VS49K10ZXVJ1MTM)

-------------------------------------------------------------------------------------------------------------

[How To Configure Single Sign-On (SSO)](https://support.bynder.com/hc/en-us/articles/6614562131474)

[How To Configure Single Sign-On (SSO) For Content Workflow](https://support.bynder.com/hc/en-us/articles/22605853760658)

[How To Use Single Sign-On (SSO) Troubleshooting Logs](https://support.bynder.com/hc/en-us/articles/7780356129426)

Share
