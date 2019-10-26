#!/usr/bin/env python2

"""picofix.py: reboot the a router when it fails to contact a distant node."""

__author__ = "Alex 'Chozabu' P-B"


import pyping
from time import sleep
from datetime import datetime
import pxssh

def reboot_router():
	try:
		s = pxssh.pxssh()
		s.login('192.168.2.209', 'root', 'thereisapassword')
		s.sendline('reboot')   # run a command
		s.prompt()             # match the prompt
		print(s.before)        # print everything before the prompt.
		s.logout()
	except pxssh.ExceptionPxssh as e:
		print("pxssh failed on login.")
		print(e)

def main_loop():
	reboots = [None]
	fail_count = 0
	ok_count = 0
	while True:
		if pyping.ping('192.168.32.1').ret_code:
			ok_count = 0
			fail_count += 1
			print("FAIL", fail_count)
			if fail_count > 10:
				reboots.append(datetime.now().strftime("%Y-%m-%m %H:%M"))
				print("rebooting router!")
				reboot_router()
				print("rebooted router, waiting 60 seconds")
				print('reboots:', reboots)
				sleep(60)
				print("OK, back to normal")
				fail_count = 0
		else:
			fail_count = 0
			ok_count += 1
			print("seems OK, ok_count:", ok_count, 'last_reboot:', reboots[-1], 'of', len(reboots)-1)
		sleep(2)

if __name__ == "__main__":
	main_loop()