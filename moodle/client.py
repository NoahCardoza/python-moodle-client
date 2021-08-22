import requests
import json

brace = lambda s: '%s%s%s' % ('[', s, ']')

def formatMoodlePostBody(src, dpth=0):
    """ Recursively formats Dictionary like XML tree."""
    if isinstance(src, list):
        src = dict(enumerate(src))

    if isinstance(src, dict):
        ret = []
        for key, value in src.items():
            ret.extend([((brace(key) if dpth else key) + pair[0], pair[1]) for pair in formatMoodlePostBody(value, dpth + 1)])
        if not dpth:
            return dict(ret)
        return ret
    else:
        return [('', str(src))]

class MoodleError(Exception):
    """Rasied when the Moodle endpoint returns an error to the client."""

class MoodleClient:
    """
    Docstring for MoodleClient
    Using the REST protocol.
    """
    def __init__(self, token, wwwroot):
        self.token          = token
        self.wwwroot        = wwwroot
        self.protocol       = 'rest'
        self.format         = 'json'
        self.url            = f'{self.wwwroot}/webservice/{self.protocol}/server.php'
        self.defalut_args   = {
            'wstoken': self.token,
            f'moodlews{self.protocol}format': self.format
        }


    def request(self, fn, args):
        resp = requests.post(self.url,
            params={
                **self.defalut_args,
                'wsfunction': fn
            },
            data=formatMoodlePostBody(args)
        ).json()
        if type(resp) == dict and resp['exception']:
            raise MoodleError(json.dumps(resp, indent=4))
        else:
            return resp
