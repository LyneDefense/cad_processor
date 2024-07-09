import os

from fastapi import APIRouter, HTTPException, Request

from processor.cad_reader import parse_source_entity_by_layer

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.post("/dxf/parse")
async def create_upload_file(request: Request):
    # 从请求体中读取表单数据
    form = await request.form()
    file = form["file"]  # 假设HTML表单中的文件字段名为"file"

    # 检查文件名是否以.dxf结尾
    filename = file.filename
    if not filename.lower().endswith(".dxf"):
        raise HTTPException(status_code=400, detail="Invalid file extension. Only .dxf files are allowed.")
    # 将上传的文件保存到临时文件中
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, 'wb') as temp_file:
        contents = await file.read()  # 读取文件内容
        temp_file.write(contents)  # 将内容写入临时文件

    # 使用ezdxf.read从保存的文件中读取DXF数据
    try:
        response = parse_source_entity_by_layer(filename, temp_file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # 删除临时文件
        os.remove(temp_file_path)
    return response
