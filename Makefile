.PHONY: default help render clean publish \
	gen-release x-release-pages

OUTPUT_DIR := "output"
SITE_URL := "file://$(shell readlink -f ${OUTPUT_DIR})"

default: render

help:
	@echo "render (the default)"
	@echo "clean"
	@echo "publish"

render: clean
	mkdir -p ${OUTPUT_DIR}
	scripts/render ${SITE_URL} input ${OUTPUT_DIR}

clean:
	rm -rf ${OUTPUT_DIR}

publish: TAG := "head"
publish: OUTPUT_DIR := $(shell mktemp -d)
publish: SITE_URL := "/~jross/transom/${TAG}"
publish: render
	rsync -av "${OUTPUT_DIR}/" "jross@people.apache.org:public_html/transom/${TAG}"
	rm -rf ${OUTPUT_DIR}

x-release-pages:
	scripts/gen-release-page 0.20 > input/releases/qpid-0.20/index.md
	scripts/gen-release-page-pre-0.20 0.18 > input/releases/qpid-0.18/index.md
	scripts/gen-release-page-pre-0.20 0.16 > input/releases/qpid-0.16/index.md
	scripts/gen-release-page-pre-0.20 0.14 > input/releases/qpid-0.14/index.md
	scripts/gen-proton-release-page 0.3 > input/releases/qpid-proton-0.3/index.md

gen-release:
	test ! -z "${RELEASE}"
	scripts/gen-release-page ${RELEASE} > input/releases/qpid-${RELEASE}/index.md
	scripts/gen-release-docs ${RELEASE} input/releases/qpid-${RELEASE}
