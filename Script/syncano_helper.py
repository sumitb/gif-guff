from syncano.client import SyncanoApi
import sys

def get_comments(folder_name):
	INSTANCE = "holy-surf-639401"
	API_KEY = "bd6e4f117fe7f6c1db89a9bc626c06c92ec6304d"
	syncano = SyncanoApi(INSTANCE, api_key=API_KEY)
	data = syncano.data_get(6182, collection_id=18729, collection_key='trackSubmit', state='All', 
		folders= folder_name, since_id=None, max_id=None, since_time=None, limit=100, 
		order='ASC', order_by='created_at', filter=None, include_children=True, depth=None, 
		children_limit=100, parent_ids=[], by_user=None, message_id=None)
	comments_count = len(data['data']['data'])
	comments = []
	for i in range(0, comments_count):
		comments.append(data['data']['data'][i]['title'])
	
	print comments

def add_post(folder_name):
	INSTANCE = "holy-surf-639401"
	API_KEY = "bd6e4f117fe7f6c1db89a9bc626c06c92ec6304d"
	syncano = SyncanoApi(INSTANCE, api_key=API_KEY)
	syncano.folder_new(6182, folder_name, collection_id=18729, collection_key='trackSubmit', source_id=None, message_id=None)

def delete_post(folder_name):
	INSTANCE = "holy-surf-639401"
	API_KEY = "bd6e4f117fe7f6c1db89a9bc626c06c92ec6304d"
	syncano = SyncanoApi(INSTANCE, api_key=API_KEY)
	syncano.folder_delete(6182, folder_name, collection_id=18729, collection_key='trackSubmit', message_id=None)

def add_comment(folder_name, comment):
	INSTANCE = "holy-surf-639401"
	API_KEY = "bd6e4f117fe7f6c1db89a9bc626c06c92ec6304d"
	syncano = SyncanoApi(INSTANCE, api_key=API_KEY)

	syncano.data_new(6182, collection_id=18729, collection_key='trackSubmit',
		user_name=None, source_url=None, title=comment, text=None, link=None, image=None,
		image_url=None, folder=folder_name, state='Pending', data_key=None,
		parent_id=None, message_id=None)

def delete_comment(folder_name, comment):
	INSTANCE = "holy-surf-639401"
	API_KEY = "bd6e4f117fe7f6c1db89a9bc626c06c92ec6304d"
	syncano = SyncanoApi(INSTANCE, api_key=API_KEY)
	data = syncano.data_get(6182, collection_id=18729, collection_key='trackSubmit', state='All', 
		folders= folder_name, since_id=None, max_id=None, since_time=None, limit=100, 
		order='ASC', order_by='created_at', filter=None, include_children=True, depth=None, 
		children_limit=100, parent_ids=[], by_user=None, message_id=None)
	idx = 0	
	comments_count = len(data['data']['data'])

	for i in range(0, comments_count):
		if data['data']['data'][i]['title'] == comment:
			idx = data['data']['data'][i]['id']
			break
	if idx != 0:
		syncano.data_delete(6182, collection_id=18729, collection_key='trackSubmit', data_ids=idx,
			state='All', folders=folder_name, filter=None, by_user=None, limit=100, message_id=None)

def get_post():
	INSTANCE = "holy-surf-639401"
        API_KEY = "bd6e4f117fe7f6c1db89a9bc626c06c92ec6304d"
	syncano = SyncanoApi(INSTANCE, api_key=API_KEY)
	folder=syncano.folder_get(6182, collection_id=18729, collection_key='trackSubmit', message_id=None)
	count = len(folder['data']['folder'])
	folder_name=[]	
	for i in range(1, count):
		 folder_name.append(folder['data']['folder'][i]['name'])

	print folder_name

if __name__ == "__main__":
	
        if sys.argv[1] == "addPost":
                add_post(sys.argv[2])
        elif sys.argv[1] == "getComments":
                get_comments(sys.argv[2])
        elif sys.argv[1] == "deletePost":
                delete_post(sys.argv[2])
        elif sys.argv[1] == "addComments":
                add_comment(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "deleteComments":
                delete_comment(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "getPost":
                get_post()
