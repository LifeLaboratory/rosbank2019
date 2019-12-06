from app.route.user.route import Auth, Register
from app.route.profile.route import Profile


ROUTES = {
    '/register': Register,
    '/auth': Auth,
    '/profile/<int:id_user>': Profile,
}
