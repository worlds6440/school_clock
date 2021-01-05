# school_clock
Simple clock that also shows a school routine notice to help keep school routine during home learning.  
  
Download the python file from the following github repository, store it in your home folder and ensure it is executable:  
'chmod +x clock.py'  
  
The code is currently set up to update the clock every minute and display a new message every half hour between 8:30am and 5pm but you can obviously and easily change this by editing the contents of the get_message() method inside the clock.py file. I do intend on improving the code at some point to take it’s messages from a file or online location to make it easier to configure, but it’s not strictly necessary and this write-up has taken longer to do than the project itself :)
You can test the project now by running in the terminal:  
'python clock.py'  
  
To make the clock start at boot, run:  
'sudo crontab -e'  
  
And add the following line at the bottom:  
'@reboot /usr/bin/python /home/pi/clock.py'
