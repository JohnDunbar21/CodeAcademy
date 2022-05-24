# CSV stands for comma-separated values. These are usually spreadsheets from programs like Excel or Google Sheets. 
# For example:
#       Name,Username,Email
#       Roger Smith,rsmith,wigginsryan@yahoo.com
#       Michelle Beck,mlbeck,hcosta@hotmail.com
#       Ashley Barker,a_bark_x,a_bark_x@turner.com
#       Lynn Gonzales,goodmanjames,lynniegonz@hotmail.com
#       Jennifer Chase,chasej,jchase@ramirez.com
#       Charles Hoover,choover,choover89@yahoo.com
#       Adrian Evans,adevans,adevans98@yahoo.com
#       Susan Walter,susan82,swilliams@yahoo.com
#       Stephanie King,stephanieking,sking@morris-tyler.com
#       Erika Miller,jessica32,ejmiller79@yahoo.com

with open('logger.csv') as log_csv_file:
    print(log_csv_file.read())