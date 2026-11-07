# SSO FAQ

Q: How do I enable SSO?
A: Contact your admin to enable SSO for your account.

Q: What is single sign-on (SSO) in TechFlow?
A: SSO in TechFlow lets people sign in with the account they already use at their company identity provider (IdP) instead of a separate TechFlow password. The IdP verifies the user and TechFlow trusts that result.

Q: What are the benefits of using SSO with TechFlow?
A: SSO with TechFlow gives users one set of credentials, lets admins apply company security policies in one place, and removes access automatically when someone leaves. It also reduces password reset requests.

Q: Can an end user turn on SSO for their own TechFlow account?
A: No, end users cannot turn on SSO themselves in TechFlow. SSO is configured for the whole organization by an admin, so users should ask their admin.

Q: Who can configure SSO in TechFlow?
A: Only TechFlow admins with the Owner or Security Admin role can configure SSO. They do it in Settings > Security > Single sign-on.

Q: Where do admins find the SSO settings in TechFlow?
A: Admins find the SSO settings in TechFlow under Settings > Security > Single sign-on. The page contains the protocol choice, metadata fields, domain verification, and enforcement options.

Q: Which SSO protocols does TechFlow support?
A: TechFlow supports SAML 2.0 and OpenID Connect (OIDC) for single sign-on. Admins choose one protocol per organization.

Q: Should I choose SAML 2.0 or OpenID Connect for TechFlow SSO?
A: Choose the protocol your identity provider supports best; both give the same user experience in TechFlow. SAML 2.0 is the common choice for enterprise IdPs, while OIDC is often simpler to set up.

Q: Can TechFlow use SAML and OpenID Connect at the same time?
A: No, a TechFlow organization can have only one active SSO connection at a time, either SAML 2.0 or OpenID Connect. To change protocol, an admin must reconfigure the connection.

Q: Which identity providers does TechFlow support?
A: TechFlow works with Okta, Microsoft Entra ID (formerly Azure AD), Google Workspace, OneLogin, Ping Identity, and JumpCloud. Any other IdP that supports SAML 2.0 or OpenID Connect should also work.

Q: How do I set up TechFlow SSO with Okta?
A: In Okta, create a SAML 2.0 app integration, paste the TechFlow ACS URL and Entity ID from Settings > Security > Single sign-on, and map the email attribute. Then upload Okta's metadata XML to TechFlow and assign users or groups to the app.

Q: How do I set up TechFlow SSO with Microsoft Entra ID?
A: In Microsoft Entra ID, create an enterprise application, choose SAML single sign-on, and enter the TechFlow Entity ID and ACS URL. Then copy the App Federation Metadata URL or XML into TechFlow and assign users to the application.

Q: Is Azure AD still supported by TechFlow?
A: Yes, Azure AD is now called Microsoft Entra ID, and TechFlow supports it exactly as before. Existing Azure AD connections keep working without changes.

Q: How do I set up TechFlow SSO with Google Workspace?
A: In the Google Admin console, add a custom SAML app, copy the TechFlow ACS URL and Entity ID into it, and download Google's metadata XML. Upload that XML in TechFlow and turn on the app for the right organizational units.

Q: Can I use OneLogin, Ping Identity, or JumpCloud with TechFlow?
A: Yes, TechFlow supports OneLogin, Ping Identity, and JumpCloud through SAML 2.0 or OpenID Connect. Create a custom app in the IdP and use the values shown in TechFlow's SSO settings.

Q: What is the TechFlow Entity ID?
A: The TechFlow Entity ID, also called the SP Entity ID or audience, is a unique identifier for your organization shown in Settings > Security > Single sign-on. You paste it into the IdP so the IdP issues assertions meant for TechFlow.

Q: What is the TechFlow ACS URL?
A: The ACS (Assertion Consumer Service) URL is the TechFlow address where your IdP posts the signed SAML response after login. It is displayed in Settings > Security > Single sign-on and must be entered into your IdP exactly as shown.

