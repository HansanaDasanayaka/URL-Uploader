class Translation(object):

    START_TEXT = """<b>Hello, This is a Telegram URL Upload Bot 🤖

Please send me any Direct download URL link, I can upload to telegram as File or Video 🥳

/help for more details 🙃

Made with ❤ 🇱🇰 by @TGRobotz</b>
"""

    HELP_USER = """<u><b>More Help and Commands</u>
    
1. Send URL (Link | New Name with Extension)
2. Send Custom Thumbnail (Optional)
3. Select the button
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots

Made by @TGRobotz</b>
"""

    FORMAT_SELECTION = """Select the desired format, file size might be approximate.
    
Send your custum thumbnail if required.
You can use /deletethumbnail to delete the auto-generated thumbnail."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    DOWNLOAD_START = "<b>Downloading... Please Wait 🥺</b>"
    
    UPLOAD_START = "<b>Uploading... Please Wait 🙃</b>"
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds \n\nUploaded in {} seconds\n\n<b>By @TGRobotz</b>"

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    CUSTOM_CAPTION_UL_FILE = "Uploaded by @Infinity_BOTs"

    SLOW_URL_DECED = "Nigga, that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try @HK_transloader_BOT and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
