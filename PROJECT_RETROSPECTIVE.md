# BlogStar：個人部落格專案回顧與保存紀錄

> 本文件用來保存這個個人網站的開發歷程、技術選擇、分支差異與未來修復注意事項。它不是履歷包裝，也不把尚未完成的功能描述成已完成產品。
>
> 內容依 Repository 中的程式碼、Git commit、templates、migrations、部署設定與 Notebook 整理。作者對當年操作的回憶會另外標示；未重新執行驗證的部分，不宣稱目前仍可正常運作。

## 1. 專案的由來與定位

BlogStar 是一個以 Django 開發的個人 Blog。最初從日本線上教學中的 Django CRUD 練習開始，後來逐步延伸成自己的網站：除了文章列表與文章內容，也加入首頁、個人介紹、登入、文章管理介面、版面設計與部署嘗試。

它的價值不只在於完成 CRUD 範例，而在於記錄一段自主開發的過程：從理解框架與資料庫操作，逐步思考個人 Blog 實際需要哪些頁面、資料欄位、操作流程與使用體驗。

這是一個供作者個人使用的網站。未來修復以作者本人能夠使用、撰寫與保存文章，以及專案能在可控環境中重新啟動為優先；不需要為多人協作、商業營運或大型產品增加不必要的複雜度。

## 2. 開發歷程

### 2021 年 3 月：建立 Django 專案

- main 的起始 commit 為 2021-03-30，訊息為「blog up 0330」。
- master 的起始 commit 為 2021-03-31。
- 專案以 Django 建立，包含文章 Model、View、URL routing、HTML templates 與 Django Admin。
- 網站名稱與介面以「Izumiの家」為主，也包含個人介紹與技術作品展示。

### 2021 年 4 月：CRUD 延伸與 Heroku 部署研究

Herokubranch 的起始 commit 是 2021-04-02，訊息為「heroku push」。接下來幾天的 commit 記錄了部署與功能調整，例如：

- 加入資料庫與調整資料庫設定。
- 安裝 django-heroku 相關套件及部署依賴。
- 調整 static files。
- 加入或調整文章新增、編輯與更新流程。
- 安裝 TinyMCE 相關套件並修改表單及 templates。
- 2021-04-04 出現「heroku-V1」commit。

這些 commit 可證明當時曾密集研究部署、資料庫與文章 CRUD；但 Git 歷史不能完整還原作者當時每一個終端機指令或操作原因。

### 2021 年 12 月至 2022 年 3 月：其他實驗檔案進入 Repository

main 的後續 commit 在 2021 年底至 2022 年 3 月增加了 Notebook 與其他上傳內容，包括：

- weather_alert.ipynb
- 日本語VL-T5推論.ipynb

這些檔案與 Django Blog 的網站功能沒有直接依賴關係，應視為 Repository 中另外保存的資料處理／AI 推論實驗。

作者回憶，這些 Notebook 可能是在當時整理或上傳檔案時混入 Repository。這是作者對當年操作的回憶；Git commit 本身只能證明檔案在後續提交中被加入，無法單獨證實是否為誤傳。

## 3. Git 分支與版本定位

| 分支 | 可確認的歷史 | 建議定位 |
|---|---|---|
| main | 2021-03-30 起始；後續有截圖、Notebook 與其他上傳內容 | 主要保存版本；建議作為未來修復基底 |
| master | 2021-03-31 起始；保留早期 Django 網站程式 | 早期版本參考 |
| Herokubranch | 2021-04-02 以「heroku push」起始；後續密集修改部署與 CRUD | 部署研究及功能演進參考 |
| docs/portfolio-retrospective | 保存專案 README 與回顧文件 | 文件整理分支 |

### 分支歷史的重要限制

目前檢查到 main、master、Herokubranch 的起始 commit 各自沒有 parent commit，且 main 與 Herokubranch 的 GitHub compare 顯示沒有共同祖先。

因此，這三條分支不是一般從同一個共同 commit 分岔出來的標準分支關係。它們更像是分別建立並各自保存的程式版本。這與作者回憶當年研究部署、分支操作不熟悉的情況相容，但不能只憑 Git 資料斷定當年實際如何操作。