Q: How do I give TechFlow my IdP metadata XML?
A: In Settings > Security > Single sign-on, upload the metadata XML file from your IdP or paste its metadata URL. TechFlow reads the sign-in URL, entity ID, and signing certificate from it automatically.

Q: Can I enter the SAML settings manually instead of uploading metadata?
A: Yes, TechFlow lets admins enter the IdP sign-in URL, IdP issuer, and X.509 signing certificate by hand. Uploading metadata is recommended because it avoids typing mistakes.

Q: What certificate format does TechFlow accept for the IdP signing certificate?
A: TechFlow accepts X.509 signing certificates in PEM or CER format, typically using RSA 2048-bit or stronger keys and SHA-256 signatures. Certificates signed with SHA-1 are rejected.

Q: What attributes does TechFlow need from the identity provider?
A: TechFlow requires an email attribute and recommends first name and last name attributes. Groups can be sent as an optional attribute for role mapping.

Q: How does attribute mapping work in TechFlow SSO?
A: Attribute mapping tells TechFlow which IdP claim holds each user property, such as email, firstName, lastName, and groups. Admins set this in Settings > Security > Single sign-on under Attribute mapping.

Q: What NameID format should I use for TechFlow SAML?
A: Use the emailAddress NameID format so the NameID matches the user's work email in TechFlow. A persistent or unspecified format can work only if the email is also sent as an attribute.

Q: Why does TechFlow ask me to verify my domain for SSO?
A: Domain verification proves your company owns the email domain, which prevents others from claiming it for SSO. TechFlow only applies SSO to users whose email belongs to a verified domain.

Q: How do I verify my domain in TechFlow?
A: In Settings > Security > Single sign-on, add your domain and TechFlow shows a DNS TXT record to create at your DNS provider. Once the record propagates, click Verify, which usually completes within an hour.

Q: Can I verify more than one email domain for SSO?
A: Yes, an organization can verify multiple domains, for example after a merger or for subsidiaries. All verified domains use the same SSO connection.

Q: Should I test SSO before enforcing it?
A: Yes, always test SSO before enforcing it in TechFlow. Saving the connection does not force anyone to use it, so you can test safely first.

Q: How do I test my TechFlow SSO configuration?
A: Click Test connection in Settings > Security > Single sign-on, which opens your IdP login in a new window. If the test succeeds, TechFlow shows the attributes it received; if not, it shows a specific error code.

Q: Will testing SSO log out other users?
A: No, testing SSO in TechFlow only affects the admin running the test. Other users continue to sign in as usual until SSO is enforced.

Q: What does enforcing SSO do in TechFlow?
A: When SSO is enforced, everyone with an email on a verified domain must sign in through the IdP, and TechFlow password login is disabled for them. Existing sessions end at their next re-authentication.

Q: How do I enforce SSO for my organization?
A: After a successful test, an admin turns on Require SSO in Settings > Security > Single sign-on. TechFlow asks for confirmation before the setting takes effect.

Q: Can I enforce SSO for only some users?
A: Yes, admins can enforce SSO for everyone or exempt specific users, such as the break-glass admin accounts. Exemptions are managed in the Enforcement section of the SSO settings.

Q: How do I exempt a user from SSO enforcement?
A: Add the user to the SSO exemption list in Settings > Security > Single sign-on. Exempt users can still sign in with their TechFlow password and MFA.

Q: How many users can be exempt from SSO?
A: An organization can exempt up to 5 users from SSO enforcement in TechFlow. Exemptions are intended for emergency access, not regular use.

Q: What is break-glass access in TechFlow SSO?
A: Break-glass access is an emergency admin account that can sign in with a password even when SSO is enforced. It lets you recover if your IdP is down or misconfigured.

Q: How should I set up a break-glass admin account?
A: Create a dedicated TechFlow admin with a unique non-personal email, add it to the SSO exemption list, and protect it with a strong password and MFA. Store the credentials in a secure vault and review its use regularly.

