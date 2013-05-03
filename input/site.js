/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
 */

"use strict";

function getDescendant(elem, path) {
    var names = path.split(".");
    var node = elem;

    for (var i = 0; i < names.length; i++) {
        var elems = node.getElementsByTagName(names[i]);

        if (elems.length === 0) {
            return null;
        }

        node = elems[0];
    }

    return node;
}

function getText(elem) {
    var child = elem.firstChild;

    while (child) {
        if (child.nodeType === 3 && child.data.trim() !== "") {
            return child.data;
        }

        child = child.nextSibling;
    }
}

function gotoJira() {
    var form = document.getElementById("jira-goto-form");

    if (!form) {
        return;
    }

    form.jira.value = form.jira.value.trim();

    var jira = form.jira.value;
    var uri = "https://issues.apache.org/jira/browse/" + encodeURIComponent(jira);

    form.action = uri;
}

function searchJiras() {
    var form = document.getElementById("jira-search-form");

    if (!form) {
        return;
    }

    var text = form.text.value;
    var jql = "project in (QPID, PROTON) and text ~ \"" + text + "\" order by updatedDate desc";
    var uri = "https://issues.apache.org/jira/issues/?jql=" + encodeURIComponent(jql);

    form.action = uri;
}

function normalizeRevision() {
    var form = document.getElementById("viewvc-goto-form");

    form.revision.value = form.revision.value.trim();
}

function registerEventListeners() {
    var jiraGotoForm = document.getElementById("jira-goto-form");
    var jiraSearchForm = document.getElementById("jira-search-form");
    var viewvcGotoForm = document.getElementById("viewvc-goto-form");

    if (jiraGotoForm) {
        jiraGotoForm.addEventListener("submit", gotoJira, false);
    }

    if (jiraSearchForm) {
        jiraSearchForm.addEventListener("submit", searchJiras, false);
        window.addEventListener("hashchange", focusJiraSearchForm, false);
    }

    if (viewvcGotoForm) {
        viewvcGotoForm.addEventListener("submit", normalizeRevision, false);
    }
}

function focusJiraSearchForm() {
    var hash = window.location.hash;

    if (hash === "#search-issues") {
        var searchForm = document.getElementById("jira-search-form");

        if (searchForm !== null) {
            searchForm.text.focus();
        }
    }
}

function updateGlobalNavigation() {
    var elem = document.getElementById("global-navigation");
    var pageTitleElems = document.getElementsByTagName("h1");

    if (!elem || pageTitleElems.length === 0) {
        return;
    }

    var pageTitle = getText(pageTitleElems[0]).trim();
    var child = elem.firstChild;

    while (child) {
        if (child.nodeType === 1) {
            var desc = getDescendant(child, "a");

            if (getText(desc).trim() === pageTitle) {
                desc.style.color = "black";
                break;
            }
        }

        child = child.nextSibling;
    }

    if (pageTitle === "Search") {
        elem = document.getElementById("search-link");
        child = getDescendant(elem, "img");
        child.src = child.src.replace("-blue", "-black");
    }
}

function updatePathNavigation() {
    var elem = document.getElementById("path-navigation");

    if (!elem) {
        return;
    }

    var child = elem.firstChild;
    var count = 0;

    while (child) {
        if (child.nodeType === 1) {
            count++;
        }

        child = child.nextSibling;
    }

    if (count >= 2) {
        elem.style.display = "inherit";
    }
}

window.addEventListener("load", registerEventListeners, false);
window.addEventListener("load", focusJiraSearchForm, false);
window.addEventListener("load", updateGlobalNavigation, false);
window.addEventListener("load", updatePathNavigation, false);
