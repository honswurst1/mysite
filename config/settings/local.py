from .base import *
DEBUG = env.bool("DJANGO_DEBUG" , default=True)
SECRET_KEY = env('DJANGO_SECRET_KEY', default='rb%+0b#0*(ooi)d7+g%b4y2&=k3m=ajq#&0$b2c6hutfazu&69')
