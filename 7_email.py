email = 'purvi@datagrokr.com'

company_name=''
flag=0
for ch in email:
    if ch == "@":
        # print(ch)
        flag = 1

    elif ch != '.' and flag == 1:
        # print(ch)
        company_name += ch

    if ch == '.':
        break



print(company_name)

# Output : datagrokr