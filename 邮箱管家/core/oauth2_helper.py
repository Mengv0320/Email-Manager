# -*- coding: utf-8 -*-
"""
OAuth2 授权助手 - 使用 Selenium 手动登录获取 Microsoft refresh_token
"""

import urllib.parse
import requests
import secrets
import time
import webbrowser


# Thunderbird 邮件客户端的 Client ID
DEFAULT_CLIENT_ID = "9e5f94bc-e8a4-4e73-b8be-63364c29d753"

# 授权范围
SCOPES = [
    "offline_access",
    "https://outlook.office.com/IMAP.AccessAsUser.All",
    "https://outlook.office.com/SMTP.Send",
]

# 回调地址
REDIRECT_URI = "https://localhost"


class SeleniumOAuth2:
    """使用 Selenium 手动登录获取 OAuth2 Token"""
    
    def __init__(self, client_id=None):
        self.client_id = client_id or DEFAULT_CLIENT_ID
        self.driver = None
    
    def init_driver(self):
        """初始化 - 使用系统默认浏览器"""
        # 不需要 Selenium，直接使用系统浏览器
        return True, None
    
    def close_driver(self):
        """关闭浏览器"""
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            self.driver = None
    
    def get_auth_url(self, email=''):
        """生成授权 URL"""
        state = secrets.token_urlsafe(16)
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'response_mode': 'query',
            'scope': ' '.join(SCOPES),
            'state': state,
        }
        if email:
            params['login_hint'] = email
        
        base_url = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
        return f"{base_url}?{urllib.parse.urlencode(params)}"
    
    def open_browser(self, email=''):
        """打开系统浏览器进行授权"""
        auth_url = self.get_auth_url(email)
        webbrowser.open(auth_url)
        return auth_url
    
    def exchange_code_for_token(self, redirect_url):
        """从重定向 URL 中提取授权码并换取 token"""
        try:
            # 从 URL 中提取 code
            if 'code=' not in redirect_url:
                return None, None, "无效的 URL，找不到授权码"
            
            parsed = urllib.parse.urlparse(redirect_url)
            url_params = urllib.parse.parse_qs(parsed.query)
            
            if 'code' not in url_params:
                return None, None, "无效的 URL，找不到授权码"
            
            auth_code = url_params['code'][0]
            
            # 换取 token
            token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
            data = {
                'client_id': self.client_id,
                'code': auth_code,
                'redirect_uri': REDIRECT_URI,
                'grant_type': 'authorization_code',
                'scope': ' '.join(SCOPES),
            }
            
            response = requests.post(token_url, data=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                refresh_token = result.get('refresh_token')
                if refresh_token:
                    return self.client_id, refresh_token, None
                else:
                    return None, None, "未获取到 refresh_token"
            else:
                error_data = response.json()
                error = error_data.get('error_description', response.text)
                return None, None, f"获取 Token 失败: {error}"
        except Exception as e:
            return None, None, f"授权过程出错: {str(e)}"
    
    def authorize_semi_auto(self, email='', progress_callback=None, timeout=120):
        """半自动模式 - 打开授权页面"""
        if progress_callback:
            progress_callback("打开浏览器进行授权...")
        self.open_browser(email)
        return None, None, "请在浏览器中完成登录，然后复制重定向后的 URL"
