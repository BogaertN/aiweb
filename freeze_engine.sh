#!/bin/bash

# =============================
# AI.Web Engine Freezer + Auditor + Git Auto-Updater (v1.01+ support)
# =============================

engine_name=$1

if [ -z "$engine_name" ]; then
  echo "[ERROR] No engine folder specified."
  echo "Usage: ./freeze_engine.sh <engine_folder_name>"
  exit 1
fi

src_path="$HOME/aiweb/engines/$engine_name"
base_dst_path="$HOME/aiweb/engines/${engine_name}_frozen_v1"
freeze_log_engines="$HOME/aiweb/engines/engine_freeze_log.txt"
freeze_log_root="$HOME/aiweb/engine_freeze_log.txt"
tree_snapshot="$HOME/aiweb/aiweb_project_tree.txt"
archive_dir="$HOME/aiweb/system_docs/tree_snapshots"

# --- Check if engine source exists
if [ ! -d "$src_path" ]; then
  echo "[ERROR] Engine folder '$engine_name' does not exist."
  exit 1
fi

# --- Determine next available version number
version="1.01"
while [ -d "${base_dst_path}.${version}" ]; do
  version=$(awk "BEGIN {printf \"%.2f\", $version + 0.01}")
done

dst_path="${base_dst_path}.${version}"

# --- Freeze the engine
cp -r "$src_path" "$dst_path"

timestamp=$(date -u +"%a %b %d %T %Z %Y")

# --- Append freeze logs
echo "✅ Froze $engine_name as ${engine_name}_frozen_v1.${version} on $timestamp" | tee -a "$freeze_log_engines" "$freeze_log_root"

# --- Regenerate project tree
tree -a -I '__pycache__|*.pyc|*.log' ~/aiweb > "$tree_snapshot"

# --- Save snapshot permanently
mkdir -p "$archive_dir"
cp "$tree_snapshot" "$archive_dir/tree_snapshot_$(date +%Y%m%d_%H%M%S).txt"

echo "✅ Freeze complete and project tree snapshots updated."

# --- GitHub section
cd ~/aiweb
git add .
git commit -m "✅ Freeze $engine_name version v1.${version} at $timestamp — Full tree + logs updated"
git push

echo "✅ GitHub push complete."

