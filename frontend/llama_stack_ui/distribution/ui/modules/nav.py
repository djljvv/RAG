"""Shared sticky top navigation component for all pages."""

import streamlit as st


_NAV_PAGES = [
    ("Chat", "💬", "llama_stack_ui.distribution.ui.page.playground.chat", "tool_chat_page"),
    ("Upload", "📄", "llama_stack_ui.distribution.ui.page.upload.upload", "upload_page"),
    ("Inspect", "🔍", "llama_stack_ui.distribution.ui.page.distribution.inspect", "inspect_page"),
]


def get_page_registry() -> dict:
    """Return a mapping of page label -> (module_path, function_name)."""
    return {label: (mod, func) for label, _, mod, func in _NAV_PAGES}

_STICKY_CSS = """
<style>
div[data-testid="stElementToolbar"] {
    display: none;
}
div.sticky-nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background: var(--background-color, #0e1117);
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.6rem 1rem;
    border-bottom: 1px solid rgba(128, 128, 128, 0.2);
    backdrop-filter: blur(12px);
}
div.sticky-nav-spacer {
    height: 3.5rem;
}
</style>
"""


def render_top_nav():
    """Render a sticky top-center navigation bar."""
    st.markdown(_STICKY_CSS, unsafe_allow_html=True)
    st.markdown('<div class="sticky-nav-spacer"></div>', unsafe_allow_html=True)

    _, center, _ = st.columns([1, 2, 1])
    with center:
        cols = st.columns(len(_NAV_PAGES))
        for col, (label, icon, *_) in zip(cols, _NAV_PAGES):
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
