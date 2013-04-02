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

function gotoJira() {
    form = document.getElementById("jira-goto-form");

    jira = form.jira.value;
    uri = "https://issues.apache.org/jira/browse/" + encodeURIComponent(jira);

    form.action = uri;
}

function searchJiras() {
    form = document.getElementById("jira-search-form");

    text = form.text.value;
    jql = "project in (QPID, PROTON) and text ~ \"" + text + "\" order by updatedDate desc";
    uri = "https://issues.apache.org/jira/issues/?jql=" + encodeURIComponent(jql);

    form.action = uri;
}

function register() {
    gotoForm = document.getElementById("jira-goto-form")
    searchForm = document.getElementById("jira-search-form")

    if (gotoForm !== null) {
        gotoForm.addEventListener("submit", gotoJira, false);
    }

    if (searchForm !== null) {
        searchForm.addEventListener("submit", searchJiras, false);
    }
}

function focusJiraSearchForm() {
    hash = window.location.hash;

    if (hash === "#search-existing-issues") {
        searchForm = document.getElementById("jira-search-form")

        if (searchForm !== null) {
            searchForm.text.focus()
        }
    }
}

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
        if (child.nodeType === 3) {
            return child.data;
        }

        child = child.nextSibling;
    }
}

function updateNavigation() {
    var elem = document.getElementById("global-navigation");

    if (!elem) {
        return;
    }

    var pageTitleElems = document.getElementsByTagName("h1");

    if (pageTitleElems.length === 0) {
        return;
    }

    var pageTitle = getText(pageTitleElems[0]);
    var child = elem.firstChild;

    while (child) {
        if (child.nodeType === 1) {
            desc = getDescendant(child, "a");

            if (getText(desc) === pageTitle) {
                desc.style.color = "black";
                break;
            }
        }

        child = child.nextSibling;
    }

    elem = document.getElementById("path-navigation");
    child = elem.firstChild;
    var count = 0;

    while (child) {
        if (child.nodeType === 1) {
            count++;
        }

        child = child.nextSibling;
    }

    if (count < 2) {
        elem.style.display = "none";
    }
}

window.addEventListener("load", register, false);
window.addEventListener("load", focusJiraSearchForm, false);
window.addEventListener("load", updateNavigation, false);
