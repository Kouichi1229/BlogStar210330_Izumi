# BlogStar：個人網站重新啟用計畫

> 本文件定義最小可用修復範圍。目標不是復原 2021 年的資料或部署環境，而是讓原本的 Django 個人網站在現代本機環境重新運作。

## 1. 修復目標

### 主要目標

- 以 `main` 分支為程式修復基準，保留原本網站的首頁、About Me、文章列表與文章詳細頁。
- 在本機建立可重現的 Python / Django 環境。
- 使用 SQLite 作為新的本機資料庫；舊資料庫檔案保留原狀，不作為新環境的資料來源。
- 使用 Django Admin 管理文章，支援新增、查看、編輯與刪除。
- 保留 TinyMCE 富文字編輯體驗。
- 修正會阻止網站啟動或造成核心功能錯誤的問題。
- 提供簡單的安裝、啟動與管理說明。

### 明確不做

- 不尋找或復原舊文章，不讀取舊文章內容。
- 不為了舊文章而處理舊桌機、舊 MySQL 或可能存在的 PostgreSQL。
- 不重現 Heroku 部署，不做公開部署。
- 不重新實作前台新增／編輯／刪除介面；文章管理以 Django Admin 為準。
- 不重寫網站外觀，不整合 Notebook，不做多人產品化或不必要的基礎設施。
- 不刪除歷史分支、Notebook、圖片、舊 SQLite 或其他原始資產。

## 2. 修復基準與技術方案

| 項目 | 決定 |
|---|---|
| Repository | `Kouichi1229/BlogStar210330_Izumi` |
| 程式修復基準 | `main` |
| 基準 Commit | `6bff2a39440a50c8bc79efda9aadbdef374616fa` |
| Python | 3.12 |
| Django | 5.2 LTS，採用當前可用的 5.2.x 安全修補版本 |
| Database | SQLite，新建本機資料庫 |
| Rich Text Editor | 與 Django 5.2 相容的 django-tinymce 5.x |
| 管理介面 | Django Admin |
| 執行方式 | 本機開發伺服器，僅供個人使用 |
| 文件分支 | `docs/portfolio-retrospective` |

選擇依據：
- Django 5.2 是 LTS 系列，官方安全支援至 2028 年 4 月。
- Django 5.2 支援 Python 3.10–3.14；本專案選用 Python 3.12。
- django-tinymce 5.0.0 官方套件資訊列出支援 Django 4.2–5.2 與 Python 3.9 以上。
- SQLite 隨 Python 提供，適合本機個人網站，不需要額外資料庫服務。

以上版本是目標相容組合；實際安裝時仍須鎖定可取得的安全修補版本，並以乾淨環境測試確認。

## 3. 已確認的程式問題

| 優先級 | 問題 | 修復方向 |
|---|---|---|
| P0 | Settings 使用佔位 Secret Key、DEBUG=True、ALLOWED_HOSTS=['*'] | 使用環境設定與本機安全預設值 |
| P0 | 刪除文章使用 GET，且沒有後端登入保護 | 不再提供前台刪除路由；由 Django Admin 權限管理 |
| P1 | Model 的 `published_time` 使用 `default=datetime.now()` | 改用適當的 callable default，或依 Django 時區策略設定 |
| P1 | ModelForm 欄位名稱 `published_time ` 有尾端空白 | 若不再使用前台表單，移除未使用表單；否則修正欄位名稱 |
| P1 | 前台新增／編輯流程未完整啟用 | 不重建前台 CRUD，改由 Django Admin 提供 |
| P1 | 新增頁 Submit button 位於 form 外 | 若不再使用該頁，確認後移除未使用路由／模板引用 |
| P1 | 詳細頁使用 `safe` 顯示 TinyMCE HTML | 檢查輸入與輸出安全邊界，避免危險 HTML 執行 |
| P1 | 部分模板繼承不同 layout，可能造成頁面樣式不一致 | 統一模板繼承並驗證主要頁面 |
| P2 | main 缺少 Python requirements manifest | 建立最小且鎖定版本的依賴清單 |
| P2 | Settings 的 Static 路徑需重新驗證 | 以 Django staticfiles 慣例修正並測試 |
| P2 | Repository 追蹤 node_modules／__pycache__ | 先確認必要性；本次不因清理而大量刪除歷史檔案 |

