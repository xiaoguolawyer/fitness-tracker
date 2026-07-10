#!/bin/bash
# 一键部署：把本地改动提交并推送到 GitHub（Pages 约 30s 后更新）
cd "$(dirname "$0")"
git add -A
git commit -m "update $(date '+%Y-%m-%d %H:%M')"
git push
echo "✅ 已推送。GitHub Pages 约 30 秒后生效。"
