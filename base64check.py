# return true if input is likely base 64 encoded text based on length (suspiciously long)
# return false if length seems reasonable

def b64Check(link):
  totLen = len(link)
  # Check url total length < 200
  if totLen < 200:
    # find last period
    index_TLD = link.rfind('.')
    # if no period
    if index_TLD == -1:
      print('not a url')
    # if there is a period
    else:
        if index_TLD < 30:
            print('Non-Flag 3 - Likely not base64 encoded multiple times')
            return False
        else:
            return True
  else:
    return True

def b64(val):
    if val:
        print("Likely base64 encoded multiple times")