import requests

def send_telegram(text: str):
    token = "5776059773:AAHlx9nAJ-YDNDfDmtjpbTPmhAgFhBtUoaM"
    url = "https://api.telegram.org/bot"
    channel_id = "647297557"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram("hello world!")

