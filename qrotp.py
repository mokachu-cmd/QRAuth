import time
import pyotp
import base64
import qrcode

def generate_otp_and_verify():
    key = base64.b32encode(str(time.time()).encode()).decode()
    key_encoded = base64.b32encode(key.encode()).decode()

    totp = pyotp.TOTP(key_encoded, interval=30)

    uri = totp.provisioning_uri(name="Mo", 
                                issuer_name="OTPApp")

    qrcode.make(uri).save("totp.png")

    while True:
        user_otp = input("Enter the OTP from your authenitcator app: ")

        if totp.verify(user_otp, valid_window=1):
            print("OTP is valid.")
            return True
        else:
            print("OTP is invalid.")
            return False

while True:
    if generate_otp_and_verify():
        break
    else:
        print("Failed to verify OTP. Generating a new one.")