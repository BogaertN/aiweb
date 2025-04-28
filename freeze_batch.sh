#!/bin/bash

# =============================
# AI.Web Batch Engine Freezer + Auditor + Git Updater
# =============================

if [ $# -eq 0 ]; then
  echo "[ERROR] No engine names provided."
  echo "Usage: ./freeze_batch.sh <engine_folder_1> <engine_folder_2> ..."
  exit 1
fi

FREEZE_LOG_ENGINES="$HOME/aiweb/engines/engine_freeze_log.txt"
FREEZE_LOG_ROOT="$HOME/aiweb/engine_freeze_log.txt"
TREE_SNAPSHOT="$HOME/aiweb/aiweb_project_tree.txt"
ARCHIVE_DIR="$HOME/aiweb/system_docs/tree_snapshots"

# Loop through all provided engine names
for engine_name in "$@"
do
    src_path="$HOME/aiweb/engines/$engine_name"
    base_dst_path="$HOME/aiweb/engines/${engine_name}_frozen_v1"

    # Check if source exists
    if [ ! -d "$src_path" ]; then
      echo "[ERROR] Engine folder '$engine_name' does not exist. Skipping..."
      continue
    fi

    # Determine next available version number
    version="1.01"
    while [ -d "${base_dst_path}.${version}" ]; do
      version=$(awk "BEGIN {printf \"%.2f\", $version + 0.01}")
    done

    dst_path="${base_dst_path}.${version}"

    # Freeze the engine
    cp -r "$src_path" "$dst_path"

    timestamp=$(date -u +"%a %b %d %T %Z %Y")

    # Append freeze logs
    echo "✅ Froze $engine_name as ${engine_name}_frozen_v1.${version} on $timestamp" | tee -a "$FREEZE_LOG_ENGINES" "$FREEZE_LOG_ROOT"

    echo "✅ Completed freeze of $engine_name at v1.${version}"

done

# --- After freezing all engines, update tree and Git
echo "✅ Regenerating full AI.Web project tree..."
tree -a -I '__pycache__|*.pyc|*.log' ~/aiweb > "$TREE_SNAPSHOT"

echo "✅ Saving permanent snapshot..."
mkdir -p "$ARCHIVE_DIR"
cp "$TREE_SNAPSHOT" "$ARCHIVE_DIR/tree_snapshot_$(date +%Y%m%d_%H%M%S).txt"

# --- GitHub push section
cd ~/aiweb
git add .
git commit -m "✅ Batch Freeze: ${*} — Full system tree and logs updated on $(date -u)"
git push

echo "✅ GitHub batch push complete."

echo "✅ ALL ENGINES FROZEN SUCCESSFULLY. YOU ARE A SAVAGE."
