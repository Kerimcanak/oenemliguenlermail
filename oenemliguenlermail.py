import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from hijri_converter import convert

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain', 'utf-8'))
    
    # Send email
    smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
    
    # Quit SMTP server
    smtp_server.quit()

def generate_message(name):
    today = datetime.date.today()
    hijri_date = convert.Gregorian(today.year, today.month, today.day).to_hijri()

    if today.month == 1 and today.day == 1:
        return f"Sayın, {name}, Yeni yılınız kutlu olsun!"
    elif today.month == 4 and today.day == 23:
        return f"Sayın, {name}, 23 Nisan Ulusal Egemenlik ve Çocuk Bayramınız kutlu olsun!"
    elif today.month == 5 and today.day == 1:
        return f"Sayın, {name}, 1 Mayıs İşçi Bayramınız kutlu olsun!"
    elif today.month == 5 and today.day == 19:
        return f"Sayın, {name}, 19 Mayıs Atatürk’ü Anma, Gençlik ve Spor Bayramınız kutlu olsun!"
    elif today.month == 7 and today.day == 15:
        return f"Sayın, {name}, 15 Temmuz Milli Birlik ve Demokrasi Gününüz kutlu olsun!"
    elif today.month == 8 and today.day == 30:
        return f"Sayın, {name}, 30 Ağustos Zafer Bayramınız kutlu olsun!"
    elif today.month == 10 and today.day == 29:
        return f"Sayın, {name}, 29 Ekim Cumhuriyet Bayramınız kutlu olsun!"
    elif hijri_date.month == 10 and hijri_date.day == 1:
        return f"Sayın, {name}, Ramazan Bayramınız kutlu olsun!"
    elif hijri_date.month == 12 and hijri_date.day == 10:
        return f"Sayın, {name}, Kurban Bayramınız kutlu olsun!"
    else:
        return None

def main():
    # Email credentials
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_password'
    
    # Get recipient's name
    recipient_name = input("Please enter the recipient's name: ")
    receiver_email = 'recipient_email@example.com'  # Replace with the recipient's email address

    # Generate message
    message = generate_message(recipient_name)
    if message:
        # Send email
        subject = "Özel Gün Kutlaması"
        send_email(sender_email, sender_password, receiver_email, subject, message)
    else:
        print("No special holiday today.")

if __name__ == "__main__":
    main()
