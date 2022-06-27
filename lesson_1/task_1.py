import re


def find_domain_name(url):
    pattern = r'(https?://)?(www.)?([A-Za-z_0-9-]+).*'
    return re.search(pattern, url).group(3)


assert find_domain_name('http://google.com') == 'google'
assert find_domain_name('http://google.co.jp') == 'google'
assert find_domain_name('www.xakep.ru') == 'xakep'
assert find_domain_name('https://youtube.com') == 'youtube'
