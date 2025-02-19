# -*- coding: utf-8 -*-

from urllib import request
import json

channels_url = 'https://raw.githubusercontent.com/bitsbb01/ez-iptvcat-scraper2/main/data/all-by-country.json'
channels_json = request.urlopen(channels_url).read().decode('utf8')
channels = json.loads(channels_json)

f = open('channels.m3u', 'w+', encoding='utf-8')

f.write('#EXTM3U\n')

for i in range(len(channels['Categories'])):
    for j in range(len(channels['Categories'][i]['Channels'])):
        line_1 = '#EXTINF:-1 group-title="' + channels['Categories'][i]['Name'] + '",' + channels['Categories'][i]['Channels'][j]['Name'] + '\n'
        m3u8_url = 'https://raw.githubusercontent.com/bitsbb01/IPTV-M3US/master/m3us/tvchans.m3u' + channels['Categories'][i]['Channels'][j]['Vid'] + '.m3u8'
        f.write(line_1)
        f.write(m3u8_url + '\n')

f.close()