Q: What if I am locked out because my IdP is misconfigured?
A: Sign in with a break-glass admin account, then fix or disable the SSO connection in Settings > Security > Single sign-on. If no break-glass account exists, contact TechFlow support to verify your identity and restore access.

Q: What is just-in-time (JIT) provisioning in TechFlow?
A: JIT provisioning creates a TechFlow account automatically the first time a user signs in through SSO. The account is filled in with attributes from the IdP.

Q: How do I turn on just-in-time provisioning?
A: An admin enables Just-in-time provisioning in Settings > Security > Single sign-on and picks a default role for new users. It applies to users on verified domains.

Q: What role does a JIT-provisioned user get?
A: A JIT-provisioned user gets the default role the admin selected, which is Member unless changed. If group-to-role mapping is configured, the mapped role takes priority.

Q: What happens if JIT provisioning is off and a new user tries SSO?
A: If JIT provisioning is off, a user without an existing TechFlow account is denied access with an account-not-found message. An admin must invite the user or provision them through SCIM first.

Q: What is SCIM in TechFlow?
A: SCIM (System for Cross-domain Identity Management) lets your IdP automatically create, update, and deactivate TechFlow users. It keeps your user list in TechFlow in sync with your directory.

Q: Which TechFlow plans include SCIM provisioning?
A: SCIM provisioning is available on the Enterprise plan only. SSO itself is available on Business and Enterprise.

Q: How do I set up SCIM in TechFlow?
A: In Settings > Security > SCIM, an admin generates a SCIM base URL and token, then enters them in the IdP's provisioning settings. Enable create, update, and deactivate users in the IdP, then assign users or groups.

Q: How often does SCIM sync with TechFlow?
A: TechFlow processes SCIM changes continuously as they arrive, and a full reconciliation sync runs every 40 minutes. Changes pushed by your IdP typically appear within a few minutes, though some IdPs push on their own schedule.

Q: What happens in TechFlow when a user is deprovisioned through SCIM?
A: The user is deactivated immediately, all active sessions are revoked, and their API keys stop working. Their data and content remain in the organization and can be reassigned.

Q: Does SCIM deprovisioning delete a user's data in TechFlow?
A: No, SCIM deprovisioning deactivates the account but keeps the user's data. An admin can reassign owned items or permanently delete the user later.

Q: What does the SCIM token do, and can it expire?
A: The SCIM token authenticates your IdP when it calls TechFlow's SCIM API. Tokens are valid for 12 months and can be regenerated at any time in Settings > Security > SCIM.

Q: Can SCIM create TechFlow users who have no SSO login?
A: Yes, SCIM creates the account, and the user can then sign in through SSO. If SSO is enforced, they cannot use a password.

Q: What is group-to-role mapping in TechFlow?
A: Group-to-role mapping assigns TechFlow roles based on the IdP groups a user belongs to. For example, the group techflow-admins can map to the Admin role.

Q: How do I configure group-to-role mapping?
A: In Settings > Security > Single sign-on, open Group mapping and enter each IdP group name next to the TechFlow role it should grant. The IdP must send the groups attribute in the SAML assertion or OIDC token.

Q: What if a user belongs to multiple mapped groups?
A: TechFlow gives the user the highest-privilege role among their mapped groups. For example, a user in both a Member group and an Admin group becomes an Admin.

Q: What role does a user get if none of their groups are mapped?
A: A user with no mapped groups receives the default role set for the organization, which is Member unless changed. If no default is set, the user is blocked from signing in.

Q: How often are roles updated from group membership?
A: TechFlow refreshes a user's role from their groups at every SSO login and during SCIM syncs every 40 minutes. A change in the IdP therefore takes effect at the user's next login or the next sync.

Q: How long is the SAML signing certificate valid in TechFlow?
A: TechFlow's SAML signing certificates are valid for 12 months. After that, a new certificate must be in place to keep SSO working.

Q: Will TechFlow warn me before my SSO certificate expires?
A: Yes, TechFlow emails admins and shows a banner in Settings 30 days before the certificate expires. Reminders repeat weekly until the certificate is rotated.

