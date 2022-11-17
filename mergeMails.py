with open("/Users/shasankjoshi/PycharmProjects/BasicsToAdvanced/Basics/names.txt", 'r', encoding = 'utf-8') as name_file: #open names.txt for reading
    with open("/Users/shasankjoshi/PycharmProjects/BasicsToAdvanced/Basics/names.txt", 'r', encoding='utf-8') as body_file: # open body.txt for reading
        body = body_file.read()

        for name in name_file:
            mail = "Hello" + name.strip() + "\n" + body

            with open(name.strip()+".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)

