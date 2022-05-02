import azapi

API = azapi.AZlyrics('google', accuracy=0.5)

API.artist = 'Ana Johnsson'
API.title = 'Bring It On'

API.getLyrics(save=True, ext='lrc')

print(API.lyrics)