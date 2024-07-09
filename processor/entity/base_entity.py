from pydantic import Field, BaseModel


class BaseEntity(BaseModel):
    # def __init__(self, entity_type: str, layer_name: str):
    #     self.entity_type = entity_type
    #     self.layer_name = layer_name

    # entity类型
    entity_type: str = Field(default='UNKNOWN')
    # 所在图层
    layer_name: str = Field(default='UNKNOWN')
