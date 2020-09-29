import pymsteams



def send_text(message: str, title: str, webhook: str) -> None:
    """Send the message to the specified Microsoft Teams channel."""
    ms_message = pymsteams.connectorcard(webhook)
    ms_message.title(title)
    ms_message.text(f'<pre>\n{message}\n</pre>')
    
    ms_message.send()




class Channel:
    def __init__(self, team_id: str, channel_id: str, 
                 bearer: str):
        """Initialize a Channel."""
        self._endpoint = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/'
        self._bearer = bearer