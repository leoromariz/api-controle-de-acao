from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from flask_cors import CORS

from logger import logger
from model.operacao import Operacao
from model import Session
from schemas import *
from flask_cors import CORS

info = Info(title="Controle de ação", version="1.0.0")
app = OpenAPI(__name__,info=info)
CORS(app)

# defining tags
home_tag = Tag(name="Documentação", description="Documentação da API")
operacao_tag = Tag(name="Operações", description="Cria, lista e deleta operações do banco de dados")
acao_tag = Tag(name="Ação", description="Cria lista de ações")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/operacao', tags=[operacao_tag],
          responses={"200": OperacaoSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_operacao(form: OperacaoSchema):
    """Adiciona uma nova Operação à base de dados

    Retorna uma representação das operações e ações associados.
    """
    operacao = Operacao(
        sigla_acao=form.sigla_acao,
        tp_operacao=form.tp_operacao,
        quantidade=form.quantidade,
        valor=form.valor,)
    if form.tp_operacao not in ["Compra", "Venda"]:
            return {"message": "Tipo de operação inválido."}, 400
    logger.debug(f"Adicionando operação de sigla: '{operacao.sigla_acao}'")
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando acao
        session.add(operacao)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado operação de sigla: '{operacao.sigla_acao}'")
        return apresenta_operacao(operacao), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova operação :/"
        logger.warning(f"Erro ao adicionar operação '{operacao.sigla_acao}', {error_msg} - {e}")
        return {"mesage": error_msg}, 400
    
@app.get('/operacoes', tags=[operacao_tag],
         responses={"200": ListagemOperacoesSchema, "404": ErrorSchema})
def get_opeacoes():
    """Faz a busca por todas as Operações cadastradas

    Retorna uma representação da listagem de Operações.
    """
    try:
        logger.debug("Buscando operações cadastradas - {e}")
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        operacoes = session.query(Operacao).all()

        if not operacoes:
            # se não há operações cadastradas
            return {"operacoes": []}, 200
        else:
            logger.debug(f"Encontradas {len(operacoes)} operações cadastradas")
            # retorna a representação das ações
            print(operacoes)
            return apresenta_operacoes(operacoes), 200
        
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível buscar as operações :/"
        logger.warning(f"Erro ao buscar operações, {error_msg} - {e}")
        return {"mesage": error_msg}, 404
    
@app.delete('/operacao', tags=[operacao_tag],
            responses={"200": OperacaoDelSchema, "404": ErrorSchema})
def del_acao(query: OperacaoBuscaSchema):
    """Deleta uma Operação a partir do id da Operação informada

    Retorna uma mensagem de confirmação da remoção.
    """
    try:
        logger.debug(f"Removendo operação de id: '{query.id}'")
        id = unquote(query.id)
        print(id)
        # criando conexão com a base
        session = Session()
        # fazendo a remoção
        count = session.query(Operacao).filter(Operacao.id == int(id)).delete()
        session.commit()

        if count:
            # retorna a representação da mensagem de confirmação
            return {"mesage": "Operação removida", "id": id}
        else:
            # se a operação não foi encontrado
            error_msg = "operação não encontrado na base :/"
            return {"mesage": error_msg}, 404
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível remover a operação :/"
        logger.warning(f"Erro ao remover operação '{query.id}', {error_msg} - {e}")
        return {"mesage": error_msg}, 404
    
@app.get('/operacao', tags=[operacao_tag],
         responses={"200": OperacaoSchema, "404": ErrorSchema})
def get_operacao(query: OperacaoBuscaSchema):
    """Faz a busca por uma Operacao a partir do id da Operação

    Retorna uma representação das Operações e ações associadas.
    """
    id = query.id
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    operacao = session.query(Operacao).filter(Operacao.id == id).first()

    if not operacao:
        # se a operação não foi encontrada
        error_msg = "Operação não encontrada na base :/"
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação da operação
        return apresenta_operacao(operacao), 200