#region debai
"""
--- ma debai / id
get_name_in_email(email_list)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310121414emailhople

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/11knZyUvwRzU7SvL6

--- debai / problem
Viết hàm 
  get_name_in_email(email_list)
trả về tên tài khoản trong email 
Nếu email không hợp lệ tả về ERROR invaid email

--- vidu mau / testcase
Khi chay voi input                                        | Ketqua output
--------------------------------------------------------- | -----------------
get_name_in_email(['ai-btx@gmail.com'])                   | ['ai-btx']
get_name_in_email(['user1@gmail.com', 'user2@gmail.com']) | ['user1', 'user2']
get_name_in_email([])                                     | []
get_name_in_email(['abb#ccc'])                            | ['ERROR invaid email']
get_name_in_email([None])                                 | ['ERROR invaid email']
get_name_in_email([None, 'abb#ccc'])                      | ['ERROR invaid email', 'ERROR invaid email']
"""
#endregion debai

#region bailam


def get_name_in_email(email_list):
  def hople(email):
    if not email:    
      return False
    return True

  list_email = []
  for a in email_list:
    if hople(a) == False:
      list_email.append('ERROR invaid email')
      continue
    result = [x for x in a]
    if not ("@" in result):
      list_email.append('ERROR invaid email')
    elif "@" in result:
      for i in range(10):
        result.pop()
      answer = ""
      for i in result:
        answer += i
      list_email.append(answer)

  return list_email
