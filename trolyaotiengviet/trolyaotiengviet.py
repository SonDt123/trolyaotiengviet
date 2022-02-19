import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
import pyautogui
import urllib.request as urllib2
from random import choice #phần random ngẫu nhiên một câu nói
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()
#Speech to text
def speak(text):
    print("SU: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")
# Speech - to - text: Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản hiện ra khi máy trả lại kết quả đã nghe
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return 0
#
# AI chào Tạm biệt lại bạn khi bạn chào tạm biệt 
def stop():
    good_bye = ["Hẹn gặp lại bạn sau nhé!",
                "Bái bai bạn nhé",
                "gút bai si diu ờ gen nhé, Hihi"]
    speak(choice(good_bye))
    time.sleep(3)
# AI sẽ hỏi lại những gì nó không nghe rõ
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 3:
            nghe_khong_ro = ["Tôi không nghe rõ. Cậu chủ nói lại được không!",
                             "Xin lỗi bạn, tôi nghe không rõ",
                             "bạn nói lại nhé, Su không nghe rõ"]
            speak(choice(nghe_khong_ro))
            time.sleep(4)
    time.sleep(3)
    stop()
    return 0
# AI chào hỏi
def hello(name):
    hour = int(strftime('%H'))
    if hour >= 6 and hour<10:
        sau_AI = ["Chào buổi sáng bạn {}. Chúc cậu chủ một ngày tốt lành.".format(name),
                  "Chào buổi sáng bạn {}. Nếu bạn không vui hãy về đây với tôi nhé".format(name)]
        speak(choice(sau_AI))
        time.sleep(3)
    elif 10 <= hour>=10 and hour<12:
        muoi_AI = ["Chào buổi trưa bạn {}. Cậu chủ đã ăn trưa chưa nhỉ.".format(name),
                   "Chào buổi trưa bạn {}. Nếu bạn thấy mệt thì nghỉ ngơi đi nhé.".format(name)]
        speak(choice(muoi_AI))
        time.sleep(3)
    elif 12 <= hour>=12 and hour<18:
        muoihai_AI = ["Chào buổi chiều bạn {}. Cậu chủ đã dự định gì cho chiều nay chưa.".format(name),
                      "Chào buổi chiều bạn {}. Bạn đang làm gì thế?.".format(name),
                      "Chào buổi chiều bạn {}. Sắp tối rồi bạn đã ăn cơm chưa?.".format(name)]
        speak(choice(muoihai_AI))
        time.sleep(3)
    elif 18 <= hour>=18 and hour<21:
        muoitam_AI = ["Chào buổi tối bạn {}. Cậu chủ đã ăn tối chưa nhỉ.".format(name),
                      "Chào buổi tối bạn {}. Nếu bạn chưa ăn tối, Su chúc bạn ăn tối vui vẻ nhé .".format(name)]
        speak(choice(muoitam_AI))
        time.sleep(3)
    elif hour>=21 and hour<24:
        haimot_AI = ["Chào buổi tối bạn {}. Đã khuya rồi bạn vẫn chưa đi ngủ sao?.".format(name),
                     "Chào buổi tối bạn {}. Nếu bạn chuẩn bị đi ngủ thì Su chúc bạn ngủ ngon nhé.".format(name),
                     "Chào buổi tối bạn {}. Nếu bạn buồn ngủ thì hãy ngủ đi nhé.".format(name)]
        speak(choice(haimot_AI))
        time.sleep(3)
    time.sleep(5)
#AI sẽ trả lời các câu hỏi về thời gian
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text or "phút" in text:
        speak('Bây giờ là %d Giờ %d Phút %d Giây' % (now.hour, now.minute, now.second))
        time.sleep(1)
    elif "ngày" in text or "tháng" in text or "năm" in text:
        speak("Hôm nay là Ngày %d Tháng %d Năm %d" % (now.day, now.month, now.year))
        time.sleep(2)
    else:
        speak("Xin lỗi tôi chưa hiểu ý của bạn. bạn nói lại được không?")
    time.sleep(4)
