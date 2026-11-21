# BlogStar — Izumi 個人部落格

這是以 Django 建立的個人網站。專案最初從 Django CRUD 教學練習開始，後來逐步加入首頁、About Me、文章列表、文章詳細頁、TinyMCE 富文字編輯器與個人作品展示。

目前的修復方向是讓網站能在現代 Python / Django 環境中於本機重新啟用。它是個人使用的網站，不以公開部署或多人產品化為目標。

## 目前狀態

- 修復分支：`restore/django-5.2-local`
- Python 目標版本：3.12
- Django：5.2.19
- 富文字編輯器：django-tinymce 5.0.0
- 資料庫：新的本機 SQLite 檔案
- 文章管理：Django Admin
- 執行方式：本機開發伺服器

**重要：** 程式碼與操作文件已整理，但 Django 執行環境尚未完成實際驗收。請依照下方步驟執行，並以命令輸出確認安裝、Migration、測試及頁面運作狀態。

## 功能範圍

- 首頁：`/context/`
- About Me：`/context/aboutme`
- 文章列表：`/context/list`
- 文章詳細頁：`/context/<文章 ID>`
- Django Admin：`/admin/`
- 登入／登出：Django 內建 authentication URLs
- TinyMCE：在 Django Admin 編輯文章內容

文章新增、編輯與刪除統一透過 Django Admin 操作，不提供前台文章 CRUD。

## 環境需求

- macOS（以下命令以 macOS / zsh 為例）
- Python 3.12
- pip
- Git

Repository 根目錄包含 `requirements.txt`；Django 專案與 `manage.py` 位於 `blog/` 目錄。

## 安裝與啟動

### 1. 取得專案並進入 Django 目錄

如果尚未 clone：

```bash
git clone https://github.com/Kouichi1229/BlogStar210330_Izumi.git
cd BlogStar210330_Izumi
git switch restore/django-5.2-local
```

如果已經有專案，請先切換到修復分支：

```bash
git switch restore/django-5.2-local
```

### 2. 建立 Python 虛擬環境

在 Repository 根目錄執行：

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

確認 Python 版本：

```bash
python --version
```

預期為 Python 3.12.x。

### 3. 安裝依賴

仍在 Repository 根目錄執行：

```bash
python -m pip install -r requirements.txt
```

### 4. 設定本機 Secret Key

每次開啟新的 Terminal session，啟動虛擬環境後，執行：

```bash
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
```

這會在目前的 Terminal session 設定一組隨機金鑰，不會將金鑰寫入 Repository。

目前 Settings 有一組明確標示為本機開發用途的 fallback，方便初次啟動；仍建議使用上述環境變數。此設定不適用於公開部署。

### 5. 執行 Django 檢查與 Migration

切換到 Django 專案目錄：

```bash
cd blog
python manage.py check
python manage.py migrate
```

新資料庫會建立在：

```text
blog/db.local.sqlite3
```

這是本次修復專用的新資料庫。Repository 原有的 `blog/db.sqlite3` 是歷史檔案，不會作為這個新環境的資料來源，也不應覆寫。

### 6. 建立個人管理員

```bash
python manage.py createsuperuser
```

依照提示輸入管理員帳號、Email（若提示）與密碼。請自行保管密碼，不要提交到 Git。

### 7. 執行測試

```bash
python manage.py test
```

### 8. 啟動本機網站

```bash
python manage.py runserver
```

開啟：

- 首頁：http://127.0.0.1:8000/
- 文章列表：http://127.0.0.1:8000/context/list
- About Me：http://127.0.0.1:8000/context/aboutme
- 管理介面：http://127.0.0.1:8000/admin/

停止伺服器可在執行中的 Terminal 按 `Ctrl + C`。

## 文章管理

1. 開啟 http://127.0.0.1:8000/admin/。
2. 使用剛建立的 superuser 登入。
3. 進入文章（Blog_Posts）管理頁。
4. 新增、編輯或刪除文章。
5. 文章內容欄位使用 TinyMCE 編輯器。
6. 儲存後到前台文章列表與詳細頁確認顯示。

