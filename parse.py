import sys
import mailbox

# Returns true if message is unread and false if message is read
def unread(message):
    flags = []
    flags = message['X-Gmail0Labels'].split(",")
    for flag in flags:
        if flag = "Unread":
            return True
        else:
            return False

def create_dict(filename):
    mbox = mailbox.mbox(filename)
    senders = dict() # Dictionary with sender as key and size 2 list as value with first elt=number unread and second elt=number read
    senders = {}

    for message in mbox:
      sender = message['From']
      # Checks if sender is already in the dictionary
      if sender in senders:
        if unread(message):
          senders[sender][0] += 1
        senders[sender][1] += 1

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print 'Usage: python genarchivesum.py mbox'
            sys.exit(1)

    gen_summary(sys.argv[1])

senders = dict()
senders = {}

senders[sender] 



