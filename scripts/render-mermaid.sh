#!/usr/bin/env bash
set -euo pipefail

README="README.md"
OUT_MMD="diagram.mmd"
OUT_PNG="diagram.png"

# 找到 mermaid 源的起始行（支持多种 diagram 类型）
start_line=$(grep -n -m1 -E '^(flowchart|graph|sequenceDiagram|classDiagram|gantt|stateDiagram)' "$README" | cut -d: -f1 || true)
if [ -z "$start_line" ]; then
  echo "未找到 mermaid 图定义行。请确保 README.md 包含以 'flowchart' 或 'graph' 开头的 mermaid 源。"
  exit 1
fi

tail -n +"$start_line" "$README" > "$OUT_MMD"
# 删除可能存在的代码块围栏（```markdown / ```）以及文件首尾空行，避免 mermaid-cli 解析错误
sed -i '/^```/d' "$OUT_MMD"
# 去除文件首尾的空白行
awk 'BEGIN{p=0} /./{p=1} p{print}' "$OUT_MMD" | sed -e ':a' -e 'N' -e '$!ba' -e 's/\n\s*$//g' > "$OUT_MMD.tmp" && mv "$OUT_MMD.tmp" "$OUT_MMD"
echo "已提取并清理 mermaid 源到 $OUT_MMD"

# 优先使用 Docker（如果可用）
if command -v docker >/dev/null 2>&1; then
  echo "检测到 Docker，使用 minlag/mermaid-cli 渲染..."
  docker run --rm -v "$PWD":/data minlag/mermaid-cli -i /data/"$OUT_MMD" -o /data/"$OUT_PNG"
  echo "已生成 $OUT_PNG"
  exit 0
fi

# 否则尝试使用 npx（需要 Node.js）
if command -v npx >/dev/null 2>&1; then
  echo "使用 npx @mermaid-js/mermaid-cli 渲染（需要网络和 Node.js）..."
  npx --yes @mermaid-js/mermaid-cli -i "$OUT_MMD" -o "$OUT_PNG"
  echo "已生成 $OUT_PNG"
  exit 0
fi

echo "未检测到 Docker 或 npx。请安装 Node.js 或 Docker，或手动运行 mermaid-cli。"
exit 2
