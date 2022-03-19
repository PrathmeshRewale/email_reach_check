def rolemails(user):
    roles = ['info', 'sales', 'support', 'office', 'admin', 'abuse', 'postmaster', 'webmaster', 'billing', 'help',
             'noc']

    for role in roles:
        if role == user:
            return True
    return False


