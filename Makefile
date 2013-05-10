gen-targets := gen-release gen-release-page gen-release-notes \
	gen-release-api-doc gen-release-examples gen-release-books
proton-gen-targets := gen-proton-release gen-proton-release-page \
	gen-proton-release-notes gen-proton-release-api-doc gen-proton-release-examples

.PHONY: default help render check-links clean publish ${gen-targets} ${proton-gen-targets}

OUTPUT_DIR := output
SITE_URL := file://$(shell readlink -f ${OUTPUT_DIR})

default: render

help:
	@echo "render (the default)"
	@echo "check-links"
	@echo "clean"
	@echo "publish"
	@echo "gen-release RELEASE=\$VERSION"
	@echo "gen-proton-release RELEASE=\$VERSION"

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

gen-release:
	gen-release-page
	gen-release-notes
	gen-release-api-doc
	gen-release-examples
	gen-release-books

gen-proton-release: 
	gen-proton-release-page
	gen-proton-release-notes
	gen-proton-release-api-doc
	gen-proton-release-examples

gen-release-%: RELEASE_DIR := input/releases/qpid-${RELEASE}
gen-release-%:
	test -n "${RELEASE}" && mkdir -p ${RELEASE_DIR}
	scripts/gen-release-$* ${RELEASE} ${RELEASE_DIR}

gen-proton-release-%: RELEASE_DIR := input/releases/qpid-proton-${RELEASE}
gen-proton-release-%:
	test -n "${RELEASE}" && mkdir -p ${RELEASE_DIR}
	scripts/gen-proton-release-$* ${RELEASE} ${RELEASE_DIR}
