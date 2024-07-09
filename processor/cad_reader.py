import ezdxf

from processor.entity.cad_file import CadFile
from processor.entity.polyline import Polyline
from processor.entity.text import Text


def parse_source_entity_by_layer(file_name: str, file_path: str) -> CadFile:
    """
    解析dxf里各图层的entity
    :param file_name: 文件名
    :param dxf_path: dxf文件路径
    :return: {layer_name: entity list}
    """
    doc = ezdxf.readfile(file_path)
    # 获取模型空间
    msp = doc.modelspace()
    entities = []
    for entity in msp:
        if hasattr(entity.dxf, 'layer'):
            # 获取实体的图层
            layer_name = entity.dxf.layer
            if entity.dxftype() == 'TEXT' or entity.dxftype() == 'MTEXT':
                insert_points = (entity.dxf.insert[0], entity.dxf.insert[1])
                # 这里MTExt也转换成了Text
                text = Text(entity_type='TEXT', layer_name=layer_name, insert_points=insert_points,
                            content=entity.dxf.text)
                entities.append(text)
            elif entity.dxftype() == 'LWPOLYLINE':
                points = entity.get_points(format='xy')  # 获取x, y坐标
                points = [point for point in points]  # 转换为列表
                polyline = Polyline(points=points, entity_type=entity.dxftype(), layer_name=layer_name,
                                    closed=entity.is_closed)
                entities.append(polyline)
            else:
                print("未识别的entity类型", entity.dxftype())
    return CadFile(file_name=file_name, entities=entities)


if __name__ == '__main__':
    with open("/Users/pinjiehu/Desktop/总图测试_t3.dxf", 'rt') as file_obj:
        parse_source_entity_by_layer(file_obj)
