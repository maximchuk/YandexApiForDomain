from django.contrib import auth

from .models import MailAdmin


TOKEN = MailAdmin.objects.get(id = 1).token2 # Token APIv.2
token = MailAdmin.objects.get(id = 1).token1 # Token APIv.1
DOMAIN = MailAdmin.objects.get(id = 1).name #


URL_API = 'https://pddimp.yandex.ru' #
URL_GET_LIST = '/api2/admin/email/list?token=%s&domain=%s' % (TOKEN, DOMAIN)#
URL_GET_LIST_PAGE = '/api2/admin/email/list?token=%s&domain=%s&page=%s'
URL_GET_FORVARD_LIST = '/get_forward_list.xml?token=%s&login=%s' #
URL_SET_FORVARD = '/set_forward.xml?token=%s&login=%s&address=%s&copy=%s' # token, login, email for forward, copy
URL_REG_USER_token = '/reg_user_token.xml?token=%s&u_login=%s&u_password=%s' # Регистрация почтового ящика
URL_REG_USER_TOKEN = '/api2/admin/email/add?token=%s&domain=%s&login=%s&password=%s' # Регистрация почтового ящика
URL_DEL_USER = '/delete_user.xml?token=%s&login=%s'
URL_DEL_FORWARD = '/delete_forward.xml?token=%s&login=%s&filter_id=%s'
URL_EDIT_USER = '/edit_user.xml?token=%s&login=%s&password=%s&domain_name=%s&iname%s=&fname=%s&sex=%s&hintq=%s&hinta=%s'
