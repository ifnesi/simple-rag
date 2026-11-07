# Auth FAQ

Q: How do I reset my password?
A: Use the reset link on the login page.

Q: How long does a TechFlow password reset link stay valid?
A: A TechFlow password reset link is valid for 60 minutes after it is sent and can be used only once.

Q: What is the minimum password length in TechFlow?
A: TechFlow requires passwords to be at least 12 characters long. There is no short-password exception for any plan.

Q: What complexity rules does a TechFlow password have to meet?
A: A TechFlow password must contain at least one uppercase letter, one lowercase letter, one number and one symbol. Passwords found in public breach lists are rejected.

Q: Does my TechFlow password expire?
A: By default a TechFlow password expires every 180 days, and you are prompted to change it at your next login. Workspace admins can lengthen or disable the expiry in security settings.

Q: Can I reuse an old password in TechFlow?
A: No, TechFlow blocks reuse of your last 5 passwords. Choose a password you have not used on your account recently.

Q: Can I use a password manager with TechFlow?
A: Yes, TechFlow works with common password managers and allows pasting into the password field. We recommend generating a random password of 16 characters or more.

Q: How do I change my TechFlow password while logged in?
A: Go to Profile, then Security, then Change password, and enter your current password followed by the new one. TechFlow signs out your other sessions after the change.

Q: I never received the TechFlow password reset email. What should I do?
A: Check your spam folder and confirm you typed the email address registered on your TechFlow account. If nothing arrives within 10 minutes, request a new link or contact support.

Q: Why does my TechFlow password reset link say it has expired?
A: TechFlow reset links expire after 60 minutes or as soon as a newer link is requested. Request a fresh link from the login page and use the most recent email only.

Q: Is there a maximum password length in TechFlow?
A: TechFlow accepts passwords up to 128 characters, including spaces and special characters. Long passphrases are encouraged.

Q: Will TechFlow ever ask me for my password by email or chat?
A: No, TechFlow staff never ask for your password, MFA code or API key by email, chat or phone. Report any such request to security@techflow.example.

Q: How do I change the email address on my TechFlow account?
A: Open Profile, then Account, then Email, enter the new address and confirm your password. TechFlow sends a verification link to the new address, and the change takes effect once you click it.

Q: Will I be notified when my TechFlow email address is changed?
A: Yes, TechFlow sends a notice to your old address when the email is changed. The notice includes a link to undo the change within 7 days.

Q: Can I change my TechFlow username?
A: Yes, you can change your TechFlow username from Profile, then Account, up to once every 30 days. Your old username becomes available to others after 14 days.

Q: Can two TechFlow accounts share the same email address?
A: No, each TechFlow account needs a unique email address. If you need a second account, use a different address or an alias.

Q: What happens to my TechFlow login if my work email changes?
A: Ask a workspace admin to update the email on your TechFlow account, or change it yourself before losing access to the old mailbox. Your data and permissions stay attached to the account.

Q: How do I turn on two-factor authentication in TechFlow?
A: Go to Profile, then Security, then Two-factor authentication, and choose a method. TechFlow walks you through scanning a QR code or registering a key.

Q: Which MFA methods does TechFlow support?
A: TechFlow supports authenticator apps (TOTP), SMS codes and hardware security keys (FIDO2/WebAuthn). Authenticator apps and security keys are recommended over SMS.

Q: Which authenticator apps work with TechFlow?
A: Any app that supports standard time-based one-time passwords works with TechFlow, including common apps such as Google Authenticator, Microsoft Authenticator and Authy. Codes refresh every 30 seconds.

Q: Why is my TechFlow authenticator code rejected?
A: The most common cause is a device clock that is out of sync. Turn on automatic time on your phone and try the next code that appears in your authenticator app for TechFlow.

Q: How do I set up SMS codes as a TechFlow MFA method?
A: Under Security, then Two-factor authentication, choose SMS and enter your mobile number. TechFlow sends a 6-digit code to verify the number before enabling it.

Q: I am not receiving my TechFlow SMS verification code. What can I do?
A: Wait 60 seconds and request a new code, and make sure your phone has signal and has not blocked short-code messages. If it still fails, use an authenticator app or a recovery code to sign in to TechFlow.

Q: How do I register a hardware security key with TechFlow?
A: Go to Security, then Two-factor authentication, then Add security key, insert or tap your FIDO2 key and name it. TechFlow recommends registering at least two keys.