## 4. 執行階段與驗收條件

### Phase 0 — 修復基準與隔離

工作：
- 從 main 建立獨立修復分支，不直接在 main 上開發。
- 保留 main 與文件分支現況。
- 確認每次變更只涉及核准的修復檔案。
- 不操作舊 SQLite，不連線任何 MySQL／PostgreSQL。

驗收：
- 修復分支起點為指定 main 基準 commit。
- 原始 main 不被直接修改。
- 舊資料庫與歷史資產保持不變。

### Phase 1 — 現代環境重建

工作：
- 建立 Python 3.12 隔離環境。
- 建立最小依賴清單，採用 Django 5.2.x 與相容的 django-tinymce 5.x。
- 將資料庫設定改為新的本機 SQLite。
- 修正必要的 Settings、URL 與 staticfiles 設定。
- 檢查並執行 Django system check 與 migration；只對新建 SQLite 資料庫操作。

驗收：
- 可從乾淨環境安裝依賴。
- `manage.py check` 通過。
- Migration 可在新 SQLite 資料庫成功執行。
- `runserver` 可啟動，首頁可載入。

### Phase 2 — 核心頁面與文章管理

工作：
- 修復首頁、About Me、文章列表與文章詳細頁的模板繼承及路由。
- 確保 Blog_Posts 正常註冊於 Django Admin。
- 修復 Model 欄位與時間預設值。
- 透過 Django Admin 完成文章新增、編輯、刪除。
- 確認 TinyMCE 編輯器正常載入，文章 HTML 以安全方式呈現。

驗收：
- 四個主要前台頁面可正常瀏覽。
- Admin 可登入，未登入者不能進入管理介面。
- 可在 Admin 建立、編輯、刪除測試文章。
- 測試文章可在前台列表與詳細頁正確顯示。
- 危險 HTML 不會以可執行形式輸出。

### Phase 3 — 回歸測試與交付

工作：
- 為 Model、主要頁面、Admin 權限與文章管理補上必要測試。
- 整理安裝、啟動、建立管理員與資料庫備份說明。
- 更新 README 與本修復計畫的完成狀態。

驗收：
- 自動化測試與 Django system check 通過。
- 可依文件在新環境重建網站。
- 個人作者能完成登入與文章管理。
- 未完成事項與本機使用限制有明確說明。

## 5. 安全與資料保護規則

- 不讀取舊 SQLite、舊文章、帳號或密碼雜湊。
- 不連線舊 MySQL／PostgreSQL，不嘗試從舊桌機取回資料。
- 新資料庫與舊資料庫使用不同檔案路徑；不覆寫舊 `blog/db.sqlite3`。
- 不刪除歷史分支、Notebook、圖片、node_modules 或其他既有資產，除非另行確認。
- 不修改 Git 歷史、不 force push、不部署公開服務。
- 不將 Secret Key、管理員密碼或其他憑證提交到 Git。
- Migration 僅可作用於新建的本機 SQLite 資料庫。
- 每階段交付修改檔案清單、差異摘要、測試結果與未解決事項。

## 6. 最終完成定義

以下條件全部成立，即視為完成基本重新啟用：

- Python 3.12 與 Django 5.2.x 環境可依文件重建。
- 網站可在本機啟動。
- 首頁、About Me、文章列表與文章詳細頁正常顯示。
- 作者可透過 Django Admin 登入並新增、編輯、刪除文章。
- TinyMCE 可正常編輯內容，文章內容安全呈現。
- 核心測試與 Django system check 通過。
- README 有清楚的安裝、啟動與管理說明。

本專案不以找回舊文章、重現舊資料庫或重新公開部署作為完成條件。


