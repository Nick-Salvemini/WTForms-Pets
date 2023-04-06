"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

p1 = Pet(name='Jojo', species='Ferret', photo_url='https://images.unsplash.com/photo-1615087240969-eeff2fa558f2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1160&q=80', age=3, notes='Very smelly.', available=True)
p2 = Pet(name='Reptar', species='Gecko', photo_url='https://images.unsplash.com/photo-1600029175350-55029fd344b5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80', age=10, notes='Licks his/her eye, very cute.', available=True)
p3 = Pet(name='Ollie', species='Dog', photo_url='https://images.unsplash.com/photo-1604802108945-6324e7ecf45b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80', age=4, notes='Will love you aggresively, best boy.', available=True)
p4 = Pet(name='Xander', species='Cat', photo_url='https://images.unsplash.com/photo-1660053516772-24e56eae6a07?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80', age=7, notes='Chubby, very lazy, sweet.', available=True)
p5 = Pet(name='Luna', species='Cat', photo_url='https://images.unsplash.com/photo-1604916287784-c324202b3205?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=627&q=80', age=3, notes='She is a shadow.', available=True)
p6 = Pet(name='Taylor', species='Dog', photo_url='https://images.unsplash.com/photo-1552053831-71594a27632d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1862&q=80', age=11, notes='Very playful, best girl', available=True)
p7 = Pet(name='Gracie', species='Cat', photo_url='https://images.unsplash.com/photo-1543198364-e5d4f3627a02?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=627&q=80', age=6, notes='Demands the exact correct number of pets. Do not go one pet over.', available=True)
p8 = Pet(name='Ham', species='Pig', photo_url='https://images.unsplash.com/photo-1587618420273-7cdff5114eb5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=628&q=80', age=2, available=True)
p9 = Pet(name='Sebastian', species='Fish', photo_url='https://images.unsplash.com/photo-1539236754983-085fe1449ba4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=718&q=80', notes='Fish are terrible pets.', available=False)
p10 = Pet(name='Chonk', species='Chinchilla', photo_url='https://images.unsplash.com/photo-1628832824905-819f2385fd82?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80', age=5, notes='Very cute when taking a dust bath.', available=True)

db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10])
db.session.commit()