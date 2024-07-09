from typing import Tuple

from pydantic import Field

from processor.entity.base_entity import BaseEntity


class Text(BaseEntity):
    # def __init__(self, entity_type: str, layer_name: str, insert_points: Tuple[float, float], content: str):
    #     super().__init__(entity_type, layer_name)
    #     self.insert_points = insert_points
    #     self.content = content

    # 切入点
    insert_points: Tuple[float, float] = Field(default_factory=list)
    # 文字内容
    content: str
