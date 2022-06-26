from fastapi import FastAPI
from pydantic import BaseModel
from nameko.rpc import rpc
from nameko.standalone.rpc import ClusterRpcProxy

class User(BaseModel):
    username: str
    password: str
    email: str

class Login(BaseModel):
    username: str
    password: str

app = FastAPI()
broker_cfg = {'AMQP_URI': "amqp://guest:guest@mqrabbit"}

@app.post("/add/")
def api(user_item: User):
    with ClusterRpcProxy(broker_cfg) as rpc:
        sid = rpc.useradd.insert(user_item.username, user_item.password, user_item.email)
        return {'results': 'registered'}

@app.post("/login/")
def api(login_item: Login):
    with ClusterRpcProxy(broker_cfg) as rpc:
        result = rpc.Check.query(login_item.username, login_item.password)
        if result == 0:
            return {'results': 'login not success'}
        else:
            return {'results': 'login success'}
