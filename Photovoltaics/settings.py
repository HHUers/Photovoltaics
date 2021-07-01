import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-40-p(6se5xeka8zzs^3!5s=qqvnlh2^@ua$6ksi(d8dapq+7fa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False


ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # 第三方 app 注册
    'simpleui',
    'pure_pagination',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 自定义 app 注册
    'apps.web.apps.WebConfig',
    'apps.users.apps.UsersConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Photovoltaics.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Photovoltaics.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
        'NAME': 'photovoltaics',
        # 避免映射数据库时出现警告
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# 设置静态路径
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 重载AUTH_USER_MODEL
AUTH_USER_MODEL = "users.UserProfile"

# 主题设置
SIMPLEUI_DEFAULT_THEME = 'dark.green.css'
SIMPLEUI_HOME_TITLE = '光伏发电管理'
SIMPLEUI_HOME_ICON = 'fa fa-user'
SIMPLEUI_ANALYSIS = False
SIMPLEUI_HOME_INFO = False
SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['项目概况', '厂址概况', '气象特征要素', '光伏发电系统', '权限认证'],  # 开启排序和过滤功能
    'menus': [
        {
            'name': '项目概况',
            'icon': 'fas fa-tasks',
            'url': 'web/projectoverview/'
        },
        {
            'name': '厂址概况',
            'icon': 'fas fa-map-marker',
            'url': 'web/siteprofile/'
        },
        {
            'name': '气象特征要素',
            'icon': 'fas fa-thermometer-empty',
            'url': 'web/temperature/'
        },
        {
            'name': '光伏发电系统',
            'icon': 'fas fa-bolt',
            'url': 'web/pvsystem/'
        },
        {
            'app': 'auth',
            'name': '权限认证',
            'icon': 'fas fa-user-shield',
            'models': [
                {
                    'name': '用户',
                    'icon': 'fa fa-user',
                    'url': 'users/userprofile/'
                },
                {
                    'name': '组',
                    'icon': 'fa fa-users',
                    'url': 'auth/group/'
                }
            ]
        }
    ]
}

# django-pure-pagination 分页设置
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 4,  # 分页条当前页前后应该显示的总页数（两边均匀分布，因此要设置为偶数），
    'MARGIN_PAGES_DISPLAYED': 2,  # 分页条开头和结尾显示的页数
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,  # 当请求了不存在页，显示第一页
}