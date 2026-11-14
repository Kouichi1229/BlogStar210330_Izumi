# BlogStar：技術經歷回顧

> 本文件根據 Repository 中的 Django 程式碼、HTML templates、資料模型、路由、部署分支及兩份 Notebook 整理。沒有重新部署或執行完整測試，因此不將歷史程式碼描述為目前可用服務。

## 1. 專案組成

這個 Repository 其實包含三個不同性質的實作：

1. **Django 個人部落格：** 文章展示、個人介紹、登入與管理功能。
2. **災害預警資料擷取實驗：** 從公開 JSON feed 取得低溫與降雨警報，嘗試篩選指定地區訊息。
3. **日文視覺語言模型推論實驗：** 使用既有 VL-T5 與 Faster R-CNN 預訓練模型進行視覺語言任務推論。

三者不應被描述成同一個應用系統的功能模組。

## 2. Django 個人部落格

### 可由程式碼確認的功能

- 使用 Django 2.2 建立專案與 `context` app。
- 以 `Blog_Posts` Model 儲存文章標題、HTML 內容及發佈時間。
- 透過 Django ORM 查詢文章列表及單篇文章。
- 使用 Django templates 呈現首頁、個人介紹、文章列表及詳細內容。
- 將 `Blog_Posts` 註冊到 Django Admin，可透過管理後台管理文章。
- 使用 Django 內建 authentication URL patterns 提供登入／登出路由。
- 文章內容使用 TinyMCE HTMLField，支援富文字內容。
- 前端使用 Bootstrap、W3.CSS、Bootstrap Icons 等資源建立網站版面。

### 程式結構

| 檔案 | 職責 |
|---|---|
| `blog/blog/settings.py` | Django 專案設定、App、Middleware、資料庫及靜態檔案設定 |
| `blog/blog/urls.py` | Admin、文章 app、authentication、TinyMCE 路由 |
| `blog/context/models.py` | 文章資料模型 |
| `blog/context/views.py` | 首頁、個人介紹、文章列表、文章詳細頁及刪除 view |
| `blog/context/urls.py` | 網站頁面路由 |
| `blog/context/admin.py` | 註冊文章 Model 至 Django Admin |
| `blog/context/templates/` | 網站頁面模板 |

### 功能邊界

- 一般使用者介面具備文章列表與詳細頁。
- 文章資料可透過 Django Admin 管理。
- Repository 有建立文章的表單模板，但目前 `views.py` 中表單 view 與對應路由已註解，不能宣稱前台新增／編輯流程完整。
- 刪除文章的路由使用 GET 方法直接執行刪除，沒有看到 POST 確認流程。這是歷史實作限制，不符合較安全的現代刪除操作設計。
- `published_time` 的 Model default 使用 `datetime.now()` 的呼叫結果，而不是可延後呼叫的 callable；模型載入時會固定預設時間值，可能造成新文章時間不如預期。
- 文章詳細頁以 `safe` filter 呈現 HTML 內容；若內容來源未受信任，需額外考慮 HTML sanitization。

## 3. 災害預警資料擷取 Notebook

檔案：`weather_alert.ipynb`

### 可由程式碼確認的流程

- 使用 Requests 讀取國家災害防救科技中心的 JSON Atom Feed。
- 程式分別保存低溫與降雨預警資料來源 URL。
- 解析 JSON 後，逐筆讀取 `entry` 中的警報摘要。
- 以「屏東」或「恆春」作為字串條件，嘗試篩選與目標區域相關的警報。

### 技術定位與限制

這份 Notebook 可佐證 Python Requests、JSON 解析及文字條件篩選的實作接觸，但不是完整的即時預警系統。現有程式有變數生命週期與錯誤處理問題：篩選函式在沒有符合資料時可能使用未初始化變數；外層程式的 `finally` 又會將結果變數設為 `None`。Notebook 保存的輸出也曾顯示 `None`，因此不能宣稱預警擷取流程已穩定運作。

## 4. 日文 VL-T5 視覺語言模型推論

檔案：`日本語VL-T5推論.ipynb`

### 可由程式碼確認的流程

