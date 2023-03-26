import urllib.request
import re
import time
import datetime
import sys
import downloader
import webbrowser
import getopt
import os
import traceback

#redirect traceback log
os.remove('error.log')
__stderr__ = sys.stderr
sys.stderr = open('error.log', 'a')

#def ascii_word():
print("_________________           ________                       ______            _________            ")
print("__  ___/__(_)_  /_____      ___  __ \________      ___________  /___________ ______  /____________")
print("_____ \__  /_  __/  _ \     __  / / /  __ \_ | /| / /_  __ \_  /_  __ \  __ `/  __  /_  _ \_  ___/")
print("____/ /_  / / /_ /  __/     _  /_/ // /_/ /_ |/ |/ /_  / / /  / / /_/ / /_/ // /_/ / /  __/  /    ")
print("/____/ /_/  \__/ \___/______/_____/ \____/____/|__/ /_/ /_//_/  \____/\__,_/ \__,_/  \___//_/     ")
print("                     _/_____/                                                                     ")
print("By BLxcwg666｜https://blog.blxcnya.cn/archives/171｜Type -h to get help")
print(" ")
    
def usage():
    print("Usage/使用方法：")
    print("  -h 或 --help  //说明")
    print("  -u 或 --url <网页Url>  //指定要爬取的网站Url")
    print("  -d 或 --dir <存放目录>  //指定保存的目录（默认保存在同级目录的网站域名文件夹中）")
    return 0

def main():
    url = ""
    root = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'u:d:h:',
            [
                'url=',
                'dir=',
                'help=',
            ]
        )
        for opt, val in opts:
            if opt in ('-u', '--url'):
                url = val
            elif opt in ('-d', '--dir'):
                root = val
            elif opt in ('-h', '--help'):
                usage()
            else:
                raise Exception
    except getopt.GetoptError as err:
        usage()

    try:
        if root != None and os.path.exists(root) == False:
            print("[Error] 无法获取指定的保存目录，请确保该目录存在")
            raise Exception
        if re.search(r"^((https|http)?:\/\/)[^\s]+", url) == None:
            print("[Error] Url无效，请确保输入的Url包含协议头（http(s)://）")
            raise Exception

        t = downloader.thief(url, root)

        
        # 获取根目录
        root = t.getroot()
        if not root:
            root = ''

        # 爬取网页
        with urllib.request.urlopen(url) as f:
            html = f.read().decode('utf-8')
        if len(html) == 0:
            print("[Error] 发生错误，网页获取失败")
            raise Exception

        # css
        sys.stdout.write("[INFO] 开整CSS")
        css = re.findall(r"<\s*link\s+[^>]*?href\s*=\s*[\"|\'](.*?)[\"|\'][\s\S]*?>", html)
        for v in css:
            html = html.replace(v, t.get(v))
        sys.stdout.flush()
        print("\n[INFO] CSS整好了")

        # 页面内css
        sys.stdout.write("[INFO] 开整页面内CSS")
        intercss = re.findall(r"background\:url\((.*?)\)", html)
        for v in intercss:
            if v.find('data:') == -1: html = html.replace(v, t.get(v))
        sys.stdout.flush()
        print("\n[INFO] 页面内CSS整好了")

        # js
        sys.stdout.write("[INFO] 开整JavaScript")
        js = re.findall(r"<\s*script\s+[^>]*?src\s*=\s*[\"|\'](.*?)[\"|\'][\s\S]*?>", html)
        for v in js:
            html = html.replace(v, t.get(v))
        sys.stdout.flush()
        print("\n[INFO] JavaScript整好了")

        # image
        sys.stdout.write("[INFO] 开整图片")
        img = re.findall(r"<\s*img\s+[^>]*?src\s*=\s*[\"|\'](.*?)[\"|\'][\s\S]*?>", html)
        for v in img:
            html = html.replace(v, t.get(v))
        sys.stdout.flush()
        print("\n[INFO] 图片整好了")

        # 保存网页
        # 在这里将html转换为字节对象
        html_bytes = html.encode('utf-8')
        # 保存index.html
        index_path = root + 'index.html'
        with open(index_path, 'wb') as fp:
            fp.write(html_bytes)
        print("[INFO] 下载完成")

    except Exception as e:
        print("\n[Error] 下载失败，TraceBack已输出到当前目录下的 error.log")
        traceback.print_exc()


if __name__ == "__main__":
    main()
