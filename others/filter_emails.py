def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, website_extension = s.split("@")
    except:
        return False
    if username == "":
        return False

    # a-z, A-Z, 0-9, -, _
    filtered = list(filter(lambda x: (ord(x) >= ord("a") and ord(x) <= ord("z")) or (ord(x) >= ord("A") and ord(x) <= ord("Z")) or (ord(x) >= ord("0") and ord(x) <= ord("9")) or (ord(x) == ord("-")) or (ord(x) == ord("_")), username))
    if "".join(filtered) != username:
        return False

    try:
        website, extension = website_extension.split(".")
    except:
        return False
    if website == "":
        return False

    # a-z, A-Z, 0-9
    filtered = list(filter(lambda x: (ord(x) >= ord("a") and ord(x) <= ord("z")) or (ord(x) >= ord("A") and ord(x) <= ord("Z")) or (ord(x) >= ord("0") and ord(x) <= ord("9")), website))
    if "".join(filtered) != website:
        return False

    # a-z, A-Z
    filtered = list(filter(lambda x: (ord(x) >= ord("a") and ord(x) <= ord("z")) or (ord(x) >= ord("A") and ord(x) <= ord("Z")), extension))
    if "".join(filtered) != extension:
        return False

    # max 3
    if len(extension) > 3:
        return False

    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

"""
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
"""
