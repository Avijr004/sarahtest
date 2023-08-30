from pyrogram import filters
from google.cloud import speech
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class VoiceModule:
    def __init__(self, bot, speech_client, spotify_client):
        self.bot = bot
        self.speech_client = speech_client
        self.spotify_client = spotify_client

        self.bot.add_handler(filters.voice & filters.private, self.handle_voice_command)

async def handle_voice_command(self, client, message):
        voice_message = message.voice
        file_path = await client.download_media(voice_message)
        
        recognized_text = self.recognize_speech(file_path)
        response = self.process_voice_command(recognized_text)
        
        await message.reply_text(response)

        voice_message = message.voice
        file_path = await client.download_media(voice_message)
        
        recognized_text = self.recognize_speech(file_path)
        response = self.process_voice_command(recognized_text)
        
        await message.reply_text(response)

def recognize_speech(self, file_path):
     # ... Speech-to-Text code ...
       

def process_voice_command(self, text):
     # ... Command processing code ...
        

def create_voice_module(bot, speech_client, spotify_client):
    return VoiceModule(bot, speech_client, spotify_client)
        
     