1. 在 Google Colab 環境 clone 日文 VL-T5 專案。
2. 安裝指定版本的 Transformers、SentencePiece 等相依套件。
3. 載入 `sonoisa/vl-t5-base-japanese` 預訓練模型及 tokenizer。
4. 載入 `unc-nlp/frcnn-vg-finetuned` Faster R-CNN 預訓練模型。
5. 以 Faster R-CNN 抽取影像區域特徵與 bounding boxes。
6. 將日文任務提示與視覺特徵輸入 VL-T5，執行生成式推論。
7. 示範以下任務：
   - VQA：日文圖片問答。
   - Image-text matching：判斷圖片與文字描述是否匹配。
   - Visual grounding：定位文字描述對應的影像區域。
   - Region captioning：為指定影像區域產生描述。

Notebook 保存的輸出包含對騎馬圖片的日文問答結果，以及圖文匹配、區域定位等推論紀錄。

### 合理的能力描述

這份 Notebook 可呈現使用既有多模態預訓練模型、模型載入、GPU／CPU 裝置選擇、影像前處理、視覺特徵抽取及生成式推論流程的實作經驗。

**不可宣稱自行訓練 VL-T5 或 Faster R-CNN。** Notebook 主要使用已發布的預訓練權重，沒有自行訓練資料集、訓練迴圈、loss 計算或模型評估流程的證據。它也不是完整 benchmark，不能將單張示範圖片的輸出視為模型準確率。

## 5. 部署與相依環境

- `Herokubranch` 保存 Heroku 部署設定，包括 Gunicorn Procfile、Python 3.7.10 runtime、requirements 及 WhiteNoise／django-heroku 相關設定。
- `main` 分支的 Django settings 使用本機 MySQL 開發連線設定；`Herokubranch` 則有 Heroku 部署配置。
- Repository 內有大量已提交的 `node_modules`、虛擬環境套件檔及 SQLite 資料庫，增加檔案體積，也使原始碼與環境產物混雜。
- 部分依賴版本相當舊，沒有重新安裝及執行驗證，因此無法保證在現代 Python／Django 環境可直接啟動。

## 6. 技術能力摘要

| 技術 | 程式證據 | 合理定位 |
|---|---|---|
| Python | Django、Notebook | 有 Python 應用與資料處理經驗 |
| Django | Model、View、URL、Template、Admin | 有 MVC／MTV 網站開發經驗 |
| Django ORM | 文章資料模型與查詢 | 有 ORM 基本資料存取經驗 |
| Authentication | Django auth routes、登入模板 | 有網站登入流程整合經驗 |
| TinyMCE | HTMLField | 有富文字內容編輯器整合經驗 |
| Requests／JSON | 災害警報 Notebook | 有外部 JSON API 擷取與解析經驗 |
| PyTorch／Transformers | VL-T5 推論 Notebook | 有多模態預訓練模型載入與推論經驗 |
| Faster R-CNN | 影像區域抽取 | 有使用物件偵測模型產生視覺特徵的經驗 |

## 7. 履歷描述建議

### Django 網站

使用 Python、Django 開發個人部落格網站，建立文章資料模型、文章列表與詳細頁、個人介紹頁及 Django Admin 管理介面，整合 Django Authentication 與 TinyMCE 富文字編輯器，並使用 Bootstrap 等前端資源完成頁面呈現。

### AI 推論實驗

使用 Google Colab、PyTorch 與 Transformers 載入日文 VL-T5 及 Faster R-CNN 預訓練模型，完成影像特徵抽取與日文視覺語言推論示範，涵蓋圖片問答、圖文匹配、視覺定位及區域描述任務。

## 8. 安全與隱私整理紀錄

- Django settings 中原本直接寫入的 `SECRET_KEY` 已在目前的 `main`、`master` 與 `Herokubranch` 分支替換為 `SECRET_KEY` 佔位值。
- Git commit history 未重寫，舊 commit 仍可能保留原始 secret。若網站曾使用該金鑰，應視為已曝光並重新產生。
- 網站首頁模板包含一個電子郵件地址；本次未修改，因為它可能原本就是公開聯絡方式，是否保留應由作者決定。
- Repository 內含已追蹤的 SQLite 資料庫檔案；本次沒有讀取其內容或刪除它。若資料庫含個人資料、登入帳號或非公開文章，需另行檢視公開風險。

## 9. 驗證界線

- Django 程式以靜態檢視為主，沒有重新安裝依賴、執行 migrations 或啟動伺服器。
- Notebook 僅依現有程式碼與保存輸出判斷，沒有重新下載模型或重新執行 GPU 推論。
- Heroku 部署分支只證明曾保存部署設定，不代表歷史服務目前仍存在或可用。
