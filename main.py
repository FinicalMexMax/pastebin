from fastapi import FastAPI

import uvicorn


app = FastAPI()


@app.get('/')
def page_home():
    return {'data': 'Hello!', 'status_code': 200}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)