Q: What happens if the SSO certificate expires?
A: If the certificate expires, SSO sign-ins fail with a signature or certificate error. Break-glass accounts can still sign in so an admin can upload the new certificate.

Q: How do I rotate the SAML certificate in TechFlow?
A: Upload the new IdP certificate or metadata in Settings > Security > Single sign-on and click Save. If TechFlow's own certificate is rotating, copy the new metadata into your IdP before the old one expires.

Q: Can TechFlow trust two certificates during rotation?
A: Yes, TechFlow lets you add a secondary signing certificate so both the old and new IdP certificates are accepted. Remove the old one after the IdP has switched.

Q: Will users be signed out when I rotate the certificate?
A: No, rotating the certificate does not sign out existing users. Active sessions continue until their normal 8-hour expiry.

Q: How long does an SSO session last in TechFlow?
A: An SSO session in TechFlow lasts 8 hours. After that, the user must re-authenticate through the IdP.

Q: Can admins change the SSO session length?
A: Yes, admins can set the session length between 1 and 12 hours in Settings > Security > Session policy. The default is 8 hours.

Q: Does TechFlow end the session when I sign out of my IdP?
A: No, signing out of the IdP does not end an existing TechFlow session, because single logout is not supported yet. The TechFlow session ends when you sign out of TechFlow or after 8 hours.

Q: Will I need to sign in again every day with SSO?
A: Yes, because sessions last 8 hours, most users sign in about once per working day. If your IdP session is still active, the sign-in is automatic with no prompt.

Q: What is SP-initiated login in TechFlow?
A: SP-initiated login starts at TechFlow: the user enters their work email on the TechFlow sign-in page and is redirected to the IdP. This is the recommended way to sign in.

Q: What is IdP-initiated login in TechFlow?
A: IdP-initiated login starts from the IdP's app dashboard, where the user clicks the TechFlow tile and arrives already signed in. TechFlow supports it for SAML 2.0 connections.

Q: Can I disable IdP-initiated login?
A: Yes, admins can turn off IdP-initiated login in Settings > Security > Single sign-on to require SP-initiated login only. This reduces exposure to unsolicited assertions.

Q: Does TechFlow SSO work with multi-factor authentication?
A: Yes, when SSO is enabled, your IdP handles MFA, and TechFlow accepts the IdP's authentication result. Details on TechFlow's own MFA are in the separate Auth FAQ.

Q: Will TechFlow ask for MFA again after SSO login?
A: No, TechFlow does not ask for a second MFA prompt for SSO users, since it trusts the MFA done at the IdP. Exempt users who sign in with passwords still use TechFlow MFA, described in the Auth FAQ.

Q: Where are password reset steps for non-SSO users documented?
A: Password reset and TechFlow MFA setup are covered in the separate Auth FAQ. SSO users reset their password at their IdP, not in TechFlow.

Q: What does the error "SAML response expired" or clock skew mean?
A: It means the time on the IdP and TechFlow differ by more than the allowed 5 minutes. Fix the clock on the IdP server using NTP and try again.

Q: What is the clock skew tolerance in TechFlow SSO?
A: TechFlow tolerates up to 5 minutes of clock difference between your IdP and TechFlow when validating assertions. Larger differences cause a login failure.

Q: What causes the "Invalid signature" error in TechFlow SSO?
A: The SAML response was signed with a certificate that does not match the one saved in TechFlow, often after the IdP rotated its certificate. Upload the current IdP metadata or certificate in Settings > Security > Single sign-on.

Q: What does "Audience mismatch" mean in TechFlow SSO?
A: The audience value in the IdP's assertion does not match TechFlow's Entity ID. Copy the Entity ID exactly from Settings > Security > Single sign-on into the IdP's audience field, including any trailing slash.

Q: What does the error "User not assigned to application" mean?
A: The user has not been granted access to the TechFlow app in the IdP, so the IdP refuses to issue a login. Assign the user or one of their groups to the TechFlow application in the IdP.

