import sys
import mailbox

# Returns true if message is unread and false if message is read
def unread(message):
  

# Returns dictionary of senders
# Each key is a sender and each value is a size 2 list with first elt=number unread and second elt=total (read and unread)
def create_dict(filename):
  mbox = mailbox.mbox(filename)
  senders = dict() 
  senders = {}

  for message in mbox:
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

  return senders;
  



