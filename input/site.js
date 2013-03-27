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

window.addEventListener("load", register, false);
window.addEventListener("load", focusJiraSearchForm, false);