Q: Why does TechFlow say my email does not match?
A: The email in the IdP assertion differs from the email on the TechFlow account, for example due to an alias or different domain. Align the email attribute in the IdP or ask an admin to update the TechFlow user.

Q: Why am I stuck in a redirect loop when signing in with SSO?
A: A redirect loop usually means the ACS URL is wrong, the browser blocks cookies, or the IdP session cannot be created. Clear cookies, confirm the ACS URL in the IdP, and try a private window.

Q: What does the error "Destination mismatch" mean?
A: The Destination in the SAML response does not match the TechFlow ACS URL. Re-enter the ACS URL in the IdP exactly as shown in the TechFlow SSO settings.

Q: What does "No email attribute found" mean?
A: TechFlow did not receive an email claim in the assertion or token. Check the attribute mapping in the IdP and in TechFlow so that the email field is sent.

Q: Why does OIDC login fail with "invalid redirect URI"?
A: The redirect URI registered at the IdP does not exactly match the one TechFlow uses. Copy the redirect URI from Settings > Security > Single sign-on into the IdP's allowed redirect URIs.

Q: Where can I see why an SSO login failed?
A: Admins can open the Audit log in Settings > Security and filter by SSO events to see the error code and time of each failed login. The error code maps to the troubleshooting entries in this FAQ.

Q: Why can a user sign in at the IdP but not reach TechFlow?
A: The user may be missing a TechFlow account because JIT provisioning is off, be deactivated, or be on a domain that is not verified. Check these in Settings and the Audit log.

Q: Can I switch to a different identity provider later?
A: Yes, admins can switch IdPs in Settings > Security > Single sign-on by uploading the new IdP's metadata. Users keep their TechFlow accounts as long as their emails stay the same.

Q: What is the safest way to migrate TechFlow from one IdP to another?
A: Set up the new IdP and test it, confirm a break-glass account works, and then replace the connection during a quiet period. Notify users that they may need to sign in again.

Q: Will users lose data when we change identity providers?
A: No, switching IdPs does not delete user data, because accounts are matched by email. Users who sign in with a changed email might create a duplicate, so keep emails consistent.

Q: How do I disable SSO in TechFlow?
A: An admin turns off Require SSO and then removes the connection in Settings > Security > Single sign-on. Users then sign in with TechFlow passwords.

Q: What happens to users' passwords when SSO is enabled?
A: Existing TechFlow passwords are kept but cannot be used to sign in once SSO is enforced. If SSO is disabled later, users can use their old password or reset it, as described in the Auth FAQ.

Q: Do SSO users need to create a TechFlow password?
A: No, SSO users do not need a TechFlow password, because the IdP authenticates them. A password is only needed for exempt accounts.

Q: Do my API keys stop working when SSO is enforced?
A: No, existing API keys keep working when SSO is enforced because they do not use interactive login. They stop working only if the owning user is deactivated.

Q: Can I create new API keys when SSO is enforced?
A: Yes, SSO users can create personal API keys after signing in through SSO. Admins can also issue service account keys that are not tied to a person.

Q: How do I sign in to the TechFlow mobile app with SSO?
A: In the TechFlow mobile app, enter your work email, and the app opens your IdP sign-in in a secure browser view. After you authenticate, you return to the app signed in.

Q: Does the mobile app session also last 8 hours?
A: Mobile app sessions follow the same 8-hour SSO session length by default. Admins can allow longer refresh for trusted devices in the session policy.

Q: How do I sign in to the TechFlow CLI with SSO?
A: Run the CLI's login command, which opens your browser for IdP authentication and returns a token to the CLI. The token follows the 8-hour SSO session length.

Q: Can automation scripts use SSO?
A: Automation should not use interactive SSO. Use service account API keys or tokens created by an admin, which keep working when SSO is enforced.

