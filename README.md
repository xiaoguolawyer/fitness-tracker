# 健身打卡网页（PWA）

小国的居家弹力绳训练打卡页，部署为 GitHub Pages + 真·PWA。

## 特性
- 永久网址，改完自动同步
- 添加到主屏幕后是全屏 App（无浏览器栏），后台自动拉取新版
- 训练数据存手机 localStorage（导出/导入 JSON 备份）

## 本地结构
- `index.html` — 主页面
- `manifest.webmanifest` / `sw.js` / `icon-*.png` — PWA 资源
- `deploy.sh` — 一键提交并推送

## 更新流程
修改文件后：
```bash
./deploy.sh
```
GitHub Pages 约 30 秒后生效，手机打开即新版。

## 数据备份
换设备或清缓存前，在页面「设置 → 导出数据」存 JSON；新设备「导入数据」恢复。
