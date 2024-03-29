from app.route.notifications.route import Notification, NotificationGet
from app.route.stories.route import Stories, StoriesList
from app.route.stories.route import StoriesStatus
from app.route.stories.route import StoriesInsert
from app.route.stories.route import StoriesProfile
from app.route.stories.route import StoriesUpdate
from app.route.user.route import Auth
from app.route.profile.route import Profile
from app.route.statistic.route import Statistic, StatisticView
from app.route.features.route import Features, FeaturesAdd

ROUTES = {
    '/api/stories': Stories,
    '/api/stories/add': StoriesInsert,
    '/api/stories/profile/<int:id_profile>': StoriesProfile,
    '/api/stories/update': StoriesUpdate,
    '/api/stories/update_status': StoriesStatus,
    '/api/notifications': Notification,
    '/api/notifications/<int:id_user>': NotificationGet,
    '/api/auth': Auth,
    '/api/profile': Profile,
    '/api/features/<int:id_user>': Features,
    '/api/features/add': FeaturesAdd,
    '/api/statistic': Statistic,
    "/api/statistic/<int:id_user>": StatisticView,
    "/api/stories/<int:id_user>": StoriesList
}
