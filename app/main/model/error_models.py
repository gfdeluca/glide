from dataclasses import dataclass


class Error(Exception):
    def __init__(self, message, detail_message):
        self.message = message
        self.detail_message = detail_message


class NotFoundException(Error):
    def __init__(self, message: str, detail_message:str):
        super().__init__(message, detail_message)
