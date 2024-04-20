PACKAGE_VERSION = $(shell grep -oP 'version": \((.*?)\)' $(CURDIR)/link_librairy_auto_reload_addon/__init__.py | cut -d'(' -f2 | cut -d')' -f1 | sed 's/, /./g')

install_dev:
	@echo "------------------- INSTALL DEV ENV ------------------- "
	rm -rf /tmp/blender/link_librairy_auto_reload_addon
	mkdir /tmp/blender/link_librairy_auto_reload_addon/scripts/addons -p
	ln $(CURDIR)/link_librairy_auto_reload_addon /tmp/blender/link_librairy_auto_reload_addon/scripts/addons/link_librairy_auto_reload_addon -s
	@echo "------------------------------------------------------- "

run:
	@echo "--------------------- RUN BLENDER --------------------- "
	@export BLENDER_USER_SCRIPTS=/tmp/blender/link_librairy_auto_reload_addon/scripts; \
	blender --addons link_librairy_auto_reload_addon

deploy:release
	@echo "------------------- DEPLOY PACKAGE -------------------- "
	@echo Deploying ${PACKAGE_VERSION} version
	@git push --tags
	@gh release create ${PACKAGE_VERSION} ./dist/link_librairy_auto_reload_addon-${PACKAGE_VERSION}.zip --generate-notes --latest 
	@echo "------------------------------------------------------- "

release:build clean
	@echo "------------------- RELEASE PACKAGE ------------------- "
	@echo Releasing ${PACKAGE_VERSION} version
	@git tag ${PACKAGE_VERSION} || echo "Tag already exists."
	@echo "------------------------------------------------------- "

build: clean
	@echo "-------------------- BUILD PACKAGE -------------------- "
	mkdir -p dist
	zip -r dist/link_librairy_auto_reload_addon-${PACKAGE_VERSION}.zip link_librairy_auto_reload_addon
	@echo "------------------------------------------------------- "

clean:
	@echo "-------------------- CLEAN PACKAGE -------------------- "
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete
	@echo "------------------------------------------------------- "

test:
	@echo "---------------------- RUN TESTS ---------------------- "
	python3 -m unittest discover tests
	@echo "------------------------------------------------------- "