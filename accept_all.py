import socket
import smtplib


def checkacceptall(domain, mxrecord):
    file = open("acceptall", "r")
    for line in file:
        if line == domain:
            return True

    # Get local server hostname
    host = socket.gethostname()

    try:
        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(1)

        # SMTP Conversation
        server.connect(mxrecord)
        server.helo("jani.com")
        server.mail('info@' + "jani.com")
        code, message = server.rcpt(str("erfds234fr@" + domain))
        server.quit()

        # Assume 250 as Success
        if code == 250:
            file1 = open('acceptall', 'w')
            file1.write(domain)
            file1.close()
            return True
        else:
            return False
    except:
        return False
