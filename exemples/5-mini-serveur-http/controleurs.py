from urllib.parse import parse_qs

home_html = """<h1>Home</h1>
<h2>Registered Users</h2>
<ul>
{users}
</ul>
"""

login_html = """<h1>Home</h1>
<form action="/login" method="POST">
  <input name="email" placeholder="email" /><br>
  <input type="password" placeholder="password" name="pw" /><br>
  <input type="submit" value="Submit" />
</form>
"""

users = [
    { 'name': 'Jon Snow', 'email': 'jonsnow@winterfell.com', 'pw': 'dany' },
    { 'name': 'Arya Stark', 'email': 'arya@winterfell.com', 'pw': 'dagger' },
    { 'name': 'Sansa Stark', 'email': 'sansa@winterfell.com', 'pw': 'killramsay' },
    { 'name': 'Bran Stark', 'email': 'bran@winterfell.com', 'pw': 'raven' }
]

def make_user_list_item(user):
    return '<li><a href="mailto:' + user['email'] + '">' + user['name'] + '</a></li>'

class HomeController:
    def do_GET(self):
       items = [make_user_list_item(user) for user in users]
       items_joined = "\n".join(items)
       return home_html.replace("{users}", items_joined)

class LoginController:
    def do_GET(self):
       return login_html

    def do_POST(self, raw_body):
        body = parse_qs(raw_body)
        print("LoginController.do_POST body", raw_body, body)
        matching_users = [user for user in users if user['email'] == body['email'][0] and user['pw'] == body['pw'][0]]
        # # print(matching_users)
        # for u in users:
        #     if(u['email'] == body['email'][0] and u['pw'] == body['pw'][0]):
        #         return "<ul>" + make_user_list_item(matching_users[0]) + "</ul>"
        #     else:
        #         print("no match", u['email'], u['pw'], body['email'], body['pw'])
        return "<ul>" + make_user_list_item(matching_users[0]) + "</ul>" if matching_users else "bad credentials"

class RegisterController:
    def do_GET(self):
       print('I am RegisterController')
