from .base import Base
from ...utils import read_to_string


class Help(Base):
    name = 'help'
    text = read_to_string('resources/info/help.txt')

    @staticmethod
    def execute(bot, command):
        Help.reply(bot, command, Help.text)
