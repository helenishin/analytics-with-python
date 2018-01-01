
# coding: utf-8

# In[1]:


print("hello python")


# In[2]:


#두 수를 더한다
x=4
y=5
z=x+y

print("Output #2: Four plus finve equals {0:d}.".format(z))


# In[3]:


#두 리스트를 더한다.
a=[1,2,3,4]
b=["first","second","third","fourth"]
c=a + b
print("output #3: {0},{1},{2}".format(a,b,c))


# In[1]:


x=9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))


# In[1]:


#3f는 소수점 셋째짜리까지 보여달라는 의미
print("Output #7:{0:.3f}".format(8.3/2.7))
y=2.5*4.8
print("Output #8:{0:.1f}".format(y))
#float 내장함수는 무엇인가 실수형을 강제하는 것이군
r=8/float(3)
print("Output #9:{0:.2f}".format(r))
print("Output #10:{0:.4f}".format(8.0/3))


# In[15]:


print("Output #9:{0:2f}".format(8/3))


# In[3]:


#!/usr/bin/env python3
from math import exp,log,sqrt
print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))      
  


# In[4]:


print("Output #14:{0:s}".format('I\'m enjoying learning Python.'))


# In[5]:


print("Output #14:{0:s}".format("I'm enjoying learning Python."))


# In[9]:


print("Output #15:{0:s}".format("This is a long string. Without the backslashit would run off of the page on the right in the text editor and be verydifficult to read and edit.By using the backslash you can split the longstring into smaller strings on seperate lines so that the whole string is easyto view in the text editor."))                        


# In[11]:


print("Output #16:{0:s}".format('''you can use triple single quotes 
for multi-line comment strings.'''))


# In[14]:


print("Output #17:{0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))


# In[21]:


string1 = "This is a"
string2 = "short string."
sentence = string1 + string2
print("Output #18:{0:s}".format(sentence))
print("Output #19:{0:s}{1:s}{2:s}".format("she is","very"*4,"beautiful."))
m=len(sentence)
print("Output #20:{0:d}".format(m))


# In[22]:


string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18:{0:s}".format(sentence))
print("Output #19:{0:s}{1:s}{2:s}".format("she is","very"*4,"beautiful."))
m=len(sentence)
print("Output #20:{0:d}".format(m))


# In[26]:


#띄어쓰기 위해서는 공백문자 추가해야한다는 게 포인트, len함수는 문자열 내 문자의 수를 측정한다(공백문자나 마침표 등 포함)
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18:{0:s}".format(sentence))
print("Output #19:{0:s}{1:s}{2:s}".format("she is ","very "*4,"beautiful."))
m=len(sentence)
print("Output #20:{0:d}".format(m))


# In[29]:


#split
#21번은 어떤 인수도 입력 안되었기 때문에 기본값인 공백문자" "(5개)로 문자열을 나눈다.(인수 없으면 공백문자가 디폴트라는 뜻인가?)
#22번에서 인수는 " "와 2 2개이고,2는 처음 2번만 문자열을 나누라는 뜻, 앞 두 덩어리와 나머지= 총 3개의 원소로 문자열을 나눈다.
string1 ="My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ",2)
print("Output #21:{0}".format(string1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}".format(string1_list2[0],string1_list2[1],string1_list2[2]))


# In[30]:


#문자열에 음수 나오는거 반칙 아닙니까 여기 잘 모르겠음, 갑자기 어려워짐.
string2 = "Your,deliverable,is,due,in,June" 
string2_list=string2.split(',')
print("Output #23:{0}".format(string2_list))
print("Output #24:{0}{1}{2}".format(string2_list[1],string2_list[5],string2_list[-1]))


# In[31]:


#join은 join앞에 하나의 인수를 받고,
print("Output #25:{0}".format(','.join(string2_list)))


# In[33]:


#strip은 문자열의 끝에서 원하지 않는 문자를 지우는 함수
string3 = " Remove unwanted characters from this string.\t\t \n"
print("Output #26: string3: {0:s}".format(string3))
string3_lstrip=string3.lstrip()


# In[35]:


#lstrip
print("Output #27:lstrip:{0:s}".format(string3_lstrip))


# In[39]:


#rstrip
string3_rstrip=string3.rstrip()
print("Output #28:rstrip:{0:s}".format(string3_rstrip))


# In[40]:


#strip
string3_strip=string3.strip()
print("Output #29:strip:{0:s}".format(string3_strip))


# In[4]:


#1월1일부터 새로운 마음으로 다시 strip함수부터 볼까요: 제거의 아이콘이구만
#t은 탭, n은 개행문자
string3 = " Remove unwanted characters from this string.\t\t \n"
print("Output #26: string3: {0:s}".format(string3))


# In[5]:


string3_lstrip =string3.lstrip()
print("Output #27: lstrip:{0:s}".format(string3_lstrip))


# In[6]:


string3_rstrip=string3.rstrip()
print("Output #28: rstrip:{0:s}".format(string3_rstrip))


# In[7]:


string3_strip=string3.strip()
print("Output #29: strip:{0:s}".format(string3_strip))


# In[8]:


string4="$$Here's another string that has unwanted characters.__---++"
print("Output #30:{0:s}".format(string4))


# In[12]:


string4="$$The unwanted characters have been removed.__---++"
string4_strip=string4.strip('$_-+')
print("Output #31:{0:s}".format(string4_strip))


# In[22]:


#replace: 문자열 내에 있는 하나의 문자나 문자집합을 다른 문자 혹은 다른 문자집합으로 치환하는 방법-replace단어 뜻 자체가 대체하다, 이런거니까
string5="Let's replace the spaces in this sentence with other characters."
string5_replace= string5.replace(" ","!@!")
print("Output #32(with !@!):{0:s}".format(string5_replace))


# In[23]:


string5_replace=string5.replace(" ",",")
print("Output #33(with commas):{0:s}".format(string5_replace))


# In[24]:


# lower, upper, capitalize
string6="Here's WHAT Happens WHEN You Use lower."
print("Output #34:{0:s}".format(string6.lower()))


# In[26]:


string7="Here's what Happens when You Use UPPER. "
print("Output #35:{0:s}".format(string7.upper()))


# In[27]:


string5="here's WHAT Happens WHEN you use Capitalize."
print("Output #36: {0:s}".format(string5.capitalize()))


# In[28]:


string5_list=string5.split()
print("Output #37 (on each word):")
for word in string5_list:
    print("{0:s}".format(word.capitalize()))


# In[29]:


#!/usr/bin/env python3
from math import exp,log,sqrt
import re

#문자열 내에 등장하는 패턴의 횟수를 세기
string="The quick brown fox jumps over the lazy dog."
string_list=string.split()
pattern=re.compile(r"The",re.I)
count=0
for word in string_list:
    if pattern.search(word):
        count +=1
print("Output #38: {0:d}".format(count))


# In[30]:


#문자열 내에서 발견된 패턴 출력하기
string="The quick brown fox jumps over the lazy dog."
string_list=string.split()
pattern=re.compile(r"(?P<match_word>The)",re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))


