import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail

class User(object):

    # map the template id accordingly with the keywords of the API


    def __init__(self, name, email, template):
        self.name = name
        self.email = email
        self.template = template

    def __str__(self):
        return "{}'s email address is {}".format(self.name, self.email)

    def create_mail(self):
        """
        Creates email to send to this users
        """
        template_dict = {
            'welc': 'A9325134'
        }

        to_email = Email(self.email)
        sender_email = Email("interwovn@gmail.com")

        mail = Mail(from_email=sender_email, to_email=to_email)

        print(template_dict[self.template], self.name, self.email)

        mail.template_id(template_dict[self.template])
        mail.personalizations[0].add_substitution(Substitution("-name-", self.name))
        return mail