Q: Can contractors and guests use SSO in TechFlow?
A: Guests with an email on a verified domain sign in through SSO like employees. Guests from other domains are not covered by your SSO and use TechFlow password and MFA, described in the Auth FAQ.

Q: How do I handle contractors who are not in our identity provider?
A: Invite them as guests with their own email, or add them to the SSO exemption list if they need password sign-in. Alternatively, create contractor accounts in your IdP so they can use SSO.

Q: Can external guests be blocked when SSO is enforced?
A: Enforcement applies only to verified-domain users, so guests on other domains are not blocked. Admins can restrict guest invitations in Settings > Security > Guest access.

Q: Does TechFlow record SSO activity in audit logs?
A: Yes, TechFlow logs SSO configuration changes, logins, failures, and provisioning events in the Audit log. Entries include time, user, IP address, and result.

Q: How long are SSO audit logs kept?
A: SSO audit logs are retained for 12 months on Enterprise and 90 days on Business. Admins can export them as CSV from Settings > Security > Audit log.

Q: Can I get an alert when someone changes the SSO settings?
A: Yes, admins can turn on security notifications in Settings > Security > Alerts to receive an email whenever SSO settings change. The change is also recorded in the Audit log.

Q: Which TechFlow plans include SSO?
A: SSO with SAML 2.0 and OpenID Connect is available on the Business and Enterprise plans. The Free and Starter plans use password sign-in only.

Q: Does SSO cost extra?
A: No, SSO is included in the Business and Enterprise plans at no additional charge. SCIM is limited to Enterprise.

Q: How do I upgrade my plan to get SSO?
A: An account Owner can upgrade in Settings > Billing, or contact TechFlow sales. SSO becomes available as soon as the upgrade completes.

Q: How many users can use SSO?
A: There is no separate limit on SSO users, and every seat in your plan can sign in through SSO. The limit is your number of paid seats.

Q: Can different teams use different identity providers?
A: No, a TechFlow organization supports one SSO connection. Teams with separate IdPs should federate them into a single IdP or use separate TechFlow organizations.

Q: Is the SSO sign-in page branded for my company?
A: Yes, Enterprise admins can add a company logo and a custom sign-in message in Settings > Security > Sign-in page. Users who enter a verified-domain email are redirected to the IdP.

Q: How do users start SSO login from the TechFlow sign-in page?
A: Users enter their work email on the TechFlow sign-in page, and TechFlow detects the verified domain and redirects them to the IdP. There is no separate SSO button to find.

Q: Can I sign in with a personal email when my company uses SSO?
A: A personal email outside your verified domains cannot use the company SSO. It requires an invited guest account, which uses a password and MFA from the Auth FAQ.

Q: What happens to a user's account when their email changes in the IdP?
A: With SCIM, the TechFlow account email updates automatically at the next sync. Without SCIM, the user may get a new account at their next login if JIT is enabled, so an admin should update the old account first.

Q: Is SSO traffic encrypted?
A: Yes, all SSO communication with TechFlow uses HTTPS with TLS 1.2 or higher. SAML responses must also be digitally signed.

Q: Does TechFlow support encrypted SAML assertions?
A: Yes, TechFlow can accept encrypted assertions if you upload TechFlow's encryption certificate to your IdP. This is optional, since signed assertions are always required.

Q: Does TechFlow require signed SAML requests?
A: Signing of authentication requests is optional and can be enabled in Settings > Security > Single sign-on. Signed responses from the IdP are always required.

Q: Who do I contact if I need help with SSO setup?
A: Admins can contact TechFlow support at support@techflow.example, which is available on every support plan. End users should first contact their company admin or IT helpdesk.

Q: What should I include when asking TechFlow support about an SSO problem?
A: Include your organization name, the IdP you use, the error code shown, the time of the failure, and a screenshot. Admins can also attach the matching Audit log entry to speed up the diagnosis.

Q: Is there a guided setup for Enterprise customers?
A: Yes, Enterprise customers can request a guided SSO onboarding session with a TechFlow solutions engineer. Book it through your account manager or support.
