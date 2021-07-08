from little_notes.ext.auth import login_manager
from little_notes.ext.db.models import User


@login_manager.user_loader
def load_user(user_id: int):
    return User.query.get(int(user_id))
