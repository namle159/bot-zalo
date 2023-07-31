from Base.base import Base
from selenium.webdriver.common.keys import Keys
import time
def messageZalo(self):
    Base(self.driver).click_element(('xpath','//header//div[@class="zavatar zavatar-l zavatar-single flx flx-al-c flx-center rel clickable disableDrag"]'))
    try:
        gioi_tinh= Base(self.driver).getElement(('xpath','//span[contains(@data-translate-inner, "STR_GENDER")]'))
        if gioi_tinh.text == 'Nữ':
            danh_xung= 'Chị'
        elif gioi_tinh.text == 'Nam':
            danh_xung= 'Anh'
        else:
            danh_xung= 'Anh/Chị'
    except:
        danh_xung= 'Anh/Chị'
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
    # tinnhan5=Base(self.driver).getElement(('xpath','//div[@id="input_line_4"]'))
    # tinnhan5.send_keys('Trân trọng cảm ơn!')
    # tinnhan5.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan6=Base(self.driver).getElement(('xpath','//div[@id="input_line_5"]'))
    # tinnhan6.send_keys('- Khách hàng tiềm năng đang quan tâm đến khía cạnh nào của sự kiện BLACKPINK?”...')
    # tinnhan6.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan7=Base(self.driver).getElement(('xpath','//div[@id="input_line_6"]'))
    # tinnhan7.send_keys('- Tất cả sẽ có trong “Đêm Nhạc BLACKPINK - Người Việt Ủng Hộ Nhiều Hơn Hay Phản Đối Nhiều Hơn”.')
    # tinnhan7.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan8=Base(self.driver).getElement(('xpath','//div[@id="input_line_7"]'))
    # tinnhan8.send_keys('- Socialyze Asia mang đến cho bạn bức tranh tổng quan xoay quanh sự kiện này một cách nhanh chóng, để kịp thời đưa ra các quyết định đúng đắn.')
    # tinnhan8.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan9=Base(self.driver).getElement(('xpath','//div[@id="input_line_8"]'))
    # tinnhan9.send_keys('- Để không bỏ lỡ bất kỳ thông tin mới nào liên quan đến [sản phẩm/dịch vụ] của Socialyze Asia, chúng tôi sẽ gửi đến bạn các thông tin về [sản phẩm/dịch vụ] thông qua thư điện tử.')
    # tinnhan9.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan10=Base(self.driver).getElemaent(('xpath','//div[@id="input_line_9"]'))
    # tinnhan10.send_keys('- Nếu bạn có bất kỳ câu hỏi hoặc thắc mắc nào, vui lòng liên hệ với chúng tôi qua số điện thoại (+84) 0903983811 hoặc Email: info@socialyze.asia')
    # tinnhan10.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan11=Base(self.driver).getElement(('xpath','//div[@id="input_line_10"]'))
    # tinnhan11.send_keys('--- ĐĂNG KÝ NGAYa ĐỂ NHẬN MIỄN PHÍ BÁO CÁO ĐẦY ĐỦ ---')
    # tinnhan11.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan12=Base(self.driver).getElement(('xpath','//div[@id="input_line_11"]'))
    # tinnhan12.send_keys('Chân thành cảm ơn bạn đã tin tưởng và sử dụng sản phẩm/dịch vụ của Socialyze Asia.')
    # tinnhan12.send_keys(Keys.SHIFT + Keys.ENTER)
    # tinnhan13=Base(self.driver).getElement(('xpa368525951th','//div[@id="input_line_12"]'))
    # tinnhan13.send_keys('Trân trọng,')
    # Base(self.driver).click_element(('xpath','//div[@data-translate-inner="STR_SEND"]'))
    return messageZalo