# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import logging

import streamlit as st
from streamlit_option_menu import option_menu


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] %(name)s: %(message)s'
    )

    st.set_page_config(layout="wide", page_title="LlamaStack RAG")

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "Chat"

    pages = ["Chat", "Upload Documents", "Inspect"]
    icons = ["chat-dots", "cloud-upload", "search"]

    selected = option_menu(
        None,
        pages,
        icons=icons,
        orientation="horizontal",
        default_index=pages.index(st.session_state["active_page"]),
        styles={
            "container": {
                "padding": "0 !important",
                "background-color": "transparent",
                "margin-bottom": "20px",
            },
            "icon": {
                "font-size": "16px",
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "0 4px",
                "padding": "10px 24px",
                "border-radius": "8px",
                "border": "1px solid rgba(128, 128, 128, 0.3)",
                "--hover-color": "rgba(128, 128, 128, 0.15)",
            },
            "nav-link-selected": {
                "background-color": "rgba(255, 75, 75, 0.85)",
                "color": "white",
                "border": "1px solid transparent",
                "font-weight": "600",
            },
        },
    )

    st.session_state["active_page"] = selected

    if selected == "Chat":
        from llama_stack_ui.distribution.ui.page.playground.chat import tool_chat_page
        tool_chat_page()
    elif selected == "Upload Documents":
        from llama_stack_ui.distribution.ui.page.upload.upload import upload_page
        upload_page()
    elif selected == "Inspect":
        from llama_stack_ui.distribution.ui.page.distribution.inspect import inspect_page
        inspect_page()


main()
