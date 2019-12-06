from app.route.user.route import Auth
from app.route.profile.route import Profile
from app.route.statistic.route import Statistic


ROUTES = {
    '/api/auth': Auth,
    '/api/profile/<int:id_user>': Profile,
    '/api/statistic': Statistic,
}
