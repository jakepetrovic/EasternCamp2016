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


def get_day(day_num):
	if day_num == "1":
		return "Sunday"
	elif day_num == "2":
		return "Monday"
	elif day_num == "3":
		return "Tuesday"
	elif day_num == "4":
		return "Wedensday"
	elif day_num == "5":
		return "Thursday"
	elif day_num == "6":
		return "Friday"

print "Tagging MP3s:"
# Get the current scirpts directory
run_dir = os.path.dirname(os.path.abspath(__file__))
# Now search through all the child directories of this directory and find
# the MP3 files.
for root, dirs, files in os.walk(run_dir):
    for file in files:
        file_path = os.path.abspath(os.path.join(root, file))
        # We only care about mp3 files, skip over non-mp3 files.
        if file.endswith(".mp3"):
       	    print(file_path)
            audioFileName = file_path
	    	audiofile = eyed3.load(audioFileName)

	        # There's a bug where this doesn't load sometimes, so need to do this
	        # stuff if it doesn't load right.
		    if audiofile.tag is None:
		      	audiofile.tag = eyed3.id3.Tag()
		       	audiofile.tag.file_info = eyed3.id3.FileInfo(audioFileName)
		       	audiofile = eyed3.load(audioFileName)

		    event = audioFileName[:1]
	        year = "2016"
	        artist = "Eastern Camp 2016"
	        album = ''
	        title = audioFileName[6:]
	        track_num = ''
	        day = ''

	        # Choirs
	        if event == '1':
	        		choir_type = audioFileName[:2]
	            if choir_type == '1' or choir_type == '2' or choir_type == '3' :
        				album = "Men's, Teen, & Adult Choirs"
	            else 
            		album = "Children's Choirs & Orchestra"   
	            track_num = audioFileName[3:5]                
	        # Inspiration Hours
	        elif event == '2' or event == '3' :
	        	  # Get the day
	            day_num = audioFileName[:2]
	            day = get_day(day_num)	 
	            track_num = audioFileName[3:5]
	            album = day + " Inspiration Hour"
	        # Sermons
	        elif event == '3':
	          	# Get the day
	            day_num = audioFileName[:2]
	            day = get_day(day_num)	 
	            track_num = audioFileName[3:5]
	            if 'Teen' not in title 
            		album = day + " Night Sermon"
	        	else
    				album = day + " Night Teen Sermon"

	        # Forum
	        # Track numbers are not included in the title name, and thus we don't wory about them for forums. 
	        elif event == '4':
	        		# Get the day
	            day_num = audioFileName[:2]
	            day = get_day(day_num)	 
	            album = "Forums"
	        else 
	        		print "File "+ audioFileName + " named incorrectly. Does not start with a number between 1 and 4. Skipping to next file."
			     
			 # Finish up and tage the file!
	        audiofile.tag.artist = artist
	        audiofile.tag.album = album
	        audiofile.tag.album_artist = artist
	        audiofile.tag.title = title
	        audiofile.tag.track_num = track_num
	        audiofile.tag.year = year q
	        audiofile.tag.save()

	        # Rename file not used
	        # new_filename = "D:/Dropbox/Eastern_Camp/2016/MP3_TAG/01 SONG.mp3".format(audiofile.tag.artist, audiofile.tag.title)
	        # os.rename(audioFileName, new_filename)


