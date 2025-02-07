import requests
import time

def send_discord_message(webhook_url, message):
    """
    Sends a message to a Discord webhook.
    :param webhook_url: The Discord webhook URL
    :param message: The message to send
    """
    payload = {"content": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("message sent successfully")
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Discord Webhook Messager")
    webhook_url = input("discord webhook url: ").strip()
    
    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        print("invalid discord webhook url")
        return

    while True:
        print("\nOptions:")
        print("1. send out a message")
        print("2. spam messages")
        print("3. exit")
        choice = input("choose an option: ").strip()

        if choice == "1":
            message = input("enter the messages to send: ") 
            send_discord_message(webhook_url, message)
        elif choice == "2":
            message = input("enter the message to spam: ")
            count = int(input("how many messages to send: "))
            delay = float(input("delay messages in second: "))
            
            print("\nstarting spam...")
            for _ in range(count):
                send_discord_message(webhook_url, message)
                time.sleep(delay)
            print("\nspam completed...")
        elif choice == "3":
            print("exiting...")
            break
        else:
            print("invaild option")

if __name__ == "__main__":
    main()
