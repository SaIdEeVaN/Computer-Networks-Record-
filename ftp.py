import ftplib

def anonymousLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        response = ftp.login("anonymous", "anonymous")
        print(response)
        if "230" in response:
            print(f"\n[*] Anonymous login on {hostname} is sucessful")
            print(ftp.getwelcome())
            ftp.dir()
    except Exception as e:
        print(str(e))
        print(f"\n[-] Anonymous login on {hostname} is unsucessful")

hostname = "ftp.be.debian.org"
anonymousLogin(hostname)

