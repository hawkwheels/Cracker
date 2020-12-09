from crypt import crypt

def test_password (ussr,hash):
    salt = hash[:20]
    with open ("dist.txt","r") as guess:
        for word in guess.readlines():
            test_word = crypt(word.strip("\n"),salt)
            if test_word == hash:
                print("[+] Password found!")
                print ("username:"+ussr)
                print ("password:"+word)
                return


def main():
    with open("shadow.txt","r") as target:
        for line in target.readlines():
                user = line.split(":")[0]
                crypt_passwd = line.split(":")[1]
                test_password(user,crypt_passwd)

if __name__ == "__main__":
    main()
