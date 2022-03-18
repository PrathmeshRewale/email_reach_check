import dns.resolver


def dnscheck(domain):
    records = dns.resolver.query(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    return mxRecord
