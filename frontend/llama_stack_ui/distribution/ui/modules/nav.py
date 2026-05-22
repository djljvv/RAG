# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

"""Shared bottom navigation component for all pages."""

import streamlit as st


_NAV_PAGES = [
    ("Chat", "💬"),
    ("Upload", "📄"),
    ("Inspect", "🔍"),
]


def render_bottom_nav():
    """Render compact page navigation buttons below page content."""
    cols = st.columns(len(_NAV_PAGES))
    for col, (label, icon) in zip(cols, _NAV_PAGES):
        with col:
            is_active = st.session_state.get("active_page") == label
            if st.button(
                f"{icon} {label}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
                key=f"nav_{label}",
            ):
                st.session_state["active_page"] = label
                st.rerun()