詳細頁會先經過 `nh3` HTML sanitizer，再輸出文章內容。這是為了避免直接將未清理的 HTML 當成可信任內容輸出。

## 資料庫與備份

本機文章資料庫：

```text
blog/db.local.sqlite3
```

此檔案已加入 `.gitignore`，不會隨一般 Git commit 提交。

備份前先停止 Django 開發伺服器，然後在 Repository 根目錄執行：

```bash
cp blog/db.local.sqlite3 "blog/db.local.sqlite3.backup"
```

若要保存多份備份，請自行使用不同檔名或放在 Repository 外部的安全位置。不要把含有個人文章或帳號資料的資料庫上傳到公開 Repository。

**不要刪除或覆寫歷史檔案 `blog/db.sqlite3`。** 新網站只使用 `blog/db.local.sqlite3`。

## 常見操作

所有以下命令都應在 `blog/` 目錄且已啟動虛擬環境後執行：

```bash
# 檢查 Django 設定
python manage.py check

# 查看 Migration 狀態
python manage.py showmigrations

# 執行 Migration
python manage.py migrate

# 建立管理員
python manage.py createsuperuser

# 執行測試
python manage.py test

# 啟動本機伺服器
python manage.py runserver
```

## 專案結構（主要部分）

```text
.
├── README.md
├── requirements.txt
├── .gitignore
└── blog/
    ├── manage.py
    ├── blog/
    │   ├── settings.py
    │   └── urls.py
    └── context/
        ├── admin.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        ├── views.py
        ├── migrations/
        ├── templates/
        └── templatetags/
            └── sanitize_html.py
```

## 修復與驗收狀態

| 項目 | 狀態 |
|---|---|
| Django 5.2 本機設定 | 已提交，尚待實際執行驗證 |
| 獨立 SQLite 路徑 | 已設定，尚待 Migration 驗證 |
| Django Admin 文章管理 | 已實作，尚待瀏覽器驗證 |
| TinyMCE | 已設定，尚待瀏覽器驗證 |
| 主要前台頁面 | 已整理模板與路由，尚待瀏覽器驗證 |
| HTML sanitizer | 已實作，尚待自動化測試驗證 |
| 自動化測試 | 已新增測試案例，尚未執行 |
| 本機安裝與備份說明 | 已整理於本文件 |

請勿將「程式碼已提交」解讀成「網站已經在本機成功啟動」。只有在乾淨環境完成上述安裝步驟，並確認命令與頁面結果後，才能將相應項目標記為通過。

## 歷史畫面截圖

以下截圖是 Repository 原先保存的網站畫面，作為歷史作品紀錄。它們不代表目前線上服務仍可使用。

![Historical screenshot 1](https://user-images.githubusercontent.com/24285484/159891995-ecc39809-efcc-4209-a92e-1eea00bcd6a1.png)

![Historical screenshot 2](https://user-images.githubusercontent.com/24285484/159892048-5e1618a6-dd91-401d-a48c-cb9a7287c055.png)

![Historical screenshot 3](https://user-images.githubusercontent.com/24285484/159892077-ee50b961-9dd5-4c24-8714-11b17f50a81c.png)

![Historical screenshot 4](https://user-images.githubusercontent.com/24285484/159892176-6a9120bb-7edb-4cc3-91fa-3f10c98e0502.png)

![Historical screenshot 5](https://user-images.githubusercontent.com/24285484/159892217-834e3a53-8896-4670-a6b7-5aefb614719a.png)

![Historical screenshot 6](https://user-images.githubusercontent.com/24285484/159892251-d49ec84f-33e5-4b3b-8936-3ae0afbce21c.png)

![Historical screenshot 7](https://user-images.githubusercontent.com/24285484/159892285-cef025cb-ee98-4d48-9a43-a92cc5747381.png)

## 歷史文件

專案開發歷程、Git 分支差異與早期技術調查，請參考：

- `PROJECT_RETROSPECTIVE.md`
- `docs/portfolio-retrospective/RESTORATION_PLAN.md`

本次修復不包含舊文章復原、舊 MySQL／PostgreSQL 連線或 Heroku 重新部署。
