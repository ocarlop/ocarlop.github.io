from pydub import AudioSegment

path = '/home/cpicanco/music/Carlop/'
slugname = 'quando-a-vi-passar'
filename = slugname+'.wav'
inptname = path+filename

title = 'Quando a vi passar'
album = 'Quando a vi passar'
artist = 'Carlop'
date = '2021'
UPC = ''
ISRC = ''
cover = '/home/cpicanco/code/git/ocarlop.github.io/assets/img/single/'+slugname+'/01.400.jpg'

outppath = '/home/cpicanco/code/git/ocarlop.github.io/assets/audio/'
AudioSegment.from_wav(inptname).export(outppath+slugname+'.mp3',
                           format='mp3',
                           bitrate='320k',
                           tags={
                             'title' : title,
                             'album' : album,
                             'artist': artist,
                             'date'  : date,
                             'UPC'   : UPC,
                             'ISRC'  : ISRC},
                           cover=cover)

AudioSegment.from_wav(inptname).export(outppath+slugname+'.ogg',
                           format='ogg',
                           bitrate='320k',
                           tags={
                             'title' : title,
                             'album' : album,
                             'artist': artist,
                             'date'  : date,
                             'UPC'   : UPC,
                             'ISRC'  : ISRC})