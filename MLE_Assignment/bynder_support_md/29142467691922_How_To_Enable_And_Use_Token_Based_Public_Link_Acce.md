# How To Enable And Use Token Based Public Link Access – Bynder Support

**Source URL:** https://support.bynder.com/hc/en-us/articles/29142467691922-How-To-Enable-And-Use-Token-Based-Public-Link-Access

Summary[](https://support.bynder.com/hc/en-us/articles/29142467691922-How-To-Enable-And-Use-Token-Based-Public-Link-Access#h_01K425QCRXEATPDYF08P4WJF16)

---------------------------------------------------------------------------------------------------------------------------------------------------------

Bynder's Token based authentication solution for restricted public assets enables users to have full control over how they request assets from Bynder's APIs. Users can mark an asset as _limited-use_ which prevents the public asset from being viewed by anyone, but this stops testing capabilities. Some users need to test proprietary assets in a testing environment before pushing to production, and Bynder offers Token based authentication as a secure solution. This feature is supported for public links, DAT links, AVS links, and predictable URLs.

Who?[](https://support.bynder.com/hc/en-us/articles/29142467691922-How-To-Enable-And-Use-Token-Based-Public-Link-Access#h_01K425SNBFNWKP43VJH7ER9SMR)

------------------------------------------------------------------------------------------------------------------------------------------------------

This feature/solution requires your Customer Success Contact to enable, but then individual permissions can be done by the Bynder Admin.

Once enabled users will need the _view limited assets_ permission. Setting up the users requires other permissions that are laid out in the article attached to step one. 

Why?[](https://support.bynder.com/hc/en-us/articles/29142467691922-How-To-Enable-And-Use-Token-Based-Public-Link-Access#h_01K425SSTK7PDX9CWCRHR127G5)

------------------------------------------------------------------------------------------------------------------------------------------------------

This feature allows specific users to access limited-use assets before they become fully public. The token based authentication ensures only the right users can view the assets and test them in testing environments before they go public. 

How?[](https://support.bynder.com/hc/en-us/articles/29142467691922-How-To-Enable-And-Use-Token-Based-Public-Link-Access#h_01K425SX7EVMQWW2QR0PEPN81M)

------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Begin by creating a client in the portal to get the JWT. Users will do this using Bynder's OAuth2 app creation procedure.
    *   [How To Create And Manage OAuth2 Apps](https://support.bynder.com/hc/en-us/articles/360013875180-How-To-Create-And-Manage-OAuth2-Apps)
        .
        *   Ensure the OAuth2 app scope has been set up to include the **asset:read** functionality.
        *   Ensure the user has the _view Limited Assets_ permission.
            *   Bynder recommends using/creating a user named _**API User**_  for this purpose. 
        *   Ensure you copy & paste your ClientID and ClientSecret in a secure place as you will not be able to see your secret again. If the ClientID and ClientSecret are lost they will need to be regenerated and everything will need to be reprovisioned. 
            
            _When complete users will be able to authenticate with this portal and retrieve a token._
            
2.  Request a JWT bearer token with the **asset:read** permission by using this [Token API Endpoint](https://bynder.docs.apiary.io/#reference/oauth-2.0/token-endpoint/using-client-credentials)
    , and sending your ClientID and ClientSecret to the portal URL.
    *   The token expires after one hour, and users will need to re-authenticate. 
3.  With the Bearer token, users can now make a GET request for a _**limited-use asset**_. The request to the asset's public URL must include the token in the Authorization header. Once the request is made with the valid token, the asset will be delivered by the CDN, allowing users to view and test it in your pre-production environment.
    
    **Example Header:** **Authorization:** Bearer _<your\_bearer\_token>_
    
    Restricted assets can now be accessed through the following public links:
    
    *   `/transform/{asset_id}/...` (DAT links)
        
    *   `/asset/asset_id}/...` (standard public links)
        
    *   `/match/{meta_property}/{option_name}/...` (predictable urls)
        
    *   `/vod-stream/{asset_id}/...` (adaptive video links)
        

### Viewing A Limited Access Asset With A Demo Website

1.  **Input your credentials** (ClientID and ClientSecret from the Bynder OAuth2 app)
    
2.  **Paste your image DAT URL** (from the specific Bynder portal)
    
    *   **Ensure** the user is impersonating the profile set up in the OAuth2 app.
        
    *   **Ensure** the asset is set to public and “limited-use”.
        
3.  **Select the OAuth2 authentication method. Click Preview.**
    
     The system will:
    
    1.  Extract your portal domain from the URL.
        
    2.  Request a JWT token from the portal's OAuth2 endpoint.
        
    3.  Use the token to fetch the protected image.
        
    4.  Display the image and corresponding metadata.
        

### Viewing A Limited Access Asset With A Local (macOS) Host

Users will need [_**these**_](https://drive.google.com/drive/folders/1uU0RgOp-MJonQRhIwUWh7I9cxgBdJX1k)
 documents to provision this option properly. 

1.  Ensure you add [http://localhost:8000](http://localhost:8000/ "http://localhost:8000")
     to the Bynder Portals CORS exception policies for the OAuth2 Token.
2.  **Install Homebrew (if not already present):**
    *   Command: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
3.  **Install Python 3 via Homebrew:**
    
    Command: brew install python
    
    _After installation, close and reopen the Terminal to ensure the_ python3 _and_ pip3 _commands are recognized._
    
4.  **Create a Python Virtual Environment:**
    *   Navigate to your project directory (where [proxy.py](https://drive.google.com/file/d/1uzL1FqnOifSyFTFjrd0EjGleeZ4DLyO-/view?usp=drive_link)
         and [bynder\_auth.html](https://drive.google.com/file/d/1VA5D_-uu18PFkjm9WgJk76iW-wxaK63z/view?usp=drive_link)
         are).
    *   Command: python3 -m venv venv (This creates a folder named venv).
5.  **Activate the Virtual Environment:**
    *   Command: source venv/bin/activate (Your terminal prompt will usually show (venv)).
        
        _Note:_ You must do this _every time_ you open a new terminal to work on this project.
        
6.  **Install Flask, Flask-CORS, and Requests:**
    *   Command: pip install Flask Flask-CORS requests
        
        _Note: Ensure your virtual environment is active._
        
7.  **Run the Python Proxy Server:**
    *   _Open a **new** terminal window. (or open a new tab, so you don’t have to navigate)_
    *   _Navigate to your project directory._
    *   _Activate the virtual environment in this new terminal._
    *   Command: python _proxy.py_ (It typically runs on http://127.0.0.1:5000 or http://localhost:5000).
8.  **Run the Local HTTP Server for your HTML:**
    *   _Open a **new** terminal window. (or open a new tab, so you don’t have to navigate)_
    *   _Navigate to your project directory._
    *   _Activate the virtual environment in this new terminal._
    *   Command: python3 -m http.server 8000 (It typically runs on http://localhost:8000).
9.  **Access your HTML in the Browser:**
    *   Open your web browser and go to http://localhost:8000/bynder\_auth.html.

This page provides everything you need to test the endpoint.

FAQs[](https://support.bynder.com/hc/en-us/articles/29142467691922-How-To-Enable-And-Use-Token-Based-Public-Link-Access#h_01K42764TEBTC1PN01ZKP94RYT)

------------------------------------------------------------------------------------------------------------------------------------------------------

**Why can I still not see an asset set up with token based access?**

Ensure that your JWT Bearer token possesses the proper permissions we set earlier, which are needed to access a restricted asset through a public link.

Related Articles[](https://support.bynder.com/hc/en-us/articles/29142467691922-How-To-Enable-And-Use-Token-Based-Public-Link-Access#h_01K4291C5PSR01Y22YRRF62VKC)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Bynder Supported Browsers](https://support.bynder.com/hc/en-us/articles/360013873080)

[Understanding And Enabling Public Assets](https://support.bynder.com/hc/en-us/articles/360013870200)

### _Level: Expert_

Expert-level articles are for users who have significant prior Bynder knowledge. These articles require you to know a lot of Bynder information and may also require higher-level portal rights to accomplish the task outlined within the article. 

Share
