import vk #need pip install vk, google 'vk api python' for module documentation
SERVICE_KEY = '26ed4c1326ed4c1326ed4c135826b730c2226ed26ed4c137f375dd7e14f769494a0797b'
#read about service keys https://vk.com/dev/access_token

session = vk.Session(access_token=SERVICE_KEY)
vk_api = vk.API(session)

GID = 4569

posts = vk_api.wall.get(owner_id=-GID, count = 2) #can use all methods from https://vk.com/dev/methods like this with vk_api.method.name(parameters)

#print (posts) #run 2 check full out
print (posts[2]['text']) #text of second post (first is pinned)
post_id = (posts[2]['id'])
print (post_id)

likes = vk_api.likes.getList(type = 'post', owner_id=-GID, item_id = post_id, count = 3, extended = 1)
#print (posts) #text of second post (first is pinned)
print (likes)

#Твоя задача: найти пару пользователей с минимум пятью взаиимными лайками (т.е. оба залакали один пост). 
#вывести имя фамилию первого, второго и список постов в формате - первые 200 символов текста поста. 
