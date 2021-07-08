from little_notes.ext.db.models import User


def test_user_create(session):
    user = User(username="gabriel", email="gabriel@email.com", password="123456")
    session.add(user)
    session.commit()
    assert user.id > 0


def test_user_list(session):
    user = User(username="gabriel", email="gabriel@email.com", password="123456")
    session.add(user)
    session.commit()
    assert len(User.query.all()) > 0


def test_user_filter(session):
    user = User(username="gabriel", email="gabriel@email.com", password="123456")
    session.add(user)
    session.commit()
    user1 = User.query.filter(User.id == 1).first()
    user2 = User.query.get(1)
    assert user1 == user2
    assert user1.username == user2.username
    assert user1.created_at == user2.created_at


def test_user_delete(session):
    user = User(username="gabriel", email="gabriel@email.com", password="123456")
    session.add(user)
    session.commit()
    assert user.id > 0
    session.delete(user)
    session.commit()
    assert len(User.query.all()) == 0
