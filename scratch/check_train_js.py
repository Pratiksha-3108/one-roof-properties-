with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

pos = text.find('function updateCategoryShowcaseOnScroll')
if pos != -1:
    print(text[pos:pos+1500])
else:
    # search for srProjectsViewport or srTrainResidential
    for m in re.finditer(r'srTrainResidential', text):
        p = m.start()
        print(text[p-100:p+600])
        print('='*50)

