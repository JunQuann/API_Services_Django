import os
import asyncio

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

async def send_email(email):
    try:
        response = sg.client.mail.send.post(request_body=email.get())
        # if response.status_code < 300:
        #     print("Email #{} processed".format(n), response.body, response.status_code)
    except urllib.error.HTTPError as e:
        e.read()

@asyncio.coroutine
def send_async(email):
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(send_email(email))
    loop.run_until_complete(task)
