# Kanon Voice Assistant 🎙️🌸

**斎藤かのんアシスタント for macOS**  
現在アクティブなウィンドウを検知し、優しい英語のひと言をしゃべってくれるAI風ボイスアシスタントです。

## 🛠️ 特徴
- macOSの `say` コマンドで自然な音声出力（複数声対応）
- ウィンドウタイトルに応じたメッセージ切り替え
- Python製、軽量でシンプル

## 🚀 Getting Started

### 1. 必要ライブラリをインストール

```bash
pip install -r requirements.txt
```

### 2. スクリプトを実行

```bash
python3 kanon_smart.py
```

### 3. おすすめ設定
- `VOICE = "Samantha"` の部分を `"Karen"` や `"Kyoko"` に変更
- お好きな声をお楽しみください！

## 📦 Requirements

- Python 3.9+
- macOS
- `say` コマンドが有効なこと
- ライブラリ：`pygetwindow`

## 📄 License
MIT License
