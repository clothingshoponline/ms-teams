import pymsteams




def send_text(message: str, program_name: str, webhook: str, 
                 include_traceback: bool = False):
    ''' Send the message to the specified Microsoft Teams channel. 
    If include_traceback is True, send the most recent exception raised.'''
    ms_message = pymsteams.connectorcard(webhook)
    ms_message.title(program_name)
    if include_traceback:
        message = f'{message}\n{traceback.format_exc()}'
    ms_message.text(f'<pre>\n{message}\n</pre>')
    
    ms_message.send()