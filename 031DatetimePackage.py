import datetime
import locale
import pytz

locale.setlocale( locale.LC_ALL, 'es-MX' )

dt = datetime.datetime.now()

print( 'dt = datetime.datetime.now() => {}'.format( dt ) )
print( 'dt.year => {}'.format( dt.year ) )
print( 'dt.month => {}'.format( dt.month ) )
print( 'dt.day => {}'.format( dt.day ) )
print( 'dt.hour => {}'.format( dt.hour ) )
print( 'dt.minute => {}'.format( dt.minute ) )
print( 'dt.second => {}'.format( dt.second ) )
print( 'dt.microsecond => {}'.format( dt.microsecond ) )

dt = datetime.datetime(1994, 9, 3)
print( 'dt = datetime.datetime(1994, 9, 3) => {}'.format( dt ) )
dt = dt.replace(hour=11)
dt = dt.replace(minute=11)
dt = dt.replace(second=11)
print( dt )

dt = datetime.datetime.now()
print( 'dt.isoformat() => {}'.format( dt.isoformat() ) )
print( 'dt.strftime("%A %d %B %Y %I:%M") => {}'.format( dt.strftime("%A %d %B %Y %I:%M") ) )
print( 'dt.strftime("%A %d de %B del %Y - %H:%M") => {}'.format( dt.strftime("%A %d de %B del %Y - %H:%M") ) )

three_weeks = datetime.timedelta(days=21)
four_hours = datetime.timedelta(hours=4)
five_minutes = datetime.timedelta(minutes=5)
six_seconds = datetime.timedelta(seconds=6)
dt = dt + three_weeks + four_hours + five_minutes + six_seconds
print( 'now plus 3 weeks, 4 hours, 5 minutes, 6 seconds => {}'.format( dt ) )

print( '\n' )

# print( pytz.all_timezones )
dt = datetime.datetime.now( pytz.timezone( 'Asia/Tokyo' ) )
print( 'datetime.datetime.now( pytz.timezone( "Asia/Tokyo" ) ) => {}'.format( dt.strftime("%A %d de %B del %Y - %H:%M") ) )