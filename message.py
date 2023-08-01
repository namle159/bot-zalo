from Base.base import Base
from selenium.webdriver.common.keys import Keys
import time
def messageZalo(self):
    Base(self.driver).click_element(('xpath','//header//div[@class="zavatar zavatar-l zavatar-single flx flx-al-c flx-center rel clickable disableDrag"]'))
    try:
        gioi_tinh= Base(self.driver).getElement(('xpath','//span[contains(@data-translate-inner, "STR_GENDER")]'))
        if gioi_tinh.text == 'Nữ':
            danh_xung= 'chị'
        elif gioi_tinh.text == 'Nam':
            danh_xung= 'anh'
        else:
            danh_xung= 'anh/chị'
    except:
        danh_xung= 'anh/chị'
    time.sleep(1)
    Base(self.driver).click_element(('xpath','//div[@icon="close f16"]'))
    ten_nguoi_nhan= Base(self.driver).getElement(('xpath','//div-b18[@class="header-title flx flx-al-c flex-1"]'))
    ten_nguoi_nhan_text = ten_nguoi_nhan.text
    tinnhan=Base(self.driver).getElement(('xpath','//div[@data-translate-placeholder="STR_MESSAGE_TO"]'))
    tinnhan.send_keys(f'Chào {danh_xung} {ten_nguoi_nhan_text}. Em xin lỗi nếu đang làm phiền {danh_xung}. Em gửi tin nhắn vì thấy {danh_xung} đang làm về marketing. Đêm nhạc của Black Pink đang thu hút nhiều quan tâm, em có biết báo cáo phân tích chuyên sâu về sự kiện này, em nghĩ {danh_xung} sẽ có thông tin hữu ích nên em xin chia sẻ.')
    time.sleep(2)
    tinnhan.send_keys(Keys.ENTER)
    tinnhan2=Base(self.driver).getElement(('xpath','//div[@id="input_line_0"]'))
    tinnhan2.send_keys('Trong báo cáo này cung cấp đánh giá tổng quan về mức độ ảnh hưởng của sự kiện, các tập đối tượng đang thảo luận: họ là ai, có đặc điểm gì và phân tích sâu nhiều luồng ý kiến xoay quanh đêm nhạc.')
    time.sleep(2)
    tinnhan2.send_keys(Keys.ENTER)
    tinnhan3=Base(self.driver).getElement(('xpath','//div[@id="input_line_0"]'))
    tinnhan3.send_keys('Đây là link đăng ký hoàn toàn miễn phí: https://socialyze.asia/dang-ky/bao-cao-social-listening-dem-nhac-blackpink-born-pink-nguoi-viet-ung-ho-hay-phan-doi-nhieu-hon?utm_source=facebook-messenger&utm_medium=social&utm_campaign=2707-BornPink-direct-message&utm_content=message-to-friend&utm_term=nick')
    time.sleep(2)
    tinnhan3.send_keys(Keys.ENTER)
    tinnhan4=Base(self.driver).getElement(('xpath','//div[@id="input_line_0"]'))
    tinnhan4.send_keys(f'Em hy vọng {danh_xung} sẽ có trải nghiệm tốt với nội dung này và rất mong được kết nối với {danh_xung}')
    time.sleep(2)
    tinnhan4.send_keys(Keys.ENTER)
    return messageZalo