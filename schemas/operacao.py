from pydantic import BaseModel, ConfigDict
from typing import List
from model.operacao import Operacao


class OperacaoSchema(BaseModel):
    """ Define uma nova operação a ser inserida e como deve ser representado
    """
    sigla_acao: str = "PETR4"
    tp_operacao: int = 1
    quantidade: int = 100
    valor: float = 37.50
    
class OperacaoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id da operação.
    """
    id: str = 1


class ListagemOperacoesSchema(BaseModel):
    """ Define como uma listagem de operações será retornada.
    """
    operacoes:List[OperacaoSchema]


def apresenta_operacoes(operacoes: List[Operacao]):
    """ Retorna uma representação das operações seguindo o schema definido em
        AcoesViewSchema.
    """
    result = []
    for operacoes in operacoes:
        result.append({
            "sigla_acao": operacoes.sigla_acao,
            "tp_operacao": operacoes.tp_operacao,
            "quantidade": operacoes.quantidade,
            "valor": operacoes.valor,
            
        })

    return {"operacoes": result}


class OperacaoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    sigla_acao: str

def apresenta_operacao(operacao: Operacao):
    """ Retorna uma representação da operação seguindo o schema definido em
        OperacaoViewSchema.
    """
    return {
        "id": operacao.id,
        "sigla_acao": operacao.sigla_acao,
        "quantidade": operacao.quantidade,
        "valor": operacao.valor,
        "tp_operacao": operacao.tp_operacao,
    }

    
