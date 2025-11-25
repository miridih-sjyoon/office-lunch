import json
from dataclasses import dataclass

import requests


@dataclass
class SlackWebhookPayload:
    text: str
    username: str | None
    blocks: list[ImageBlock] | None = None

    @dataclass
    class ImageBlock:
        alt_text: str
        image_url: str
        type: str = 'image'


def send_slack_webhook(payload: SlackWebhookPayload, webhook_url: str):
    requests.post(webhook_url, json=json.loads(json.dumps(payload, default=lambda x: x.__dict__)))
