msg_template='''Hello {name},
Thank you for joining {website}, We are very\
happy to have you eith us.
'''
def format_msg(my_name="Justin", my_website="cdfe.sh"):
    my_msg=msg_template.format(name=my_name, website=my_website)
    return my_msg
