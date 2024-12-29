import os
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz

def get_user_input():
    print("กรอกข้อมูลสำหรับสร้างสลิปปลอม:\n")
    name_user = input("ชื่อผู้โอนจ่าย: ")
    name_me = input("ชื่อผู้รับเงิน: ")
    phone_me = input("เบอร์โทรศัพท์ผู้รับ: ")
    money = input("จำนวนเงิน: ")
    return name_user, name_me, phone_me, money

def generate_slip(name_user, name_me, phone_me, money):
    try:
        thailand_timezone = pytz.timezone('Asia/Bangkok')
        current_time_thailand = datetime.datetime.now(thailand_timezone)

        time = current_time_thailand.strftime("%H:%M:%S")
        day = current_time_thailand.strftime("%d")
        month = current_time_thailand.strftime("%m")
        year = current_time_thailand.strftime("%Y")

        image = Image.open("truemoney.png")
        draw = ImageDraw.Draw(image)

        font_folder = "font"

        font_money = ImageFont.truetype(os.path.join(font_folder, "Lato-Heavy.ttf"), 87)
        font_user = ImageFont.truetype(os.path.join(font_folder, "Kanit-ExtraLight.ttf"), 48)
        font_me = ImageFont.truetype(os.path.join(font_folder, "Kanit-ExtraLight.ttf"), 48)
        font_phone = ImageFont.truetype(os.path.join(font_folder, "Prompt-Light.ttf"), 40)
        font_time = ImageFont.truetype(os.path.join(font_folder, "Kanit-Light.ttf"), 37)
        font_order = ImageFont.truetype(os.path.join(font_folder, "Kanit-Light.ttf"), 37)

        text_money = money + ".00"
        text_name_user = name_user
        text_name_me = name_me
        text_name_phone = f"{phone_me[:3]}-xxx-{phone_me[6:]}"
        text_name_time = f"  {day}/{month}/{year} {time}"
        text_name_order = "50018935012188"

        draw.text((560, 270), text_money, font=font_money, fill=(44, 44, 44))
        draw.text((302, 485), text_name_user, font=font_user, fill=(20, 20, 20))
        draw.text((302, 648), text_name_me, font=font_me, fill=(20, 20, 20))
        draw.text((302, 720), text_name_phone, font=font_phone, fill=(80, 80, 80))
        draw.text((781, 885), text_name_time, font=font_time, fill=(60, 60, 60))
        draw.text((827, 953), text_name_order, font=font_order, fill=(60, 60, 60))

        folder_name = "slip"
        os.makedirs(folder_name, exist_ok=True)

        output_filename = os.path.join(folder_name, "truemoney_with_text.png")
        image.save(output_filename)
        print(f"\n✅ : {output_filename} \n")
        input("ENTER")
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e} \n")
        input("ENTER")

if __name__ == "__main__":
    user_data = get_user_input()

    generate_slip(*user_data)