from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('93df9f0110abd0769341300c7eba9f1e
')
handler = WebhookHandler('F4dJKRV2kJaju+A4uIM0hf+ad1dcvd24PnSrZizTvmuQAACsQ5vZ4T/DfI1cb+UBmOsZbVad64/zMMY9fLK7dgwz8XrQhDB//O3uVhTFI/wHbCF6PTq6tUI3FF/KNy9PBT1gLRvHvQI7YdEUR1apvwdB04t89/1O/w1cDnyilFU=')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
