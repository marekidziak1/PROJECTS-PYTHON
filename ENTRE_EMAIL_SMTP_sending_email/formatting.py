msg='''Hello {name} Thank you for joing {website}. I wish good time here'''
def format_msg(my_name="Marek", my_website="cfe.sh"):
    my_msg=msg.format(name=my_name, website=my_website)
    return my_msg
