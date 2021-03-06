from datetime import datetime
from dataloader import db


class GenData(db.Model):
    __tablename__ = 'gen_data'
    id = db.Column('id', db.Integer, primary_key=True)
    gen = db.Column(db.String(40), nullable=False)
    test = db.Column(db.String(40), nullable=False)
    tpm = db.Column(db.Float(), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return "<Book(Gen='{}', Sample='{}', TPM={})>".format(
                self.gen, self.test, self.tpm)
