import vk #need pip install vk, google 'vk api python' for module documentation
SERVICE_KEY = '26ed4c1326ed4c1326ed4c135826b730c2226ed26ed4c137f375dd7e14f769494a0797b'
#read about service keys https://vk.com/dev/access_token

session = vk.Session(access_token=SERVICE_KEY)
vk_api = vk.API(session, v='4.1.6')

GID = 4569

posts = vk_api.wall.get(  owner_id=-GID  ) #can use all methods from https://vk.com/dev/methods like this with vk_api.method.name(parameters)
i = 1
while i < 10:
    post_id = (posts[i]['id'])
    like = vk_api.likes.getList(type='post', owner_id=-GID, item_id=post_id, count=2, extended=1)
    print(like)
    i = i + 1

