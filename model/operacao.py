from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from datetime import datetime
from typing import Union
from model.base import Base

class Operacao(Base):
    __tablename__ = 'operacao'

    id = Column(Integer, primary_key=True)
    sigla_acao = Column(String(10))
    tp_operacao = Column(String(10))
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, sigla_acao:str, tp_operacao:str, quantidade:int, valor:float, data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Operação

        Arguments:
            tipoOperacao: 1 = Compra , 2 = Venda
            quantidade: quantidade que se espera comprar daquele ação
            valor: valor esperado para a ação
            data_insercao: data de quando a operação foi feito ou inserido
                           à base
        """

        self.sigla_acao = sigla_acao
        self.quantidade = quantidade
        self.valor = valor
        self.tp_operacao = tp_operacao
        if data_insercao:
            self.data_insercao = data_insercao

