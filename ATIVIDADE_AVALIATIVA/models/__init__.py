# Aqui nasce o "db" — é ele que conversa com o arquivo .db do SQLite.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# O PONTO (.) no import = "pega da MESMA pasta models/"
from .base import ModeloBase
from .filme import Filme
from .ingresso import Ingresso
from .sala import Sala
from .sessao import Sessao

__all__ = ["db", "ModeloBase", "Filme", "Sala", "Sessao", "Ingresso"]
