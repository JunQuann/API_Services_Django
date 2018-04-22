import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail

class User(object):

    # map the template id accordingly with the keywords of the API
    template_dict = {
        'welcome': {
            'subject': 'Welcome to interwovn',
            'template_id': "8b687c2a-7739-429a-ad81-466abb59b93d"
        }
    }


    def __init__(self, name, email, template):
        self.name = name
        self.email = email
        self.template = template

    def __str__(self):
        return "{}'s email address is {}".format(self.name, self.email)

    def create_mail(self):
        """
        Creates email to send to this user
        """

        to_email = Email(self.email)
        from_email = Email("interwovn@gmail.com")
        subject = User.template_dict[self.template]['subject']
        template_id = User.template_dict[self.template]['template_id']
        content = Content("text/plain", "text")
        mail = Mail(from_email, subject, to_email, content)
        mail.personalizations[0].add_substitution(Substitution("-name-", self.name))
        mail.personalizations[0].add_substitution(Substitution("-city-", "Denver"))
        mail.template_id = template_id

        return mail
