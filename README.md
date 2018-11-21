# OpsToolCollection
Useful small tool collections for Ops

1. iislog_timetaken_analysis.py - count scatter of time-taken for IIS requests, from IIS log.
	Usage:
		#Firstly, you extract only fields you are interested
		cat u_ex181121.log|grep '1.2.3.4'|awk '{print $1,$2,$NF} >filtered_log.txt
		./iislog_timetaken_analysis.py filtered_log.txt begintime endtime
		
	This will count how time-taken scattered (count of responses finished within 1s, 1-2s, and so on) 