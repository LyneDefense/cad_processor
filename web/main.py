from typing import Dict

import uvicorn
from fastapi import FastAPI, APIRouter

# from CadRecognition.custom_logging import CustomizeLogger, global_logger
import warnings

from uvicorn import Config, Server

from web.resource import router

# 本地运行测试用

warnings.filterwarnings("ignore")  # 日志中不显示代码的warnning


def make_app(title: str = "FastAPI", version: str = "0.1.0", description: str = "", contact: Dict = None):
    app = FastAPI(title=title, version=version, description=description, contact=contact)
    app.include_router(router)
    return app


app = make_app(title="dxf解析服务", version="1.0", description="dxf解析服务",
               contact={"server_consumer": "xxx", "server_provider": "xxx"})

