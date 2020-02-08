import datetime
import calendar


strtTime = '2017/08/01 00:00:00'
endTime = '2017/11/20 00:00:00'
strtDate = datetime.datetime.strptime(strtTime, "%Y/%m/%d %H:%M:%S")
endDate = datetime.datetime.strptime(endTime, "%Y/%m/%d %H:%M:%S")
print strtDate,endDate
strt = calendar.timegm(strtDate.utctimetuple())
end = calendar.timegm(endDate.utctimetuple())
print strt,end
nextDate = strtDate + datetime.timedelta(days=1)
#print "nextDate=", nextDate
print "nextDate=", nextDate.strftime("%Y-%m-%d")
