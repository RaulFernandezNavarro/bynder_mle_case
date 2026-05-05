# Export Bynder Assets with SFTP or S3 – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/21403219582866-Export-Bynder-Assets-with-SFTP-or-S3

To export your Bynder assets securely, use SFTP or S3 without external hard drives. Bynder can send files to your SFTP server or AWS S3 bucket. For S3 transfers, provide the bucket address, Access Key ID, and Access Key for a user with permission to list and transfer files. After the SFTP export, files will be deleted from the AWS bucket and SFTP server within 90 days.

#### **How to request an export?**

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

How to Generate an SSH Key and log in to the SFTP Location[](https://support.bynder.com/hc/en-us/articles/21403219582866-Export-Bynder-Assets-with-SFTP-or-S3#h_01HMHW90MS0X16AC1S5F1BB8SD)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Create an RSA-2048 SSH key pair on your side, including a private and public key. Follow the instructions below depending on your operating system:
    *   [Windows](https://learn.microsoft.com/en-us/viva/glint/setup/sftp-ssh-key-gen#create-an-ssh-key-pair-on-microsoft-windows)
        
    *   [MacOS](https://help.dreamhost.com/hc/en-us/articles/115001736671-Creating-a-new-Key-pair-in-Mac-OS-X-or-Linux)
        *   When you create your keys, we strongly suggest setting up a passphrase for the private key.
        *   Keep the private key and passphrase private from everyone. Bynder will never ask you for this information.
2.  Send the public key to your Onboarding Manager or Customer Success Contact, who will provide you with a username and other necessary details to connect to the SFTP server.
    *   _Never_ send us the **private** key and its passphrase. The key will then be compromised, and a new key pair must be generated.
3.  Create a new SFTP connection using the following details in your preferred SFTP client. We recommend using [Cyberduck](https://cyberduck.io/)
     or [FileZilla](https://filezilla-project.org/)
    . In the below example, we use Cyberduck.
    *   The name of the fields below may vary depending on the SFTP client you're using.
        *   **Server**: Fill in the server endpoint that Bynder provided you with.
        *   **Port**: The port number will be set automatically and should always be 22.
        *   Username: The username Bynder provided you with.
            
            **SSH** **Private** **Keys**: Select the private key you generated in step 1. When prompted, enter the passphrase for this key![](https://support.bynder.com/hc/article_attachments/22559398874514)
            
            Above is an example of SFTP configuration in Cyberduck. An example of FileZilla can be found [here](https://wiki.filezilla-project.org/Howto)
            .
            
4.  Connect to the SFTP server. You may see a Host Key Fingerprint the first time you connect. Check if this fingerprint matches the Host Key Fingerprint Bynder provided you with. This way, you can ensure you're connecting to the correct server. The Host Key Fingerprint may not be shown depending on your SFTP client.
5.  Start transferring your files once you're successfully connected to the SFTP server.
6.   Notify your onboarding manager or customer success contact once all the files have been transferred successfully, and you've filled out your import sheet.
7.  We'll start importing your files into your Bynder portal and let you know when the import is complete.

FAQ[](https://support.bynder.com/hc/en-us/articles/21403219582866-Export-Bynder-Assets-with-SFTP-or-S3#h_01J7XMYVTPS22PE8P5DMDBHED2)

-------------------------------------------------------------------------------------------------------------------------------------

**How long does it take to complete the export?**  
SFTP: It takes approximately one week per TB to load via SFTP.  
S3: It takes approximately 3-5 days per TB to load from S3 to S3.

**How do you create a user with correct S3 bucket permissions?**

Click [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example1.html)
 to learn how to grant the correct permission.

Share
