import socket
import smtplib


def mailboxcheck(email, mx_record):
    # Get local server hostname example.com
    host = socket.gethostname()

    try:

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(1)

        # SMTP Conversation
        server.connect(mx_record)
        server.helo(host)
        server.mail('info@' + host)
        code, message = server.rcpt(str(email))
        server.quit()

        # Assume 250 as Success
        if code == 250:
            return "deliverable"
        elif code == 252 or code == 554 or code == 252 or code == 251 or code == 452:
            return "risky"
        elif code == 421:
            return "unknown"
        elif code == 450 or code == 550:
            return "undeliverable"
        else:
            return "undeliverable"
    except:
        return "risky"
    # (e.g. deliverable, undeliverable, risky, unknown)
    # Code	Meaning
    # 200	(nonstandard success response, see rfc876)
    # 211	System status, or system help reply
    # 214	Help message
    # 220	<domain> Service ready
    # 221	<domain> Service closing transmission channel
    # 250	Requested mail action okay, completed
    # 251	User not local; will forward to <forward-path>
    # 252	Cannot VRFY user, but will accept message and attempt delivery
    # 354	Start mail input; end with <CRLF>.<CRLF>
    # 421	<domain> Service not available, closing transmission channel
    # 450	Requested mail action not taken: mailbox unavailable
    # 451	Requested action aborted: local error in processing
    # 452	Requested action not taken: insufficient system storage
    # 500	Syntax error, command unrecognised
    # 501	Syntax error in parameters or arguments
    # 502	Command not implemented
    # 503	Bad sequence of commands
    # 504	Command parameter not implemented
    # 521	<domain> does not accept mail (see rfc1846)
    # 530	Access denied (???a Sendmailism)
    # 550	Requested action not taken: mailbox unavailable
    # 551	User not local; please try <forward-path>
    # 552	Requested mail action aborted: exceeded storage allocation
    # 553	Requested action not taken: mailbox name not allowed
    # 554	Transaction failed
