import os
import random
import string
from ast import ExceptHandler

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InputMediaPhoto, Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS, lyrical
from strings import get_command
from ShizukaXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from ShizukaXMusic.core.call import Shizuka
from ShizukaXMusic.utils import seconds_to_min, time_to_seconds
from ShizukaXMusic.utils.channelplay import get_channeplayCB
from ShizukaXMusic.utils.database import is_video_allowed
from ShizukaXMusic.utils.decorators.language import languageCB
from ShizukaXMusic.utils.decorators.play import PlayWrapper
from ShizukaXMusic.utils.formatters import formats
from ShizukaXMusic.utils.inline.play import (
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from ShizukaXMusic.utils.inline.playlist import botplaylist_markup
from ShizukaXMusic.utils.logger import play_logs
from ShizukaXMusic.utils.stream.stream import stream
from pyrogram import Client, filters
from pyrogram.types import InputFile
from google.cloud import speech

# Initialize the Google Cloud client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"
client = speech.SpeechClient()

# Telegram bot configuration
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("voice_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@filters.voice
def process_voice(client, message):
    chat_id = message.chat.id

    # Check if the user is in a voice chat
    if not client.get_chat_member_voice(chat_id, message.from_user.id):
        message.reply_text("You need to be in a voice chat to use this command.")
        return

    # Download the voice message
    file_path = message.download()

    # Convert voice to text using Google Speech-to-Text
    with open(file_path, "rb") as audio_file:
        audio_content = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=16000,  # Adjust sample rate based on your audio
        language_code="en-US",  # Set the appropriate language code
    )

    response = client.recognize(config=config, audio=audio)
    if response.results:
        command = response.results[0].alternatives[0].transcript.strip()
        if command.startswith("/play"):
            # Extract the song name from the command and play it in the voice chat
            song_name = command[len("/play"):].strip()
            # Implement logic to play the song using your preferred music API
        else:
            message.reply_text("Unknown command.")

# Handler for processing voice messages
@app.on_message(filters.voice)
def handle_voice(client, message):
    process_voice(client, message)

app.run()
