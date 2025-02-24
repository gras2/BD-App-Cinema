from sqlalchemy.orm import Session
from models import Usuario, Filme, Avaliacao, SolicitacaoFilme, Tag
from schemas import UsuarioCreate, FilmeCreate, AvaliacaoCreate, SolicitacaoFilmeCreate

# 📌 CRUD para Usuário
def criar_usuario(db: Session, usuario: UsuarioCreate):
    novo_usuario = Usuario(username=usuario.username, email=usuario.email, senha=usuario.senha)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def buscar_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def buscar_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

# 📌 CRUD para Filmes
def criar_filme(db: Session, filme: FilmeCreate):
    novo_filme = Filme(
        nome=filme.nome,
        ano=filme.ano,
        diretor=filme.diretor,
        genero=filme.genero,
        sinopse=filme.sinopse
    )
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

def listar_filmes(db: Session):
    return db.query(Filme).all()

def buscar_filme_por_id(db: Session, filme_id: int):
    return db.query(Filme).filter(Filme.id == filme_id).first()

# 📌 CRUD para Avaliações
def criar_avaliacao(db: Session, avaliacao: AvaliacaoCreate):
    nova_avaliacao = Avaliacao(
        usuario_id=avaliacao.usuario_id,
        filme_id=avaliacao.filme_id,
        nota=avaliacao.nota,
        comentario=avaliacao.comentario
    )
    db.add(nova_avaliacao)
    db.commit()
    db.refresh(nova_avaliacao)
    return nova_avaliacao

def listar_avaliacoes_por_filme(db: Session, filme_id: int):
    return db.query(Avaliacao).filter(Avaliacao.filme_id == filme_id).all()

# 📌 CRUD para Solicitação de Filmes
def criar_solicitacao_filme(db: Session, solicitacao: SolicitacaoFilmeCreate):
    nova_solicitacao = SolicitacaoFilme(
        nome=solicitacao.nome,
        ano=solicitacao.ano,
        diretor=solicitacao.diretor,
        genero=solicitacao.genero,
        sinopse=solicitacao.sinopse,
        usuario_id=solicitacao.usuario_id
    )
    db.add(nova_solicitacao)
    db.commit()
    db.refresh(nova_solicitacao)
    return nova_solicitacao

def listar_solicitacoes_pendentes(db: Session):
    return db.query(SolicitacaoFilme).filter(SolicitacaoFilme.aprovado == False).all()

def aprovar_solicitacao(db: Session, solicitacao_id: int):
    solicitacao = db.query(SolicitacaoFilme).filter(SolicitacaoFilme.id == solicitacao_id).first()
    if solicitacao:
        solicitacao.aprovado = True
        db.commit()
        db.refresh(solicitacao)
    return solicitacao

# 📌 CRUD para Tags
def criar_tag(db: Session, nome: str):
    nova_tag = Tag(nome=nome)
    db.add(nova_tag)
    db.commit()
    db.refresh(nova_tag)
    return nova_tag

def buscar_tag_por_nome(db: Session, nome: str):
    return db.query(Tag).filter(Tag.nome == nome).first()