Q: How many security keys can I register on my TechFlow account?
A: You can register up to 5 hardware security keys on a TechFlow account. Each one can be named and removed separately.

Q: What are TechFlow recovery codes?
A: TechFlow recovery codes are one-time codes that let you sign in if you cannot use your normal MFA method. Each account receives 10 recovery codes when MFA is enabled.

Q: Where should I store my TechFlow recovery codes?
A: Store your TechFlow recovery codes offline or in a trusted password manager, separate from your phone. Anyone with a code and your password can sign in to your account.

Q: Can a TechFlow recovery code be used more than once?
A: No, each TechFlow recovery code works only one time and is then invalidated. Generate a fresh set when you have only a few left.

Q: How do I generate new TechFlow recovery codes?
A: Open Security, then Recovery codes, then Generate new codes, and confirm with your password and MFA. Generating a new set immediately invalidates all 10 previous codes.

Q: What should I do if I lose my phone with my TechFlow authenticator app?
A: Sign in to TechFlow with one of your recovery codes, then remove the lost device and set up MFA on your new phone. If you have no recovery codes, request an MFA reset.

Q: How do I request an MFA reset for my TechFlow account?
A: Ask your workspace admin to reset your MFA from the Users page, or contact TechFlow support if you are the only admin. Identity verification is required and may take up to 2 business days.

Q: Can a workspace admin reset MFA for another TechFlow user?
A: Yes, workspace admins can reset MFA for members from Admin, then Users, then Reset MFA. The user must enroll a new method at their next login.

Q: Can I have more than one MFA method on TechFlow?
A: Yes, you can enable several methods, such as an authenticator app plus a security key, and choose the one to use at login. Having a backup method is strongly recommended.

Q: How do I disable MFA on my TechFlow account?
A: Go to Security, then Two-factor authentication, then Disable, and confirm with your password and a current code. If your workspace enforces MFA, the option is unavailable.

Q: Can my workspace require MFA for everyone in TechFlow?
A: Yes, workspace admins can require MFA for all members under Admin, then Security policies. Members without MFA are asked to enroll at their next login.

Q: How do I move my TechFlow authenticator to a new phone?
A: Add the new phone as a second authenticator in Security before wiping the old one, then remove the old device. If the old phone is already gone, use a recovery code.

Q: How long is the grace period for enrolling in MFA when my TechFlow workspace requires it?
A: The default grace period is 7 days from when the policy is enabled. After that, TechFlow blocks login until you complete enrollment.

Q: After how many failed attempts does TechFlow lock my account?
A: TechFlow locks an account after 5 failed login attempts in a row. The lockout lasts 15 minutes.

Q: How long does a TechFlow account lockout last?
A: A TechFlow lockout lasts 15 minutes, after which you can try again. Repeating the failures right away restarts the lockout.

Q: Can I unlock my TechFlow account before the 15 minutes are over?
A: Yes, use the Unlock account link on the login page to receive an email that clears the lockout immediately. A workspace admin can also unlock you from the Users page.

Q: Does entering a wrong MFA code count toward the TechFlow lockout?
A: Yes, 5 consecutive wrong MFA codes also lock the TechFlow account for 15 minutes. A successful login resets the counter.

Q: Does the TechFlow failed-attempt counter ever reset?
A: Yes, the counter resets after a successful login or after 30 minutes without any failed attempt. Unlocking the account also clears it.

Q: How can an admin unlock a locked TechFlow user?
A: Admins open Admin, then Users, select the locked member and choose Unlock. The user can log in again straight away.

Q: Why does TechFlow say my password is incorrect when I am sure it is right?
A: Check that Caps Lock is off, that your password manager filled the correct entry and that you are not using an old password. If you are unsure, reset your password rather than risk a lockout.

Q: Why does TechFlow say the email address is not recognized?
A: The address may be mistyped or may differ from the one registered on your TechFlow account. For privacy, TechFlow shows a similar message whether or not an account exists.

Q: TechFlow login keeps redirecting me back to the login page. How do I fix it?
A: This is usually caused by blocked or stale cookies. Clear cookies for the TechFlow domain, allow first-party cookies and try again in a private window.

Q: Which browsers does TechFlow login support?
A: TechFlow login supports the current and previous major versions of Chrome, Firefox, Safari and Edge. Older browsers may fail to load the login form or MFA prompt.

Q: Do I need to enable cookies to log in to TechFlow?
A: Yes, TechFlow needs first-party cookies to keep you signed in. Blocking all cookies will cause login loops.

