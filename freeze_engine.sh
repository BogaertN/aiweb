#!/bin/bash

engine_name=$1

if [ -z "$engine_name" ]; then
  echo "[ERROR] No engine folder specified."
  echo "Usage: ./freeze_engine.sh <engine_folder_name>"
  exit 1
fi

src_path="$HOME/aiweb/engines/$engine_name"
dst_path="$HOME/aiweb/engines/${engine_name}_frozen_v1"

if [ ! -d "$src_path" ]; then
  echo "[ERROR] Engine folder '$engine_name' does not exist."
  exit 1
fi

# Freeze the engine
cp -r "$src_path" "$dst_path"

timestamp=$(date -u +"%a %b %d %T %Z %Y")

# Append freeze logs
echo "✅ Froze $engine_name as ${engine_name}_frozen_v1 on $timestamp" >> "$HOME/aiweb/engines/engine_freeze_log.txt"
echo "✅ Froze $engine_name as ${engine_name}_frozen_v1 on $timestamp" >> "$HOME/aiweb/engine_freeze_log.txt"

# Regenerate project tree
tree "$HOME/aiweb" > "$HOME/aiweb/aiweb_project_tree.txt"

# Save tree snapshots for version history
mkdir -p "$HOME/aiweb/system_docs/tree_snapshots"
tree "$HOME/aiweb" > "$HOME/aiweb/system_docs/tree_snapshots/tree_snapshot_$(date +%Y%m%d_%H%M%S).txt"

echo "✅ Freeze complete and project tree snapshots updated in engines/, top-level aiweb/, and system_docs/tree_snapshots/"

