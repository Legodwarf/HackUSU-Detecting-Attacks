There have been recent attacks by Russian cybercriminals that alter plaintext on sites such as Instagram to redirect the client to malicious websites which include malware.
In the following program we will attempt to detect the following attacks with the following techniques:

1. Verify the site re-directs to another website

We will first see if the user trusts the original site being accessed. If they do, we will check if the web link re-directs to another page on that website. If it does redirect from the trusted website to another subdomain of that trusted website, we will not perform the other checks. Although malicious actors can alter DNS records to corrupt a subdomain but not the primary domain, accounting for this will not be part of the scope of our program at this point in time.

2. Detect Unicode Homoglyphs

Once we have ascertained that a link re-directs to another website, we will investigate how popular that website's search term is compared with the Latin version of that site.
This will help us flag a site that replaces, for example, a cryllic character in an otherwise Latin name and redirects traffic to a malicious version of a website.
Take, for example, apple vs. аррlе. Do they look the same? They do to a casual user, but they are not. The "a" in one is in Latin, the other in cryllic.

3. Base64 Encoding

Base64 Encoding is a form of attack masking otherwise concerning data or code as nonsense text making direct detection of the malware more difficult and in HTML smuggling.
There are several ways to detect base 64 encoding:
You can look for decoding prompts within text (EX:javascript (btoa, atob), python (base.b64encode or decode)).
If the same text has been encoded multiple times, a pattern emerges of a pretext "Vm0wd" at the start of the text.
These two features are not currently addressed in our program.
Encoding data in base64 also increases the size of the data by about 33% each time it is encoded, so you can also check for file size/text length above an expected threshold.
The file base64check.py contains a python function definition that reads a url.
The function then checks the length of the input to see if the url is arbitrarily large and therefore was possibly masked with base64 encoding.

5. Check for hidden URLs

We will then check if the URL's link opacity has been turned to 0, the style has been turned to display "non", or visibility is "hidden". This is highly suspicious and should flag an alert.
