import common

domain="http://localhost:9031/nisg"

access_token = ''
def getUrl(uri):
    return domain+uri

print('==> test login system <===')

# admin登录
headers=common.login("SckY4x8ZKcXREQLYphA63UfVxg8C+b51BXNqyOSuSBF/OGbrqxrJT56ZOrivquf8HqWooqhbLzESZNFN2bUQdQgLRroUYep1hfFj3eGj2GRxRYEAWLZ58zT3DEfeRo1jYi+UBSJsncRBoDpIHQA4fkgTAFqxWXvpcfuvCn/gOn4=","cdD4jBcXaI0GAuqik10zdnEpi7ZGDDYMXjNNleRb4TRoJkaTAhjkLfgnXI6XUWKGfMR124fYDDBE0rOw8yZzNSDxWtwDhd+O0fYt+v5XdkK8iHRXC5G6m6YHbGTGDZRO2GyzKaIdK1INUa1ZM0ZFcEOcPp7Hi7BCXSnYTe8oj5E=")
print(headers)

