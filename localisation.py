from bot.get_cfg import get_config

class Localisation:
    START_TEXT = "<blockquote><b>𝗛𝗲𝗹𝗹𝗼, 𝗧𝗵𝗶𝘀 𝗜𝘀 𝗔 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝟰𝟴𝟬𝗽 𝗩𝗶𝗱𝗲𝗼 𝗘𝗻𝗰𝗼𝗱𝗲𝗿 𝗕𝗼𝘁, 𝗠𝗮𝗱𝗲 𝗕𝘆 @ProToppers </b>. \n\n<b>𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗔𝗻𝘆 𝗕𝗶𝗴 𝗩𝗶𝗱𝗲𝗼 𝗙𝗶𝗹𝗲 𝗜 𝗪𝗶𝗹𝗹 𝗖𝗼𝗺𝗽𝗿𝗲𝘀𝘀 𝗜𝘁 𝗔𝘀 𝗦𝗺𝗮𝗹𝗹 𝗩𝗶𝗱𝗲𝗼 𝗙𝗶𝗹𝗲 & 𝗜 𝗢𝗻𝗹𝘆 𝗪𝗼𝗿𝗸 𝗢𝗻 @Video_Compressor_Free ⚠️</b> \n\n/help 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗗𝗲𝘁𝗮𝗶𝗹𝘀.</blockquote>"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "Dᴏᴡɴʟᴏᴀᴅɪɴɢ...📥" 
    
    UPLOAD_START = "Uᴘʟᴏᴀᴅɪɴɢ...📤"
    
    COMPRESS_START = "Tʀʏɪɴɢ ᴛᴏ Eɴᴄᴏᴅᴇ...🗜️"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS =  "𝙼𝚊𝚍𝚎 𝙱𝚢➛ @ProToppers"

    COMPRESS_PROGRESS = "<blockquote>⏳ ETA: {}\n🚀 Pʀᴏɢʀᴇꜱꜱ: {}%</blockquote>"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Cʟᴇᴀʀᴇᴅ Sᴜᴄᴄᴇꜱꜰᴜʟʟʏ...✅"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Mᴇᴅɪᴀ Cʟᴇᴀʀᴇᴅ Sᴜᴄᴄᴇꜱꜰᴜʟʟʏ...✅"
    
    SAVED_RECVD_DOC_FILE = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ...✅"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "Nᴏ Cᴜꜱᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Fᴏᴜɴᴅ...💔"
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Encoder Logs ."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nMaintained By @ProToppers"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
