from bs4 import BeautifulSoup


def extract_data(data):
    """
    Extracts relevant information from the provided data.

    Parameters:
    data (list):
    A list containing URL, general information, and detailed information.
    The general and detailed information should be in HTML format.

    Returns:
    dict:
        A dictionary containing the extracted information.

    Raises:
    Exception: If the length of the input list is less than 3.
    """
    if len(data) < 3:
        raise Exception('data not valid')
    ans = {}
    ans["URL"] = data[0]
    general_info = BeautifulSoup(data[1], 'html.parser')
    detail_info = BeautifulSoup(data[2], 'html.parser')

    # Xe cũ hay mới
    text = general_info.find('div', class_='cb1').text.strip()
    ans["Tình trạng chung"] = " ".join(text.split()[:2])

    # Tên dòng xe
    name = general_info.find('h3').text
    ans["Tên xe"] = name

    # Giá
    price = general_info.find('b', itemprop='price')['content']
    ans["Giá"] = price

    # Tỉnh thành
    location = general_info.find('div', class_='cb4').find('b').text
    ans["Tỉnh"] = location

    # Mã xe
    car_code = general_info.find('span', class_='car_code').text.split()[-1]
    ans["Mã xe"] = car_code

    # Tất cả thông tin trong trang chi tiết
    details = detail_info.find_all("div", class_="label")

    for e in details:
        title = e.text.strip()[:-1]
        value = e.find_next_sibling().text.strip()
        ans[title] = value

    # Thông tin mô tả
    description = detail_info.find('div', class_='des_txt').text.strip()
    ans['Mô tả'] = description
    return ans
