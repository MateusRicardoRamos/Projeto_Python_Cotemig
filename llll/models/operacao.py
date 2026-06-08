from datetime import datetime

from . import db


class Operacao(db.Model):
    """Model — dados e acesso ao banco (tabela operacoes)."""

    __tablename__ = "operacoes"
    
    # insira as operações

    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Float, nullable=False)
    num2 = db.Column(db.Float, nullable=True)
    operacao = db.Column(db.String, nullable=False)
    etapas = db.Column(db.Integer, nullable=False)
    resultado = db.Column(db.Integer, nullable=False)
    criado_em = db.Colunm(db.DateTime, default = datetime.now)


    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado, criado_em):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
        )
        
        #insira os comandos para salvar

        db.session.add(registro)
        db.session.commit()
        return registro

    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.criado_em.desc()).limit(limite).all()
        )

    def __repr__(self):
        return f"<Operacao {self.id}: {self.etapas}>"