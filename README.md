# Email MTA,MX Check


**accept_all = True**   
_Whether the mail server used to verify indicates that all addresses are deliverable regardless of whether or not the email is valid._  
**disposable = False**    
_Whether this email is hosted on a disposable or temporary email service._  
**domain = "gmail.com"**  
_The domain of the email. (e.g. The domain for john.smith@gmail.com would be gmail.com)_  
**duration = 0.493**  
_The length of time (in seconds) spent verifying this email._  
**email = email**  
_The email that was verified._  
**first_name = "John"**  
_The possible first name of the user._  
**free = True**  
_Whether the email is hosted by a free email provider._  
**full_name = "John Smith"**  
_The possible full name of the user._  
**gender = "male"**  
_The possible gender of the user._  
**last_name = "Smith"**  
_The possible last name of the user._  
**mx_record = "aspmx.l.google.com"**  
_The address of the mail server used to verify the email._  
**reason = "accepted_email"**  
_The reason for the associated state._  
**role = False**  
_Whether the email is considered a role address. (e.g. support, info, etc.)_  
**score = 100**  
_The score of the verified email._  
**smtp_provider = "google"**  
_The SMTP provider of the verified email's domain._  
**state = "deliverable"**  
The state of the verified email. (e.g. deliverable, undeliverable, risky, unknown)  
**user = "john.smith"**  
_The user part of the verified email. (e.g. The user for john.smith@gmail.com would be john.smith)_  


# Sample Response

```
{
"accept_all": false,
"disposable": false,
"domain": "webzworld.com",
"duration": 0.3289344310760498,
"email": "prathmesh@webzworld.com",
"free": false,
"mx_record": "webzworld-com.mail.eo.outlook.com.",
"reason": "Email undeliverable",
"role": "unknown",
"state": "undeliverable",
"user": "prathmesh"
}
```