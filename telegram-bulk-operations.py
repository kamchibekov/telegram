import os
from telethon.sync import TelegramClient

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')

client = TelegramClient('test_session', API_ID, API_HASH)
client.start()

def bulk_download():
    for message in client.iter_messages('some_username', limit=10000):
        print(message.download_media())

def list_groups():
    # Get all dialogs
    dialogs = client.get_dialogs()
    # Filter only groups
    groups = [d for d in dialogs if d.is_group]
    # Print group names
    for g in groups:
        # if g.name in groups:
        print(g.name, g.id, g.title)

group_ids = []

def remove_groups(group_ids):
    for group_id in group_ids:
        client.delete_dialog(group_id)