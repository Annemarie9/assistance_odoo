#!/bin/bash

# ==========================
# Configuration manuelle
# ==========================
# Liste des versions à traiter (séparées par des espaces)
ODOO_VERSIONS=("16.0" "17.0" "18.0")

# Dépôt officiel de la documentation Odoo
REPO_URL="https://github.com/odoo/documentation.git"
REMOTE_NAME="odoo-docs"
BASE_DIR="raw_data/versions"

# ==========================
# Début du script
# ==========================

# Créer le dossier principal s’il n’existe pas
mkdir -p "$BASE_DIR"

# Se déplacer dans le dossier
cd "$BASE_DIR" || exit 1

# Boucle sur chaque version
for VERSION in "${ODOO_VERSIONS[@]}"; do
    echo "🟦 Traitement de la version $VERSION..."

    # Si le dossier existe déjà et contient un dépôt git, on met à jour
    if [ -d "$VERSION/.git" ]; then
        echo "→ Mise à jour du dépôt existant pour la version $VERSION"
        cd "$VERSION" || exit 1
        git fetch "$REMOTE_NAME" "$VERSION"
        git merge "$REMOTE_NAME/$VERSION" --ff-only
        cd .. || exit 1
    else
        echo "→ Clonage du dépôt pour la version $VERSION"
        mkdir -p "$VERSION"
        cd "$VERSION" || exit 1

        git init
        git remote add "$REMOTE_NAME" "$REPO_URL"
        git sparse-checkout init
        echo "content/**" > .git/info/sparse-checkout

        git fetch "$REMOTE_NAME" "$VERSION"
        git checkout -b "$VERSION" "$REMOTE_NAME/$VERSION"

        echo "✅ Version $VERSION installée."
        cd .. || exit 1
    fi
done

echo "🎉 Toutes les versions ont été traitées avec succès."
