from datetime import datetime
digits = ["oh", "one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","forteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty"]
hour = ""
minute = ""
def convertTime(currentTime):
    if currentTime.hour < 13:
        hour = digits[currentTime.hour]
    else:
        hour = digits[currentTime.hour - 12]
    if str(currentTime.minute)[0] < '2':
        minute = digits[currentTime.minute]
    elif str(currentTime.minute)[1] == '0':
        minute = tens[int(str(currentTime.minute)[1])]
    else:
        minute = tens[int(str(currentTime.minute)[0])] + digits[int(str(currentTime.minute)[1])]
    print hour + " " +minute






convertTime(datetime.now())
