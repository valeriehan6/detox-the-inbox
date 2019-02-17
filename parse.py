import sys
import mailbox

n = 0 # n is the total number of messages seen so far

# Returns true if message is unread and false if message is read
def unread(message):
  

# Input: - filename: mbox file
# Output: - senders: dictionary of senders
# Each key is a sender and each value is a size 2 list with first elt=number unread and second elt=total (read and unread)
# Also updates value n
def create_dict(filename):
  mbox = mailbox.mbox(filename)
  senders = dict() 
  senders = {}

  for message in mbox:
    n += 1
    sender = message['From']
    # Checks if sender is already added
    if sender in senders:
      if unread(message):
        senders[sender][0] += 1
      senders[sender][1] += 1
    else:
      senders[sender]=[0,0]
      if unread(message):
        senders[sender][0] = 1
      senders[sender][1] = 1

  return senders

# Input: - senders: dictionary of senders (the output of create_dict)
#        - threshold_perc: threshold percentage
#        - n: total number of emails in mbox
# Output: ignored: list of senders who satisfy:
#           - their emails are more unread than the threshold percentage 
#           - If n<100, each sent more than 5
#           - If 10< n<1000, each sent more than 10
#           - Else, each sent more than 20
def most_unread(senders, threshold_perc):
  ignored = []

  for sender in senders:
    if sender[0]/sender[1] > threshold_perc:
      if n < 100:
        if sender[1] > 5:
          ignored.append(sender)
      else if n < 1000:
        if sender[1] > 10:
          ignored.append(sender)
      else
        if sender[1] > 20:
          ignored.append(sender)
    
  return ignored



