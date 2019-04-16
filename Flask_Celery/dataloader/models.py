    from datetime import datetime
from dataloader import db


class GenData(db.Model):
    gen = db.Column(db.String(40), nullable=False)
    test = db.Column(db.String(40), nullable=False)
    tmp = db.Column(db.Float(), nullable=False)
    update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