**保存原則：** 不要為了整理而直接合併或刪除這些分支。它們保留了不同時間點的程式與嘗試，應先比較差異，再決定哪些功能值得移植到修復版本。

## 4. Django 網站功能與架構

### 網站頁面

目前 templates 可確認包含：

- 首頁：介紹網站與作者。
- About Me：個人介紹、技能與其他作品展示。
- 文章列表：顯示文章資料。
- 文章詳細頁：呈現單篇文章內容。
- 登入／登出相關頁面：使用 Django authentication templates 與 URL patterns。

### 文章資料模型

| 欄位 | 型別／用途 |
|---|---|
| title | 最長 200 字元的文章標題 |
| content | 文章內容；main 使用 TinyMCE 的 HTMLField |
| published_time | 文章發佈時間 |

### 主要技術

- Python、Django 2.2.x
- Django ORM、Django Admin、Django Authentication
- TinyMCE
- HTML、CSS、Bootstrap、W3.CSS
- MySQL（main 目前設定中的資料庫）
- SQLite（Repository 另有追蹤資料庫檔案，實際用途及內容尚待確認）

### TinyMCE 與 Markdown 的區別

這個專案使用 TinyMCE 富文字編輯器，搭配 Django 的 HTMLField 儲存 HTML 內容。

**本專案沒有完成 Markdown 編輯功能。** TinyMCE 是所見即所得（WYSIWYG）富文字編輯器，不應在文件或作品說明中稱為 Markdown 套件。

Herokubranch 的 requirements 曾出現 DjangoUeditor 相關依賴，但目前檢視到的 settings、Model 與 templates 尚不足以證明它曾真正整合到網站功能中，因此不把它列為已使用的編輯器。

## 5. 各分支功能差異

### main

- 有首頁、個人介紹、文章列表、文章詳細頁與登入相關頁面。
- Blog_Posts 的 content 使用 TinyMCE HTMLField。
- 有 Django Admin 文章管理。
- 前台新增／編輯文章的 View 與 URL 並未完整啟用；存在表單模板不代表操作流程已完成。
- 有文章刪除 View，但目前使用 GET 路由執行刪除，需在修復時改為安全的 POST 操作並確認權限。

### Herokubranch

- 有前台新增、編輯、更新等 View、URL 與 edit.html。
- 相關流程仍有錯誤處理缺口，例如表單驗證失敗或非預期請求時，可能使用尚未建立的變數。
- content 使用一般 TextField，與 main 的 TinyMCE HTMLField 不同。
- 保存 Heroku 部署設定，適合參考當年的部署嘗試，不宜直接取代 main。

### master

- 保留早期網站程式。
- 主要頁面與 main 有大量重疊，但沒有 main 後續加入的截圖與 Notebook。
- 可作為早期程式差異的參考版本。

## 6. SQLite 資料庫：目前已知與未知

Repository 的 main 分支追蹤了 blog/db.sqlite3，Git tree 顯示檔案大小為 131,072 bytes（128 KiB）。

但 main 的 blog/blog/settings.py 目前啟用的是 MySQL：

- Engine：django.db.backends.mysql
- Database：blogdb
- Host：127.0.0.1
- Port：3306

SQLite 設定則被註解：

- django.db.backends.sqlite3
- BASE_DIR 下的 db.sqlite3

因此可以確認 SQLite 檔案存在於 Repository，但**目前不能確認檔案內有多少篇文章、是否包含完整貼文、是否為早期版本資料，或是否只是測試資料庫**。

由於它可能含有私人文章或帳號資料，檢查時應先只確認資料表名稱、欄位與各表筆數，不讀取或公開文章標題、正文、密碼雜湊或個人資料。確認內容後再決定是否保留、備份或轉移。

## 7. 歷史部署設定

Herokubranch 保存了當年的部署相關檔案：

- blog/Procfile
- blog/runtime.txt
- blog/requirements.txt
- WhiteNoise、Gunicorn、django-heroku、dj-database-url 等相關依賴

其中 runtime 指定 Python 3.7.10，Procfile 使用 Gunicorn 啟動 Django WSGI application。

