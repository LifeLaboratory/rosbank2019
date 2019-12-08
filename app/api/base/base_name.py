WARNING = "Warning"
ERROR = "Error"
OK = "Ok"
SUCCESS = "Success"
ANSWER = "Answer"
SESSION = 'session'

NAME_ACTION = "name_action"
ID_ACTION = "id_action"
NAME_PLATFORM = "platform"
STATS_POSTS_ID = "@статистика_постов"
STATS_POSTS = "статистика_постов"
DESCRIPTION = "description"
FIO = "fio"
IS_OPEN = 'is_open'
IS_VIEW = 'is_view'
ACTIVE = 'active'
TITLE = "title"
URL = "url"
PHOTO = "photo"
CARD = "card"
BUDGET = "budget"
DATA = "data"
COMPANY = "Company"
LOGIN = "login"
PASSWORD = "password"
TYPE = "type"
QUERY = "query"
STATUS = "status"
IMAGE = 'image'
FIELD = "field"
ID_NAME = "id_nom"
ID_USER = "id_user"
ID_PROFILE = "id_profile"
ID_NOTIFICATION = 'id_notification'
ID_STORIES = 'id_stories'
ID_CV = "id_cv"
ID_PROJECT = "id_project"
ID_LESSON = "id_lesson"
ID_NOM = "id_nom"
ID_SALES = "id_sales"
ID_DOCUMENT = "id_document"
IS_LIKE = 'is_like'
ID_CATEGORY = "id_category"
CODE = "code"
CATEGORIES = "categories"
CATEGORY = "category"
INTERVAL = "interval"
ID_USER_NOM = "id_user_nom"
EXPIRED_START = 'expired_start'
EXPIRED_END = 'expired_end'
NAME = "name"
SURNAME = "surname"
EMAIL = "email"
SEX = "sex"
CITY = "city"
EDUCATION = "educational"
LOGO_NAME = "logo_name"
LOGO = "logo"
UUID = "UUID"
PAGE = "page"
ID_NEWS = "id_news"
RATE = "rate"
LINK = "link"

ERROR_EXECUTE_DATABASE = "Fatal error: execute database"
ERROR_CONNECT_DATABASE = "Error connect database"

STATUS_OK = 200
STATUS_PARSE_DATA = 102
STATUS_CONVERTER = 103
STATUS_CHECK_DATA = 104
STATUS_SQL_ERROR = 105
STATUS_AUTH_FAILED = 106

INN = 'ИНН'
BIRTHDAY = 'ДеньРождения'
PLACE_BIRTHDAY = 'МестоРождения'
country_code = 'КодСтраны'
post_code = 'ПочтовыйИндекс'
subject_code_rf = 'СубъектРФ'
area = 'Район'
name_area = 'НаименованиеРайона'
city = 'Город'
name_city = 'ГородНазвание'
locality = 'НаселенныйПункт'
locality_name = 'НаселенныйПунктНазвание'
street = 'Улица'
street_name = 'УлицаНазвание'
house = 'Дом'
house_number = 'НомерДома'
corps = 'Корпус'
corps_number = 'НомерКорпус'
room_number = 'НомерКвартира'
type_doc = 'ВидДокумента'
passport = 'Паспорт'
date_passport = 'ПаспортДатаВыдачи'
issued_passport = 'ПаспортКемВыдан'
code_division = 'КодПодразделения'
residence = 'ВидЖительства'  # 1 - вид на жительство 2 - временное
number_doc_residence = 'ВидЖительстваНомерДок'
date_residence = 'ВидЖительстваДатаВыдачи'
issued_residence = 'ВидЖительстваКемВыдан'
exiration_date_residence = 'ВидЖительстваСрокДействия'
code_activity = 'КодДеятельности'
code_another_activity = 'КодДопДеятельности'
get_answer = 'СпособОтвета'
tel_number = 'НомерТел'
email = 'email'
POSITION = 'position'
attestor = 'Свидетель'
inn_attestor = 'СвидетельИНН'
likes = 'лайки'
views = 'просмотры'
comments = 'комментарии'
post = 'пост'
post_id = "@пост"
post_title = "заголовок"
post_text = "текст"
post_photo = "фото"
it = "номенклатура"
date_time = "датавремя"
post_deleted = 'удален'
post_draft = 'черновик'
face = 'лицо'
nom_id = 'номенклатура'
nom_name = 'наименование'
nom_text = 'описание'
nom_category = 'категория'
nom_price = 'цена'
nom_photo = 'фото'
movement = 'movement'
client = 'клиент'

socnet_id = '@соцсеть'
socnet = 'соцсеть'

qty = 'количество'
nom_field = [nom_name, nom_text, nom_category, nom_price, nom_photo, post_deleted]
post_fields = [post_draft, post_deleted, post_photo, post_text, post_title, date_time]
double_prec = [nom_price]
bool = [post_deleted, post_draft]
date_time_fields = [date_time]
face_id = "@user"

print_form_fields = [
    INN,
    BIRTHDAY,
    PLACE_BIRTHDAY,
    country_code,
    post_code,
    subject_code_rf,
    area,
    name_area,
    city,
    name_city,
    locality,
    locality_name,
    street,
    street_name ,
    house,
    house_number,
    corps,
    corps_number,
    room_number,
    type_doc,
    passport,
    date_passport,
    issued_passport,
    code_division,
    residence,
    number_doc_residence,
    date_residence,
    issued_residence,
    exiration_date_residence,
    code_activity,
    code_another_activity,
    get_answer,
    tel_number,
    email
]

CORS_HEADERS = {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
                }
