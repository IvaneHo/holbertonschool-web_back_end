#!/bin/bash

# Chemin du dossier à traiter (défaut : dossier courant)
TARGET_DIR="${1:-.}"

echo "🔍 Traitement des fichiers directement dans : $TARGET_DIR"
echo

# Traitement uniquement des fichiers non cachés dans le dossier courant
for file in "$TARGET_DIR"/*; do
    [ -f "$file" ] || continue  # ignore les répertoires

    ext="${file##*.}"
    filename="$(basename "$file")"

    case "$ext" in
        sh|py|pl)
            chmod +x "$file"
            echo "🟢 chmod +x : $filename"
            ;;
        txt|md|sql|c|h|json|yml|yaml|xml|ini|cfg|conf)
            chmod 644 "$file"
            echo "📄 chmod 644 : $filename"
            ;;
        *)
            if grep -q '^#!' "$file"; then
                chmod +x "$file"
                echo "⚙️  chmod +x (shebang) : $filename"
            else
                chmod 644 "$file"
                echo "📄 chmod 644 : $filename"
            fi
            ;;
    esac
done

echo
echo "✅ Terminé."
