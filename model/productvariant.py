import datetime

from pydantic import BaseModel
from typing import List

from model.config_attribute import ConfigAttribute


class ProductVariant(BaseModel):

    id					: int
    product_id			: int
    sku					: str
    type				: str
    sales_price			: float
    purchase_price		: float
    config_attributes	: List[ConfigAttribute]
    created_at			: datetime.datetime
    updated_at			: datetime.datetime
