import os
import eyed3
# great example here http://opentechschool.github.io/python-scripting-mp3/
# This script MUST be run at the top level of the EC folders (2016 MP3 Files). It assumes the following directory structure:
# -2016 MP3 Files
# --Choirs
# ---Adult
# ---Junior
# ---Orchestra
# ---Primary
# ---Teen
# ---Tiny Tots
# --Disc Images
# --Forum PDFs
# --Forums
# --Inspiration Hours
# ---01 Sun, Bro Peter
# ---02 Mon, Bro James
# ---03 Tues, Bro Andrew
# ---04 Wed, Bro Levi
# ---05 Thurs, Bro Paul
# ---06 Fri, Bro Barnabas
# --Sermons

print "Tagging MP3s"
audioFileName = "D:/Dropbox/Eastern_Camp/2016/MP3_TAG/song.mp3"

audiofile = eyed3.load(audioFileName)
#There's a bug where this doesn't load sometimes, so need to do this stuff if it doesn't load right.
if audiofile.tag is None:
    audiofile.tag = eyed3.id3.Tag()
    audiofile.tag.file_info = eyed3.id3.FileInfo(audioFileName)
    audiofile = eyed3.load(audioFileName)

audiofile.tag.artist = u"Christians"
audiofile.tag.album = u"God be with Us"
audiofile.tag.album_artist = u"ACCN"
audiofile.tag.title = u"To God be the Glory"
audiofile.tag.track_num = 4

audiofile.tag.save()

new_filename = "D:/Dropbox/Eastern_Camp/2016/MP3_TAG/01 SONG.mp3".format(audiofile.tag.artist, audiofile.tag.title)
os.rename(audioFileName, new_filename)


