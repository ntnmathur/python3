def IPaddress(ip):
    ip_lst = ip.split('.')
    if len(ip_lst) !=4:
        return False
    else:
        for elem in ip_lst:
            try:
                i = int(elem)
                if not (i >=0 and i <=255):
                    return False
            except:
                return False
        return True


if __name__ == "__main__":
    ip='69.89.18.226'
    print(IPaddress(ip))

    ip='69.89.345.226'
    print(IPaddress(ip))

    ip = '69.89.345'
    print(IPaddress(ip))

    ip = '69.89.345.aa'
    print(IPaddress(ip))