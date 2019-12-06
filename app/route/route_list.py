from app.route.notifications.route import Notification, Notification_get
from app.route.stories.route import Stories
from app.route.user.route import Auth
from app.route.profile.route import Profile
from app.route.statistic.route import Statistic


ROUTES = {
    '/api/stories': Stories,
    '/api/notifications': Notification,
    '/api/notifications/<int:id_user>': Notification_get,
    '/api/auth': Auth,
    '/api/profile/<int:id_user>': Profile,
    '/api/statistic': Statistic,
}
