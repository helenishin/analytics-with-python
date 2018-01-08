
# coding: utf-8

# In[13]:


#2장으로 일단 넘어가자
#제발 
#!/usr/bin/env pyhton3
import sys

input_file='supplier_data.csv'
output_file='real.csv'


with open(input_file,'r',newline='') as filereader:
    with open(output_file,'w',newline='') as filewriter:
        header=filereader.readline()
        header=header.strip()
        header_list=header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')
        for row in filereader:
            row =row.strip()
            row_list=row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')


# In[8]:


sys.argv[1]
sys.argv[2]


# In[10]:


get_ipython().magic('pwd')


# In[14]:


#2.2.2 팬더스
#팬더스로 오지 못할 뻔 했다.
#!/urs/bin/env python3
import sys
import pandas as pd
imput_file='supplier_data.csv'
output_file='real.csv'

data_frame=pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file,index=False)



# In[16]:


#2.3 기본 문자열 파싱이 실패하는 경우
#csv 파일에서 기본 문자열 파싱이 실패하는 경우
#마지막 두 행에 쉼표값이 포함되어 있으므로 파시이 실패하게 된다.
#!/usr/bin/env pyhton3
import sys

input_file='supplier_data.csv'
output_file='real.csv'


with open(input_file,'r',newline='') as filereader:
    with open(output_file,'w',newline='') as filewriter:
        header=filereader.readline()
        header=header.strip()
        header_list=header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n')
        for row in filereader:
            row =row.strip()
            row_list=row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')


# In[20]:


#2.4 CSV 파일 읽고 쓰기(파트2)
#2.4.1 기본 파이썬(csv모듈 사용)
#파이썬에 내장된 csv 모듈을 사용하여 데이터 값에 포함된 쉼표 및 기타 복잡한 패턴을 정확하게 처리할 수 있다.
#정규표현식 및 조건부 수식을 설계하는 것보다 훨씬 간단
#책에서는 명령 프롬프트로 설명하고 있는데 나는 쥬피터를 쓰고 있어서 이렇게 저렇게 바꿔서 해봐야한다.
#여기서는 마지막 줄에 print(row_list)를 추가했는데,for문 아래에 추가했을 때는 마지막 행 한줄만 결과가 나왔다. 왜지?!
#!/usr/bin/env pyhton3
import csv
import sys

input_file='supplier_data.csv'
output_file='real.csv'

with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        filereader=csv.reader(csv_in_file,delimiter=',')
        filewriter=csv.writer(csv_out_file,delimiter=',')
        for row_list in filereader:
            filewriter.writerow(row_list)
            print(row_list)


# In[ ]:


#2.5 특정 행을 필터링하기
#분석해야하는 파일에 필요한 것보다 많은 행이 포함되어 있는 경우가 있는데 쓸데없는 행들을 쳐내서 필터링할 수 있는 방법을 배워본다.
##1특정 조건을 충족하는 행을 필터링하기
##2특정 집합의 값을 포함하는 행을 필터링하기
##3정규 표현식을 활용해 필터링하기
# ***으로 둘러싸인 라인들을 수정하여 특정 비즨스 규칙을 적용하고 필요한 행을 추출하는 방법을 알아본다.
for row in filereader:
    ***if 행에 있는 값이 특정한 규칙(들)을 충족한다면***
    이러이러한 일을 한다.
    else:
        아니면 뭔가 다른 일을 한다.


# In[29]:


#2.5.1 특정 조건을 충족하는 행의 필터링
#Supplier Name이 Supplier Z이거나 또는 Cost가 $600.00이상인 행만 필터링하고 그 결과를 출력 파일에 기록할 것이다.
#동일여부를 평가하는데 등호== 2개 쓰는 것 기억할것
#!/usr/bin/env python3
import csv
import sys

input_file='supplier_data.csv'
output_file='real.csv'

with open(input_file,'r',newline='')as csv_in_file:
    with open(output_file,'w',newline='')as csv_out_file:
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        header=next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier=str(row_list[0]).strip()
            cost=str(row_list[3]).strip('$').replace(',','')
            if supplier =='Supplier Z' or float(cost)>600.0:
                filewriter.writerow(row_list)
                


# In[31]:


#팬더스
#팬더스는 특정 행과 열을 동시에 선택할 수 있는 loc()함수를 제공한다.
#쉼표를 기준으로 앞에는 행을 필터링하는 조건을 지정하고, 뒤에는 열을 필터링하는 조건을 지정
#!/usr/bin/env python3
import pandas as pd
import sys

input_file='supplier_data.csv'
output_file='real.csv'

data_frame=pd.read_csv(input_file)

data_frame['Cost']=data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition=data_frame.loc[(data_frame['Supplier Name'].str.contains('Z'))|(data_frame['Cost']>600.0),:]
data_frame_values_meets_condition.to_csv(output_file,index=False)
print(output_file)

