#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"十水"
SITENAME = u"日记本:十水说"
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}.html'
DISPLAY_PAGES_ON_MENU = True
FEED = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None


DEFAULT_LANG = 'en'

THEME = 'waterspill'

# Blogroll
LINKS =  ((u"王小峰", 'http://www.wangxiaofeng.net/'),
          (u"牛博", 'http://www.bullock.cn/'),
          (u"尹珊珊", 'http://hi.baidu.com/girlvia'),
          (u"苗师傅", 'http://miaowei.net/'),
          (u"陈晓卿", 'http://hizi17881965.spaces.live.com/'),
          (u"土摩托", 'http://www.immusoul.com/'),
          (u"乔小刀", 'http://blog.sina.com.cn/u/1407225950'),
          (u"傅真", 'http://fz0512.com/archives/1218'),
          (u"Apollo", 'http://imapollo.blogbus.com/'),
          (u"卯卯", 'http://blog.sina.com.cn/wangmomo'),
          (u"姐姐", 'http://daidaidaidaihuar.spaces.live.com/'),
          (u"飞扬", 'http://blog.sina.com.cn/feiyangxiao'),
          (u"杨乐", 'http://blog.sina.com.cn/lelegna'),
          (u"vivi", 'http://sunshinegirl-vivi.blogbus.com/'),
          (u"西米", 'http://xs1234.blogbus.com/'),
          (u"润声", 'http://huangrs555.blogbus.com/'),
          (u"晨曦", 'http://dymicx.blogbus.com/'),
          (u"Prekop", 'http://yangzetian.github.com/'),)


# Social widget
SOCIAL = (('Douban', 'http://www.douban.com/people/louxiaomi/'),
          ('Weibo', 'http://weibo.com/cinderelladaidai'),)

DEFAULT_PAGINATION = 10
