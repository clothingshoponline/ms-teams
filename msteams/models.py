from collections import namedtuple

import pymsteams
import requests


def send_text(message: str, title: str, webhook: str) -> None:
    """Send the message to the specified Microsoft Teams channel."""
    ms_message = pymsteams.connectorcard(webhook)
    ms_message.title(title)
    ms_message.text(f'<pre>\n{message}\n</pre>')
    
    ms_message.send()


Message = namedtuple('Message', ['id', 'parent_id', 
                                 'sender', 'sender_id', 
                                 'last_modified', 
                                 'subject', 'body'])

class Channel:
    def __init__(self, team_id: str, channel_id: str, 
                 bearer: str):
        """Initialize a Channel."""
        self._endpoint = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}'
        self._headers = {'Authorization': 'Bearer ' + bearer}

    def post(self, message: str) -> None:
        """Send text message."""
        payload = {'body': {'content': f'<pre>\n{message}\n</pre>'}}
        requests.post(self._endpoint + '/messages', 
                      headers=self._headers, 
                      json=payload)