from pydantic import BaseModel


class ConfigAttribute(BaseModel):

    config_name	: str
    config_value: str

