import uvicorn

if __name__ == '__main__':
    uvicorn.run("web.main:app", host="0.0.0.0", port=8890, reload=True, use_colors=True)
