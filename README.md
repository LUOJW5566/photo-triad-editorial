# Photo Triad Editorial

一个面向 Codex 的照片抽象编辑 skill：保留上传照片作为纪实证据，并把照片中的结构、体积和像素关系重构为一个宽阔留白的下方面板。

下方面板将三种语言融合为一个连续母题：

- **Isometric**：轴测方向、平面和结构骨架；
- **3D**：受控的体积、层叠、遮挡和材质；
- **Pixel**：粗颗粒块面、阶梯边缘和离散细节。

## 输出流程

skill 支持三个独立产物：

1. `RAW_PANEL`：图像模型生成的无文字下方面板；
2. `ANNOTATED_PANEL`：由 `add_metadata.py` 加入日期和主题；
3. `FINAL_COMPOSITE`：由 `compose_diptych.py` 将原照片和标注面板拼接。

```text
RAW_PANEL
  -> scripts/add_metadata.py
ANNOTATED_PANEL
  -> scripts/compose_diptych.py + USER_PHOTO
FINAL_COMPOSITE
```

## 安装

将 `photo-triad-editorial` 文件夹复制到 Codex skills 目录：

```text
C:\Users\<user>\.codex\skills\photo-triad-editorial
```

## Python 脚本

需要 Pillow：

```bash
python -m pip install pillow
```

给原始面板加入日期和主题：

```bash
python scripts/add_metadata.py RAW_PANEL ANNOTATED_PANEL --date "27 AUG 2026" --theme "CITY BENDS"
```

将原照片与标注面板拼接：

```bash
python scripts/compose_diptych.py USER_PHOTO ANNOTATED_PANEL FINAL_COMPOSITE
```

拼接脚本会验证最终图的上方照片区域与输入照片逐像素一致；只会按照片宽度缩放下方面板。

## 许可

本项目以 MIT License 发布。生成作品仍需遵守输入照片、人物、商标、建筑和所用 AI 平台的相应权利与条款。

