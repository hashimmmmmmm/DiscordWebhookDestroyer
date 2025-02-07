import requests
import time

def send_discord_message(webhook_url, message):
    """
    sends a message to a discord webhook.
    :param webhook_url: the discord webhook url
    :param message: the message to send
    """
    payload = {"content": message}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("message sent successfully")
        else:
            print(f"failed to send message. status code: {response.status_code}")
            print(f"response: {response.text}")
    except Exception as e:
        print(f"an error occurred: {e}")

def delete_webhook(webhook_url):
    """
    deletes the discord webhook.
    :param webhook_url: the discord webhook url
    """
    try:
        response = requests.delete(webhook_url)
        if response.status_code == 204:
            print("webhook deleted successfully")
        else:
            print(f"failed to delete webhook. status code: {response.status_code}")
            print(f"response: {response.text}")
    except Exception as e:
        print(f"an error occurred: {e}")

def main():
    print("discord webhook messager")
    webhook_url = input("discord webhook url: ").strip()
    
    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        print("invalid discord webhook url")
        return

    while True:
        print("\noptions:")
        print("1. send out a message")
        print("2. spam messages")
        print("3. delete webhook")
        print("4. exit")
        choice = input("choose an option: ").strip()

        if choice == "1":
            message = input("enter the message to send: ")
            send_discord_message(webhook_url, message)
        elif choice == "2":
            message = input("enter the message to spam: ")
            count = int(input("how many messages to send: "))
            delay = float(input("delay messages in seconds: "))
            
            print("\nstarting spam...")
            for _ in range(count):
                send_discord_message(webhook_url, message)
                time.sleep(delay)
            print("\nspam completed...")
        elif choice == "3":
            confirm = input("are you sure you want to delete this webhook? (yes/no): ").strip().lower()
            if confirm == "yes":
                delete_webhook(webhook_url)
                break
            else:
                print("webhook not deleted")
        elif choice == "4":
            print("exiting...")
            break
        else:
            print("invalid option")

if __name__ == "__main__":
    main()

