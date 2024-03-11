from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://play1.automationcamp.ir'
driver.get(f"{url}/keyboard_events.html")
write_text = driver.find_element('id', 'area')
write_text.send_keys('hello')
write_text.send_keys(Keys.RETURN)
sleep(3)

# ------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://play1.automationcamp.ir/'
driver.get(f"{url}/forms.html")
driver.find_element('id', 'check_python').click()
check = driver.find_element('id', 'check_validate').text
assert check == 'PYTHON'
sleep(5)
# بستن سشن به طور کامل
driver.quit()

# ------------------------------------------------------------------------------------------------------------------
# اسکرول کردن در صفحه
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.yahoo.com/')
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(6)

# ------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://play1.automationcamp.ir/'
uel_1 = 'https://play2.automationcamp.ir/'
url_2 = 'https://www.yahoo.com/'
driver.get(url)
sleep(4)
driver.switch_to.new_window('tab')
driver.get(uel_1)
sleep(5)
driver.switch_to.new_window('tab')
driver.get(url_2)
sleep(5)
# مثلا بخوایم بریم روی صفحه اجتماعی سایت و اونجا ولیدیت انجام بدیم
current_window = driver.current_window_handle
print('current_window is : ' + str(current_window))
sleep(2)
all_handle = driver.window_handles
print('all_handles is : ' + str(all_handle))
sleep(2)
driver.switch_to.window(all_handle[0])
sleep(5)

# ------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from time import sleep

url = 'https://play1.automationcamp.ir'
driver = webdriver.Chrome()
driver.get(url)
# بدست اوردن سایز صفحه
window_size = driver.get_window_size()
print(window_size)
# برای اینکه بفهمیم المنت دقیقا کجای صفحه قرار دارد
width = window_size['width']
print(f"width is : {width}")
height = window_size['height']
print('height is : ' + str(height))
# ریسپانسیو بودن سایت رو با پایین اوردن سایز صفحه بررسی می کنیم
driver.set_window_size(800,600)
sleep(4)
window_size_1 = driver.get_window_size()
assert window_size_1['width'] == 1000
print(window_size_1)

# ------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from time import sleep

url = 'https://play1.automationcamp.ir'
driver = webdriver.Chrome()
driver.get(url)
sleep(4)
driver.minimize_window()
sleep(4)
driver.maximize_window()
sleep(4)
driver.fullscreen_window()
sleep(4)

# ------------------------------------------------------------------------------------------------------------------
# استفاده از دستورات جاوااسکریپ برای اسکرول
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = 'https://www.yahoo.com/'
driver.get(url)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(4)

# ------------------------------------------------------------------------------------------------------------------
# تشخیص دادن ادرس روی هر سیستم عاملی که وجود دارد
# session_2  1:20
from selenium import webdriver
# از روش زیر برای دادن آدرس استفاده می کنیم
# در این روش میاد میبینه توی چه سیستمی هست و طبق اون میاد آدرسی که میخوایم رو ایجاد میکنه
# با توجه به سیستمی که داریم میاد اسمی که میخوایم رو با آدرسی که path می سازه جوین میکنه
import os
# path میاد آدرسی که بهش نیاز داریم رو می سازه
from pathlib import Path

driver = webdriver.Chrome()
url = 'https://www.yahoo.com/'
driver.get(url)
# به جای sleep میایم میگیم به ازای هر اکشن یا عملی بیا3ثانیه تایم بزار اگر در ثانیه1عمل رو انجام دادی صبر نکن برو بعدی
driver.implicitly_wait(3)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session2.png')
driver.save_screenshot(file_name)

# ------------------------------------------------------------------------------------------------------------------
# incognito  کوکی ها و اطلاعات کاربر ذخیره نمی شود
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument("--incognito")
driver = webdriver.Chrome(chrome=chrome_option)

driver.get('https://www.yahoo.com/')
sleep(2)

# ------------------------------------------------------------------------------------------------------------------
# hesdless بدون اینکه کروم باز شود کد ما در حال پردازش و اجرا می باشد
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option = Options()
chrome_option.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_option)

driver.get('https://www.yahoo.com/')

# ------------------------------------------------------------------------------------------------------------------
#  Xpath expression
# site for practice = https://trytestingthis.netlify.app/

