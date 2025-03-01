There have been recent attacks by Russian cybercriminals that alter plaintext on sites such as Instagram to redirect the client to malicious websites which include malware.
In the following program we will attempt to detect the following attacks with the following techniques:

1. Using Unicode Homoglyphs

We first will detect a hyperlink within a webpage's comments.
We will then check Google's Custom Search JSON API to check the amount of traffic related to that domain.
If the domain's Google search-related traffic falls below a threshold, it will flag the hyperlink. 
E.G. If a link points to a cyrillic version of "Disney.com," that will fall below the threshold compared to the Latin search.
If the site is in cyrillic, then, it follows that it will likely fall below the threshold and flag the hyperlink.

Usage:
Go into the directory where the code is and then run the command: python -m http.server 8000.
This will make it so that all the files in the directory will be hosted here, so you can access it like this: http://localhost:8000/homoglyph.html

2. Base64 Encoding
Base64 Encoding is a form of attack masking otherwise concerning data or code as nonsense text making direct detection of the malware more difficult and in HTML smuggling.
There are several ways to detect base 64 encoding,
   You can look for decoding prompts within text (EX:javascript (btoa, atob), python (base.b64encode or decode)) * Not currently addressed by code in this repository
   If the same text has been encoded multiple times, a pattern emerges of a pretext "Vm0wd" at the start of the text * Not currently addressed by code in this repository
   Encoding data in base64 increases the size of the data by about 33% each time it is encoded, so you can also check for file size/text length above an expected threshold.
The file base64check.py contains a python function definition that reads a url
The function then checks the length of the input to see if the url is arbitrarily large and therefore was possibly masked with base64 encoding.

CHECK IF SITE TO SITE OR SITE-> OUT OF SITE
