import vlc, os, sys, time
# from vlc import Instance as IN
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new("/home/seek/Desktop/Movies/Hollywood/We're.the.Millers.2013.1080p.BluRay.x264.mp4")
player.set_media(Media)
player.play()
time.sleep(100)