Q: Why does TechFlow show a captcha when I log in?
A: TechFlow shows a captcha after repeated failed attempts or when the login looks automated. Solving it lets you continue, and it usually disappears after a successful login.

Q: The TechFlow captcha will not load. What can I do?
A: Disable extensions that block scripts, allow the captcha provider domain and refresh the page. If it still fails, try another browser or network.

Q: Can I log in to TechFlow while connected to a VPN?
A: Yes, but some VPN exit locations may trigger extra verification or a captcha. Switching to another server or disconnecting briefly often resolves login problems.

Q: Why does TechFlow ask for extra verification when I log in from a new country?
A: TechFlow flags logins from unusual locations and asks for an email or MFA confirmation. This protects your account if your password was exposed.

Q: What does the TechFlow error "Too many requests" at login mean?
A: It means your IP address sent too many login requests in a short time and was rate-limited. Wait 5 minutes and try again.

Q: Why is my TechFlow account showing as disabled?
A: A workspace admin may have deactivated your TechFlow user, or your account was suspended for security reasons. Contact your admin or TechFlow support to find out which.

Q: Why do I get a "verification required" message after registering for TechFlow?
A: TechFlow needs you to confirm your email before you can log in. Click the link in the verification email, which is valid for 24 hours, or request another from the login page.

Q: How long is a TechFlow session before it times out?
A: A TechFlow session ends after 30 minutes of inactivity. You are asked to log in again when you return.

Q: Can I change the TechFlow session timeout?
A: Workspace admins can set the inactivity timeout between 15 minutes and 8 hours under Admin, then Security policies. The default is 30 minutes.

Q: What does the Remember me option do on the TechFlow login page?
A: Remember me keeps you signed in on that browser for up to 14 days even after you close it. Do not use it on shared computers.

Q: Where can I see my active TechFlow sessions?
A: Open Profile, then Security, then Active sessions to see each device, browser, approximate location and last activity. You can end any session from that list.

Q: How do I sign out of a single TechFlow session on another device?
A: In Active sessions, choose the session you want to end and click Revoke. That device is signed out of TechFlow immediately.

Q: How do I sign out of TechFlow everywhere?
A: Go to Security, then Active sessions, and click Sign out all other sessions. Use it if you lost a device or suspect someone else has access.

Q: Does changing my password sign me out of other TechFlow devices?
A: Yes, changing or resetting your TechFlow password ends all other sessions and revokes remember-me tokens. API keys are not affected.

Q: Why was I signed out of TechFlow unexpectedly?
A: Common reasons are the 30-minute inactivity timeout, a password change, an admin revoking your session or cleared browser cookies. Log in again to continue.

Q: Can I be logged in to TechFlow on multiple devices at once?
A: Yes, you can have up to 10 active TechFlow sessions at the same time. When you exceed the limit, the oldest session is ended.

Q: What is the maximum length of a TechFlow session, even if I stay active?
A: A TechFlow session lasts at most 12 hours of continuous activity before you must log in again. Remember me sessions are limited to 14 days.

Q: How do I create a TechFlow API key?
A: Go to Profile, then Developer, then API keys, click Create key, name it and choose scopes. The key is shown only once, so copy it right away.

Q: What is the difference between a TechFlow API key and a personal access token?
A: A TechFlow API key belongs to a workspace integration, while a personal access token acts as you with your own permissions. Tokens are tied to your user and stop working if your account is removed.

Q: How long do TechFlow API keys last?
A: TechFlow API keys expire after 90 days by default. You can choose a shorter lifetime, or up to 365 days if your admin allows it.

Q: Will TechFlow warn me before my API key expires?
A: Yes, TechFlow emails the key owner 14 days and 3 days before expiry. The warning names the key and its expiration date.

Q: How do I rotate a TechFlow API key?
A: Create a new key with the same scopes, update your application to use it and then revoke the old key. TechFlow lets two keys be valid at once so rotation causes no downtime.

Q: How often should I rotate my TechFlow API keys?
A: We recommend rotating TechFlow API keys at least every 90 days, matching the default expiry. Rotate immediately if a key may have been exposed.

Q: How do I revoke a TechFlow API key?
A: Open Developer, then API keys, select the key and click Revoke. Revocation takes effect within seconds and cannot be undone.

Q: What should I do if I accidentally committed my TechFlow API key to a public repository?
A: Revoke the key immediately, create a replacement and review the audit log for unexpected use. Removing the commit alone does not make the key safe.

