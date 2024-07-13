# Zabbix_PowerAutomate

These are media type replacements i converted for using with PowerAutomate, which requires/expects you to attach an adaptive card instead of just POSTing an HTML body

I have a template for version 5.0, and 7.0 created and tested.

https://adaptivecards.io/designer/ - Helpful for card design

https://hradek.de/html/AdaptiveCardColorGIF.html - This was not doing colors right for me. I used chatgpt to write up a python script to generate 8x1 gifs instead.

![preview](https://i.imgur.com/SUzKuMJ.png)


# Known Issues:

Currently Desktop/Mobile notifications show up as "Workflows sent a card": [Link](https://powerusers.microsoft.com/t5/Using-Connectors/MS-Teams-Adaptive-Cards-No-ability-to-customize-quot-From-quot/td-p/2843061)

Supposedly you can do this, but i have not been successful, as the PowerAutomate flow only accepts the CARD json, you cant prepend anything outisde that
[Link](https://stackoverflow.com/questions/61229084/how-to-change-notification-text-when-bot-sends-an-adaptive-card-in-microsoft-tea)

I have not found a solution yet, please let me know. I'd rather not write a full bot from scratch.
