from app.route.user.route import Auth
from app.route.profile.route import Profile


ROUTES = {
    'api/auth': Auth,
    'api/profile/<int:id_user>': Profile,
}
