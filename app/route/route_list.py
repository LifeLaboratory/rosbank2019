from app.route.user.route import Auth
from app.route.profile.route import Profile
from app.route.statistic.route import Statistic, StatisticView

ROUTES = {
    '/api/auth': Auth,
    '/api/profile/<int:id_user>': Profile,
    '/api/statistic': Statistic,
    "/api/statistic/<int:id_user>": StatisticView
}
