from pydantic import BaseModel

class sent (BaseModel):
    sentence : list[str]