Q: What scopes are available for TechFlow API keys?
A: TechFlow offers read, write and admin scopes, split by resource such as projects, users and billing. Choose the narrowest scopes your integration needs.

Q: Can I change the scopes of an existing TechFlow API key?
A: No, scopes are fixed when a TechFlow key is created. Create a new key with the right scopes and revoke the old one.

Q: I lost my TechFlow API key. Can I view it again?
A: No, TechFlow shows the full key only once at creation and stores only a hash. Create a new key and revoke the lost one.

Q: How many TechFlow API keys can I create?
A: Each TechFlow user can have up to 25 active API keys and personal access tokens combined. Revoke unused ones to free space.

Q: How do I send a TechFlow API key with my requests?
A: Send it in the Authorization header as a Bearer token over HTTPS. TechFlow rejects keys placed in URLs or sent over plain HTTP.

Q: Why does the TechFlow API return 401 Unauthorized?
A: A 401 means the key is missing, expired, revoked or mistyped. Check the key's status under Developer, then API keys.

Q: Why does the TechFlow API return 403 Forbidden?
A: A 403 means the key is valid but lacks the scope or the user permission for that action. Add the needed scope with a new key or ask an admin for the right role.

Q: Can I see when a TechFlow API key was last used?
A: Yes, the API keys page shows the last-used date and IP address for each key. Unused keys are good candidates for revocation.

Q: Can I restrict a TechFlow API key to specific IP addresses?
A: Yes, workspace admins can add an IP allowlist to a key under its settings. Requests from other addresses are rejected.

Q: How do I create a TechFlow personal access token?
A: Go to Profile, then Developer, then Personal access tokens, click Generate token, set the scopes and expiry and copy the value. Tokens follow the same 90-day default expiry as API keys.

Q: What happens to my TechFlow personal access tokens if I change my password?
A: They keep working, because tokens are separate credentials from your password. Revoke them manually if you suspect compromise.

Q: What happens to TechFlow API keys when the owner leaves the company?
A: Keys owned by a removed user are revoked automatically, which can break integrations. Use service accounts for shared or long-lived integrations instead.

Q: What is an OAuth app authorization in TechFlow?
A: It is permission you give a third-party application to access your TechFlow data without sharing your password. Each authorization lists the scopes granted.

Q: How do I see which apps have access to my TechFlow account?
A: Open Profile, then Security, then Authorized apps to see each app, its scopes and the date it was granted. You can revoke any of them.

Q: How do I revoke an app's access to my TechFlow account?
A: In Authorized apps, select the application and click Revoke access. Its tokens stop working immediately.

Q: What does the consent screen show when I authorize an app with TechFlow?
A: The TechFlow consent screen shows the app name, the developer and the exact scopes requested. Review it carefully and decline anything unfamiliar.

Q: Can workspace admins restrict which apps can connect to TechFlow?
A: Yes, admins can allowlist approved OAuth apps or require admin approval for new ones under Admin, then Integrations. Members cannot authorize blocked apps.

Q: How long do OAuth access tokens last in TechFlow?
A: TechFlow OAuth access tokens last 1 hour, and refresh tokens last 30 days unless revoked. Apps renew access automatically while the authorization is active.

Q: What is a trusted device in TechFlow?
A: A trusted device is a browser where you chose to skip MFA prompts after a successful login. TechFlow remembers it for 30 days.

Q: How do I remove a trusted device from my TechFlow account?
A: Go to Security, then Trusted devices, and click Remove next to the device. You will be asked for MFA on that device at the next login.

Q: Can admins disable trusted devices for the TechFlow workspace?
A: Yes, admins can turn off device trust under Security policies so every login requires MFA. Existing trusted devices are cleared.

Q: What are TechFlow login alerts?
A: Login alerts are emails sent when your account is accessed from a new device or location. They include the time, browser and approximate place.

Q: How do I turn TechFlow login alerts on or off?
A: Go to Profile, then Notifications, then Security alerts. New-device alerts are on by default and we recommend keeping them enabled.

Q: What should I do if I get a TechFlow login alert for a login I did not make?
A: Change your password immediately, sign out all other sessions and review your MFA methods and API keys. Then report it to security@techflow.example.

Q: How can I check my recent TechFlow login history?
A: Open Profile, then Security, then Login history to see the last 90 days of successful and failed logins. Each row shows the IP address, device and result.

