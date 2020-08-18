# selenium 으로 크롤링하기

```
# URL에 접근하는 api
get('http://url.com')

# 페이지의 단일 element에 접근하는 api
find_element_by_name('HTML_name')
find_element_by_id('HTML_id')
find_element_by_xpath('/html/body/some/xpath')

# 페이지의 여러 elements에 접근하는 api
find_element_by_css_selector('#css > div.selector')
find_element_by_class_name('some_class_name')
find_element_by_tag_name('h1')
```



# time sleep

```
import time
time.sleep(1)
```

