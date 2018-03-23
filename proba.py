import vk #need pip install vk, google 'vk api python' for module documentation
SERVICE_KEY = '26ed4c1326ed4c1326ed4c135826b730c2226ed26ed4c137f375dd7e14f769494a0797b'
#read about service keys https://vk.com/dev/access_token

session = vk.Session(access_token=SERVICE_KEY)
vk_api = vk.API(session, v='4.1.6')

GID = 4569

for post in posts:
    likes = vk_api.likes.getList(item_id = post['id'],...)#параметры нужные в скобки сама подставь.
    #вот мы молучили список залайкавших профилей. идем по нему
    user_likes = {} #это словарь вида {'uid1':[like1, like2...], 'uid2' [like1, like3], т.е. словарь где ключ
    # - имя пользователя, а значение по ключу - список лайков
    for like in likes['items']:
        uid = like['uid']
        if uid in user_likes: #ну тут надо уточнить как проверять в словаре на вхождение ключа, не помню точно
            user_likes['uid'] = post['id'] #та же фигня, надо уточнить как именно добавлять значение в словарь списков по ключу
        
        #пока реализуем это, задачу упрощаем и в качестве вывода просто получим список пользовоателей, которые поставили больше одного лайка, т.е.
    
    for user in user_likes:
        if len(user)>1:
            print user #еще раз - это псевдокод, он только про логику, не будет работать, пока не доделан правильно.
# i = 1
