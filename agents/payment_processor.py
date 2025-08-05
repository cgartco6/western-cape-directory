import stripe
import fnb_api  # (Mock FNB API)

class PaymentProcessor:
    def __init__(self):
        stripe.api_key = "YOUR_STRIPE_TEST_KEY"
        self.fnb = fnb_api.SandboxClient()

    def charge_customer(self, user_id, amount):
        stripe.PaymentIntent.create(amount=amount, currency="zar")
        self.fnb.transfer(amount, "OWNER_ACCOUNT")

if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.charge_customer("user123", 1000)  # R10.00
