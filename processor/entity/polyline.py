from typing import List, Tuple

from pydantic import Field

from processor.entity.base_entity import BaseEntity


class Polyline(BaseEntity):
    # def __init__(self, points: List[Tuple[float, float]], entity_type: str, layer_name: str, closed: bool = False):
    #     super().__init__(entity_type, layer_name)
    #     self.closed = closed
    #     self.polyline = points

    # 是否闭合
    closed: bool = Field(default=False)
    # 构成polyline的点的集合
    points: List[Tuple[float, float]] = Field([])
