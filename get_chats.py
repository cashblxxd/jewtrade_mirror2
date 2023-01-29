from telethon.sync import TelegramClient, events

with TelegramClient('MyApp', "18846638", "26b31c20a07385d0770ce216a6f61c63") as client:
    for dialog in client.iter_dialogs():
        print('{:>14}: {}'.format(dialog.id, dialog.title))

    client.run_until_disconnected()
