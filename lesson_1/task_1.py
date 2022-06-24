def find_domain_name(url):
    if 'http://www.' in url:
        s = url.partition('://www.')[2]
        domain = s.split('.')[0]
        return domain
    elif 'https://www.' in url:
        s = url.partition('://www.')[2]
        domain = s.split('.')[0]
        return domain
    elif 'https://' in url:
        s = url.partition('https://')[2]
        domain = s.split('.')[0]
        return domain
    elif 'www.' in url:
        s = url.partition('www.')[2]
        domain = s.split('.')[0]
        return domain
    else:
        domain = url[7:].split('.')[0]
        return domain


assert find_domain_name('http://google.com') == 'google'
assert find_domain_name('http://google.co.jp') == 'google'
assert find_domain_name('www.xakep.ru') == 'xakep'
assert find_domain_name('https://youtube.com') == 'youtube'
