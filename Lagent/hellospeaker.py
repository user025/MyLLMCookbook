import json
import requests

from lagent.actions.base_action import BaseAction, tool_api
from lagent.actions.parser import BaseParser, JsonParser
from lagent.schema import ActionReturn, ActionStatusCode


class HelloSpeaker(BaseAction):
    language_options = {
        'english' : 'Hello',
        'chinese' : 'Nihao',
        'japanese' : 'konnijiwa'
    }
    def __init__(self, language = 'english'):
        super().__init__()
        if language not in self.language_options:
            raise ValueError(f"{language} not supported")
        else:
            self.l = language

    @tool_api
    def say_hello(self, language: str) -> str:
        """ say hello in different languages

        Args:
            language (:class:`str`): required language in English

        Returns:
            :class:`str`: result
        
        """
        r = language.lower()
        return self.language_options.get(r, "hello")