## 7. 執行進度紀錄（2026-11-21）

本節記錄目前已提交的程式與文件工作。**程式碼已提交不等於 Django 執行驗收通過**；尚未在 Python 3.12 的乾淨環境中執行的項目，明確標示為待驗證。

### 分支與提交

| 用途 | 分支 | 最新已知 Commit |
|---|---|---|
| 文件整理 | `docs/portfolio-retrospective` | `28b56adc42cf1525b805b8ba748478ae467f4099`（本文件更新前） |
| 程式修復 | `restore/django-5.2-local` | `cb2a5d7ffd1ddc03d79b0f0a5b42acf5ceb5d47d`（README 更新後） |
| 修復基準 | `main` | `6bff2a39440a50c8bc79efda9aadbdef374616fa` |

### 已提交的程式變更

- 建立 Django 5.2.19 與 django-tinymce 5.0.0 的依賴清單。
- 將資料庫設定改為獨立的 `blog/db.local.sqlite3`，舊 `blog/db.sqlite3` 不在修復差異中。
- 改用本機用途的 Secret Key 環境變數設定與 localhost ALLOWED_HOSTS。
- 將文章時間預設值改為 `django.utils.timezone.now`，並新增對應 migration。
- 新增 migration，讓既有 migration state 的 TextField 與目前 Model 使用的 TinyMCE HTMLField 一致。
- 將文章管理集中至 Django Admin，移除前台 GET 刪除路由。
- 加入 `nh3` HTML sanitizer，並在文章詳細頁使用。
- 整理主要模板繼承與 Django 5.2 登出 POST 表單。
- 新增主要頁面、Admin 權限、時間預設值及 HTML 清理的測試案例。

### 已提交的文件變更

- 修復分支的 `README.md` 已加入 macOS 本機安裝、虛擬環境、依賴安裝、Secret Key、Migration、建立管理員、測試、啟動、資料庫備份及歷史截圖說明。
- README 明確指出 Django 執行驗收尚未完成，不將程式碼提交誤報為網站已成功啟動。

### 階段狀態

| 階段 | 狀態 | 說明 |
|---|---|---|
| Phase 0 — 修復基準與隔離 | 已完成 | 修復分支由指定 main commit 建立；main HEAD 未變更 |
| Phase 1 — 現代環境重建 | 程式修改已提交；執行驗收待完成 | Settings、依賴清單、新 SQLite 路徑及 migrations 已提交；尚未在乾淨 Python 3.12 環境安裝及執行 |
| Phase 2 — 核心頁面與文章管理 | 程式修改已提交；功能驗收待完成 | 模板、路由、Admin、TinyMCE 與 sanitizer 已實作；尚未用瀏覽器完成操作驗證 |
| Phase 3 — 回歸測試與交付 | 部分完成 | 已新增測試案例及 README 操作文件；尚未執行測試及確認乾淨環境可重建 |

### 尚待執行的驗收

必須在 Python 3.12 環境、Repository 的 `blog/` 目錄中執行，且確認使用新的 `db.local.sqlite3`：

1. `python manage.py check`
2. `python manage.py makemigrations --check --dry-run`
3. `python manage.py migrate`
4. `python manage.py test`
5. `python manage.py runserver`
6. 透過瀏覽器驗證首頁、About Me、文章列表、文章詳細頁、Admin 登入、文章 CRUD 與 TinyMCE 編輯器。

上述命令尚未執行前，不應標記為通過。若驗收出現錯誤，先記錄錯誤訊息並定位原因，再針對最小範圍修正；不得以未經驗證的成功敘述取代實際測試結果。

### 安全與資料邊界

- 不讀取或修改歷史 `blog/db.sqlite3`。
- Migration 只允許對新建的 `blog/db.local.sqlite3` 執行。
- 不連接 MySQL／PostgreSQL，不啟動公開服務。
- 不提交本機資料庫、Secret Key 或管理員密碼。
- 不修改 main，不刪除舊分支或歷史資產。
