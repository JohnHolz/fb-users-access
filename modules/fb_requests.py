import requests 

### Pages and page_permissions
def pages(api,business_id,some_value):
    url = "https://graph.facebook.com/{api}/{some_value}/assigned_users?business={business_id}".format(api=api,business_id = business_id,some_value = some_value)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)

def page_permissions(token,api,business_id,some_value):
    url = "https://graph.facebook.com/{api}/{some_value}/assigned_users?business={business_id}".format(api=api,business_id = business_id,some_value = some_value)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)


### apps and app_permissions
def apps_permissions(token,business_id,api,some_value): 
    url = "https://graph.facebook.com/{api}/{some_value}/assigned_users?business={business_id}".format(api = api, business_id = business_id,some_value = some_value)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)
    
def apps(token,business_id):
    url = "https://graph.facebook.com/{business_id}/owned_apps".format(business_id = business_id)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)


### ad accounts and permissions
def ad_accounts(token, business_id, api):
    url = "https://graph.facebook.com/{api}/{business_id}/owned_ad_accounts".format(business_id = business_id,api=api)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)
    
def ad_account_premissions(token, api, act, business_id):
    url = "https://graph.facebook.com/{api}/{act}/assigned_users?business={business_id}".format(api = api, act = act, business_id = business_id)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)


### assets and permissions
def assets(token, api, business_id):
    url = "https://graph.facebook.com/{api}/{business_id}/owned_ad_accounts".format(api = api, business_id = business_id)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)

def assets_permissions(token, api, act, business_id):
    url = "https://graph.facebook.com/{api}/{act}/assigned_users?business={business_id}".format(api = api, act=act, business_id = business_id)
    payload={}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    return requests.request("GET", url, headers=headers, data=payload)