absolute xpath = /html/body/div[3]/div[2]/form/fieldset/input[2]

relational xpath = // * [ @value = 'option 1' ]   or    // option [ @value = 'option 1' ]

# expression and / or
// * [ @type = 'checkbox' and @name = 'option2' ]
// * [ @name = 'option2' or @value = 'Option 2' ]

# ترکیب and / or
# در اپیوم و اندروید کاربرد زیادی دارد
// * [ ( @name = 'option2' or @value = 'Option 2' ) and @type = 'checkbox']

# رسیدن از child به parent
// * [ @id = 'uname' ] / ..
a = driver.find_element('xpath' , '// * [ @id = 'uname' ]')
# یکی برو عقب
a.find_element('xpath' , '..')
# دوتا برو عقب
a.find_element('xpath' , '../..')

# رسیدن از parent به child
# رفتن به child بعدی
// * [ @class = 'login form' ]/*  and  // * [ @class = 'login form' ]/*/*
# // یعنی من میخوام تمام چیزهایی که از این نقطه به پایین وجود دارند را نگاه کنم
// * [ @class = 'login form' ] // * [ @value = 'login' ]
// * [ @class = 'login form' ] / input [ @value = 'login' ]

# index xpath از یک شروع می شود
// * [ @id = 'moption' ] [2]
# اگر با ایندکس 1 دوتا مقدار پیدا کردیم برای رسیدن به المنت مدنظرمون از پرانتز استفاده می کنیم
// * [ text() = 'Option 1' ] [1]
( // * [ text() = 'Option 1' ] ) [1]

# xpath تو در تو
// td [ text() = 'Actor' ] / ..
// tr [ td [ text() = 'Actor' ] ]
# بهترین روش به صورت زیر است
# در اینجا فرقی ندارد فرزند td در کدوم نسل از parent وجود دارد
// tr [ .// td [ text() = 'Actor' ] ]
# اگر قبل از // نقطه نزاریم میره تمام tr هارو از اول بر می گرداند
// tr [  // td [ text() = 'Actor' ] ]
// tbody // tr[1]  and   // tbody // tr[3-2]



# ------------------------------------- functions
# position() = index
# position دقیقا همانند index می باشد
// tbody // tr [ position() = 1 ]   ==   // tbody // tr[1]

# last()
# اخرین سطر رو برای ما پیدا میکند
// tbody // tr [ last() ]   or  // tbody // tr [ last() ] / td [ 1 ]
# سطر یکی مونده به اخر
// tbody // tr [ last() - 1 ]

# count() = attribute
# tbody رو میخوام که tr آن برابر با 6 تا باشد
// tbody [ count ( .//tr ) = 6 ]
# اگر نقطه نزاریم کل صفحه html رو میگرده
// tbody [ count ( //tr ) = 6 ]

# contains ( attribute , 'value' )
# پیدا کردن المنت با استفاده از بخشی از xpath
// * [ contains ( text() , 'layout two' ) ]  or  // * [ contains ( @id , 'lan' ) ]

# starts-with ( attribute , 'value' )
site for practice = https://www.wikipedia.org/
// * [ starts-with ( @class , 'central-featured-lang' ) ]



# ------------------------------------- functions ignore case
# باعث میشن بخشی از المنت رو ازش صرف نظر بکنیم

# normalize-space ( attribute ) = 'value'
# space اول یا آخر رو حذف میکند
// * [ normaliza-space ( text() ) = 'Option 1' ]

# translate ( attribute , 'srting1' , 'srting2' )
# sring2 رو با sring1 جابجا می کند
// * [ translate ( @value , 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' , 'abcdefghijklmnopqrstuvwxyz' ) = 'option 1' ]

# combine normalize-space and translate
//*[ normaliza-space ( translate (@value ,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz' ) )='Option 1' ]

# string-length( attribute ) = value
// * [ string-length ( @id ) = 4 ]

# not ( attribute = 'value' )
// * [ @type = 'radio' and not ( @id = 'male' ) ]

# substring-before ( attribute , 'value' ) = 'value'
// * [ substering-before ( text() , ':' ) = 'Username' ]

# substring-after ( attribute , 'value' ) = 'value'
// * [ substering-after ( text() , ':' ) = 'test' ]

# از طریق پیدا کردن عدد به المنت برسیم که در سایت های ارزدیجیتال یا مالی کاربرد دارد
# site for practice = https://www.londonstockexchange.com/
round ( attribute ) = 'value'     430.10 = 430   and    430.50 = 431
* // [ round( text() ) = '430' ]

# floor ( attribute ) = 'value'     448.25 = 448
# مقدار اعشار رو در نظر نمیگیرد و فقط مقدار صحیح آن را مدنظر قرار می دهد
// * [ floor ( text() ) = '448' ]



# ------------------------------------- Axes
# میوانیم با استفاده از یک المنت به بچه ها یا اجدا یا خانوادش برسیم

# / parent :: xpath-parent
# رسیدن از child به parent
// * [ @id = 'uname' ] / parent :: * [ @class = 'login form' ]
// * [ @id = 'uname' ] / parent :: div [ @class = 'login form' ]

# / ancestor :: xpath-parent  اجداد
# رسیدن از child به تمام اجداد آن
// td [ text() = 'singer' ] / ancestor :: table [ @style = 'width:100%' ]

# / ancestor-or-self :: xpath-parent
// * [ @name = 'uname' ] / ancestor-or-self :: * [ @id = 'uname' ]

# / child :: xpath-child
# رسیدن از parent به child
// tbody / tr[3] /child :: * [ text() = 'singer' ]
// * /child :: * [ text() = 'singer' ]
// tbody / tr[3] / td[5]

# / descendant :: xpath-child
# رسیدن از parent به تمام نوادگان آن
// table / descendant :: * [ text() = 'singer' ]
// table // * [ text() = 'singer' ]

# / descendant-or-self :: xpath-child

# / following  :: xpath
// select [ @id = 'option' ] / following :: * [ @value = 'option 1' ]

# / following-sibling :: xpath
# المنت هایی که هم سطح هم هستن یعنی از یک خانواده هستن و خواهر و برادر هم به حساب می آیند
// * [ @id = 'abc123' ] / following-sibling :: * [ @value = 'option 2' ]

# / preceding :: xpath
# برعکس following است یعنی از یه المنت به قبلش رو می گرده
// select [ @id = 'optionx' ] / preceding :: * [ @value = 'option 2' ]

# / preceding-sibling :: xpath

# ------------------------------------------------------------------------------------------------------------------
# MouseActions
# Get Coordinates
# نحوه پیدا کردن offset بر روی صفحه
driver.get("http://play2.automationcamp.ir")
offset = driver.find_element("xpath", "//*[text()='Lets you select only one option']").location

# Move by offset
# به موقعیت المنت روی صفحه offset میگن
# کلیک کردن روی خالی صفحه که باعث میشه لیستی که باز کردیم بسته بشه
driver.execute_script("scroll(0,500)")
sleep(1)
driver.find_element("id", 'option').click()
actions.move_by_offset(offset['x'], offset['y']).pause(1).click().perform()
sleep(3)

# Drag and Drop by Offset
# 1
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
el1 = driver.find_element('id', 'draggable')
offset = driver.find_element('id', 'droppable').location
print(offset)
actions.drag_and_drop_by_offset(el1, 200, 60).pause(1).perform()
sleep(2)
# 2
driver.get("https://selenium08.blogspot.com/2020/01/drag-drop.html")
el1 = driver.find_element('id', 'draggable')
el2 = driver.find_element('id', 'droppable')
coord_el1 = driver.find_element('id', 'draggable').location
coord_el2 = driver.find_element('id', 'droppable').location
print("Coord1: " + str(coord_el1))
print("Coord2: " + str(coord_el2))
offset_x = (coord_el2['x'] - coord_el1['x']) + (el2.rect['width']-el1.rect['width'])/2
offset_y = (coord_el2['y'] - coord_el1['y']) + (el2.rect['height']-el1.rect['height'])/2
actions.drag_and_drop_by_offset(el1, offset_x, offset_y).pause(1).perform()
sleep(2)


# ------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver=driver)
driver.maximize_window()
driver.implicitly_wait(2)

# بدست اوردن ارتفاع صفحه
# document.body.scrollheight

# -------------------------------------- Scroll Using JavaScript Commands
# Scroll down by pixel
# به یک میزان خاصی بر روی صفحه اسکرول می نماییم
driver.get("http://play2.automationcamp.ir")
driver.execute_script("window.scrollBy(0,200)")
sleep(3)

# Scroll to specific position
# هرجایی در صفحه هستی به نقطه انتخاب شده برو
driver.get("http://play2.automationcamp.ir")
driver.execute_script("window.scrollTo(0,500)")

# Scroll to element if could find by driver
# یک المنتی بر روی صفحه وجود داره که برای دیدن اون المنت بر روی صفحه اسکرول می کنیم
# المنت توسط driver پیدا میشه یعنی در صفحه هست اما قابل دیدن نیست چون اسکرول نشده و نمیتونیم ببینیمش
# وقتی قابل نمایش نباشه قابل کلیک کردن نیست و نمیتونیم روش اکشنی انجام بدیم که به اصطلاح interacteble نیست
driver.get("https://www.imdb.com/chart/top/")
element = driver.find_element('link text', 'The Handmaiden')
print(element)
driver.execute_script("arguments[0].scrollIntoView();", element)
sleep(3)

# Scroll to element if currently cannot be found or not sure if it is in the page (True-False)
# وقتیه که ما مطمین نیستیم المنت در صفحه وجود دارد یا خیر
# بدست اوردن ارتفاع صفحه
# document.body.scrollheight
def scroll_to_find_element(locator, pixel):
    for i in range(10):
        try:
            driver.find_element(locator[0], locator[1])
            return True
        except:
            driver.execute_script(f"window.scrollBy(0,{str(pixel)})")
            sleep(0.5)
    return False

driver.get("https://www.imdb.com/chart/top/")
result = scroll_to_find_element(['link text', 'fwfwfqgeqrhr'], 1800)
print(result)

# Scroll to element if currently cannot be found or not sure if it is in the page (Assertion)
def scroll_to_find_element(locator, pixel):
    for i in range(10):
        try:
            driver.find_element(locator[0], locator[1])
            print(f"The element '{locator}' has been found")
        except:
            driver.execute_script(f"window.scrollBy(0,{str(pixel)})")
            sleep(0.5)
    raise Exception(f"The element '{locator}' cannot be found")

driver.get("https://www.imdb.com/chart/top/")
scroll_to_find_element(['link text', 'fwfwfqgeqrhr'], 1800)
driver.quit()


# Scroll to down of the page
# اسکرول کردن تا انتهای صفحه
driver.get("https://www.imdb.com/chart/top/")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")  #1
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  #2


# Scroll to top of the page
# اسکرول کردن تا ابتدای صفحه
driver.get("https://www.imdb.com/chart/top/")
driver.execute_script("window.scrollBy(0, 0)")

# Scroll horizontally
# اسکرول کردن به صورت افقی
driver.get("https://datatables.net/examples/basic_init/scroll_x.html")
driver.execute_script("document.getElementById('quantity').scrollIntoView()") # 1
# وقتی میخوایم توسط expresion CssSelector المنت رو پیدا کنیم
driver.execute_script("document.querySelector('#quantity'').scrollIntoView()") # 2
driver.execute_script("document.querySelector('table td:last-child').scrollIntoView()") # 3


# -------------------------------------- Is displayed
# المنت روی صفحه پیدا میشه اما قابل دیدن نیست و نمیتونیم بر روی آن اکشنی انجام بدیم
driver.get("https://www.imdb.com/chart/top/")
for i in range(10):
    try:
        result = driver.find_element('link text', 'Andrei Rublev').is_displayed()
    except:
        sleep(0.5)


# -------------------------------------- Scroll Using ActionChains
driver.get("http://play2.automationcamp.ir")
el1 = driver.find_element('xpath', "//*[@name='message']")
el2 = driver.find_element('id', 'fname')
actions.move_to_element(el2).click_and_hold().move_to_element(el1).release().perform()
sleep(3)


# -------------------------------------- Scroll Using Keyboard
# Scroll to End of page and Top of the page
driver.get("http://play2.automationcamp.ir")
page_el = driver.find_element('tag name', 'html')
actions.send_keys_to_element(page_el, Keys.END).perform()
sleep(3)
actions.send_keys_to_element(page_el, Keys.HOME).perform()
sleep(3)

# Scroll to find element
driver.implicitly_wait(2)
def scroll_to_find_element(locator):
    page_el = driver.find_element('tag name', 'html')
    for i in range(10):
        try:
            driver.find_element(locator[0], locator[1])
            return True
        except:
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            # actions.send_keys_to_element(page_el, Keys.DOWN).perform()
            actions.send_keys_to_element(page_el, Keys.PAGE_DOWN).perform()
            sleep(0.5)
    return False


# # -------------------------------------- Scroll Using WebDriver
# Scroll to element
driver.get("https://www.imdb.com/chart/top/")
element = driver.find_element('link text', 'The Handmaiden')
element.location_once_scrolled_into_view
sleep(3)

# Scroll horizontally
driver.get("https://datatables.net/examples/basic_init/scroll_x.html")
driver.set_window_size(480,640)
element = driver.find_element('xpath', '//tbody//td[last()]')
sleep(1)
element.location_once_scrolled_into_view
sleep(3)

# ------------------------------------------------------------------------------------------------------------------
# css selectors
# syntax css selectors  -->  tag [ AttributeName = 'AttributeValue' ] = input [ id = 'fname' ] or * [ id = 'fname' ]

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://play2.automationcamp.ir/index.html")

# driver.find_element("css selector")
driver.find_element(By.CSS_SELECTOR, "input[id='fname']").send_keys("AutomtionCamp")
sleep(3)

# id and class selector
tag # id-Value  -->  input # fname       and        tag . class-Value  -->  div . tooltip

# combination ترکیب کردن سلکتور ها باهم
# and
tag # id-Value [ AttributeName1 = 'AttributeValue1' ] [ AttributeName2 = 'AttributeValue2' ]
# or
tag1 . class-Value , tag2 . class-Value

# sub-string Match
# بیشتر برای پیدا کردن المنتی بکار میره که یه بخشی از آن ثابت است و یک بخشی از آن داینامیک می باشد یعنی تغییر میکند
# id = 'moption'
^ start with   با مقدار فلان شروع بشه   -->   input [ id ^= 'mop' ]
$ ends with    با مقدار فلان تموم بشه   -->   input [ id $= 'tion' ]
* partial text     قسمتی از متن باشه   -->   input [ id *= 'opt' ]

# child / descendant
direct child                    اولین فرزندش رو پیدا میکنه -->  tag # id-value > tag # id-value
# descendant ( child and sub-child )                -->  tag # id-value tag # id-value
# بین بچه ها و نوادگانش می گرده و المنت رو پیدا میکنه
next-sibling ( adjacent )  فرزند بعد از اون تگی که نوشتیم  -->  tag # id-value + tag # id-value

# Pseudo Class-Child
first-child      -->  tag # id-value :first-child
last-child       -->  tag # id-value :last-child
select by index  -->  tag # id-value :nth-child(index)  and  tag # id-value :nth-last-child(index)

# Pseudo Class-type of Child
first-of-type       -->  tag # id-value > tag # id-value:first-of-type
last-of-type        -->  tag # id-value > tag # id-value:last-of-type
nth-of-type(index)  -->  tag # id-value > tag # id-value:nth-of-type(index)

# برای اینکه بتوانیم کلاسی که مقدارش اسپیس دارد را پیدا کنیم از . استفاده می نماییم
<div class='side  ex1'>   -->   div.side.ex1

# Pseudo Class
<tag>:checked  -->  input:checked  المنت هایی که تیک خوردن رو پیدا کن
<tag>:disabled -->  input:disabled المنت هایی که غیر فعال هستند
<tag>:enabled  -->  input:enabled المنت هایی که فعال هستند
<tag>:empty    -->  input:empty  المنتی ه هیچ فرزندی نداره رو پیدا کن
<tag>:hover    -->  input:hover المنتی که زیر موس قرار داره رو پیدا کن
<tag>:only-of-type
<tag>:only-child  --> td:only-child المنتی که تنها فرزند خانواده خودشه
<tag>::placeholder
<tag>:invalid  -->  input:invalid
<tag>:valid
<tag>:link
<tag>:visited

# ------------------------------------------------------------------------------------------------------------------
