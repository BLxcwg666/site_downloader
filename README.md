```
_________________           ________                       ______            _________              
__  ___/__(_)_  /_____      ___  __ \________      ___________  /___________ ______  /____________  
_____ \__  /_  __/  _ \     __  / / /  __ \_ | /| / /_  __ \_  /_  __ \  __ `/  __  /_  _ \_  ___/  
____/ /_  / / /_ /  __/     _  /_/ // /_/ /_ |/ |/ /_  / / /  / / /_/ / /_/ // /_/ / /  __/  /      
/____/ /_/  \__/ \___/______/_____/ \____/____/|__/ /_/ /_//_/  \____/\__,_/ \__,_/  \___//_/       
                     _/_____/                                                                     
```

Python3构造的网站下载器（“扒站”工具）
# 使用说明
Usage/使用方法：
  -h 或 --help  //说明  
  -u 或 --url <网页Url>  //指定要爬取的网站Url  
  -d 或 --dir <存放目录>  //指定保存的目录（默认保存在同级目录的网站域名文件夹中）  
  
目前仅完美兼容 Linux with Python3.8 环境运行，在 Windows 环境下运行可能会点奇奇怪怪的问题（PR Welcome）  
另外请不要删除运行目录下的 error.log 文件，不管有没有发生错误，用于输出错误TraceBack  
  
downloader.py 部分代码来自 https://github.com/paperen/website-clone/blob/master/core.py  
本项目使用 Python3 重构并修复部分错误
