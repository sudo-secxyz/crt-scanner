# crt-scanner
An HTTP scanning tool that leverages crt.sh and selenium.

`Usage: python3 crt-scanner.py -d <URL to scan>`

![alt text](image.png)

### Logging
Tool will create a directory using the name of the url given, and then create files corresponding to the discovered urls based on crt.sh common names
uses selenium to take screenshots of urls it can visit.