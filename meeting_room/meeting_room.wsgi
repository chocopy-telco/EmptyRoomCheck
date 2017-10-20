# mysite_uwsgi.ini file
[uwsgi]
# Django-related settings
# the base directory (full path)
chdir           = /Users/byungwoo/git/meeting_room_check/meeting_room
# Django's wsgi file
module          = meeting_room.wsgi
# the virtualenv (full path)
home            = /Users/byungwoo/git/meeting_room_check
# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 1
# the socket (use the full path to be safe
#socket          = /tmp/testproject.sock
# ... with appropriate permissions - may be needed
 chmod-socket    = 666
# clear environment on exit
vacuum          = true

