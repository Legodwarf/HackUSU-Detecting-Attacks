# return true if input is likely base 64 encoded text based on length (suspiciously long)
# return false if length seems reasonable
def b64Check(link):
  totLen = len(link)
  print(f'{link}, {totLen}')
  # Check url total length < 200
  if totLen < 200:
    # find last period
    index_TLD = link.rfind('.')
    # if no period
    if index_TLD == -1:
      print('not a url')
    # if there is a period
    else:
        
        print(f"Domain length is {index_TLD}, in: {link[:index_TLD]}|{link[index_TLD:]}")
        if index_TLD < 30:
            print('likely not base64 encoded multiple times')
            return False
        else:
            return True
  else:
    return True
print(b64Check('https://ec2-18-191-214-99.us-east-2.compute.amazonaws.com/?folder=/home/ubuntu'))