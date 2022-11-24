from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from time import sleep
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)



@app.get("/")
async def get():
    return 'hello'




@app.websocket("/socket")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # sleep(2)
        # await websocket.receive_text()
        await websocket.send_json({'abcd':'manjith'})
        return 'aaaaaa'
