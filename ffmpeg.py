import logging
import asyncio
import os
import time
import re
import json
import subprocess
import math
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.helper_funcs.display_progress import TimeFormatter
from bot.localisation import Localisation
from bot import (
    FINISHED_PROGRESS_STR,
    UN_FINISHED_PROGRESS_STR,
    DOWNLOAD_LOCATION,
    crf,
    resolution,
    audio_b,
    preset,
    codec,
    pid_list
)

logging.basicConfig(
    level=logging.WARNING, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

async def convert_video(video_file, output_directory, total_time, bot, message, chan_msg):
    kk = video_file.split("/")[-1]
    aa = kk.split(".")[-1]
    
    season_match = re.search(r'S(\d+)', kk)
    episode_match = re.search(r'E(\d+)', kk)
    
    season_number = season_match.group(1) if season_match else ''
    episode_number = episode_match.group(1) if episode_match else ''
    
    kk = re.sub(r'S\d+', '', kk)
    kk = re.sub(r'E\d+', '', kk)
    
    if not season_number and episode_number:
        kk = f'E{episode_number}' + kk
        
    elif not season_number and not episode_number and re.search(r'\d+', kk):
        number_match = re.search(r'\d+', kk)
        number = number_match.group(0)
        kk = f'{number} ' + kk.replace(number, '', 1)
    
    elif season_number or episode_number:
        kk = f'S{season_number}E{episode_number}' + kk

    if resolution[0] == "854x480":
        kk = re.sub(r'(720p|1080p|HDRip)', '480p', kk)

    if resolution[0] == "1280x720":
        kk = re.sub(r'(1080p|HDRip)', '720p', kk)
       
    if resolution[0] == "1920x1080":
        kk = re.sub(r'(HDRip)', '1080p', kk)
    
    out_put_file_name = kk.replace(f".{aa}", ".mkv")
    
    progress = output_directory + "/" + "progress.txt"
    with open(progress, 'w') as f:
        pass
    
    file_genertor_command = f"""ffmpeg -hide_banner -loglevel quiet -progress '{progress}' \
    -i '{video_file}' \
    -c:v {codec[0]} -crf {crf[0]} -preset {preset[0]} \
    -map 0 -c:s copy -pix_fmt yuv420p -s {resolution[0]} -b:v 150k \
    -c:a libopus -b:a {audio_b[0]} \
    -metadata title="JOIN US ON TELEGRAM: @chrunchyrool" \
    -metadata:s:v title="Encoded by @KGN_BOTZ" \
    -metadata:s:a title="@chrunchyrool" \
    -metadata:s:s title="@chrunchyrool" \
    '{out_put_file_name}' -y"""
    
    COMPRESSION_START_TIME = time.time()
    process = await asyncio.create_subprocess_shell(
        file_genertor_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    
    LOGGER.info("ffmpeg_process: " + str(process.pid))
    pid_list.insert(0, process.pid)
    status = output_directory + "/status.json"
    
    with open(status, 'r+') as f:
        statusMsg = json.load(f)
        statusMsg['pid'] = process.pid
        statusMsg['message'] = message.id
        f.seek(0)
        json.dump(statusMsg, f, indent=2)
    
    isDone = False
    while process.returncode != 0:
        await asyncio.sleep(3)
        with open(DOWNLOAD_LOCATION + "/progress.txt", 'r+') as file:
            text = file.read()
            frame = re.findall("frame=(\d+)", text)
            time_in_us = re.findall("out_time_ms=(\d+)", text)
            progress = re.findall("progress=(\w+)", text)
            speed = re.findall("speed=(\d+\.?\d*)", text)
            
            if len(frame):
                frame = int(frame[-1])
            else:
                frame = 1
            if len(speed):
                speed = speed[-1]
            else:
                speed = 1
            if len(time_in_us):
                time_in_us = time_in_us[-1]
            else:
                time_in_us = 1
            if len(progress):
                if progress[-1] == "end":
                    LOGGER.info(progress[-1])
                    isDone = True
                    break
            
            execution_time = TimeFormatter((time.time() - COMPRESSION_START_TIME) * 1000)
            elapsed_time = int(time_in_us) / 1000000
            difference = math.floor((total_time - elapsed_time) / float(speed))
            ETA = "-"
            if difference > 0:
                ETA = TimeFormatter(difference * 1000)
            percentage = math.floor(elapsed_time * 100 / total_time)
            progress_str = "<blockquote><b>ᴘʀᴏɢʀᴇss:</b> {0}%\n[{1}{2}]</blockquote>".format(
                round(percentage, 2),
                ''.join([FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 10))]),
                ''.join([UN_FINISHED_PROGRESS_STR for i in range(10 - math.floor(percentage / 10))])
            )
            stats = f'<blockquote> <b>ᴇɴᴄᴏᴅɪɴɢ ɪɴ ᴘʀᴏɢʀᴇss</b></blockquote>\n' \
                    f'<blockquote><b>ᴛɪᴍᴇ ʟᴇғᴛ:</b> {ETA}</blockquote>\n' \
                    f'{progress_str}\n'
            try:
                await message.edit_text(
                    text=stats,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [ 
                                InlineKeyboardButton('❌ Cancel ❌', callback_data='fuckingdo') # Nice Call 🤭
                            ]
                        ]
                    )
                )
            except:
                pass
            try:
                await bug.edit_text(text=stats)
            except:
                pass
        
    stdout, stderr = await process.communicate()
    r = stderr.decode()
    try:
        if r:
            await message.edit_text(str(r) + "\n\n**ERROR** Contact ")
            os.remove(video_file)
            os.remove(out_put_file_name)
            return None
    except BaseException:
        pass
    
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    LOGGER.info(e_response)
    LOGGER.info(t_response)
    del pid_list[0]
    
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    else:
        return None

async def media_info(saved_file_path):
    process = subprocess.Popen(
        [
            'ffmpeg', 
            "-hide_banner", 
            '-i', 
            saved_file_path
        ], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT
    )
    stdout, stderr = process.communicate()
    output = stdout.decode().strip()
    duration = re.search("Duration:\s*(\d*):(\d*):(\d+\.?\d*)[\s\w*$]", output)
    bitrates = re.search("bitrate:\s*(\d+)[\s\w*$]", output)
    
    if duration is not None:
        hours = int(duration.group(1))
        minutes = int(duration.group(2))
        seconds = math.floor(float(duration.group(3)))
        total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
    else:
        total_seconds = None
        
    if bitrates is not None:
        bitrate = bitrates.group(1)
    else:
        bitrate = None
        
    return total_seconds, bitrate

async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = os.path.join(
        output_directory,
        str(time.time()) + ".jpg"
    )
    if video_file.upper().endswith(("MKV", "MP4", "WEBM")):
        file_genertor_command = [
            "ffmpeg",
            "-ss",
            str(ttl),
            "-i",
            video_file,
            "-vframes",
            "1",
            out_put_file_name
        ]
        
        process = await asyncio.create_subprocess_exec(
            *file_genertor_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
    
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    else:
        return None

def get_width_height(video_file):
    metadata = extractMetadata(createParser(video_file))
    if metadata.has("width") and metadata.has("height"):
        return metadata.get("width"), metadata.get("height")
    else:
        return 1280, 720