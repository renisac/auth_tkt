from auth_tkt.encrypted import EncryptedAuthTkt
from auth_tkt.ticket import validate


def get_ticket_data(ticket, authtkt_secret, crypted_cookie_secret=None,
                    timeout=7200, encoding='utf-8', algo='MD5'):
    """We store user information in our session hashes. You can retreive that
    data with this function."""
    ticket = validate(
        ticket, authtkt_secret, timeout=timeout, encoding=encoding, algo=algo)

    if not ticket:
        return None

    data = {
        'id': ticket.uid,
        'tokens': ticket.tokens,
    }

    if crypted_cookie_secret:
        ticket = EncryptedAuthTkt(ticket, crypted_cookie_secret)
        data.update(ticket.data)

    return data
