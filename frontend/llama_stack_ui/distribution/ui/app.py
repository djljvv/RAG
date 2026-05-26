# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import importlib
import logging

import streamlit as st

from llama_stack_ui.distribution.ui.modules.api import llama_stack_api


def check_server_connection():
    """Check LlamaStack server connectivity and display error if unreachable."""
    if st.session_state.get("_connection_verified"):
        return True

    connected, error = llama_stack_api.check_connection()
    if connected:
        st.session_state["_connection_verified"] = True
        return True

    st.error(
        f"**Unable to connect to the LlamaStack server** at "
        f"`{llama_stack_api.base_url}`.\n\n"
        f"Please verify the server is running and the `LLAMA_STACK_ENDPOINT` "
        f"environment variable is set correctly.",
        icon="🔌",
    )
    with st.expander("Error details"):
        st.code(error)
    if st.button("Retry Connection"):
        st.session_state.pop("_connection_verified", None)
        st.rerun()
    return False


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] %(name)s: %(message)s'
    )

    st.set_page_config(layout="wide", page_title="LlamaStack RAG")

    if not check_server_connection():
        st.stop()

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "Chat"

    from llama_stack_ui.distribution.ui.modules.nav import render_top_nav, get_page_registry
    render_top_nav()

    active = st.session_state["active_page"]
    registry = get_page_registry()

    if active in registry:
        module_path, func_name = registry[active]
        module = importlib.import_module(module_path)
        getattr(module, func_name)()


main()
