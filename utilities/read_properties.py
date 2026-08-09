from configparser import ConfigParser
from pathlib import Path


class ReadConfig:
    """
    Read values from config.ini
    """

    BASE_DIR = Path(__file__).resolve().parent.parent
    CONFIG_PATH = BASE_DIR / "config" / "config.ini"

    config = ConfigParser()
    config.read(CONFIG_PATH)

    @staticmethod
    def get_url():
        return ReadConfig.config.get("common", "baseURL")

    @staticmethod
    def get_product():
        return ReadConfig.config.get("common", "product")

    @staticmethod
    def get_email():
        return ReadConfig.config.get("common", "email")

    @staticmethod
    def get_password():
        return ReadConfig.config.get("common", "password")

    @staticmethod
    def get_browser():
        return ReadConfig.config.get("common", "browser")

    @staticmethod
    def get_timeout():
        return ReadConfig.config.getint("common", "timeout")