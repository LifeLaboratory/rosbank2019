from app.route.user.route import Auth, Register
from app.route.profile.route import Profile
from app.route.statistic.route import Statistic





ROUTES = {
    '/register': Register,
    '/auth': Auth,
    '/profile/<int:id_user>': Profile,
    '/api/statistic': Statistic,

}
