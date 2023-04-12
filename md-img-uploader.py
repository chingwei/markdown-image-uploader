import os
import re
import subprocess

# 指定 MD 檔案所在的目錄
# 不斷請求使用者輸入存在的目錄
while True:
    md_dir = input("請輸入目錄名稱：").strip().replace("\\", "")
    if os.path.exists(md_dir):
        break
    else:
        print("目錄不存在，請重新輸入。")

# 定義正則表達式，用於匹配 MD 檔案中的圖片路徑
img_pattern = re.compile(r"!\[.*?\]\((.*?)\)")

# 定義 picgo-core 的指令
picgo_cmd = "picgo upload {input}"

# 定義函數，用於上傳圖片並返回上傳後的網址
def upload_image(img_path):
    result = subprocess.run(picgo_cmd.format(input=f'"{img_path}"'), stdout=subprocess.PIPE, shell=True)

    # 只取得輸出的最後一行，因為這行才是網址
    tmp = result.stdout.decode().strip().split()
    url = result.stdout.decode().strip().split("\n")[-1]
    # print(f"img: {url}")
    if not url.startswith('http'):
        # print(f"tmp:{tmp}")
        raise ValueError(f"Error: Failed to upload image: {tmp}")
    
    return url

# 遍歷指定目錄下的所有 MD 檔案
for file_name in os.listdir(md_dir):
    if file_name.endswith(".md"):
        file_path = os.path.join(md_dir, file_name)
        with open(file_path, "r+", encoding="utf-8") as f:
            print(f"file: {file_path}")
            content = f.read()
            # 查找圖片路徑並進行上傳及替換
            for img_path in img_pattern.findall(content):
                if img_path.startswith("http"):
                    continue
                img_abs_path = os.path.abspath(os.path.join(os.path.dirname(file_path), img_path))

                try:
                    url = upload_image(img_abs_path)
                except ValueError as e:
                    print(e)
                    exit(1)

                print(f"img-path: {img_abs_path}")
                url = upload_image(img_abs_path)
                content = content.replace(img_path, url)
            # 將更新後的內容寫回檔案
            f.seek(0)
            f.write(content)
            f.truncate()

