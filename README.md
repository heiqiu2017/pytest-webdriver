# 启动多浏览器
pytest --browser=chrome_firefox -s --html=./report.html
# 启动单浏览器
pytest --browser=chrome -s --html=./report.html

# 多线程根据driver对象个数开启
