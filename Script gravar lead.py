#!/usr/bin/env python
# coding: utf-8

# # Criando o token na base 64

# ### Importando as bibliotecas

# In[ ]:


from pybase64 import b64encode
from datetime import date
from datetime import datetime


# #### Pegando a Data e hora atual

# In[24]:


GetDateandHourNow = datetime.now()
DateandHourNow = GetDateandHourNow.strftime('%Y%m%d%H%M%S')
DayofWeek = GetDateandHourNow.strftime('%w')


# #### Dados da integração

# In[28]:


TokenOrigen = 'ac7470e2aed06703e0181c195d149de5'
TokenTypeLead = '65ba2ceb99baef90c363bf395c1a9bdd'
IdProject = '2'
IdTypeLead = '53'


# #### Concatenando e Convertendo os dados para base64

# In[29]:


ConcatAllParameters = f'{DateandHourNow}{TokenOrigen}|{IdProject}|{TokenTypeLead}|{DayofWeek}'
ConcatAllParameters


# #### Convertendo para a base64

# In[31]:


ConvertForBase64 = b64encode(b'20221221160705ac7470e2aed06703e0181c195d149de5|2|65ba2ceb99baef90c363bf395c1a9bdd|3')
ConvertForBase64


# In[ ]:




