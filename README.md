# DaLiuRen Learning Prototype v1.0

一個使用 Python / Tkinter 製作的「大六壬學習型排盤原型」。

此專案的目的，是把天干地支、五行、月將、天地盤、四課、三傳、十二神將與文字解讀等概念，轉換成可以閱讀、修改與實驗的程式架構。

> **重要：本專案不是完整、經典校勘級或專業術數用途的大六壬排盤器。**
> 目前部分規則採用簡化實作，適合程式學習、規則研究與 GUI 原型驗證。

## 已實作功能

- Tkinter 圖形介面
- 年 / 月 / 日 / 時 / 分輸入
- 問事類型輸入
- 日干支推算
- 簡化月將
- 天盤 / 地盤
- 簡化四課
- 部分三傳推導
  - 賊剋概念
  - 遙剋概念
  - 部分別責
  - 部分昴星
- 十二神將資料
- 工作 / 感情 / 財運文字解讀
- JSON 分章資料庫

## 專案結構

```text
DaLiuRen/
├─ main.py
├─ core.py
├─ data/
│  ├─ chapter_1.json
│  ├─ chapter_2.json
│  ├─ chapter_3.json
│  └─ chapter_4.json
├─ README.md
├─ ALGORITHM_STATUS.md
├─ SECURITY.md
├─ CHANGELOG.md
├─ LICENSE
├─ requirements.txt
└─ .gitignore
```

## 執行

Windows 安裝一般 Python 3.11 / 3.12 後：

```bash
python main.py
```

目前不需要額外第三方 Python 套件。

## 資料章節

- `chapter_1.json`：天干地支、五行與寄宮入門
- `chapter_2.json`：天地盤、四課、三傳概念
- `chapter_3.json`：十二神將象徵與說明
- `chapter_4.json`：工作、感情、財運的示範性文字解讀

## 目前演算法限制

請先閱讀 `ALGORITHM_STATUS.md`。

目前版本刻意標示為 **Learning Prototype**，不宣稱：
- 完整還原傳統大六壬全部起課規則
- 完整實作所有九宗門 / 三傳取法
- 完整處理晝夜貴人與天將順逆
- 以真太陽時、節氣交接時刻或曆法資料庫做嚴格校正

## 安全原則

- 無病毒
- 無背景常駐
- 不修改 Registry
- 不執行 BAT / PowerShell
- 不下載外部程式
- 不蒐集或上傳任何使用者資料
- 全部運算皆在本機完成

## 授權

採用 Non-Commercial License v1.0。

允許個人、教育、研究、學習與非商業修改／分享；
未經作者書面同意禁止商業使用。
