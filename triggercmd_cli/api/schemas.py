from pydantic import BaseModel


class Command(BaseModel):
    trigger: str
    command: str
    ground: str
    voice: str
    allowParams: str
