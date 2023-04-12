# Markdown Image Uploader

Markdown Image Uploader 是一個 Python 程式，可用於將 Markdown 檔案中的本地圖片自動上傳至圖床，並將圖片路徑替換為上傳後的圖片網址，以便在網路上分享 Markdown 檔案時顯示圖片。

程式主要功能：

- 遍歷指定目錄下的所有 Markdown (.md) 檔案。
- 查找 Markdown 檔案中的圖片路徑。
- 自動將圖片上傳至圖床。
- 將 Markdown 檔案中的圖片路徑替換為上傳後的圖片網址。
- 將更新後的 Markdown 檔案寫回檔案。

程式使用 PicGo-Core 套件來進行圖片上傳，支援常見的圖床服務，例如 Imgur、GitHub、Gitee、阿里雲等等。使用者需要在 PicGo 設定中設置所需的圖床服務。

## 安裝

1. 安裝 Python 3 環境

如果尚未安裝 Python 3 環境，可到官方網站下載安裝檔進行安裝：https://www.python.org/downloads/

1. 安裝 PicGo-Core

Markdown Image Uploader 使用 PicGo-Core 來進行圖片上傳，因此需要安裝 PicGo-Core 套件。

使用以下指令進行安裝：

```
npm install picgo -g
```

1. 安裝依賴套件

使用以下指令安裝 Markdown Image Uploader 所需的依賴套件：

```
pip install os re subprocess
```

## 使用

1. 下載或複製上述程式碼到本機端。

2. 開啟 Terminal，切換至該程式碼所在目錄。

3. 執行以下指令：

   ```
   python md-image-uploader.py
   ```

4. 程式會要求輸入存放 MD 檔案的目錄名稱，請輸入存在的目錄名稱，程式會檢查是否存在該目錄，若存在則會開始執行。

5. 程式會遍歷指定目錄下的所有 MD 檔案，查找圖片路徑並進行上傳及替換，最後將更新後的內容寫回檔案。

6. 程式執行完畢後會顯示完成訊息。

## 備註

- 程式執行期間需要保持網路連接，以便進行圖片上傳。
- 程式運行期間，將使用 PicGo-Core 進行圖片上傳，因此需要在 PicGo 設定中設定好圖床的相關資訊，例如圖床名稱、API Key 等等。具體設定方式請參考 picgo-core 的官方文件。
- 程式僅適用於 macOS 作業系統。
- 使用程式前請先確認已安裝 Python 3.x 環境以及 picgo-core 套件。