# In[31]:


#문자열 내 "a"를 "the"로 대체하기, string_to_find에 정규표현식을 먼저 할당하는 것이 필수는 아니나 코드 가독성을 높이는데 좋다.
string="The quick brown fox jumps over the lazy dog."
string_to_find=r"the"
pattern=re.compile(string_to_find,re.I)
print("Output #40: {:s}".format(pattern.sub("a",string)))


# In[32]:


#!/usr/bin/env python3
from math import exp,log,sqrt
import re
from datetime import date,time,datetime,timedelta

#오늘 날짜와 년, 월, 일 요소들을 출력하기
today=date.today()
print("Output #41: today:{0!s}".format(today))


# In[33]:


print("Output #42: {0!s}".format(today.year))


# In[34]:


print("Output #43: {0!s}".format(today.month))


# In[35]:


print("Output #44: {0!s}".format(today.day))


# In[36]:


current_datetime=datetime.today()
print("Output #45: {0!s}".format(current_datetime))


# In[37]:


#timedelta 함수를 이용하여 새로운 날짜 계산하기-date객체에 특정 시간을 더하거나 빼는 방법
one_day=timedelta(days=-1)
yesterday=today + one_day
print("Output #46: yesterday:{0!s}".format(yesterday))


# In[41]:


#output에 나오는 저 엄청난 숫자가 정확히 무엇을 의미하는 것인가...일단 pass
eight_hours=timedelta(hours=-8)
print("Output #47:{0!s}{1!s}".format(eight_hours.days,eight_hours.seconds))


# In[43]:


#두 날짜 사이의 날짜 차이를 계산하기: 두 date 객체에서 뺄셈하는 방법이고,output은 날짜,시간,분,초의 차이를 나타내는 datetime 객체
date_diff=today-yesterday
print("Output #48:{0!s}".format(date_diff))


# In[44]:


#오 앞에서 배운 거 응용해서 수치만 나오게 하는 건데 앞 내용을 숙지한 것이 아니라서 가물가물
print("Output #49:{0!s}".format(str(date_diff).split()[0]))


# In[45]:


#date 객체를 특정 형식의 문자열로 만들기
print("Output #50: {:s}".format(today.strftime('%m/%d/%y')))


# In[ ]:


### https://docs.python.org/3/library/datetime.html


# In[49]:


print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))


# In[50]:


