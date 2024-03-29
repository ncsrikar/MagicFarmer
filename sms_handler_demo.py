#!/usr/bin/env python

"""\
Demo: handle incoming SMS messages by replying to them

Simple demo app that listens for incoming SMS messages, displays the sender's number
and the messages, then replies to the SMS by saying "thank you"
"""

from __future__ import print_function

import logging
from test import detect_intent_texts
PORT = 'COM12'  #Check your system settings to check which port the SIM800A module is connected to
BAUDRATE = 57600    #The baud rate of Termite should match with this one
PIN = None # SIM card PIN (if any)

from gsmmodem.modem import GsmModem

def handleSms(sms):
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage:\n{2}\n'.format(sms.number, sms.time, sms.text))

    detect_intent_texts(sms.number,sms.number+" "+sms.text)
    print('Replying to SMS...')
     sms.reply(u'SMS received:Added')
    print('SMS sent.\n')
    
def main():
    print('Initializing modem...')
    # Uncomment the following line to see what the modem is doing:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=handleSms)
    modem.smsTextMode = False 
    modem.connect(PIN)
    print('Waiting for SMS message...')    
    try:    
        modem.rxThread.join(2**10)
    finally:
        modem.close()

if __name__ == '__main__':
    main()
