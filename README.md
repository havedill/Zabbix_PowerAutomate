# Zabbix_PowerAutomate

These are media type replacements i converted for using with PowerAutomate, which requires/expects you to attach an adaptive card instead of just POSTing an HTML body

I have a template for version 5.0, and 7.0 created and tested.

https://adaptivecards.io/designer/ - Helpful for card design

https://hradek.de/html/AdaptiveCardColorGIF.html - Helpful for card color scheme (I'm colorblind so i apologize if they look horrible out of the box)

![preview](https://i.imgur.com/oGcv5zB.png)


# Known Issues:

Currently Desktop/Mobile notifications show up as "Workflows sent a card". Similar to this issue https://answers.microsoft.com/en-us/msteams/forum/all/change-adaptive-card-summary-from-sent-a-card-in/b516d8fe-f4a1-4c5a-9b57-b6c385647040 / https://github.com/OfficeDev/teams-toolkit/issues/6752, stupid power automate may not support setting this field...

Supposedly you can do this, but i have not been successful:
https://stackoverflow.com/questions/61229084/how-to-change-notification-text-when-bot-sends-an-adaptive-card-in-microsoft-tea

I have not found a solution yet, please let me know

Also if there is a way to change "who" the message is from, instead of having the workflow owners name appear.