print("Output #52:{:s}".format(today.strftime('%Y-%m-%d')))


# In[53]:


print("Output #53:{:s}".format(today.strftime('%B %d, %Y')))


# In[58]:


#날짜 문자열로부터 특정 형식의 datetime 객체를 생성하기
date1=today.strftime('%m/%d/%Y')
date2=today.strftime('%b %d,%Y')
date3=today.strftime('%Y-%m-%d')
date4=today.strftime('%B %d,%Y')

#다른 date형식을 지닌 4가지 문자열에 기반한
#각각 2종류의 datetime 객체들과 date객체들
print("Output #54:{!s}".format(datetime.strptime(date1,'%m/%d/%Y')))
print("Output #55:{!s}".format(datetime.strptime(date2,'%b %d,%Y')))


# In[59]:


#날짜 부분만 출력하기
print("Output #56:{!s}".format(datetime.date(datetime.strptime(date3,'%Y-%m-%d'))))


# In[62]:


print("Output #57:{!s}".format(datetime.date(datetime.strptime(date4,'%B %d,%Y'))))


# In[63]:


print("Output #57:{!s}".format(datetime.date(datetime.strptime(date4,'%B%d,%Y'))))


# In[66]:


#리스트를 만들기 위해 대괄호를 사용한다.
#len()함수를 통해 리스트 내 원소의 수를 센다.
#max()함수와 min()함수는 최대/최소값을 찾는다.
#count()함수는 리스트 내 특정 값이 등장한 횟수를 센다.
a_list=[1,2,3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list=['printer',5,['star','circle',9]]
print("Output #62:{}".format(another_list))
print("Output #63: another_list also has {} elements.".format(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))


# In[67]:


#인덱스
#리스트 내 특정 원소에 접근하려면 인덱스 이용하기
#[0]은 첫번째 원소이다.[-1]은 마지막 원소이다.
print("Output #65:{}".format(a_list[0]))
print("Output #66:{}".format(a_list[1]))
print("Output #67:{}".format(a_list[2]))
print("Output #68:{}".format(a_list[-1]))
print("Output #69:{}".format(a_list[-2]))
print("Output #70:{}".format(a_list[-3]))
print("Output #71:{}".format(another_list[2]))
print("Output #72:{}".format(another_list[-1]))


# In[68]:


#리스트 분할하기
#리스트 분할을 사용하여 리스트 원소들의 부분집합 만들기
#맨 앞부터 분할하는 경우, 최초 인덱스를 생략한다.
#맨 뒤까지 리스트를 분할하는 경우, 마지막 인덱스를 생략한다.
print("Output #73:{}".format(a_list[0:2]))
print("Output #74:{}".format(another_list[:2]))
print("Output #75:{}".format(a_list[1:3]))
print("Output #76:{}".format(another_list[1:]))


# In[69]:


#리스트 복사하기
#[:]를 이용하여 리스트 복사하기
a_new_list=a_list[:]
print("Output #77:{}".format(a_new_list))


# In[70]:


#리스트 병합하기-2개 리스트의 모든 원소들을 포함하는 하나의 리스트가 된다
#+연산자를 이용하여 2개 이상의 리스트를 병합하기
a_longer_list=a_list+another_list
print("Output #78:{}".format(a_longer_list))


# In[72]:


#in 과 not in->특정 원소의 리스트 포함 여부를 확인하는 방법, 표현식들의 결과는 True나 False값으로 나오게 된다.
#in과 not in을 이용하여 특정 원소의 리스트 내 포함 여부를 확인하기
a=2 in a_list
print("Output #79:{}".format(a))
if 2 in a_list:
    print("Output #80: 2 is in{}".format(a_list))
b=6 not in a_list
print("Output #81:{}".format(b))
if 6 not in a_list:
    print("Output #82: 6 is not in {}.".format(a_list))


# In[73]:


#append(덧붙이다),remove(제거하다),pop 함수들

#append()함수를 이용하여 리스트의 마지막에 원소를 추가하기
#remove()함수를 이용하여 리스트 내 특정 원소를 제거하기
#pop()함수를 이용하여 리스트의 마지막 원소를 제거하기
a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83:{}".format(a_list))
a_list.remove(5)
print("Output #84:{}".format(a_list))
a_list.pop()
a_list.pop()
print("Output #85:{}".format(a_list))


# In[74]:


#reverse함수 
#reverse() 함수를 이용하여 리스트 반전하기
#해당 리스트 내에서 (인플레이스) 변경이 일어나므로
#기존 리스트를 변경하지 않고 반전하려면 먼저 사본을 만들어둬야 한다.
a_list.reverse()
print("Output #86:{}".format(a_list))
a_list.reverse()
print("Output #87:{}".format(a_list))


# In[ ]:


#sort 함수

