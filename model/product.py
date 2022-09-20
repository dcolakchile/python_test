import datetime

from pydantic 	import BaseModel
from typing 	import List

from model.productvariant import ProductVariant


class Product(BaseModel):

    id							: int
    name						: str
    uom							: str
    category_name				: str
    is_producible				: bool
    is_purchasable				: bool
    type						: str
    purchase_uom				: str
    purchase_uom_conversion_rate: float
    batch_tracked				: bool
    variants					: List[ProductVariant]
    additional_info				: str
    created_at					: datetime.datetime
    updated_at					: datetime.datetime
