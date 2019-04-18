from dataloader import db
from dataloader.models import GenData

db.drop_all()
db.create_all()

"""
gen = GenData(gen='asd', test='s01',tpm=12345)
db.session.add(gen)
db.session.commit()


    id = db.Column('id', db.Integer, primary_key=True)
    gen = db.Column(db.String(40), nullable=False)
    test = db.Column(db.String(40), nullable=False)
    tpm = db.Column(db.Float(), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
"""