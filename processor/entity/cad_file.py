from typing import List, Union

from pydantic import BaseModel

from processor.entity.polyline import Polyline
from processor.entity.text import Text


class CadFile(BaseModel):
    # 文件名
    file_name: str
    # cad文件里的所有entity
    entities: List[Union[Polyline, Text]]
