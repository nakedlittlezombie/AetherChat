from email_service import send_verification_email

# Test the email sending
test_email = "nexusjuan@gmail.com"  # Your email for testing
test_token = "test-token-123"

print(f"Attempting to send test email to: {test_email}")
result = send_verification_email(test_email, test_token)
if result:
    print("Test email sent successfully!")
else:
    print("Failed to send test email.")
