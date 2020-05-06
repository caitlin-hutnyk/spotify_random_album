import sys
import spotipy
import spotipy.util as util
import random
import os

os.environ["SPOTIPY_CLIENT_ID"] = 'd3a91496416f4f7ea08588bdc0c1cf80'
os.environ["SPOTIPY_CLIENT_SECRET"] = '98c2bb51c6a044719275c7e7bb40ca33'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost'

scope = 'user-library-read'

un = ''

if len(sys.argv)<= 1:
	un = '' # enter your spotify username here
else:
	un = sys.argv[1]

if un == '':
	print('You need to give your spotify username as an argument, or edit it into random_saved.py')
	print('Aborted')
else:
	token = util.prompt_for_user_token(un, scope)

	albums = []

	if token:
		sp = spotipy.Spotify(auth=token)

		off = 0
		l = 0
		results = sp.current_user_saved_albums(limit=50,offset=off)

		for a in results['items']:
			albums.append(a['album']['name'])
		off += 50
		while len(albums) != l:
			l = len(albums)
			results = sp.current_user_saved_albums(limit=50,offset=off)
			for a in results['items']:
				albums.append(a['album']['name'])
			off += 50

		print(random.choice(albums))
	else:
	    print("Can't get token for", username)

