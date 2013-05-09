.PHONY: default help render check-links clean publish \
	gen-release gen-proton-release regen-release-pages

OUTPUT_DIR := output
SITE_URL := file://$(shell readlink -f ${OUTPUT_DIR})

default: render

help:
	@echo "render (the default)"
	@echo "clean"
	@echo "publish"

render: clean
	mkdir -p ${OUTPUT_DIR}
	scripts/render ${SITE_URL} input ${OUTPUT_DIR}

check-links: INTERNAL := 1
check-links: EXTERNAL := 0
check-links: render
	scripts/check-links ${SITE_URL} input ${OUTPUT_DIR} ${INTERNAL} ${EXTERNAL}

clean:
	test -n "${OUTPUT_DIR}"
	rm -rf ${OUTPUT_DIR}

publish: OUTPUT_DIR := $(shell mktemp -d)
publish: SITE_URL := http://qpid.apache.org
publish: PUBLISH_DIR := ""
publish: render
	test -n "${PUBLISH_DIR}" -a -d ${PUBLISH_DIR} -a -f ${PUBLISH_DIR}/index.html
	cp -a ${OUTPUT_DIR}/* ${PUBLISH_DIR}
	rm -rf ${OUTPUT_DIR}

publish-devel: TAG := "head"
publish-devel: OUTPUT_DIR := $(shell mktemp -d)
publish-devel: SITE_URL := /~jross/transom/${TAG}
publish-devel: render
	rsync -av ${OUTPUT_DIR}/ jross@people.apache.org:public_html/transom/${TAG}
	rm -rf ${OUTPUT_DIR}

gen-release: RELEASE_DIR := input/releases/qpid-${RELEASE}
gen-release:
	test -n "${RELEASE}"
	mkdir -p ${RELEASE_DIR}
	scripts/gen-release-page ${RELEASE} > ${RELEASE_DIR}/index.md
	scripts/gen-release-api-doc ${RELEASE} ${RELEASE_DIR}
	scripts/gen-release-books ${RELEASE} ${RELEASE_DIR}
	scripts/gen-release-examples ${RELEASE} ${RELEASE_DIR}

gen-proton-release: RELEASE_DIR := input/releases/qpid-proton-${RELEASE}
gen-proton-release:
	test -n "${RELEASE}"
	mkdir -p ${RELEASE_DIR}
	scripts/gen-proton-release-page ${RELEASE} > ${RELEASE_DIR}/index.md
	scripts/gen-proton-release-api-doc ${RELEASE} ${RELEASE_DIR}
	scripts/gen-proton-release-examples ${RELEASE} ${RELEASE_DIR}

gen-proton-release-notes: RELEASE_DIR := input/releases/qpid-proton-${RELEASE}
gen-proton-release-notes:
	test -n "${RELEASE}"
	mkdir -p ${RELEASE_DIR}
	scripts/gen-proton-release-notes ${RELEASE} ${RELEASE_DIR}

regen-release-pages:
	scripts/gen-release-page 0.22 > input/releases/qpid-0.22/index.md
	scripts/gen-release-page 0.20 > input/releases/qpid-0.20/index.md
	scripts/gen-release-page-pre-0.20 0.18 > input/releases/qpid-0.18/index.md
	scripts/gen-release-page-pre-0.20 0.16 > input/releases/qpid-0.16/index.md
	scripts/gen-release-page-pre-0.20 0.14 > input/releases/qpid-0.14/index.md
	scripts/gen-proton-release-page 0.4 > input/releases/qpid-proton-0.4/index.md
