
class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


allowed_domains = ['com', 'net', 'org', 'bg']
email = input()
while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    username, domain = email.split('@')
    if len(username) < 5:
        raise NameTooShortError('Name must be more than 4 characters')
    domain_extension = domain.split('.')[-1]
    if domain_extension not in allowed_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    print('Email is valid')
    email = input()
