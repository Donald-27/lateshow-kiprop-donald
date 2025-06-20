from app import app, db
from models import Episode, Guest, Appearance

with app.app_context():
    print("🌱 Seeding database...")

    db.drop_all()
    db.create_all()

    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)

    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    g3 = Guest(name="Tracey Ullman", occupation="television actress")

    a1 = Appearance(rating=4, guest=g1, episode=ep1)
    a2 = Appearance(rating=5, guest=g3, episode=ep2)
    db.session.add_all([ep1, ep2, g1, g2, g3, a1, a2])
    db.session.commit()

    print("Done seeding!")
