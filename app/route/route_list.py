from app.route.user.route import Auth, Register
from app.route.profile.route import Profile
from app.route.notifications.route import Notification, Notification_get


ROUTES = {
    '/register': Register,
    '/auth': Auth,
    '/notifications': Notification,
    '/profile/<int:id_user>': Profile,
    '/notifications/<int:id_user>': Notification_get,
}
