# README for Email Service
This README entails everything that is needed to run this service.  
To use this service, POST to /send/ with a JSON payload.

```Format for JSON payload
    {
        user: {
            user_id: ...
            template: ...
        }
    }
```

## Third Party Dependencies
* Django
* Sendgrid

## Environment Variables
* BASE_URL
* SENDGRID_API_KEY

## Components
* query
* sender
* user

### Query
Fetch user information from API endpoint

### Sender
Call SendGrid API to send email

### User
Model that represents the user after fetching data from endpoint
