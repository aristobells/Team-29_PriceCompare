def scraper(base_url, brand, category):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    import re
    import time


    driver = Service("C:/Users/MY PC/Downloads/chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.add_argument('--headless --window-size=400,800') 
    options.add_argument('start-maximized') 
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')

    browser = webdriver.Chrome(service=driver, options=options)
    browser.implicitly_wait(60)

    if 'www' in base_url:
        merchant_name= re.search(r'www\.(.*?)\.', base_url).group(1)
    else:
        merchant_name= re.search(r'//(.*?)\.', base_url).group(1)
    
    if merchant_name=="jumia":
        title_class_name="name"
        price_class_name="prc"
        image_id="div.img-c>img"
        product_link_id="a.core"
    elif merchant_name=="slot":
        title_class_name="text-truncate.font-size-14.font-weight-medium"
        price_class_name="d-block.Shared_Price__fYddd.text-right.text-truncate"
        image_id= "div.Carousel_carouselSlideActive__aDcau>img"
        product_link_id="div.p-2>a"
    elif merchant_name=="konga":
        title_class_name="_24849_2Ymhg"
        price_class_name="d7c0f_sJAqi"
        image_id="div._7e903_3FsI6>a>picture>img"
        product_link_id="div._4941f_1HCZm>a"

    temporary_scraped_data=[]
    final_scraped_data={}
    page=1
    j=0
        

    def get_image_and_product_link():
        link=browser.find_elements(By.CSS_SELECTOR, product_link_id)[i].get_attribute('href')
        temporary_scraped_data.append(link)
        if merchant_name=="slot":
            browser.get(link)
            temporary_scraped_data.append(browser.find_elements(By.CSS_SELECTOR, image_id)[0].get_attribute('src'))
            browser.get(url)
            return
        temporary_scraped_data.append(browser.find_elements(By.CSS_SELECTOR, image_id)[i].get_attribute('data-src'))
        return link
    
    def save_data():
            from ..models import productDetails
            for i in range(length_final_scraped_data_after):
                data=final_scraped_data[i]
                if data[2] not in list(productDetails.objects.values_list('productLink', flat=True)):
                    productDetails.objects.create(name=data[0],price=data[1],productLink=data[2],imageLink=data[3],merchantName=merchant_name.capitalize(),category=category,brand=brand.capitalize())
  
    while True:
        try:
            url = base_url + str(page)
            browser.get(url)
            length_final_scraped_data_before = len(final_scraped_data)
            for i in range(len(browser.find_elements(By.CLASS_NAME, price_class_name))):
                if merchant_name=='konga':
                    link = get_image_and_product_link()
                    temporary_scraped_data=[]
                    browser.get(link)
                    temporary_scraped_data.append(browser.find_elements(By.CLASS_NAME, title_class_name)[0].text)
                    browser.get(url)
                else:
                    temporary_scraped_data.append((browser.find_elements(By.CLASS_NAME, title_class_name)[i].text))
                temporary_scraped_data.append((browser.find_elements(By.CLASS_NAME, price_class_name)[i].text))
                get_image_and_product_link()
                final_scraped_data[j]= temporary_scraped_data
                j+=1
                temporary_scraped_data=[]
            length_final_scraped_data_after = len(final_scraped_data)
            if length_final_scraped_data_before==length_final_scraped_data_after:
                break
            page+=1
        except:
            browser.close() 
            break

    save_data()

#SCRAPING TASKS

#DONE
# scraper(base_url='https://slot.ng/search/result?q=iphone&page=', brand='apple',category='phone')
# scraper(base_url="https://www.jumia.com.ng/smartphones/samsung/?page=",brand="samsung",category="phone")
# scraper(base_url="https://www.jumia.com.ng/laptops/apple/?page=",brand="apple",category="laptop")
# scraper(base_url="https://www.jumia.com.ng/smartphones/infinix/?page=",brand="infinix",category="phone")
# scraper(base_url="https://www.jumia.com.ng/smartphones/lenovo/?page=",brand="lenovo",category="phone")
# scraper(base_url="https://www.konga.com/category/macbooks-5249?page=",brand="apple",category="laptop")
# scraper(base_url='https://slot.ng/search/result?q=asus&page=', brand='asus',category='laptop')
# scraper(base_url='https://slot.ng/search/result?q=hp&page=', brand='hp',category='laptop')
# scraper(base_url='https://slot.ng/search/result?q=infinix&page=', brand='infinix',category='phone')
# scraper(base_url='https://slot.ng/search/result?q=tecno&page=', brand='tecno',category='phone')





###########################################################################################################

#To-Do

# scraper(base_url='https://slot.ng/search/result?q=samsung&page=', brand='samsung',category='phone')

# scraper(base_url='https://slot.ng/search/result?q=macbook&page=', brand='apple',category='laptop')



# scraper(base_url="https://www.jumia.com.ng/smartphones/tecno/?page=",brand="tecno",category="phone")
# scraper(base_url="https://www.jumia.com.ng/smartphones/apple/?page=",brand="apple",category="phone")


# scraper(base_url="",brand="",category="")
# scraper(base_url="",brand="",category="")
# scraper(base_url="",brand="",category="")
# scraper(base_url="",brand="",category="")
# scraper(base_url="",brand="",category="")
# scraper(base_url="",brand="",category="")
# scraper(base_url="",brand="",category="")