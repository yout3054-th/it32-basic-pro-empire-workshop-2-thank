name = str(input("ชื่อ "))
age = int(input("อายุ "))
tall = float(input("ส่วนสูง "))
stg = int(input("ความแข็งแกร่ง "))
monny =float(input("จำนวนเงิน"))
if stg == 10 and monny > 5000 :
    print ("คุณผ่านโดยได้ระดับสูง : ตำแหน่งหัวหน้ากลุ่ม")
elif stg >= 8 and monny >=2500 :
    print ("คุณผ่านโดยได้ระดับกลาง : ตำแหน่งกีกี้")
elif stg >=5 and monny > 1000 :
    print ("คุณผ่านโดยได้ระดับต่ำ : ตำแหน่งกีกี้ทำความสะอาด")
else :
    print("อ่อนแอเกินไปคุณไม่ผ่าน")
    print("กลับบ้านไปซะเด็กน้อย")