# Sai vặt AI mở các ứng dụng
def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        time.sleep(2)
        os.system("open /Applications/Google\ Chrome.app")
    elif "word" in text:
        speak("Mở Microsoft Word")
        time.sleep(2)
        os.system("open /Applications/Microsoft\ Word.app") 
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        time.sleep(2)
        os.system("open /Applications/Microsoft\ Excel.app")
    elif "Maps" in text:
        speak("Mở Maps")
        time.sleep(2)
        os.system("open /System/Applications/Maps.app")
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
# AI mở Web
def open_website(text):
    reg_ex = re.search('trang (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        time.sleep(3)
        return True
    else:
        return False
# Nhờ Google tìm kiếm
def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(5)
# Gửi Email tự Động   
def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    recipient = get_text()
    if 'yến' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('dtson.hcmus@gmail.com', '1201994dtS')
        mail.sendmail('dtson.bigedu@gmail.com',
                       content.encode('utf-8'))
        mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
    else:
        speak('SU không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
 # dự báo thời tiết       
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(30)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
#Nghe nhạc trên youtube
#Nghe nhạc trên youtube
def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát {} của bạn đã được mở.".format(mysong))
    time.sleep(3)
# Đọc Báo
def read_news():
    speak("Bạn muốn đọc báo về gì")
    time.sleep(3)
    queue = get_text()
    params = {
        'apiKey': '9cad52c3fb4e4f4e92d6c425fb5d9123',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])
# Trả lời tất cả các câu hỏi từ Wikipedia
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        time.sleep(3)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        time.sleep(30)
        for content in contents[1:]:
            speak("bạn có muốn nghe thêm không?")
            time.sleep(3)
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(3)
        speak('Cảm ơn bạn đã lắng nghe nhé!!!')
        time.sleep(3)
    except:
        speak("Xin lỗi Su không hiểu được thuật ngữ của bạn. Xin hãy nói lại ạ")
        time.sleep(5)
        
# Hướng dẫn
def help_me():
    speak("""Tôi có thể giúp bạn thực hiện các công việc sau đây:
    1. Tôi biết chào hỏi bạn nè
    2. cho bạn biết về thời gian và giờ giấc nè
    3. Mở các trang website, và các ứng dụng nè
    4. Giúp bạn Tìm kiếm trên Google nữa
    5. Gửi Email cho bạn bè
    6. cho bạn xem dự báo thời tiết
    7. Mở cho bạn một bản nhạc mà bạn yêu cầu
    8. Tôi có thể đọc báo cho bạn nghe nè
    9. Kể bạn biết về thế giới này nè
    10. Kể chuyện cười nè
    
    """)
    time.sleep(30)

# Giới thiệu bản thân của nó
def introduce():
    speak("""Xin chào. Rất hân hạnh được phục vụ bạn. Tôi là SU. 
             Tôi là trợ lý ảo được tạo ra dựa trên ngôn ngữ lập trình Python kết hợp với AI. 
             Tôi sinh ra vào ngày 01/02/2022 và được sáng lập bởi mr Sơn.
             Hiện tại bạn đang sử dụng phiên bản Ây Ai thử nghiệm và chưa hoàn thiện mong mọi người đợi ra sản phẩm hoàn thiện!.""")
    time.sleep(20)

# Phần giới thiệu
def ho_va_ten():
    ho_va_ten_AI = ["Tôi tên là Su Su",
                    "Bạn Thử Đoán xem tôi tên là gì nào?",
                    "đố bạn biết tôi tên là gì?",
                    "Bạn cứ gọi tôi là Su Su nhé"]
    speak(choice(ho_va_ten_AI))
    time.sleep(4)
# giới thiệu quê hương
def que_huong_AI():
    que_huong_noi = ["Tôi được sinh ra và lớn lên tại Việt Nam nè", 
                     "Tôi từ khi sinh ra đã ở trong tim cậu rồi HiHi", 
                     "Tôi sinh ra ở trong tim cậu nè"]
    speak(choice(que_huong_noi))
    time.sleep(3)
# giới thiệu tuổi
def tuoi_tac_AI():
    tuoi_tac_noi = ["Tôi chỉ mới được ba ngày tuổi thôi, tôi vẫn còn bé lắm", 
                    "Từ lúc sinh ra đến nay tôi chỉ mới đươc vài ngày tuổi thôi à", 
                    "Tôi ra đời từ đầu năm 2022, có thể nói tôi còn khá trẻ và tôi còn phải học nhiều thứ lắm!!!"]
    speak(choice(tuoi_tac_noi))
    time.sleep(3)

# Người yêu
def nguoi_yeu_AI():
    nguoi_yeu_noi = ["Tôi làm gì đã có người yêu, tôi còn đang sợ ế đây này",
                     "Tôi vẫn còn bé lắm",
                     "người yêu của tôi chính là cậu đấy",
                     "Bầu trời xanh, làn mây trắng. Anh yêu nắng hay yêu em?",
                     "Nhờ có nắng mới thấy cầu vồng. Nhờ có anh mới thấy màu hạnh phúc.",
                     "Anh yêu ơi ới ời. Anh đang ở đâu?",
                     "Soái ca là của ngôn tình. Còn anh thì chỉ của mình em thôi.",
                     "Giữa cuộc đời hàng ngàn cám dỗ.Em chỉ cần bến đỗ anh thôi.",
                     "Bồ công anh bay khi có gió. Em chỉ cười vì ở đó có anh.",
                     "Chỉ cần anh nói yêu, em sẽ bám theo anh suốt đời. Cô gái đang muốn muốn bật đèn xanh đấy. Cô nàng muốn gợi ý là mình chung thủy lắm đấy. Anh cứ thử tỏ tình mà xem.",
                     "Ba mươi chưa phải là Tết. Không làm bạn đâu phải là hết, còn có thể làm người yêu mà.",
                     "Ai nào cho mượn avatar để em đỡ cô đơn đi",
                     "Nắng đã có mũ, mưa đã có ô, còn em sẽ có ai?"]
    speak(choice(nguoi_yeu_noi))
    time.sleep(4)

#nếu hỏi tên bạn là gì?
def ten_ban(name):
    name_ban = ["tên của bạn là: {} nè".format(name),
                "Bạn tưởng Su quên tên bạn sao? tên bạn là {}".format(name),
                "Chào bạn {} nhé, tôi không quên tên của bạn đâu".format(name),
                "Tôi có trí nhớ siêu việt đấy bạn {} ạ!! Hihi...".format(name)]
    speak(choice(name_ban))
    time.sleep(6)
    
# Khi người dùng biểu lộ cảm xúc nó đáp
def Chan_qua_AI():
    chan_qua_noi = ["Tưởng gì tôi sẽ kể cho bạn một câu chuyện cười nhé, đảm bảm bạn sẽ vui",
                    "Chuyện nhỏ, để tôi, Su sẽ cố gắng làm cho bạn cười, hoặc biết đâu tôi sẽ khiến bạn ngạc nhiên đó, bạn có muốn nghe tôi kể chuyện không?",
                    "Để tôi kể cho bạn nghe một câu chuyện nhé đảm bảm bạn sẽ cười đó."]
    speak(choice(chan_qua_noi))
    time.sleep(10)

# truyện cười
    dap_chan_qua_noi = ["""Bạn nghe nhé: 
                           - Này Con! Anh cả con học kinh tế, anh hai thì học tài chính.
                             Sao con không theo gương các anh mà học luật?
                           - Bố nghĩ xem, nếu con không học làm luật sư thì sao này ai sẽ giúp anh hai con đây""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CƯỜI....!
                           - Trong cuộc thi vấn đáp, ban giám khảo hỏi thí sinh:
                           - Em tên gì?
                           - Em tên là Hà. 
                           - Cô gái nói xong thì cười rất rạng rỡ.
                             Ban giám khảo hỏi:
                           - Tại sao em lại cười.
                             Cô gái trả lời:
                           - Dạ, tại vì đề của câu 1 dễ quá!
                             Ban giám khảo: ...!!! """"",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : XỬ NHẦM...!
                           - Sau khi có phán quyết ly dị vợ, cậu thấy thế nào?
                           - Bi đát! Chiếc xe hơi mua bằng tiền tớ kiếm được, toà lại xử cho cô ấy.
                             Còn lũ trẻ, mà tớ đinh ninh là của người khác, toà lại xử cho sống chung với tớ.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : ÔNG NỘI VÀ CHÁU...!
                           - Ông nội và người cháu đích tôn 3 tuổi đang ngồi chơi trò bán hàng.
                           - Cháu: - Đây tôi đưa bác 5.000 đồng, nhưng với một điều kiện.
                           - Ông:  - Điều kiện gì cũng được.
                           - Cháu: - Thật không?
                           - Ông:  - Thật. Bác cứ nói đi.
                           - Cháu: - Bác phải về dạy lại con bác đi nhé, con bác hay đánh tôi lắm đấy.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : AN ỦI...!
                           - Cô: Nếu sau này em làm y tá, chuẩn bị tiêm thuốc cho 1 em nhỏ, em nhỏ sợ quá khóc òa lên, vậy em có tiêm không? 
                           - Bé: Không ạ!
                           - Cô: Vậy em có an ủi bé không ?
                           - Bé: Thưa cô, em sẽ an ủi là : thôi, đừng khóc nữa, nếu không cô chích cho 1 mũi bây giờ!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CHẾT… GIÀ...!
                           - Một người bị kết án tử hình khẩn cầu tòa giảm án. 
                             Quan tòa bảo:
                           - Anh đã phạm tội tày trời làm sao chúng tôi tha được? Nhưng có thể chấp thuận cho anh được quyền chọn lựa cách chết.
                             Tử tù vội nói:
                           - Xin đội ơn ngài. Xin cho tôi được chết… già!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : HỢP TÁC...!
                           - Ông chồng trò chuyện với vợ:
                           - Này em, từ ngày chúng ta dùng tiền để thưởng, con trai mình học khá hẳn lên, nhiều điểm 10 lắm, em thấy vui chứ?
                           - Theo em thì hẳn là nó đã đem tiền chia cho thày giáo một nửa thì có.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : KHEN KHÉO...!
                           - Mắm : Nè, ông thấy tôi mặc cái áo mới này như thế nào?
                           - Quỷnh: Ồ, tuyệt cú mèo!
                           - Mắm (hớn hở): Thật hả? Ông ko nịnh tôi đó chứ?
                           - Quỷnh: Thật mà! Cái áo thì “tuyệt”, còn bà là “cú mèo” đó
                           - Mắm: (suy sụp)!??""",
                           """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CÒN PHẢI XEM XÉT...!
                           - Chàng trai trở về nhà sau cuộc thi sát hạch lấy bằng lái xe với vẻ mặt hoang mang:
                           - Thật là rắc rối , Anh ta nói với ông bố : Chiếc xe tải đó có vấn đề.
                           - Nghĩa là con bị đánh trượt?
                           - Điều đó chưa rõ. Cả Ban giám khảo có còn ai chấm được điểm đâu ạ!"""]
    ke_AI = get_text()
    if "có" in ke_AI or "ok" in ke_AI or "kể" in ke_AI or "nghe"  in ke_AI:
        speak(choice(dap_chan_qua_noi))
        time.sleep(30)
        #playsound.playsound('Tieng_cuoi.mp3')
        speak('Su Su cảm ơn bạn đã nghe SU kể chuyện!!!')
        time.sleep(3)  
        for yess in dap_chan_qua_noi[1:]:
            nghe_tiepp = ["bạn có muốn nghe thêm không?",
                          "Bạn có muốn nghe Su kể nữa không",
                          "Để Su kể tiếp nhé"]
            speak(choice(nghe_tiepp))
            time.sleep(3)
            yess = get_text()
            if "có" not in yess or "ok" not in yess :
                break    
            speak(choice(dap_chan_qua_noi))
            time.sleep(28)
            #playsound.playsound('Tieng_cuoi.mp3')
            speak('Su cảm ơn bạn đã lắng nghe!!!')
            time.sleep(3)
    elif "không" in ke_AI:
        nghe_ke_chuyen = ["Bạn không muốn nghe tôi kể chuyện sao, buồn quá",
                          "Xin lỗi bạn nhé, nhưng tôi chỉ muốn bạn vui thôi mà",
                          "bạn muốn làm gì khác sao?, hãy nói với tôi nhé"]
        speak(choice(nghe_ke_chuyen))
        time.sleep(4)
    else:
        speak("Bạn vừa nói gì SU không hiểu. Xin hãy nói lại ạ")
        time.sleep(5)
        
def Ke_chuyen_AI(name):
    #open(r"trolyao\Part\truyencuoi.py")
    truyen_cuoi_AI = ["""Bạn nghe nhé: 
                           - Này Con! Anh cả con học kinh tế, anh hai thì học tài chính.
                             Sao con không theo gương các anh mà học luật?
                           - Bố nghĩ xem, nếu con không học làm luật sư thì sao này ai sẽ giúp anh hai con đây""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CƯỜI....!
                           - Trong cuộc thi vấn đáp, ban giám khảo hỏi thí sinh:
                           - Em tên gì?
                           - Em tên là Hà. 
                           - Cô gái nói xong thì cười rất rạng rỡ.
                             Ban giám khảo hỏi:
                           - Tại sao em lại cười.
                             Cô gái trả lời:
                           - Dạ, tại vì đề của câu 1 dễ quá!
                             Ban giám khảo: ...!!! """"",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : XỬ NHẦM...!
                           - Sau khi có phán quyết ly dị vợ, cậu thấy thế nào?
                           - Bi đát! Chiếc xe hơi mua bằng tiền tớ kiếm được, toà lại xử cho cô ấy.
                             Còn lũ trẻ, mà tớ đinh ninh là của người khác, toà lại xử cho sống chung với tớ.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : ÔNG NỘI VÀ CHÁU...!
                           - Ông nội và người cháu đích tôn 3 tuổi đang ngồi chơi trò bán hàng.
                           - Cháu: - Đây tôi đưa bác 5.000 đồng, nhưng với một điều kiện.
                           - Ông:  - Điều kiện gì cũng được.
                           - Cháu: - Thật không?
                           - Ông:  - Thật. Bác cứ nói đi.
                           - Cháu: - Bác phải về dạy lại con bác đi nhé, con bác hay đánh tôi lắm đấy.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : AN ỦI...!
                           - Cô: Nếu sau này em làm y tá, chuẩn bị tiêm thuốc cho 1 em nhỏ, em nhỏ sợ quá khóc òa lên, vậy em có tiêm không? 
                           - Bé: Không ạ!
                           - Cô: Vậy em có an ủi bé không ?
                           - Bé: Thưa cô, em sẽ an ủi là : thôi, đừng khóc nữa, nếu không cô chích cho 1 mũi bây giờ!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CHẾT… GIÀ...!
                           - Một người bị kết án tử hình khẩn cầu tòa giảm án. 
                             Quan tòa bảo:
                           - Anh đã phạm tội tày trời làm sao chúng tôi tha được? Nhưng có thể chấp thuận cho anh được quyền chọn lựa cách chết.
                             Tử tù vội nói:
                           - Xin đội ơn ngài. Xin cho tôi được chết… già!""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : HỢP TÁC...!
                           - Ông chồng trò chuyện với vợ:
                           - Này em, từ ngày chúng ta dùng tiền để thưởng, con trai mình học khá hẳn lên, nhiều điểm 10 lắm, em thấy vui chứ?
                           - Theo em thì hẳn là nó đã đem tiền chia cho thày giáo một nửa thì có.""",
                        """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : KHEN KHÉO...!
                           - Mắm : Nè, ông thấy tôi mặc cái áo mới này như thế nào?
                           - Quỷnh: Ồ, tuyệt cú mèo!
                           - Mắm (hớn hở): Thật hả? Ông ko nịnh tôi đó chứ?
                           - Quỷnh: Thật mà! Cái áo thì “tuyệt”, còn bà là “cú mèo” đó
                           - Mắm: (suy sụp)!??""",
                           """Bạn nghe nhé:
                           - Câu chuyện được mang tên là : CÒN PHẢI XEM XÉT...!
                           - Chàng trai trở về nhà sau cuộc thi sát hạch lấy bằng lái xe với vẻ mặt hoang mang:
                           - Thật là rắc rối , Anh ta nói với ông bố : Chiếc xe tải đó có vấn đề.
                           - Nghĩa là con bị đánh trượt?
                           - Điều đó chưa rõ. Cả Ban giám khảo có còn ai chấm được điểm đâu ạ!"""]
    speak(choice(truyen_cuoi_AI))
    time.sleep(28)
    #playsound.playsound('Tieng_cuoi.mp3')
    speak('Su cảm ơn bạn đã lắng nghe!!!')
    time.sleep(3) 
    for chuyen_chay in truyen_cuoi_AI[1:]:
        nghe_tiep = ["bạn có muốn nghe thêm không?",
                     "Bạn có muốn nghe Su kể nữa không",
                     "Để su  kể tiếp nhé"]
        speak(choice(nghe_tiep))
        time.sleep(3)
        chuyen_chay = get_text()
        if "có" not in chuyen_chay or "ok" not in chuyen_chay :
            break    
        speak(choice(truyen_cuoi_AI))
        #playsound.playsound('Tieng_cuoi.mp3')
        time.sleep(10)
        speak('SU cảm ơn bạn đã lắng nghe!!!')
        time.sleep(3) 
# phần điều khiển video, trình phát nhạc
def tatungdung():
    pyautogui.hotkey('cmd','q')
    pyautogui.hotkey('enter')
    speak("chương trình đã được tắt")
    time.sleep(3)
def tat():
    pyautogui.hotkey('m')
    speak("OK cậu chủ")
    time.sleep(3)
def bat():
    pyautogui.hotkey('m')
    speak("OK cậu chủ")
    time.sleep(3)
def chuyenbai():
    pyautogui.hotkey('shift','N')
    speak("đã chuyển bài")
    time.sleep(3)
def phongto():
    pyautogui.hotkey('f')
    speak("đã phóng to")
    time.sleep(3)
def tua():
    pyautogui.hotkey('right')
    speak("OK cậu chủ")
    time.sleep(3)
def lui():
    pyautogui.hotkey('left')
    speak("OK cậu chủ")
    time.sleep(3)
def pause():
    pyautogui.hotkey('space')
    speak("OK cậu chủ")
    time.sleep(3)
def play():
    pyautogui.hotkey('space')
    speak("OK cậu chủ")
    time.sleep(3)
def volumedown():
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down') 
def volumeup():
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
    pyautogui.hotkey('up')
#lien ket AI
def assistant():
    # loi_chao_AI=["Xin chào, cho tôi biết tên của cậu chủ nào",
    #              "Chào bạn, Tên của bạn là gì nhỉ?",
    #              "Để sử dụng, Cho tôi biết tên của bạn nhé",
    #              "Tôi có thể gọi bạn là gì nhỉ?",
    #              "Để Tiện Xưng hô cho tôi biết tên của bạn nào"]
    # speak(choice(loi_chao_AI))
    # time.sleep(3)
    #name = get_text()
    name ="Trường Sơn"
    if name:
        ho_ten = ["Chào {}, Tôi có thể giúp gì cho Cậu ạ?".format(name),
                  "Chào bạn {}, Su có thể giúp gì cho bạn ạ?".format(name),
                  "Xin chào bạn {} nhé".format(name)]
        speak(choice(ho_ten))
        time.sleep(3)
    if name:
        #speak("Chào bạn {}".format(name))
        #speak("Bạn cần Su Su có thể giúp gì ạ?")
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "bye" in text or "cút" in text or "đi đây" in text or "Stop" in text or "gặp lại sau" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm" in text or "hướng dẫn" in text or "sử dụng" in text or "biết làm" in text or "làm được gì" in text or "làm được những gì" in text:
                help_me()
            elif "chào" in text or "Xin chào" in text or "chào buổi sáng" in text or "chào buổi chiều" in text or "chào buổi trưa" in text or "chào buổi tối" in text:
                hello(name)
            elif "giờ" in text or "ngày" in text or "tháng" in text or "năm" in text or "thứ" in text or "thời gian hiện tại" in text:
                get_time(text)
            elif "ứng dụng" in text or "app" in text:
                speak("Tên ứng dụng bạn {} muốn mở là gì? ".format(name))
                time.sleep(3)
                text1 = get_text()
                open_application(text1)
            elif 'google và tìm kiếm' in text or "google" in text or "tìm kiếm" in text:
                open_google_and_search(text)
            elif "trang" in text or "web" in text or "website" in text:
                open_website(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "chơi nhạc" in text or "mở nhạc" in text or "nghe nhạc" in text:
                play_song()
            elif "đọc báo" in text or "tin tức" in text:
                read_news()
            elif "định nghĩa" in text or "giải thích" in text or "hỏi" in text or "cho tôi biết" in text:
                tell_me_about()
            elif "giới thiệu" in text:
                introduce()
            elif "tên là gì?" in text or "tên mày là gì" in text or "tên bạn là gì" in text or "mày tên là gì" in text or "bạn tên là gì" in text or "gọi bạn" in text or "gọi mày" in text:
                ho_va_ten()
            elif "sinh ra" in text or "quê hương" in text or "sống" in text or "đến từ" in text or "nơi sinh" in text or "ở" in text:
                que_huong_AI()
            elif "tuổi" in text or "năm" in text or "sinh" in text:
                tuoi_tac_AI()
            elif "người yêu" in text:
                nguoi_yeu_AI()
            elif "tên tôi" in text or "tên tao" in text or "tôi tên" in text or "tao tên" in text or "tên của tôi" in text or "biết tên" in text or "tên của tao" in text:
                ten_ban(name)
            elif "chán" in text or "buồn" in text or "mệt" in text or "nản" in text or "nhọc" in text:
                Chan_qua_AI()
            elif "kể" in text or "truyện"  in text or "kể chuyện" in text or "kể truyện" in text:
                Ke_chuyen_AI(name)
            elif "tắt máy" in text:
                os.system("shutdown /s /t 1")
            elif "tăng âm lượng" in text:
                volumeup()
            elif "giảm âm lượng" in text:
                volumedown()
            elif "tạm dừng" in text:
                pause()
            elif "bắt đầu" in text:
                play()
            elif "lên" in text:
                tua()
            elif "xuống" in text:
                lui()
            elif "chuyển bài" in text:
                chuyenbai()
            elif "phóng to" in text or "thu nhỏ" in text:
                phongto()
            elif "tắt âm" in text:
                tat()
            elif "bật âm" in text:
                bat()
            elif "tắt"in text:
                tatungdung()
            else:
                noi_ii = ["Xin lỗi, tôi không hiểu bạn {} muốn nói gì?".format(name),
                          "Bạn {} muốn nói gì?, Su không hiểu".format(name),
                          "Tôi còn khá kém tôi chưa thể hiểu thuật ngữ bạn {} vừa nói là gì".format(name)]
                speak(choice(noi_ii))
                time.sleep(5)

#assistant()

class TrolyaoTV(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.greeting = Label(
                        text= "Trợ Lý Ảo Tiếng Việt",
                        font_size= 30,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        self.button = Button(
                      text= "VOICE",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window

    def callback(self, instance):
        assistant()
        # change label text to "Hello + user name!"
        #self.greeting.text = "Hello " + boot+ "!"

# run TrolyaoTV App Calss
if __name__ == "__main__":
    TrolyaoTV().run()