這些檔案是歷史部署紀錄，不代表 Heroku 上的舊服務仍存在，也不代表原環境能在目前的平台直接重現。未來若要重新部署，應先確認個人網站實際需求，再選擇維護成本合理的方式，不必為了重現 Heroku 而保留過時依賴。

## 8. 其他 Notebook 的定位

### weather_alert.ipynb

使用 Requests 讀取公開 JSON Feed，解析低溫與降雨警報，再以地區關鍵字篩選訊息。它是獨立的資料擷取實驗，不是 Blog 網站功能，也不應描述為已完成的即時預警服務。

### 日本語VL-T5推論.ipynb

使用既有的日文 VL-T5 與 Faster R-CNN 預訓練模型進行推論示範，包含圖片問答、圖文匹配、視覺定位與區域描述等任務。

目前證據支持「載入並使用預訓練模型進行推論」，不支持「自行訓練 VL-T5 或 Faster R-CNN」。

## 9. 已知技術問題與修復方向

| 項目 | 已知狀況 | 修復方向 |
|---|---|---|
| Django 版本 | 2.2.x，年代久遠 | 先建立可重現環境，再評估升級 |
| Secret Key | 現行程式以佔位字串取代 | 改由環境變數提供；檢查 Git 歷史中的舊值 |
| DEBUG／ALLOWED_HOSTS | main 仍是 DEBUG=True、ALLOWED_HOSTS=['*'] | 依個人本機或正式部署環境分開設定 |
| 資料庫 | MySQL 設定啟用，SQLite 檔案另行追蹤 | 先確認 SQLite 內容與保存需求 |
| published_time | Model 使用 default=datetime.now() | 改為可呼叫的時間函式，並檢查時區 |
| Form 欄位 | main 的 Form 欄位名稱曾出現尾端空白 | 修正欄位名稱 |
| 刪除操作 | GET 請求可觸發刪除 | 改用 POST、CSRF 保護與適當權限 |
| HTML 內容 | detail template 使用 safe 顯示內容 | 評估 HTML 清理與可信任內容邊界 |
| 前台 CRUD | main 的新增／編輯流程未完整接通 | 依個人使用需求補齊，不追求不必要功能 |
| 靜態檔案 | 有舊版 static 路徑與部署設定 | 重新驗證收集與載入方式 |
| Repository 體積 | 曾追蹤 node_modules、Python env 等環境產物 | 先保存歷史，再決定是否從未來版本排除 |

## 10. 未來修復的範圍與原則

本專案的修復目標是「讓原本的個人 Blog 可以再次使用」，而不是重寫成新的產品。

建議順序：

1. **文件整理：** 整理專案故事、分支歷史、技術架構、資料庫狀態與操作說明。
2. **資料保存：** 確認 SQLite 是否含有文章及其他重要資料，建立安全備份。
3. **環境重現：** 確認 Python、Django 與舊依賴能否在隔離環境啟動。
4. **必要修復：** 修正設定、文章新增／編輯／刪除、登入權限及內容安全問題。
5. **個人使用驗證：** 確認作者能登入、管理文章、撰寫內容、瀏覽歷史文章。
6. **保存與展示：** 保留歷史截圖、README、安裝步驟與已知限制。

### 不在目前目標內

- 不為多人使用設計複雜的角色與權限系統。
- 不為了技術新潮而全面改寫成 React 或其他框架。
- 不把兩份 Notebook 強行整合進 Blog。
- 不在確認資料庫內容前刪除 SQLite。
- 不在未確認必要性前刪除 node_modules、env 或歷史分支。
- 不把未驗證的歷史部署描述成目前可用的服務。

## 11. 驗證界線

- 本文件中的程式功能描述來自靜態程式碼檢視。
- 尚未重新安裝依賴、執行 migrations、啟動 Django server 或重新部署。
- SQLite 尚未讀取資料表或資料列；目前僅確認 Repository 中存在該檔案及其 Git tree 檔案大小。
- Notebook 的描述依現有程式碼與保存輸出，不代表已在目前環境重新執行。
- Git commit 可以佐證提交時間與檔案變化，但不能完整還原作者當年的每一個操作意圖。
