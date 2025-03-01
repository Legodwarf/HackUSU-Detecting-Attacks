There have been recent attacks by Russian cybercriminals that alter plaintext on sites such as Instagram to redirect the client to malicious websites which include malware.
In the following program we will attempt to detect the following attacks with the following techniques:

1. Using Unicode Homoglyphs

We first will detect a hyperlink within a webpage's comments.
We will then check Google's Custom Search JSON API to check the amount of traffic related to that domain.
If the domain's Google search-related traffic falls below a threshold, it will flag the hyperlink. 
E.G. If a link points to a cryllic version of "Disney.com," that will fall below the threshold compared to the Latin search.
If the site is in cryllic, then, it follows that it will likely fall below the threshold and flag the hyperlink.

Usage:
Go into the directory where the code is and then run the command: python -m http.server 8000.
This will make it so that all the files in the directory will be hosted here, so you can access it like this: http://localhost:8000/homoglyph.html

2. Base64 Encoding

   

CHECK IF SITE TO SITE OR SITE-> OUT OF SITE
