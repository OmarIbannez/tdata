import fb_auth_token

fb_username = "your@email.com"
fb_password = "yourpassword"
fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
host = "https://api.gotinder.com"

