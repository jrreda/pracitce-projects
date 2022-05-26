import requests # http requests
import pandas as pd
from bs4 import BeautifulSoup # web scraping


main_cats = ["apps", "dashboards", "icons", "illustrations",
            "landing-pages", "mockups", "ui-kits", "wireframes"]

design_categories = []
pic_srcs = []
sw_types = []
sw_types_links = []
titles = []
sub_titles = []
page_links = []
design_images = []
download_links = []
features = []
view_all_texts = []
view_all_links = []
auther_names = []
auther_links = []
design_cats = []
design_cats_links = []



for c in main_cats:
    design_categories.append(c)
    url = f'https://www.uistore.design/categories/{c}/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    print("Scrapping:", c, "."*5)
    for card in soup.find_all('div', attrs={'class':'col-4'}):
        try:
            # print('PIC SRC:', card.find('div', attrs={'class':'card-image'}).a.img.get("data-src"))
            pic_srcs.append(card.find('div', attrs={'class':'card-image'}).a.img.get("data-src"))
            types = []
            types_links = []
            for _type in card.find_all('span', attrs={'class':'chip'}):
                types.append(_type.text)
                types_links.append("https://www.uistore.design/types/"+str(_type.text))
            # print("Software Types:", types)
            # print("Software Links:", types_links)
            sw_types.append(types)
            sw_types_links.append(types_links)

            # print('Title:', card.find('a', attrs={'class':'item-name'}).text.strip())
            titles.append(card.find('a', attrs={'class':'item-name'}).text.strip())
            # print('Sub-Title:', card.find('div', attrs={'class':'card-subtitle'}).text.strip())
            sub_titles.append(card.find('div', attrs={'class':'card-subtitle'}).text.strip())
            # print('Link:', "https://www.uistore.design"+card.find('a', attrs={'class':'item-name'}).get('href'))
            page_links.append("https://www.uistore.design"+card.find('a', attrs={'class':'item-name'}).get('href'))
            page_link = "https://www.uistore.design"+card.find('a', attrs={'class':'item-name'}).get('href')
            # print('-'*30)
        except:
            pass

        print(page_link)
        # url = "https://www.uistore.design"+card.find('a', attrs={'class':'item-name'}).get('href')
        url = page_link
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        images = []
        for i in soup.find_all('div', attrs={'class':'image-list'}):
            # print("Image Src.", image.img.get('src'))
            images.append(i.img.get('src'))
        design_images.append(images)

        # print("Download Link:",soup.find('div', attrs={'class':'detail-download'}).a.get('href'))
        download_links.append(soup.find('div', attrs={'class':'detail-download'}).a.get('href'))
        # print("Features: \n", soup.find('div', attrs={'class':'detail-download'}).ul)
        features.append(soup.find('div', attrs={'class':'detail-download'}).ul)
        # print("View All Text:", soup.find('a', attrs={'class':'item-view-all'}).text)
        view_all_texts.append(soup.find('a', attrs={'class':'item-view-all'}).text)
        # print("View All Link:", "https://www.uistore.design"+soup.find('a', attrs={'class':'item-view-all'}).get('href'))
        view_all_links.append("https://www.uistore.design"+soup.find('a', attrs={'class':'item-view-all'}).get('href'))
        # print("Author Name:", soup.find('li', attrs={'class':'nav-item'}).a.text)
        auther_names.append(soup.find('li', attrs={'class':'nav-item'}).a.text)
        # print("Author Link:", soup.find('li', attrs={'class':'nav-item'}).a.get("href"))
        auther_links.append(soup.find('li', attrs={'class':'nav-item'}).a.get("href"))
        for s in soup.find_all('span'):
            if s.text.strip() == 'Categories:':
                # print(s.find_next_siblings())
                cats = []
                for _cat in s.find_next_siblings():
                    cats.append(str(_cat).split('>')[1].split('<')[0])
                # print("Categories:", cats)
                cat_links = []
                for link in s.find_next_siblings():
                    # print(link)
                    cat_links.append("https://www.uistore.design"+str(link).split('="')[1].split('"')[0])
                # print("Categories Links:", cat_links)
            design_cats.append(cats)
            design_cats_links.append(cat_links)
    break


df = pd.DataFrame(data=list(zip(design_categories, pic_srcs, sw_types, sw_types_links,
                                titles, sub_titles, page_links, design_images, download_links,
                                features, view_all_texts, view_all_links, auther_names, auther_links,
                                design_cats, design_cats_links)),
                 columns=["Website Category", "Picture Source", "Software", "Software designs link",
                                 "Title", "Sub-title", "Page Link", "Images", "Downlaod Link", "Features",
                                 "View All text", "View All link", "Auther Name", "Auther Link",
                                 "Design Category", "Design category Links"])

# save the final df
df.to_csv("uistore_design.csv", index=False)
