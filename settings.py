from os import getenv, environ
from pathlib import Path
from environs import Env


class Config:
    def __init__(
        self,
        usr,
        pwd,
        url,
        port,
        secret_key,
        database,
        collections,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.usr = usr
        self.pwd = pwd
        self.url = url
        self.port = port
        self.secret_key = secret_key
        self.database = database
        self.collections = collections


Cfg = Config

p = Path(".") / ".env"

env = Env()
env.read_env(p / ".env", recurse=False)

with env.prefixed("BKP_MONGO_"):
    ENV = env("ENV")
    if ENV == "production":
        env.read_env(p / ".env.production", recurse=False)
    elif ENV == "staging":
        env.read_env(p / ".env.staging", recurse=False)
    elif ENV == "development":
        env.read_env(p / ".env.development", recurse=False)
    else:
        pass

    Cfg.usr = env("USR")
    Cfg.pwd = env("PWD")
    Cfg.url = env("URL")
    Cfg.port = env.int("PORT", 27017)
    Cfg.secret_key = env("SECRET_KEY")
    Cfg.database = env("DATABASE")
    Cfg.collections = env("COLLECTIONS")
