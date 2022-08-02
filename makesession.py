from pyrogram import Client

API_KEY = int(input("426fda5d-19cc-4c84-9f31-96a37abe3c65: "))
API_HASH = input("f8db65e3150885246e6a641360cd2033: ")
with Client(":memory:", api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
