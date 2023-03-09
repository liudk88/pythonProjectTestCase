import common

domain="http://localhost:9031/api"
# domain="https://zjjtest.sz.gov.cn/itom/nisg"
access_token = ''
def getUrl(uri):
    return domain+uri

print('==> test login system <===')

headers=common.login("admin","SGN4YTIwMTkh")
print headers

