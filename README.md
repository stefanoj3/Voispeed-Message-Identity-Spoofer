Voispeed Message Identity Spoofer
=================================
Author: Stefano Gabryel

Website: http://www.stefano-workshop.com

Released under: GPL v3


This script is used to exploit a vulnerability in the Voispeed client version 4.3.26(Raskuophone).
Basically, you can just send a well crafted UDP packet to a client connected to a Voispeed server,
then you will be able to impersonate whoever you want.
There is neither a check to verify that the packet comes from the server, nor to verify that the
message's recipient exists.
Also you can hide the real recipient number and show a fake one, so you can receive a response
from the victim on a number showing a fake one.
I've already tested it on Voispeed client and Voice client both 4.3.26(Raskuophone), but other versions
may be affected too.

If someone is interested to improve this script to make it work with other Voispeed versions,
contact me using my website's contact form.
