print(
    """
    Welcome to Session String Generator
    
    ╔════╦═══╦╗──╔═══╗╔════╦══╦═══╦═══╗
    ║╔╗╔╗║╔══╣║──║╔══╝║╔╗╔╗╠╣╠╣╔═╗║╔═╗║
    ╚╝║║╚╣╚══╣║──║╚══╗╚╝║║╚╝║║║╚═╝║╚══╗
    ──║║─║╔══╣║─╔╣╔══╝──║║──║║║╔══╩══╗║
    ──║║─║╚══╣╚═╝║╚══╗──║║─╔╣╠╣║──║╚═╝║
    ──╚╝─╚═══╩═══╩═══╝──╚╝─╚══╩╝──╚═══╝

    Enter 1: Pyrogram Session String
    Enter 2: Telethon Session String
    """
)

choice = ""
while (choice != "1" or choice != "2"):
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nSwitched to Pyrogram\n")
        API_ID = int(input("Enter API ID: "))
        API_HASH = input("Enter API HASH: ")
        print("")
        import pyrogram
        from pyrogram import enums
        with pyrogram.Client("my_account", api_id = API_ID, api_hash = API_HASH, in_memory = True) as ssg_teletips:
            ssg_teletips.send_message("me", f"Here is your session string: \n\n<code>{ssg_teletips.export_session_string()}</code> \n\nSession String Generator - @teletipsall", parse_mode=enums.ParseMode.HTML)
            print("\nYour session string has been successfully generated!")
            print("Please check your Telegram saved messages.")
        break

    elif choice == "2":
        print("\nSwitched to Telethon\n")
        API_ID = int(input("Enter API ID: "))
        API_HASH = input("Enter API HASH: ")
        print("")
        from telethon.sync import TelegramClient
        from telethon.sessions import StringSession  
        with TelegramClient(StringSession(), API_ID, API_HASH) as ssg_teletips:
            ssg_teletips.send_message("me", f"Here is your session string: \n\n<code>{ssg_teletips.session.save()}</code> \n\nSession String Generator - @teletipsall", parse_mode="html")
            print("\nYour session string has been successfully generated!")
            print("Please check your Telegram saved messages.")
        break

    else:
        print("\nInvalid input. Try again!\n")   