Q: How do I know a TechFlow security email is genuine?
A: Genuine emails come from the techflow.example domain and never ask for your password or codes. When in doubt, go to the site directly instead of clicking a link.

Q: How do I report suspicious activity on my TechFlow account?
A: Email security@techflow.example with the time and details of what you saw, or use Report a problem in Security. The security team replies within 1 business day.

Q: How do I recover a TechFlow account if I lost both my password and MFA?
A: Start with the password reset link, then use a recovery code for MFA. If you have neither, contact support to begin identity verification, which can take up to 2 business days.

Q: What proof does TechFlow support need to recover my account?
A: Support asks you to confirm the registered email, workspace name and recent billing or activity details. They may ask a workspace admin to vouch for you.

Q: How do I delete my TechFlow account?
A: Go to Profile, then Account, then Delete account and confirm with your password and MFA. Workspace owners must transfer ownership first.

Q: Can I undo deleting my TechFlow account?
A: Yes, TechFlow keeps a deleted account for 30 days, and logging in during that period restores it. After 30 days the data is permanently erased.

Q: What happens to my API keys and sessions when I delete my TechFlow account?
A: All sessions, API keys, personal access tokens and app authorizations are revoked immediately. They are not restored even if you recover the account.

Q: What TechFlow roles exist at login level?
A: TechFlow has Owner, Admin, Member and Viewer roles that apply as soon as you log in. Owners and Admins manage security settings, while Viewers have read-only access.

Q: Who can change my role in TechFlow?
A: Workspace Owners and Admins can change roles from Admin, then Users. Admins cannot promote anyone above their own role.

Q: Why can I log in to TechFlow but not see certain projects?
A: Logging in confirms who you are, while project access depends on your role and project membership. Ask a project admin to add you.

Q: Who can see the TechFlow audit log of sign-ins?
A: Owners and Admins can view workspace sign-in and security events under Admin, then Audit log. Regular members see only their own login history.

Q: What is a TechFlow service account?
A: A service account is a non-human identity for automations, integrations and CI jobs. It is not tied to a person and does not use passwords or MFA.

Q: How do I create a TechFlow service account?
A: Workspace Admins open Admin, then Service accounts, click Create, name it and assign a role. Then generate an API key for it.

Q: Can a TechFlow service account log in through the web interface?
A: No, service accounts can authenticate only with API keys and cannot sign in to the TechFlow web app. This reduces the risk of credential misuse.

Q: How long do TechFlow service account keys last?
A: Service account keys follow the same 90-day default expiry as other TechFlow API keys. Admins can extend them up to 365 days.

Q: How should I choose the role for a TechFlow service account?
A: Give it the lowest role that works, usually Member or Viewer, and restrict its key scopes and IP addresses. Avoid giving automations Admin rights.

Q: Is single sign-on available in TechFlow?
A: Yes, TechFlow supports single sign-on for workspaces, and its setup and troubleshooting are covered in the separate SSO FAQ. This Auth FAQ covers password, MFA, session and key questions.

Q: What are the best practices for keeping a TechFlow account secure?
A: Use a unique password of 12 or more characters, enable MFA with an authenticator app or security key, and store your recovery codes safely. Review active sessions and API keys regularly.

Q: Is it safe to use TechFlow on a public or shared computer?
A: Avoid it if possible, and never choose Remember me or trusted device there. Always sign out and close the browser when finished.

Q: Should I use the same password for TechFlow and other websites?
A: No, reusing passwords lets a breach elsewhere expose your TechFlow account. Use a unique password for each service.

Q: How does TechFlow protect stored passwords?
A: TechFlow never stores plain-text passwords and keeps only salted hashes created with a modern slow hashing algorithm. Support staff cannot see your password.

Q: Is TechFlow login traffic encrypted?
A: Yes, all TechFlow login and API traffic uses HTTPS with TLS 1.2 or higher. Plain HTTP requests are refused.

Q: Who do I contact if I cannot log in to TechFlow?
A: Contact TechFlow support at support@techflow.example or open a ticket from the Help link on the login page. Include your account email and any error message you see.

Q: What are the TechFlow support hours for login problems?
A: Support answers login and security tickets Monday to Friday, 8 am to 8 pm Eastern Time, with a first response time that depends on the customer's support plan. Suspected compromises are prioritized.

Q: How do I contact TechFlow about a security vulnerability?
A: Email security@techflow.example with a description and steps to reproduce. Please do not share details publicly until the team has responded.
